from django.contrib import admin

# Register your models here.
from Comments.models import Comment

admin.site.register(Comment)
