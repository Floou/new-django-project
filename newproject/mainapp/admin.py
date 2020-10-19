from django.contrib import admin

from mainapp.models import Command, Composition, Match

admin.site.register(Command)
admin.site.register(Composition)
admin.site.register(Match)