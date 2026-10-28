from django.contrib import admin

from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'name', 'date_of_birth')
    search_fields = ('roll_number', 'name')

admin.site.register(Student, StudentAdmin)
