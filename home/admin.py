from django.contrib import admin
from .models import Signup

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_at')
    search_fields = ('email', 'name')
