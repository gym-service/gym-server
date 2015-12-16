from django.contrib import admin
from django.contrib.auth import get_user_model

from gym_users.models import GymUserInfo
from gym_config.models import GymConfig
from gym_contents.models import Evento, Notizia, Press, Alert, Video, Gallery, \
                                Immaginigallerie

admin_site = admin.AdminSite(name='tenant')
admin_site.register(get_user_model())
# -- gym_users ---------------------------
admin_site.register(GymUserInfo)

# -- gym_config ---------------------------
admin_site.register(GymConfig)

# -- gym_contents ------------------------
admin_site.register(Evento)
admin_site.register(Notizia)
admin_site.register(Press)
admin_site.register(Alert)
admin_site.register(Video)
admin_site.register(Gallery)
admin_site.register(Immaginigallerie)



