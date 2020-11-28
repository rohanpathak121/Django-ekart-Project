from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.models import Group

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    # update form
    forms = UserAdminChangeForm
    fieldsets = (
        ('Personal Details', {
            'classes':('wide',),
            'fields':('full_name', 'mobile', 'email', 'password')
        }),
        ('Permissions',{'classes':('wide',),
            'fields':('active', 'admin', 'staff')
        }))

    # inserting a user
    add_form = UserAdminCreationForm
    # fieldsets (('string - Heading', dict - {classes - css name, fields : (column nmaes to displayed)}))
    add_fieldsets = (
        ('Personal Details', {
            'classes':('wide',),
            'fields':('full_name', 'mobile', 'email')
        }),
        ('Password Details',{'classes':('wide',),
            'fields':('password1', 'password2')
        }))

    filter_horizontal = []
    ordering = ['full_name']
    list_display = ['email', 'full_name']
    list_filter = ['admin']
    search_fields = ['full_name', 'email', 'mobile']

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)