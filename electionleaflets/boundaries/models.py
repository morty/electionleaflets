from django.db import models
from constituencies.models import Constituency

class Boundary(models.Model):
    constituency = models.ForeignKey( Constituency )
    boundary = models.TextField()
    zoom = models.IntegerField()
    north = models.FloatField()
    south = models.FloatField()
    east = models.FloatField()
    west = models.FloatField()
    class Meta:
        db_table = u'boundaries_boundary'
        verbose_name_plural = 'Boundaries'
