from django import forms
from .models import Post, PostComment, Category


# See "Add blog categories - Django blog #12" by Codemy for explanation (around 7min mark)
# Note that only admins can add Category-s. For users, it'll only be a dropdown selector
categories = Category.objects.all().values_list('name', 'name')
categories_list = []

for item in categories:
	categories_list.append(item)

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)		# i think this can be removed since the same field is in the model?


    class Meta:
    	model = Post
    	fields = ['title', 'tag', 'category', 'content',]
    	# I removed header_image field ATM. Still thinking if it's worth including
    	widgets = {
    		# 'tag'
    		'category' : forms.Select(choices=categories, attrs={'class': 'form-control'})
    	}


class PostCommentForm(forms.ModelForm):
	class Meta:
		model = PostComment
		fields = ('content',)