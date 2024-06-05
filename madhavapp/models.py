from django.db import models

class ResultImage(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.roll_number
