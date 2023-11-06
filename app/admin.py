from django.contrib import admin
from app.models import Climate
# Register your models here.

#admin.site.register(Climate)
@admin.register(Climate)
class ClimateAdmin(admin.ModelAdmin):
    list_display=['id','climate','area','chances','humidity']