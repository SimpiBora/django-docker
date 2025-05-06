from rest_framework import viewsets
from rest_framework.response import Response
from inventory.models import Category
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema
from rest_framework import status


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving categories.
    """

    @extend_schema(
        request=CategorySerializer,  # This links the serializer for the request body
        responses={
            201: CategorySerializer
        },  # Expected response will be the created category
        tags=["Module 4"],
    )
    def list(self, request):
        """
        List all categories.
        """
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     """
    #     Retrieve a category by its ID.
    #     """
    #     categories = ["Electronics", "Books", "Clothing"]
    #     if pk and int(pk) < len(categories):
    #         return Response(categories[int(pk)])
    #     return Response({"error": "Category not found"}, status=404)
