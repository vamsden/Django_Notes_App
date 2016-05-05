from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)

    # Inside the class. Common mistake!
    def __str__(self):
        return self.title
