from django.contrib import admin

from network.models import User, Profile, Post

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Profile)