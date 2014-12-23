from django.db import models

class Torrent(models.Model):
    name = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=20, decimal_places=0)
    hash = models.CharField(max_length=40)
    num_files = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
