from django.shortcuts import render, get_object_or_404
from .models import Post, PostComment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	FormView,
	)
from .forms import PostForm, PostCommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse





# trying out multiple objects inside one class-based listView template
class ForumIndexView(ListView):
    context_object_name = 'posts'    
    template_name = 'forum/home.html'
    queryset = Post.objects.all()
    ordering = ['-date_posted']			# filter for newest post first
    paginate_by = 20					# number of posts to show per page

    def get_context_data(self, **kwargs):
        context = super(ForumIndexView, self).get_context_data(**kwargs)
        # context['entertainment'] = ForumPost.objects.filter(tag="Entertainment").order_by('-date_posted')
        # context['help'] = ForumPost.objects.filter(tag="Help!").order_by('-date_posted')
        # context['hobby'] = ForumPost.objects.filter(tag="Hobby").order_by('-date_posted')
        # context['jokes'] = ForumPost.objects.filter(tag="Jokes").order_by('-date_posted')
        # context['school'] = ForumPost.objects.filter(tag="School").order_by('-date_posted')
        # context['social'] = ForumPost.objects.filter(tag="Social").order_by('-date_posted')
        # context['tech'] = ForumPost.objects.filter(tag="Tech").order_by('-date_posted')
        # and so on for more models
        return context


class UserPostFilter_Authed(LoginRequiredMixin, ListView):
	model = Post 			
	template_name = 'forum/userposts.html'
	context_object_name = 'posts'		# getting the 'posts' key from "context = {'posts': Post.objects.all(),}"
	ordering = ['-date_posted']
	paginate_by = 20	

	def get_queryset(self):		# this defines the filter for the specific user's posts
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView_Authed(LoginRequiredMixin, DetailView): # LoginRequiredMixin for authed users
	model = Post
	template_name = 'forum/postdetail.html'
	posts = Post.objects.all()
	context = {'posts': posts,
				'comments': PostComment.objects.filter(post=posts),
	}


class PostCreateView(LoginRequiredMixin, CreateView):		
	model = Post
	form_class = PostForm
	template_name = 'forum/postcreateform.html'
	success_message = "Successfully posted!"
	#success_url = '/home/'		# using this takes the user to a specific page after posting

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	# set the author to the current logged-in user
		return super().form_valid(form)
		

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post 
	form_class = PostForm	# forumPostForm was the one used in the tutorials
	template_name = 'forum/postupdateform.html'
	success_message = "Post updated"
	success_url = '/forum'

	def form_valid(self, form):			
		form.instance.author = self.request.user 	#to automatically get the id of the current logged-in user as the author
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = Post
	template_name = 'forum/postconfirmdelete.html'
	success_url = '/home/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False		


def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


class CommentCreateView(LoginRequiredMixin, CreateView):		
	model = PostComment
	form_class = PostCommentForm
	template_name = 'forum/comment_form.html'
	success_message = "Comment added"
	success_url = '/home/'		# using this takes the user to a specific page after posting

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	# set the author to the current logged-in user
		return super().form_valid(form)



