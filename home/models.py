from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=40, unique=False)
    email = models.EmailField()
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email