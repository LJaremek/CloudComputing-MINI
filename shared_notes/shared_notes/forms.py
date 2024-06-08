from django import forms
from django import forms
from django.contrib.auth.models import User as DjangoUser

from api.models import User, Note, SharedNote


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["content"]


class ProfileForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if DjangoUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if DjangoUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


class ShareNoteForm(forms.Form):
    email = forms.EmailField()
    permission_type = forms.ChoiceField(choices=[('read', 'Read'), ('write', 'Write')])
