from django.contrib import admin
from .models import Dog


class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')


admin.site.register(Dog, DogAdmin)
