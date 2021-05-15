
from django.urls import path, include

# from django documentation -- check CoreyMS' django tutorial Part 8 / 22:30
from .views import (
    UserPostFilter,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    ForumHomeView,
    CategoryView,   # this is a function-based view
    CategoryCreateView,
    LikeView,
    CommentCreateView,
    PostCommentCreateView,
    )
# alternatively, you can just use "from . import views".
# however, importing views one-by-one seems to be a better option so you can remember which views you have already worked on.


urlpatterns = [
    path('', ForumHomeView.as_view(), name="forum-home"),             # homepage for blog app
    path('post/new/', PostCreateView.as_view(), name='post-new'),
    path('post/detail/<int:pk>/add-comment/', PostCommentCreateView.as_view(), name='add-comment'), # not working yet
    path('post/detail/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/detail/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<str:username>/', UserPostFilter.as_view(), name='user-posts'),     # filters applied to posts
    path('post/add-category/', CategoryCreateView.as_view(), name='add-category'),
    path('post/category/<str:cats>/', CategoryView, name='category'),
    path('post/detail/<int:pk>/like/', LikeView, name='like_post'),
    ]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)