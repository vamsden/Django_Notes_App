from django.shortcuts import render

from .models import Note
from .forms import NoteForm
# Create your views here.


def index(request):
    return render(request, "index.html", {})


def notes(request):
    # delete = Note.objects.get(pk=id).delete()
    note = Note.objects.order_by('-created')
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    context = {
        'note': note,
        'form': form,
        # 'delete': delete,
    }
    return render(request, 'notes/note.html', context)
