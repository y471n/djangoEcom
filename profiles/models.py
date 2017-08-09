from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')

    def __repr__(self):
        return self.name