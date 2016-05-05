from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {'text': forms.Textarea(attrs={'rows': 5,
                                                 'cols': 6,
                                                 'style': 'resize:none;'}),
                   }
