"""shared_notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", views.index, name='index'),
    path("create_user", views.create_user, name="create_user"),
    path('accounts/logout/', views.logout_view, name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.own_profile, name="profile"),
    path("new_note", views.new_note, name="new_note"),
    path('notes', views.notes, name="notes"),
    path('note/<int:note_id>/', views.view_note, name='view_note'),
    path('shared_notes', views.shared_notes, name='shared_notes'),
    path('note/<int:note_id>/share', views.share_note, name='share_note'),
    path('note/<int:note_id>/delete', views.delete_note, name='delete_note'),
    path('note/<int:note_id>/edit', views.edit_note, name='edit_note'),
]
