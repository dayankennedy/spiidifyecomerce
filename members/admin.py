from django.contrib import admin

# from spiidcomerce.members.models import Profile
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','bio','profile_pic')
admin.site.register(Profile,ProfileAdmin)
