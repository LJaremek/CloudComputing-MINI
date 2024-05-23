from django.urls import path

from .views import CreateUserView, CreateNoteView, SharedNoteView

urlpatterns = [
    path("create_user/", CreateUserView.as_view(), name="create_user"),
    path("create_note/", CreateNoteView.as_view(), name="create_note"),
    path("share_note/", SharedNoteView.as_view(), name="share_note"),
]
