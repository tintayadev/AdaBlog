from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostListCreateView, PostDetailView, post_list, post_detail

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Para obtener tokens
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', post_list, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail-template'),
]