from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.addresses.api.serializer import AddressSerializer
from utils.pagination import ExtendedPagination
from utils.filters import AddressFilterSet
from apps.addresses.models import Address

class AddressGenericViewSet(GenericViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.filter(is_active=True)

    # Paginacion personalizada
    pagination_class = ExtendedPagination

    # Sistema de filtros
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
        ]
    
    #Define campos para la busqueda
    filterset_class = AddressFilterSet
    search_fields = ['address', 'state_id__state', 'city_id__city']
    
    # Define campos para el ordenamiento
    ordering_fields = ['address', 'state_id__state', 'city_id__city'] 
    
    # Método 'list': Obtiene una lista de direcciones
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    # Método 'retrieve': Obtiene una direccion específica por clave primaria (pk)
    def retrieve(self, request, pk):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Método 'update': Actualiza una direccion existente
    def update(self, request, pk):
        instance = self.get_object()
        
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)