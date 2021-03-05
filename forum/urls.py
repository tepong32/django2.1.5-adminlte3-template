
from django.urls import path, include

# from django documentation -- check CoreyMS' tutorial Part 8 / 22:30
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    UserPostFilter_Authed,
    PostDetailView_Authed,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    ForumIndexView,
    LikeView,
    CommentCreateView
    )


urlpatterns = [
    path('', ForumIndexView.as_view(), name="forum-home"),             # home for blog app
    path('post/new/', PostCreateView.as_view(), name='post-new'),
    path('post/detail/<int:pk>/add-comment/', CommentCreateView.as_view(), name='add-comment'),
    # path('post/quick-create/', PostCreateViewModal.as_view(), name='quickpost'),
    path('post/detail/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/detail/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/detail/<int:pk>/', PostDetailView_Authed.as_view(), name='post-detail'),
    # filters applied to posts
    path('posts/<str:username>/', UserPostFilter_Authed.as_view(), name='user-posts'),
    path('post/detail/<int:pk>/like/', LikeView, name='like_post'),
    ]


