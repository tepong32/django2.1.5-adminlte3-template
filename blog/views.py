from django.shortcuts import render, get_object_or_404
from .models import Post, PostComment, Category, BlogReminder
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
class BlogHomeView(ListView):
    context_object_name = 'posts'    
    template_name = 'blog/home.html'
    queryset = Post.objects.all()
    ordering = ['-date_posted']			# filter for newest post first
    paginate_by = 10					# number of posts to show per page

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        '''
        	This function was used to override the "context" variable on the class-based view.
        	Think of this as a way of doing 
        	context = { 'xxx': xxx.objects.all(),
        				'yyy': yyy.objects.all()
        				}
        	in a function-based view.
        	See 'home.views.home' for a better reference.
        '''
        # context['entertainment'] = blogPost.objects.filter(tag="Entertainment").order_by('-date_posted')
        # context['help'] = blogPost.objects.filter(tag="Help!").order_by('-date_posted')
        # context['hobby'] = blogPost.objects.filter(tag="Hobby").order_by('-date_posted')
        # context['jokes'] = blogPost.objects.filter(tag="Jokes").order_by('-date_posted')
        # context['school'] = blogPost.objects.filter(tag="School").order_by('-date_posted')
        # context['social'] = blogPost.objects.filter(tag="Social").order_by('-date_posted')
        context['reminders'] = BlogReminder.objects.all()
        # and so on for more models
        return context


class UserPostFilter(ListView):
	model = Post 			
	template_name = 'blog/userposts.html'
	context_object_name = 'posts'		# getting the 'posts' key from "context = {'posts': Post.objects.all(),}"
	ordering = ['-date_posted']
	paginate_by = 10	

	def get_queryset(self):		# this defines the filter for the specific user's posts
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView): # LoginRequiredMixin for authed users
	model = Post
	template_name = 'blog/postdetail.html'
	posts = Post.objects.all()
	context = {
		'posts': posts,
		'comments': PostComment.objects.filter(post=posts),
	}


class PostCreateView(LoginRequiredMixin, CreateView):		
	model = Post
	form_class = PostForm
	template_name = 'blog/postcreateform.html'
	success_message = "Successfully posted!"
	success_url = '/blogs'		# using this takes the user to a specific page after posting

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	# set the author to the current logged-in user
		return super().form_valid(form)
		

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post 
	form_class = PostForm	# blogPostForm was the one used in the tutorials
	template_name = 'blog/postupdateform.html'
	success_message = "Post updated"
	# success_url = '/blog'

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
	template_name = 'blog/postconfirmdelete.html'
	success_url = '/blog'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False		

class CategoryCreateView(LoginRequiredMixin, CreateView):
	'''
		Take note that this view may only be intended for admins. If the site has many users all of users of the site are able to access
		this page, category list for posts may become chaotic. Please handle appropriately and have it removed if needed.
	'''	
	model = Category
	fields = '__all__'
	template_name = 'blog/categorycreateform.html'
	success_url = '/blogs'		

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	# set the author to the current logged-in user
		return super().form_valid(form)

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats)
	context = {
		'cats': cats,
		'category_posts': category_posts,
	}
	return render(request, 'blog/categories.html', context)




from django.contrib.auth.decorators import login_required

'''
	login_required decorator was placed here to avoid showing a 404 page when an unauthed user
	tries to hit the like button for a post
'''
@login_required
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









# NOT WORKING!!!!!!!!!!!!!!!!!
from django.urls import reverse_lazy
from .forms import PostCommentModelForm
from bootstrap_modal_forms.generic import BSModalCreateView

class PostCommentCreateView(BSModalCreateView):
	# model = PostComment
	template_name = 'blog/comment_form.html'
	form_class = PostCommentModelForm
	success_message = "Comment added"
	success_url = reverse_lazy('blog')






# not being used ATM
class CommentCreateView(LoginRequiredMixin, CreateView):		
	model = Post
	form_class = PostCommentForm
	template_name = 'blog/comment_form.html'
	success_message = "Comment added"
	success_url = '/home/'		# using this takes the user to a specific page after posting

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	# set the author to the current logged-in user
		return super().form_valid(form)



