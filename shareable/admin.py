from django.contrib import admin
from .models import Shareable, Orig_Sharer

admin.site.register(Shareable)
admin.site.register(Orig_Sharer)