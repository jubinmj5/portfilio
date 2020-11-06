from django.contrib import admin
from .models import Resume,Project


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title','img','filetype','status')
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description','urlls','status')
    
# Register your models here.
admin.site.register(Resume,ResumeAdmin)
admin.site.register(Project,ProjectAdmin)