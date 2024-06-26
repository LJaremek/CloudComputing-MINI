from django.db import models
from django.contrib.auth.models import User as DjangoUser


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)

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
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notes"
        indexes = [
            models.Index(fields=["id_user"]),
        ]


class SharedNote(models.Model):
    PERMISSION_CHOICES = [
        ('read', 'Read'),
        ('write', 'Write')
    ]
    id_shared = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, models.CASCADE, db_column="id_user")
    id_note = models.ForeignKey(Note, models.CASCADE, db_column="id_note")
    shared_at = models.DateTimeField(auto_now=True)
    permission_type = models.CharField(max_length=50, choices=PERMISSION_CHOICES)

    class Meta:
        db_table = "shared_notes"
        indexes = [
            models.Index(fields=["id_user"]),
            models.Index(fields=["id_note"]),
        ]
