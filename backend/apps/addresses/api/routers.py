from rest_framework.routers import DefaultRouter
from apps.addresses.api.viewsets import AddressGenericViewSet

routers = DefaultRouter()
routers.register(r"addresses", AddressGenericViewSet, basename="assress")
urlpatterns = routers.urls