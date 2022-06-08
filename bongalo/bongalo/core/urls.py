from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewSpace

router = DefaultRouter()
router.register(r'spaces',ViewSpace)

urlpatterns = [
    path("", include(router.urls))
]