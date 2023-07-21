from django.db import models


class Link(models.Model):
    url = models.URLField(max_length= 1024)
    uuid = models.CharField(max_length= 5)
    
    def __str__(self):
        return self.uuid
