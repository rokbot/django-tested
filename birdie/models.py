from django.db import models

# Create your models here.
class Post(models.Model):
    body = models.TextField()

    def get_excerpt(self, number_chars):
        return self.body[:number_chars]

