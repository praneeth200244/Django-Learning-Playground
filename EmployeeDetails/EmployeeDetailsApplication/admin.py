from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'designation',
        'email',
    )

    search_fields = (
        'first_name',
        'last_name',
        'email',
    )

    list_filter = ('designation',)

    @admin.display(description='Name')
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"