from django.shortcuts import render, get_object_or_404
from .models import Shareable, Orig_Sharer
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)
from .forms import ShareableForm


def IndexView(request):
	user = User
	context = {
		'shareables': Shareable.objects.all().order_by('-id'),
		'credits': Orig_Sharer.objects.all()
	}
	# template_folder/html_file
	return render(request, 'shareable/home.html', context)


class ShareableCreateView(LoginRequiredMixin, CreateView):		
	model = Shareable
	form_class = ShareableForm
	template_name = 'shareable/add_shareable.html'
	success_message = "Shared!"
	success_url = '/shareable'		# using this takes the user to a specific page after posting

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	# set the author to the current logged-in user
		return super().form_valid(form)


class ShareableUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Shareable 
	form_class = ShareableForm	# forumPostForm was the one used in the tutorials
	template_name = 'shareable/update_shareable.html'
	success_message = "Updated!"
	# success_url = '/forum'

	def form_valid(self, form):			
		form.instance.author = self.request.user 	#to automatically get the id of the current logged-in user as the author
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False


class ShareableDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = Shareable
	template_name = 'shareable/delete_shareable.html'
	success_url = '/shareable'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False	


class Orig_SharerCreateView(LoginRequiredMixin, CreateView):
	'''
		Take note that this view may only be intended for admins. If the site has many users all of users of the site are able to access
		this page, category list for posts may become chaotic. Please handle appropriately and have it removed if needed.
	'''	
	model = Orig_Sharer
	fields = '__all__'
	template_name = 'shareable/add_sharer.html'
	success_url = '/shareable'		

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	# set the author to the current logged-in user
		return super().form_valid(form)

def Orig_SharerView(request, sharer):
	category_posts = Orig_Sharer.objects.filter(sharer=orig_sharer)
	context = {
		'sharer': sharer,
		# 'category_posts': category_posts,
	}
	return render(request, 'shareable/sharers.html', context)