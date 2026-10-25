from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed',  'updated_at')
    list_filter = ('is_completed',)
    search_fields = ('task',)
    ordering = ('-created_at',)
admin.site.register(Task, TaskAdmin)