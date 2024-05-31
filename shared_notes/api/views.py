from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .serializers import UserSerializer, NoteSerializer, SharedNoteSerializer
from .serializers import SharedNoteDetailSerializer
from .models import User, Note, SharedNote


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateNoteView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class ShareNoteView(generics.CreateAPIView):
    queryset = SharedNote.objects.all()
    serializer_class = SharedNoteSerializer


class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListNotesView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class DeleteNoteView(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_url_kwarg = 'note_id'

    def delete(self, request, *args, **kwargs):
        note = self.get_object()
        self.perform_destroy(note)
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteSharedNoteView(generics.DestroyAPIView):
    queryset = SharedNote.objects.all()
    serializer_class = SharedNoteSerializer
    lookup_url_kwarg = "shared_note_id"

    def delete(self, request, *args, **kwargs):
        shared_note = self.get_object()
        self.perform_destroy(shared_note)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SharedNotesListView(generics.ListAPIView):
    serializer_class = SharedNoteDetailSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return SharedNote.objects.filter(id_user=user_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class NoteDetailView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = "id_note"


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id_user"
