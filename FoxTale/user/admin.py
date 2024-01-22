from django.contrib import admin
from django.contrib.admin import StackedInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfileModel
# Register your models here.

class UserInLine(StackedInline):
    model = UserProfileModel
    can_delete = False

class UserAdmin(UserAdmin, admin.ModelAdmin):
    inlines = (UserInLine,)

    def save_model(self, request, obj,):
        if request.user.is_superuser:
            obj.is_staff = True
            obj.save()

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(UserProfileModel)