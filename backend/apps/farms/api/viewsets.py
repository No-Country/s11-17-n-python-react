from rest_framework import status
from rest_framework.response import Response
from apps.farms.api.serializer import farmSerializer, FarmPhotoSerializer
from apps.farms.models import Farm
from rest_framework.viewsets import GenericViewSet
from utils.pagination import FarmPagination
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from apps.farms.models import Farm
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from utils.permisssions import ListAndRetrievePermission

"""
    The FarmViewset class is a generic viewset that allows any user to access and manipulate Farm
    objects. It is used to create, retrieve, update, and delete Farm objects using the farmSerializer.
"""


class FarmViewset(GenericViewSet):
    queryset = Farm.objects.all()
    serializer_class = farmSerializer
    pagination_class = FarmPagination
    permission_classes = [ListAndRetrievePermission]

    @extend_schema(
        examples=[
            OpenApiExample(
                "Example Schema",
                {
                    "name": "string",
                    "address": "string",
                    "description": "string",
                },
            )
        ],
    )
    def create(self, request, *args, **kwargs):
        """
        The above function creates a new object using the provided request data and saves it using the
        serializer.

        :param request: The `request` parameter is an object that represents the HTTP request made by the client. It contains information such as the request method (GET, POST, etc.), headers, query
        parameters, and the request body
        return: The function returns a Response object that contains the serialized data of the created object (json).
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        """

        :param request: The `request` parameter is an object that represents the HTTP request made by
        the client. It contains information such as the request method (GET, POST, etc.), headers, query
        parameters, and the request body. It is used to retrieve data from the client and perform
        actions based on the request
        :return: The function returns a response containing serialized data from the queryset.
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        # return self.get_paginated_response(self.paginate_queryset(serializer.data))
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """
        :param request: The `request` parameter is an object that represents the HTTP request made by
        the client. It contains information such as the request method (GET, POST, etc.), headers, query
        parameters, and the request body
        :param pk: The "pk" parameter stands for "primary key". It is used to identify a specific object
        in a database. In this context, it is used to retrieve a specific item from the database based
        on its primary key value
        :return:The function retrieves an item and returns its serialized data as a response.
        """
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        The above function updates an item with the given primary key using the data from the request
        and returns the updated item.

        :param request: The `request` parameter is an object that represents the HTTP request made by
        the client. It contains information such as the request method (GET, POST, etc.), headers, query
        parameters, and the request body
        :param pk: The "pk" parameter stands for "primary key" and is used to identify a specific object
        in the database. In this case, it is used to retrieve the object that needs to be updated
        :return: a Response object with the serialized data and a status code of 200 (OK).
        """
        item = self.get_object(pk)
        serializer = self.get_serializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=FarmPhotoSerializer, responses=FarmPhotoSerializer)
    @action(
        detail=True, methods=["patch"], parser_classes=[MultiPartParser, FormParser]
    )
    def change_photo(self, request, pk=None):
        farm = self.get_object()
        serializer = FarmPhotoSerializer(instance=farm, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
