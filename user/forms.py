from django.forms import ModelForm

from note_feed.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        exclude = ('notebook',)
        help_texts = {
            'priority': 'Enter a value between 0 & 10  ...0 being lowest priority, 10 being the highest',
        }
