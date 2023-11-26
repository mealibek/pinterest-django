from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile


class ProfileAdminConfig(UserAdmin):
    model = Profile
    list_display = ("email", "is_active",
                    "created_at", "modified_at")
    list_filter = ("is_active", "created_at")
    ordering = ('-created_at',)
    search_fields = ('email', 'first_name', 'last_name', 'id',)

    # fields which are not meant to be changed.
    readonly_fields = ['id', 'created_at', 'modified_at',
                       'last_login']

    # details page structure & order.
    fieldsets = (
        ('Profile', {'fields': ('id', 'email',
         'password', 'first_name', 'last_name')}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Personal', {'fields': ('profile_image',
         'created_at', 'modified_at', 'last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2',),
        }),
    )


admin.site.register(Profile, ProfileAdminConfig)
