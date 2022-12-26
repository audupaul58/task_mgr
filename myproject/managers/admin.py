from django.contrib import admin
from .models import Contact, AirdropModel

# Register your models here.

class ModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'network', 'wallet']
    search_fields = ('title',)

admin.site.register(AirdropModel, ModelAdmin)

admin.site.register(Contact)
