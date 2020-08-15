from django.db import models

class NoteModel(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    tags = models.CharField(max_length=300)

    def __str__(self):
        return self.title   