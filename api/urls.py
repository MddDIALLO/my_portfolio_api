from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet, PostViewSet, CommentViewSet, ContactMessageViewSet

blog_router = DefaultRouter()
contact_router = DefaultRouter()

blog_router.register(r'categories', CategoryViewSet)
blog_router.register(r'tags', TagViewSet)
blog_router.register(r'posts', PostViewSet)
blog_router.register(r'comments', CommentViewSet)

contact_router.register(r'contactmessages', ContactMessageViewSet)

urlpatterns = [
    path('blog/', include(blog_router.urls)),
    path('contact/', include(contact_router.urls)),
]
