from django.contrib import admin
from customers.models import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


admin_site = admin.AdminSite(name='root')
admin_site.register(get_user_model())
admin_site.register(Group)
admin_site.register(Client)

