from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
#from utils.filters import ProfileFilterSet
from drf_spectacular.utils import extend_schema_view, extend_schema
from utils.pagination import ExtendedPagination

from apps.profiles.api.serializer import ProfileSerializer
from apps.addresses.models import Address

@extend_schema_view(
    list = extend_schema(description='permite listar los perfiles de usuario'),
    retrieve = extend_schema(description='permite ver el perfil de un usuario'),
    update = extend_schema(description='permite actualizar el perfil de usuario'),
)

class ProfileModelViewSet(GenericViewSet):
    serializer_class = ProfileSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
    
    # Paginacion personalizada
    pagination_class = ExtendedPagination
    
    # Sistema de filtros
    filter_backends = [DjangoFilterBackend,
                        filters.SearchFilter, filters.OrderingFilter]
    
    #filterset_class = ProfileFilterSet
    search_fields = ["last_name", "first_name", ]
    
    # Define campos para el ordenamiento
    ordering_fields = ["first_name", "last_name", "qualification", "created"]

    # Método 'list': Obtiene una lista de perfiles
    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    # Método 'retrieve': Obtiene un perfil específico por clave primaria (pk)
    def retrieve(self, request, pk):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # Método 'update': Actualiza un perfil existente
    def update(self, request, pk):
        instance = self.get_object()

        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)