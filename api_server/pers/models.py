from enum import auto, unique
from django.db import models

# Create your models here.


class CyTasks(models.Model):

    id = models.IntegerField(primary_key=True)

    task_id = models.CharField(max_length=64, unique=True)

    name = models.CharField(max_length=256)

    status = models.IntegerField()

    created_at = models.DateTimeField(auto_now=True)

    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cy_tasks'

class JaySong(models.Model):

    id = models.IntegerField(primary_key=True)

    cid = models.CharField(max_length=64)

    song_info = models.TextField()

    flac_url = models.TextField()

    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name + "_" + str(self.id)

    class Meta:
        db_table = 'jay_song'