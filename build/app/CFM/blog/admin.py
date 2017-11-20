from django.contrib import admin
from .models import *
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','date','rubric','image_tag']
    search_fields = ['title','date']
    list_filter = ('rubric',)
    list_editable = ('title',)
    readonly_fields = ('image_tag',)




admin.site.register(Rubric)
admin.site.register(Blog,BlogAdmin)
