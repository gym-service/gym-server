from django.contrib import admin
from django.contrib.auth import get_user_model

from gym_users.models import GymUserInfo
from gym_config.models import GymConfig
from gym_contents.models import GymContents

admin_site = admin.AdminSite(name='tenant')
admin_site.register(get_user_model())
admin_site.register(GymUserInfo)
admin_site.register(GymConfig)
admin_site.register(GymContents)



