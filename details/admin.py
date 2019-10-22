from django.contrib import admin
from .models import profile
from .models import score
from .models import attendance

admin.site.register(profile)
admin.site.register(score)
admin.site.register(attendance)

