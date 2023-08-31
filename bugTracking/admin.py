from django.contrib import admin
from .models import Bug, User, Project

admin.site.register(Bug)
admin.site.register(User)
admin.site.register(Project)
