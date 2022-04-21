from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Word)
admin.site.register(Photo)
admin.site.register(Music)
admin.site.register(Movie)
admin.site.register(Place)
admin.site.register(Food)
