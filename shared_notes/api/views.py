from rest_framework import generics

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
    queryset = User.objects.all()
    serializer_class = NoteSerializer
