from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    CategoryViewSet, TagViewSet, PostViewSet, CommentViewSet, ContactMessageViewSet, 
    CustomUserCreateAPIView, CustomUserRetrieveAllAPIView, CustomUserRetrieveOneAPIView,
    CustomUserUpdateAPIView, CustomUserDeleteAPIView, CustomUserDisableAPIView, CustomUserEnableAPIView
)

# user_router = DefaultRouter()
blog_router = DefaultRouter()
contact_router = DefaultRouter()

blog_router.register(r'categories', CategoryViewSet)
blog_router.register(r'tags', TagViewSet)
blog_router.register(r'posts', PostViewSet)
blog_router.register(r'comments', CommentViewSet)

contact_router.register(r'contactmessages', ContactMessageViewSet)

# user_router.register(r'register', CustomUserCreateAPIView, basename='register')
# user_router.register(r'login', obtain_auth_token, basename='login')
# user_router.register(r'retrieve', CustomUserRetrieveAllAPIView, basename='all-users')
# user_router.register(r'retrieve/<int:pk>', CustomUserRetrieveOneAPIView, basename='user-detail')
# user_router.register(r'update/<int:pk>', CustomUserUpdateAPIView, basename='user-update')
# user_router.register(r'delete/<int:pk>', CustomUserDeleteAPIView, basename='user-delete')
# user_router.register(r'disable/<int:pk>', CustomUserDisableAPIView, basename='user-disable')
# user_router.register(r'enable/<int:pk>', CustomUserEnableAPIView, basename='user-enable')

urlpatterns = [
    path('users/register/', CustomUserCreateAPIView.as_view(), name='register'),
    path('users/login/', obtain_auth_token, name='login'),
    path('users/', CustomUserRetrieveAllAPIView.as_view(), name='all-users'),
    path('users/<int:pk>/', CustomUserRetrieveOneAPIView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', CustomUserUpdateAPIView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', CustomUserDeleteAPIView.as_view(), name='user-delete'),
    path('users/<int:pk>/disable/', CustomUserDisableAPIView.as_view(), name='user-disable'),
    path('users/<int:pk>/enable/', CustomUserEnableAPIView.as_view(), name='user-enable'),

    path('blog/', include(blog_router.urls)),
    path('contact/', include(contact_router.urls)),
]
