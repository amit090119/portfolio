from django.db import models

# Create your models here.

class Page(models.Model):
    title= models.CharField(max_length=100)
    content = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
