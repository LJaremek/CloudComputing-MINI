from django.db import models


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    pass_hash = models.CharField(max_length=255)

    class Meta:
        db_table = "users"
        indexes = [
            models.Index(fields=["username"]),
            models.Index(fields=["email"]),
        ]


class Note(models.Model):
    id_note = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, models.CASCADE, db_column="id_user")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    shared_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notes"
        indexes = [
            models.Index(fields=["id_user"]),
        ]


class SharedNote(models.Model):
    id_shared = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, models.CASCADE, db_column="id_user")
    id_note = models.ForeignKey(Note, models.CASCADE, db_column="id_note")
    shared_at = models.DateTimeField(auto_now=True)
    permission_type = models.CharField(max_length=50)

    class Meta:
        db_table = "shared_notes"
        indexes = [
            models.Index(fields=["id_user"]),
            models.Index(fields=["id_note"]),
        ]
