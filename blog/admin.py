from django.contrib import admin
from .models import Post, PostComment, Category, BlogReminder, Tags

# Register your models here.


admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Category)
admin.site.register(BlogReminder)
admin.site.register(Tags)