from django.db import models
from django.utils import timezone	# for "default" argument in DateTimeField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Orig_Sharer(models.Model):
	# use this as the dropdown option for every Shareable's orig_sharer attribute
	name = models.CharField(max_length=50)
	profile_link1 = models.URLField(max_length=150) # at least one link is needed
	profile_link2 = models.URLField(max_length=150, blank=True, null=True, help_text="Not needed if sharer has no other profile links.")
	profile_link3 = models.URLField(max_length=150, blank=True, null=True, help_text="Not needed if sharer has no other profile links.")

	def __str__(self):
		return self.name.title() # .title() to capitalize the first letter of every word

	def get_absolute_url(self):
		return reverse('shareables-home')


class Shareable(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(default='', blank=True)	# work on slugifying titles as, currently, they show post IDs on url
	# header image
	def shareable_header_directory(instance, filename):
		return 'users/{}/shareable_images/{}/header/{}'.format(instance.author.username, instance.title, filename)
	header_image = models.ImageField(null=True, blank=True, upload_to=shareable_header_directory)

	content = RichTextUploadingField(blank=True, null=True)#models.TextField(blank=True, null=True)
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	orig_sharer = models.TextField(max_length=255, default="Item/Information was duly researched by the author.")

	# likes = models.ManyToManyField(User, related_name = "posts", blank=True) # "posts" was used in views.py's context_object_name
	# def total_likes(self):
	# 	return self.likes.count()

	category = models.CharField(max_length=50, default="E-book", help_text="Send me an email if there's no correct category for your share. :)")

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('shareable-detail', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Shareable, self).save(*args, **kwargs)
		# downsizing header_image, if there's any
		if self.header_image:
			header_img = Image.open(self.header_image.path)			# open the image of the current instance
			if header_img.height > 700 or header_img.width > 700:	# for sizing-down the images to conserve memory in the server
				output_size = (700, 700)
				header_img.thumbnail(output_size)
				header_img.save(self.header_image.path)