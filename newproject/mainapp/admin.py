from django.contrib import admin


from mainapp.models import Team, Trainer,Player , Match


admin.site.register(Team)
admin.site.register(Trainer)
admin.site.register(Match)
admin.site.register(Player)

