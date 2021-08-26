from django.shortcuts import render
from .models import Announcement, Quote
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# for needing user to be logged-in first before accessing the page requested
from django.contrib.auth.decorators import login_required


# @login_required
def home(request):
	'''
		note how I used two ways to display info to the view:
		one was thru a variable passing it as the "value" for the dictionary key,
		the other is thru directly using the imported model as the "value".

		A bit messy but I was experimenting and didn't want to change it for future reference.
	'''
	user = User
	user_list = User.objects.all()[:5]
	announcements = Announcement.objects.all().order_by("-date_posted")
	context = {

		'announcements': announcements,
		'users': user_list,
		'quotes': Quote.objects.all(),
		'usercount': user.objects.count(),
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


