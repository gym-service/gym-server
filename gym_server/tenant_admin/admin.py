from django.contrib import admin
from django.contrib.auth import get_user_model

from gym_users.models import GymUserInfo

admin_site = admin.AdminSite(name='tenant')
admin_site.register(get_user_model())
admin_site.register(GymUserInfo)

