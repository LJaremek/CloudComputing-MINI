from rest_framework import serializers

from .models import User, Note, SharedNote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id_user", "username", "email", "pass_hash"]


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id_note", "id_user", "content", "created_at", "updated_at"]


class SharedNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedNote
        fields = [
            "id_shared", "id_user", "id_note", "shared_at", "permission_type"
            ]


class SharedNoteDetailSerializer(serializers.ModelSerializer):
    note_id = serializers.IntegerField(source="id_note.id_note")
    permission_type = serializers.CharField(source="permission_type")

    class Meta:
        model = SharedNote
        fields = ["note_id", "permission_type"]
