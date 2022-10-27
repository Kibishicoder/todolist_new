from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from todolist.core.models import User


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    # customize user form
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')

    fieldsets = (
        (('General info'), {
                'fields': ('username', 'password')
        }),
        (('Personal info'), {
            'fields': ('first_name', 'last_name', 'email')
        }),
        (('Permissions'), {
             'fields': ('is_staff', 'is_active', 'is_superuser'),
         }),
        (('Important_dates'), {
             'fields': ('last_login', 'date_joined')
         }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['last_login', 'date_joined']
        return self.readonly_fields




