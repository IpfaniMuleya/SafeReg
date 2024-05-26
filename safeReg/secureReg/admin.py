from django.contrib import admin
from .models import Profile, Module, Registration


admin.site.site_header = 'SAFEREG'

admin.site.register(Profile)
admin.site.register(Module)
admin.site.register(Registration)