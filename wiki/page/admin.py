from django.contrib import admin
from page.models import Page

admin.site.register(Page)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ( 'visuel', 'titre' )

# Register your models here.
