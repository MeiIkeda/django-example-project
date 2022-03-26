from django.contrib import admin

from myapp.model import AlcoholicProduct

@admin.register(AlcoholicProduct)
class Admin(admin.ModelAdmin):
    pass
