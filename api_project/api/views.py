from django.shortcuts import render

# Create your views here.
# api/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all book instances
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all book instances
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]   # Use the BookSerializer to serialize the data


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
