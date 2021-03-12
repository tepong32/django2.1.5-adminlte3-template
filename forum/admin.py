from django.contrib import admin
from .models import Post, PostComment, Category, ForumReminder

# Register your models here.


admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Category)
admin.site.register(ForumReminder)