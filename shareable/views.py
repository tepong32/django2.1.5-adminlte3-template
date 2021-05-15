from django.shortcuts import render, get_object_or_404
from .models import Shareable, Orig_Sharer
from django.contrib.auth.models import User

# from .forms import PostForm, PostCommentForm
# from django.http import HttpResponseRedirect
# from django.urls import reverse


def IndexView(request):
	user = User
	context = {
		'shareables': Shareable.objects.all(),
		'credits': Orig_Sharer.objects.all()
	}
	# template_folder/html_file
	return render(request, 'shareable/home.html', context)
