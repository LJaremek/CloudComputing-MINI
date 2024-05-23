from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    pass_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users"


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    shared_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notes"


class SharedNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    shared_at = models.DateTimeField(auto_now=True)
    permission_type = models.CharField(max_length=50)

    class Meta:
        db_table = "shared_notes"
