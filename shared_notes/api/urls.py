from django.urls import path
# from rest_framework_swagger.views import get_swagger_view

from .views import CreateUserView, CreateNoteView, NoteDetailView, UserDetailView
from .views import ShareNoteView, SharedNotesListView
from .views import ListUsersView, ListNotesView
from .views import DeleteNoteView,  DeleteUserView, DeleteSharedNoteView

# schema_view = get_swagger_view(title="API Documentation")

urlpatterns = [
    # path("swagger/", schema_view, name="swagger"),

    path("create_user/", CreateUserView.as_view(), name="create_user"),
    path("create_note/", CreateNoteView.as_view(), name="create_note"),

    path("share_note/", ShareNoteView.as_view(), name="share_note"),

    path("delete_note/<int:note_id>/", DeleteNoteView.as_view(), name="delete_note"),
    path("delete_user/<int:user_id>/", DeleteUserView.as_view(), name="delete_user"),
    path("delete_shared_note/<int:shared_note_id>/", DeleteSharedNoteView.as_view(), name="delete_shared_note"),


    path("users/", ListUsersView.as_view(), name="list_users"),
    path("notes/", ListNotesView.as_view(), name="list_notes"),
    path("shared_notes/<int:user_id>/", SharedNotesListView.as_view(), name="shared_notes"),
    path("note/<int:id_note>/", NoteDetailView.as_view(), name="note_detail"),
    path("user/<int:id_user>/", UserDetailView.as_view(), name="user_detail"),
]
