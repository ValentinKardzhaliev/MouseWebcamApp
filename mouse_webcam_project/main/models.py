from django.db import models


class Capture(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    image = models.TextField()

    def __str__(self):
        return f'Capture at ({self.x}, {self.y})'
