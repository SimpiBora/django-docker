# module5/urls.py
from inspect import getmembers, isclass
from . import views
from rest_framework.viewsets import ViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewset with it.
router = DefaultRouter()


# The API URLs are now determined automatically by the router.
urlpatterns = router.urls


# Automatically find all ViewSets in views.py and register them
for name, cls in getmembers(views, isclass):
    if issubclass(cls, ViewSet) and cls.__module__ == views.__name__:
        router.register(
            rf"{name.lower().replace('viewset', '')}", cls, basename=name.lower()
        )

urlpatterns = [
    path("api/mod5/", include(router.urls)),  # Register the routes under '/api/m4/'
]
