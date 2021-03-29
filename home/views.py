from django.shortcuts import render
from .models import Announcement, Quote
# from todo.models import ToDoList
from forum.models import Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# for needing user to be logged-in first before accessing the page requested
from django.contrib.auth.decorators import login_required


# @login_required
def home(request):
	user = User
	user_list = User.objects.all()[:5]
	announcements = Announcement.objects.all().order_by("-date_posted")
	posts = Post.objects.all().order_by("-date_posted")[:10]
	postCount = Post.objects.all().count()
	context = {
		'announcements': announcements,
		'users': user_list,
		'posts': posts,
		'quotes': Quote.objects.all(),
		'usercount': user.objects.count(),
		'postCount': postCount,
	}
	# template_folder/html_file
	return render(request, 'home/index.html', context)


def about(request):
	user = User
	context = {}
	return render(request, 'home/about.html', context)

# def announcement(request):
# 	user = User
# 	announcements = Announcement.objects.all().order_by("-date_posted")
# 	context = {
# 		'user_count': user.objects.count(),
# 		'announcements': announcements,
# 	}

# 	return render(request, 'home_authed/announcements.html', context)


