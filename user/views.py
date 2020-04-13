from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from note_feed.models import Note, Notebook
from .forms import NoteForm


@login_required
def home(request):
    note_query = Note.objects.notes_for_user(request.user)

    return render(request, "user/home.html",
                  {'notes': list(note_query)})


@login_required
def new_note(request):
    if request.method == "POST":
        notebook = get_object_or_404(Notebook, person__username=request.user)
        note = notebook.new_note()
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_home')
    else:
        form = NoteForm()
    return render(request, "user/new_note_form.html", {'form': form})


@login_required
def delete_note(request, id):
    if request.method == "POST":
        note = get_object_or_404(Note, pk=id)
        note.delete_note()
        return redirect('user_home')
    else:
        return redirect('user_home')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Notebook.create_notebook(user=user)
            login(request, user)
            return redirect('user_home')
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", {'form': form})