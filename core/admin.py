from django.contrib import admin
from .models import User, Ad


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('name', 'email',)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cover', 'user',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)
