from rest_framework import viewsets, status, filters
from apps.rabbits.models import Rabbit
from utils.filters import RabbitFilterSet
from utils.pagination import RabbitPagination
from apps.rabbits.api.serializers import RabbitSerializer, RabbitPhotoSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema


class RabbitViewSet(viewsets.ModelViewSet):
    queryset = Rabbit.objects.all().order_by("-created")
    serializer_class = RabbitSerializer
    pagination_class = RabbitPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = RabbitFilterSet
    read_only_fields = (
        "created",
        "id",
        "age",
        "tag",
    )

    def get_queryset(self):
        queryset = Rabbit.objects.all()

        created = self.request.query_params.get("created")
        breed = self.request.query_params.get("breed")
        genre = self.request.query_params.get("genre")
        birthday = self.request.query_params.get("birthday")
        price = self.request.query_params.get("price")
        tag = self.request.query_params.get("tag")
        weight = self.request.query_params.get("weight")
        cage_id = self.request.query_params.get("cage_id")
        is_active = self.request.query_params.get("is_active")

        filters = Q()

        if created:
            filters &= Q(created__icontains=created)
        if breed:
            filters &= Q(breed__icontains=breed)
        if genre:
            filters &= Q(genre__icontains=genre)
        if birthday:
            filters &= Q(birthday__icontains=birthday)
        if price:
            filters &= Q(price=price)
        if tag:
            filters &= Q(tag__icontains=tag)
        if weight:
            filters &= Q(weight=weight)
        if cage_id:
            filters &= Q(cage_id=cage_id)
        if is_active:
            if is_active.lower() == "true":
                filters &= Q(is_active=True)
            elif is_active.lower() == "false":
                filters &= Q(is_active=False)

        queryset = queryset.filter(filters)

        return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = RabbitSerializer(instance, data=request.data, partial=partial)

        # Check if the updated field is read-only
        for field in self.read_only_fields:
            if field in request.data:
                return Response(
                    {
                        "error": f"No puedes actualizar el campo de solo lectura <<'{field}'>>"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        rabbit_destroy = self.serializer_class.Meta.model.objects.filter(id=pk).update(
            is_active=False
        )
        if rabbit_destroy == 1:
            return Response(
                {"message": "Conejo eliminado correctamente"},
                status=status.HTTP_204_NO_CONTENT,
            )
        return Response(
            {"message": "El conejo no existe"}, status=status.HTTP_404_NOT_FOUND
        )

    @extend_schema(request=RabbitPhotoSerializer, responses=RabbitPhotoSerializer)
    @action(
        detail=True, methods=["patch"], parser_classes=[MultiPartParser, FormParser]
    )
    def change_photo(self, request, pk=None):
        rabbit = self.get_object()
        serializer = RabbitPhotoSerializer(
            instance=rabbit, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
