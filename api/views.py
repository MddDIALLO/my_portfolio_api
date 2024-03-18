from rest_framework import viewsets, permissions, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Tag, Post, Comment, ContactMessage, CustomUser
from .serializers import CustomUserSerializer, CategorySerializer, TagSerializer, PostSerializer, CommentSerializer, ContactMessageSerializer
from rest_framework.permissions import IsAdminUser

class IsAdminOrSelf(permissions.BasePermission):
    """
    Custom permission to only allow admin users or the concerned user to perform actions.
    """

    def has_permission(self, request, view):
        # if view.action == 'retrieve' and request.method == 'GET':
        #     return True

        # if view.action == 'create' and request.method == 'POST':
        #     return True

        return request.user.is_staff or int(view.kwargs['pk']) == request.user.id

class CustomUserCreateAPIView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserRetrieveAllAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

class CustomUserRetrieveOneAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrSelf]

    def get(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CustomUserUpdateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrSelf]

    def put(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            serializer = CustomUserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CustomUserDeleteAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrSelf]

    def delete(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CustomUserDisableAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrSelf]

    def put(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            user.is_active = False
            user.save()
            return Response({'detail': 'User disabled'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CustomUserEnableAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrSelf]

    def put(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            user.is_active = True
            user.save()
            return Response({'detail': 'User enabled'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
