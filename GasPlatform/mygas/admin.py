from django.contrib import admin
from mygas.models import *

# Register your models here.
#显示的字段
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ['ManufactureName','code']
    # list_editable = ['code']

admin.site.register(Manufacture,ManufactureAdmin)