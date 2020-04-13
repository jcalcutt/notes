from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q


class NotesQuerySet(models.QuerySet):
    def notes_for_user(self, user):
        return self.filter(
            Q(notebook__person__username=user)
        ).order_by('-priority')


class Notebook(models.Model):
    person = models.ForeignKey(User, related_name="note_writer", on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Notebook for {self.person}"

    def new_note(self):
        return Note(notebook=self)

    @classmethod
    def create_notebook(cls, user):
        cls(person=user).save()


class Note(models.Model):
    heading = models.CharField(max_length=30, blank=False)
    comment = models.CharField(max_length=300, blank=True)
    priority = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)

    objects = NotesQuerySet.as_manager()

    def __str__(self):
        return f"{self.heading} from {self.notebook}"

    def delete_note(self):
        self.delete()
