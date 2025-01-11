from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomUser   
from .serializers import UserSerializer, LoginSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import CustomUser 
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

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
    






class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser .objects.get(id=user_id)
            request.user.following.add(user_to_follow)
            return Response({"message": f"You are now following {user_to_follow.username}"}, status=200)
        except CustomUser .DoesNotExist:
            return Response({"error": "User  not found"}, status=404)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser .objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=200)
        except CustomUser .DoesNotExist:
            return Response({"error": "User  not found"}, status=404)
        









class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')