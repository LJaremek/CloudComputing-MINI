from django.contrib import admin
from api.models import Note, User, SharedNote

# Register your models here.
admin.register(User, Note, SharedNote)