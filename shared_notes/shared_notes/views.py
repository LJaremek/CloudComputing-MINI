from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User as DjangoUser
from api.models import User, Note, SharedNote
from .forms import  ProfileForm, ShareNoteForm
from django.contrib.auth import logout
from shared_notes.forms import NoteForm



def index(request):
    return render(request, 'index.html')


def create_user(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = DjangoUser.objects.create_user(cleaned_data["username"], password=cleaned_data["password"])
            profile = User(username=cleaned_data["username"],
                           email=cleaned_data["email"],
                                user=user,
                                )
            profile.save()

            form = ProfileForm()
    else:
        form = ProfileForm()
    context = {"form": form}
    return render(request, 'create_user.html', context)

def own_profile(request):
    if request.user.is_authenticated:
        profile = User.objects.get(user=request.user.id)


        context = {"profile": profile}
    else:
        context = {}
    return render(request, "profile.html", context)

def logout_view(request):
    logout(request)
    return redirect('index')

def new_note(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NoteForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.id_user = request.user.user
                note.save()
                form = NoteForm()
        else:
            form = NoteForm()
        context = {"form": form}
        return render(request, "new_note.html", context)
    else:
        return redirect("/accounts/login")

def notes(request):
    if request.user.is_authenticated:
        current_user = request.user
        notes = Note.objects.filter(id_user__user=current_user)
        return render(request, 'notes.html', {'notes': notes})
    else:
        return redirect("/accounts/login")


def view_note(request, note_id):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, id_note=note_id, id_user__user=request.user)
        return render(request, 'view_note.html', {'note': note})
    else:
        return redirect("/accounts/login")
    
def shared_notes(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(user=request.user)
        shared_notes = SharedNote.objects.filter(id_user=current_user)
        return render(request, 'shared_notes.html', {'shared_notes': shared_notes})
    else:
        return redirect("/accounts/login")
    
def share_note(request, note_id):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, id_note=note_id, id_user__user=request.user)
        if request.method == 'POST':
            form = ShareNoteForm(request.POST)
            if form.is_valid():
                shared_note = form.save(commit=False)
                shared_note.id_note = note
                shared_note.id_user = User.objects.get(user=request.user)
                shared_note.save()
                return redirect('notes')
        else:
            form = ShareNoteForm()
        return render(request, 'share_note.html', {'form': form, 'note': note})
    else:
        return redirect("/accounts/login")
    
def delete_note(request, note_id):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, id_note=note_id, id_user__user=request.user)
        note.delete()
        return redirect('notes')
    else:
        return redirect("/accounts/login")

def edit_note(request, note_id):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, id_note=note_id, id_user__user=request.user)
        if request.method == 'POST':
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                return redirect('notes')
        else:
            form = NoteForm(instance=note)
        return render(request, 'edit_note.html', {'form': form, 'note': note})
    else:
        return redirect("/accounts/login")
