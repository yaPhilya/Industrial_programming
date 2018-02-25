from django.forms import models
from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView

from main.models import Main


class NoteDelete(DeleteView):
    model = Main
    template_name = 'main_confirm_delete.html'
    success_url = '/'


class NewNoteForm(models.ModelForm):
    class Meta:
        model = Main
        fields = ['text']


def new_note(request):
    if request.method == 'GET':
        form = NewNoteForm()
    else:
        form = NewNoteForm(request.POST)
        if form.is_valid():
            form.save()
            form = NewNoteForm()

    notes = Main.objects.filter(is_deleted=False)
    return render(request, 'main.html', {'notes': notes, 'form': form})


def main(request):
    return render(request, 'main.html')
