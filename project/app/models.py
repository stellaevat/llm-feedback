from django.db import models

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    moderation_algorithm = models.CharField(max_length=100)
    spec = models.TextField()
    rubric = models.TextField()
    prompt = models.TextField()

    def __str__(self):
        return self.name
