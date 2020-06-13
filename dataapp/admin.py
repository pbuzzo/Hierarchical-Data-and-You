from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from dataapp.models import File

admin.site.register(
    File,
    DraggableMPTTAdmin
)