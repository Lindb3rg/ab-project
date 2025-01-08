from datetime import datetime, timedelta
from django.db import models
from . import db_seeder


class Song(models.Model):
    STATUS_CHOICES = [
        ('WRITING', 'Writing'),
        ('EDITING', 'Editing'),
        ('MIXING', 'Mixing'),
        ('MASTERING', 'Mastering'),
        ('FINISHED', 'Finished'),
    ]

    name = models.CharField(max_length=200)
    starting_date = models.DateField(default=datetime.now)
    duration = models.DurationField(default=timedelta())
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='WRITING',
    )  
    notes = models.TextField()

    def duration_display(self):
        total_seconds = int(self.duration.total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def __str__(self):
        return self.name



# db_seeder.create_db_objects(20)
# Song.objects.all().delete()

