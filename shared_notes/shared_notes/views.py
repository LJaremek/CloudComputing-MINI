from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from api.models import User, Note, SharedNote
from shared_notes.forms import NoteForm
from .forms import ProfileForm, ShareNoteForm


def index(request):
    return render(request, "index.html")


def create_user(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = DjangoUser.objects.create_user(
                username=cleaned_data["username"],
                email=cleaned_data["email"],
                password=cleaned_data["password"],
            )
            profile = User(
                username=cleaned_data["username"],
                email=cleaned_data["email"],
                user=user,
            )
            profile.save()
            return redirect("index")
    else:
        form = ProfileForm()
    context = {"form": form}
    return render(request, "create_user.html", context)


def own_profile(request):
    if request.user.is_authenticated:
        profile = User.objects.get(user=request.user.id)

        context = {"profile": profile}
    else:
        context = {}
    return render(request, "profile.html", context)


def logout_view(request):
    logout(request)
    return redirect("index")


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
        return render(request, "notes.html", {"notes": notes})
    else:
        return redirect("/accounts/login")


@login_required
def view_note(request, note_id):
    note = get_object_or_404(Note, id_note=note_id)
    is_owner = False
    has_edit_permission = False

    # Check if the current user is the owner of the note
    if note.id_user.user == request.user:
        is_owner = True
        has_edit_permission = True
    else:
        # Check if the note is shared with the current user
        try:
            shared_note = SharedNote.objects.get(
                id_note=note, id_user__user=request.user
            )
            if shared_note.permission_type == "write":
                has_edit_permission = True
        except SharedNote.DoesNotExist:
            pass

    if is_owner or has_edit_permission or shared_note:
        return render(
            request,
            "view_note.html",
            {
                "note": note,
                "is_owner": is_owner,
                "has_edit_permission": has_edit_permission,
            },
        )
    else:
        return HttpResponseForbidden("You do not have permission to view this note.")


def shared_notes(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(user=request.user)
        shared_notes = SharedNote.objects.filter(id_user=current_user)
        return render(request, "shared_notes.html", {"shared_notes": shared_notes})
    else:
        return redirect("/accounts/login")


def share_note(request, note_id):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, id_note=note_id, id_user__user=request.user)
        if request.method == "POST":
            form = ShareNoteForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                permission_type = form.cleaned_data["permission_type"]
                try:
                    user = DjangoUser.objects.get(email=email)
                    shared_user = User.objects.get(user=user)
                    shared_note = SharedNote.objects.create(
                        id_user=shared_user,
                        id_note=note,
                        permission_type=permission_type,
                    )
                    shared_note.save()
                    return redirect("notes")
                except ObjectDoesNotExist:
                    form.add_error("email", "User with this email does not exist.")
        else:
            form = ShareNoteForm()
        return render(request, "share_note.html", {"form": form, "note": note})
    else:
        return redirect("/accounts/login")


def delete_note(request, note_id):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, id_note=note_id, id_user__user=request.user)
        note.delete()
        return redirect("notes")
    else:
        return redirect("/accounts/login")


def edit_note(request, note_id):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, id_note=note_id)
        if note.id_user.user == request.user:
            user_has_permission = True
        else:
            try:
                shared_note = SharedNote.objects.get(
                    id_note=note, id_user__user=request.user
                )
                user_has_permission = shared_note.permission_type == "write"
            except SharedNote.DoesNotExist:
                user_has_permission = False
        if user_has_permission:
            if request.method == "POST":
                form = NoteForm(request.POST, instance=note)
                if form.is_valid():
                    form.save()
                    return redirect("notes")
            else:
                form = NoteForm(instance=note)
            return render(
                request,
                "edit_note.html",
                {
                    "form": form,
                    "note": note,
                    "user_has_permission": user_has_permission,
                },
            )
        else:
            return render(
                request, "edit_note.html", {"user_has_permission": user_has_permission}
            )
    else:
        return redirect("/accounts/login")
