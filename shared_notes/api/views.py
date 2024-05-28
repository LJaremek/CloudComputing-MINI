from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .serializers import UserSerializer, NoteSerializer, SharedNoteSerializer
from .models import User, Note, SharedNote


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateNoteView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class SharedNoteView(generics.CreateAPIView):
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
    lookup_url_kwarg = 'user_id'

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteSharedView(generics.DestroyAPIView):
    queryset = SharedNote.objects.all()
    serializer_class = SharedNoteSerializer
    lookup_url_kwarg = 'shared_id'

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
