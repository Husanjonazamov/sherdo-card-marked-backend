from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CardView

router = DefaultRouter()
router.register("card", CardView, basename="card")
urlpatterns = [path("", include(router.urls))]
