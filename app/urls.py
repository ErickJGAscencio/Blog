from django.urls import path
from . import views
from .views import (
    UserProfileView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('register/', register, name='register'),
    
    path('user/<str:username>/', UserProfileView.as_view(), name='user-profile'),
    path('profile/', views.profile, name='profile'),
    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
