from django.urls import path
# from rest_framework_swagger.views import get_swagger_view

from .views import CreateUserView, CreateNoteView
from .views import SharedNoteView
from .views import ListUsersView, ListNotesView
from .views import DeleteNoteView, DeleteUserView, DeleteSharedView

# schema_view = get_swagger_view(title="API Documentation")

urlpatterns = [
    # path("swagger/", schema_view, name="swagger"),

    path("create_user/", CreateUserView.as_view(), name="create_user"),
    path("create_note/", CreateNoteView.as_view(), name="create_note"),

    path("share_note/", SharedNoteView.as_view(), name="share_note"),

    path("delete_note/<int:note_id>/", DeleteNoteView.as_view(), name="delete_note"),
    path("delete_user/<int:user_id>/", DeleteUserView.as_view(), name="delete_user"),
    path("delete_shared/<int:shared_id>/", DeleteSharedView.as_view(), name="delete_shared"),

    path("users/", ListUsersView.as_view(), name="list_users"),
    path("notes/", ListNotesView.as_view(), name="list_notes"),
]
