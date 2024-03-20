from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Child
from .serializers import ChildSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class ChildrenList(APIView):
    serializer_class = ChildSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        children = Child.objects.all()
        serializer = ChildSerializer(
            children, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ChildSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class ChildrenDetail(APIView):
    serializer_class = ChildSerializer
    # authentication
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            child = Child.objects.get(pk=pk)
            # authentication
            self.check_object_permissions(self.request, child)
            return child
        except Child.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        child = self.get_object(pk)
        serializer = ChildSerializer(
            child, context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        child = self.get_object(pk)
        serializer = ChildSerializer(
            child, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        child = self.get_object(pk)
        child.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
