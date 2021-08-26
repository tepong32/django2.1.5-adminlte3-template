from django.shortcuts import render, get_object_or_404
from .models import Freebie, Orig_Sharer
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)
from .forms import FreebieForm


def IndexView(request):
	user = User
	context = {
		'freebies': Freebie.objects.all().order_by('-id'),
		'credits': Orig_Sharer.objects.all()
	}
	return render(request, 'freebie/home.html', context)


class FreebieCreateView(LoginRequiredMixin, CreateView):		
	model = Freebie
	form_class = FreebieForm
	template_name = 'freebie/add_freebie.html'
	success_message = "Shared!"
	success_url = '/freebies'		# using this takes the user to a specific page after posting

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	# set the author to the current logged-in user
		return super().form_valid(form)

class FreebieDetailView(DetailView):
	model = Freebie
	context_object_name = 'freebie'
	template_name = 'freebie/freebie_detail.html'


class FreebieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Freebie 
	form_class = FreebieForm	# forumPostForm was the one used in the tutorials
	template_name = 'freebie/update_freebie.html'
	success_message = "Updated!"
	success_url = '/freebies'

	def form_valid(self, form):			
		form.instance.author = self.request.user 	#to automatically get the id of the current logged-in user as the author
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False


class FreebieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = Freebie
	template_name = 'freebies/delete_freebie.html'
	success_url = '/freebies'

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
	template_name = 'freebie/add_sharer.html'
	success_url = '/freebies'		

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	# set the author to the current logged-in user
		return super().form_valid(form)

def Orig_SharerView(request, sharer):
	category_posts = Orig_Sharer.objects.filter(sharer=orig_sharer)
	context = {
		'sharer': sharer,
		# 'category_posts': category_posts,
	}
	return render(request, 'freebie/sharers.html', context)