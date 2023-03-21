from django.shortcuts import render, redirect
from django.http import HttpResponse

from notes.forms import AddNoteForm
from notes.models import Note
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    return render(request, "index.html")


def add_note(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(title=form.cleaned_data["title"], text=form.cleaned_data["text"],
                                author=request.user)

            return redirect("/notes/")
    else:
        form = AddNoteForm()
    return render(request, "add_note.html", {"form": form})


def thanks(request):
    return HttpResponse(f"Thank you!")


def notes(request):
    notes = Note.objects.all()
    return render(request, "notes.html", {"notes": notes})
