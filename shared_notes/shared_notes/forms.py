from django import forms
from api.models import Note, SharedNote


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["content"]


class ProfileForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ShareNoteForm(forms.ModelForm):
    class Meta:
        model = SharedNote
        fields = ['id_user', 'permission_type']