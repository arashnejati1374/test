from django.contrib import admin
from .models import test1


# Register your models here.

@admin.register(test1)
class testAdmin(admin.ModelAdmin):
    pass
