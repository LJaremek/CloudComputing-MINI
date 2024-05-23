from rest_framework import serializers

from .models import User, Note, SharedNote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'pass_hash']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'user', 'content', 'created_at', 'shared_at']


class SharedNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedNote
        fields = ['id', 'user', 'note', 'shared_at', 'permission_type']
