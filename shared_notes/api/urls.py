from django.urls import path

from .views import CreateUserView, CreateNoteView
from .views import SharedNoteView
from .views import ListUsersView, ListNotesView
from .views import DeleteNoteView

urlpatterns = [
    path("create_user/", CreateUserView.as_view(), name="create_user"),
    path("create_note/", CreateNoteView.as_view(), name="create_note"),

    path("share_note/", SharedNoteView.as_view(), name="share_note"),

    path("delete_note/<int:note_id>/", DeleteNoteView.as_view(), name="delete_note"),

    path("users/", ListUsersView.as_view(), name="list_users"),
    path("notes/", ListNotesView.as_view(), name="list_notes"),
]
