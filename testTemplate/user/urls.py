
from django.urls import path, include
from . import views

# app_name = 'users'

urlpatterns = [
	# func-based view
    # path('register/', views.register, name='register' ),	# transferred to src.urls
    path('<username>/', views.profile, name='profile' ),
    path('<username>/edit/', views.profile_edit, name='profile-edit' ),
]

