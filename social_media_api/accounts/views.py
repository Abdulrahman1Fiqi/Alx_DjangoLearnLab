from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomUser  
from .serializers import UserSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView):
    """
    View for user registration.
    """
    queryset = CustomUser .objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # The token is created in the serializer, so we just return the user data
        return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    """
    View for user login.
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data  # This will be the token key
        return Response({'token': token}, status=status.HTTP_200_OK)