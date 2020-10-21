from django.contrib import admin


from mainapp.models import Team, Trainer, LineUp, Match


admin.site.register(Team)
admin.site.register(Trainer)
admin.site.register(LineUp)
admin.site.register(Match)
