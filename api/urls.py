from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EncodedTextViewSet, EncodingSchemaViewSet

router = DefaultRouter()
router.register(r'texts', EncodedTextViewSet)
router.register(r'schemas', EncodingSchemaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]