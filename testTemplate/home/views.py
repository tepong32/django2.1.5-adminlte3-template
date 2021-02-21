from django.shortcuts import render
# from .models import Announcement, Quote
# from todo.models import ToDoList
# from forum.models import Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# for needing user to be logged-in first before accessing the page requested
from django.contrib.auth.decorators import login_required


# def landing(request):
# 	user = User
# 	users = User.objects.all()
# 	# authorPost = Post.objects.all().filter(author__in=users)
# 	# postCount = authorPost.count()
# 	# posts = Post.objects.all().order_by("-date_posted")[:5]
# 	context = {
# 		# "postCount": postCount,
# 		# "posts": posts,
# 		"users": users,
# 		"usercount": users.count(),
# 	}
# 	if user == request.user:
# 		return render(request, 'home_authed/base.html', context)
# 	else:
# 		return render(request, 'home/home.html', context)


@login_required
def home(request):
	user = User
	user_list = User.objects.all()
	# announcements = Announcement.objects.all().order_by("-date_posted")
	#paginator = Paginator(user_list, 10) # not yet implemented
	context = {
		# 'todos': ToDoList.objects.filter(author=request.user).order_by("finish_by"),
		# 'posts': Post.objects.all().order_by("-date_posted"),
		'users': user_list,
		# 'announcements': announcements,
		# 'quotes': Quote.objects.all()
	}
	# template_folder/html_file
	return render(request, 'home/index.html', context)


# def about(request):
# 	user = User
# 	context = {}
# 	return render(request, 'home_unauthed/about.html', context)

# def announcement(request):
# 	user = User
# 	announcements = Announcement.objects.all().order_by("-date_posted")
# 	context = {
# 		'user_count': user.objects.count(),
# 		'announcements': announcements,
# 	}

# 	return render(request, 'home_authed/announcements.html', context)


