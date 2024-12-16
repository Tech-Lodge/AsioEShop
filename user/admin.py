from django.contrib import admin
from .models import Customer
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

@admin.register(Customer)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2", "firstname", "lastname", "email"),
            },
        ),
    )


# ... means pass
# admin.site.register(Customer)


# @admin.register(Customer)
# class CustomerAdmin(BaseUserAdmin):
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "usable_password", "password1", "password2", "firstname", "lastname", "email"),
#             },
#         ),
#     )
