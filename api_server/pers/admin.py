from typing import Sequence
from django.contrib import admin, messages
from django.utils.translation import ngettext

# Register your models here.

from .models import JaySong, CyTasks
from .tasks import download_jay_song

@admin.action(description="download")
def download(self, request, queryset):
    future = download_jay_song.delay(queryset[0].name, queryset[0].flac_url)
    self.message_user(request, "成功 任务id:" + future.id, messages.SUCCESS)

class JaySongAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']

    search_fields: Sequence[str] = ['name']

    actions = [download]

class CyTasksAdmin(admin.ModelAdmin):

    pass

admin.site.register(JaySong, JaySongAdmin)
admin.site.register(CyTasks, CyTasksAdmin)