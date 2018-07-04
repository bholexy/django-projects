from django.contrib import admin

# Register your models here.
from .models import ScrumyUser, ScrumyStatus, ScrumyGoals, ScrumyUserJS, ScrumyStatusJS, ScrumyGoalsJS


admin.site.register(ScrumyUser)
admin.site.register(ScrumyStatus)
admin.site.register(ScrumyGoals)
admin.site.register(ScrumyUserJS)
admin.site.register(ScrumyStatusJS)
admin.site.register(ScrumyGoalsJS)