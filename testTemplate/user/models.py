from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from ckeditor.fields import RichTextField


# remember to register each model to the admin.py file EVERYTIME!

class Profile(models.Model):
	'''
		TIP: Activate Wordwrap so you will not have to scroll side-ways.
		I designed this Profile model to fit the very first website I worked on. I just commented-out those attributes I think is not necessary for a default user profile for a new website. I figured leaving those attributes here will save you time researching and help in giving you ideas on how...(what do you call this..?)...certain attributes can be formatted? UGH! I know you know what I mean! LOL! Apologies for unorganized thought-processing.
	'''

	# profile-related stuffs 
	user = models.OneToOneField(User, on_delete=models.CASCADE) # if the user is deleted, the profile will be deleted, too
	display_name = models.CharField(blank=True, max_length=50, unique=True, verbose_name="Display Name",help_text="Get an alias for anonimity. We'll be using this later. Trust me. ;)") 
	Male = "Male"
	Female = "Female"
	Neutral = "Neutral"
	gender_choice = [
		(Male, "Male"),
		(Female, "Female"),
		(Neutral, "Neutral")
	]
	gender = models.CharField(
		max_length=10,
		choices=gender_choice,
		default=Neutral, verbose_name="Gender"
	)
	location = models.CharField(blank=True, null=True, max_length=255, default="Uh...Earth?", verbose_name="location", help_text="Do you want to fill this out? :D")

	# Other information that can be displayed on a user profile page:
	quote = models.CharField(blank=True, max_length=300, verbose_name="Quote you live by", help_text="'Pampa-Angas'")
	about_me = models.TextField(blank=True, default="...Default About Me text created by the dev... :D", help_text="People here love to read. Tell us something about you.")
	
	def dp_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/DP_<username>/<filename> ---check settings.py. MEDIA_ROOT=media
		return 'users/{}/DP/{}'.format(instance.user.username, filename)
	image = models.ImageField(default='defaults/round.png', blank=True, upload_to=dp_directory_path, verbose_name="Profile Picture", help_text='Tick "clear" if an image already exists.')

	# # education / school info
	# school = models.CharField(blank=True, null=True, max_length=100, default="Secret University", verbose_name="School", help_text="Might help you find co-university people. ;)")
	# course = models.CharField(blank=True, null=True, max_length=255, default="---", verbose_name="Course", help_text="Leave blank if n/a.")
	# FRESHMAN = 'Freshman'
	# SOPHOMORE = 'Sophomore'
	# JUNIOR = 'Junior'
	# SENIOR = 'Senior'
	# GRADUATE = 'Graduate'
	# YEAR_IN_SCHOOL_CHOICES = [
	# 	(FRESHMAN, 'Freshman'),
	# 	(SOPHOMORE, 'Sophomore'),
	# 	(JUNIOR, 'Junior'),
	# 	(SENIOR, 'Senior'),
	# 	(GRADUATE, 'Graduate'),
	# ]
	# year_in_school = models.CharField(
	# 	max_length=10,
	# 	choices=YEAR_IN_SCHOOL_CHOICES,
	# 	default=FRESHMAN, verbose_name="Grade/Year Level"
	# )

	# # socmed
	# google = models.CharField(max_length=150, blank=True, null=True, verbose_name="Google", help_text="Kindly post full url (e.g.: https://username@email.com. Leave blank if not available.")
	# linkedin = models.CharField(max_length=150, blank=True, null=True, verbose_name="LinkedIn", help_text="Kindly post full url. (e.g.: https://username@email.com. Leave blank if not available.")
	# github = models.CharField(max_length=150, blank=True, null=True, verbose_name="GitHub", help_text="Kindly post full url. (e.g.: https://username@email.com. Leave blank if not available.")
	# facebook = models.CharField(max_length=150, blank=True, null=True, verbose_name="Facebook", help_text="Kindly post full url. (e.g.: https://username@email.com. Leave blank if not available.")
	# twitter = models.CharField(max_length=150, blank=True, null=True, verbose_name="Twitter", help_text="Kindly post full url. (e.g.: https://username@email.com. Leave blank if not available.")
	# instagram = models.CharField(max_length=150, blank=True, null=True, verbose_name="Instagram", help_text="Kindly post full url. (e.g.: https://username@email.com. Leave blank if not available.")
	
	# # these user_group will work like a status ladder // think of it like symbianize user badges
	# # or use a "# of thanks/appreciation received for posts" ladder system in the future
	# Pawn = "Pawn"
	# Rook = "Rook"
	# Knight = "Knight"
	# Bishop = "Bishop"
	# Queen = "Queen"
	# King = "King"
	# user_group_choices = [
	# 	(Pawn, "Pawn"),
	# 	(Rook, "Rook"),
	# 	(Knight, "Knight"),
	# 	(Bishop, "Bishop"),
	# 	(Queen, "Queen"), # should this be removed?
	# 	(King, "King"),
	# ]
	# user_group = models.CharField(
	# 	max_length=10,
	# 	choices=user_group_choices,
	# 	default=Pawn,
	# )

	# profile_snippet = RichTextField(blank=True, null=True, help_text="This is what un-logged-in users see whenever they click on your username. Make your intro count! ;)")
	
	# # user_group descriptions
	# def title(self): 
	# 	if self.user_group == "Pawn":
	# 		if self.gender == "Male":
	# 			self.title = "Average Joe"
	# 		elif self.gender == "Female":
	# 			self.title = "Average Jane"
	# 		elif self.gender == "Unicorn":
	# 			self.title = "Average Unicorn"
	# 		return self.title

	# 	if self.user_group == "Rook":
	# 		if self.gender == "Male":
	# 			self.title = "Average Joe Pro Plus"
	# 		elif self.gender == "Female":
	# 			self.title = "Average Jane Pro Plus"
	# 		elif self.gender == "Unicorn":
	# 			self.title = "Average Unicorn Pro Plus"
	# 		return self.title

	# 	if self.user_group == "Knight":
	# 		if self.gender == "Unicorn":
	# 			self.title = "A helpful Unicorn"
	# 		else:
	# 			self.title = "We're helping people out."
	# 		return self.title

	# 	if self.user_group == "Bishop":
	# 		if self.gender == "Unicorn":
	# 			self.title = "Powerful Unicorn. Beware."
	# 		else:
	# 			self.title = "A little less powerful than devs"
	# 		return self.title

	# 	if self.user_group == "Queen":
	# 		if self.gender == "Female":
	# 			self.title = "A Queen. You know what that means."
	# 		elif self.gender == "Unicorn":
	# 			self.title = "Queen Unicorn! MeEe-ee-ee! (what?)"
	# 		return self.title

	# 	if self.user_group == "King":
	# 		self.title = "Dev / Admin ;)"
	# 		return self.title

	def __str__(self):
		return f"{self.user.username}"

	def get_absolute_url(self):
		return reverse('profile', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):		# for resizing/downsizing images
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)	# open the image of the current instance
		if img.height > 600 or img.width > 600:	# for sizing-down the images to conserve memory in the server
			output_size = (600, 600)
			img.thumbnail(output_size)
			img.save(self.image.path)

