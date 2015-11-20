from django.contrib.auth import get_user_model
from tenant_schemas.utils import tenant_context


def create_superuser(tenant, email):
    
    with tenant_context(tenant):
        USER_MODEL = get_user_model()
        # Create a superuser for the given tenant
        # we set a dummy password for now ...
        # we should also send an activation mail, as we set no password
        USER_MODEL.objects.create_superuser(email=email, password="admin123")


def create_or_update_superuser(tenant, old_email, email):
    
    with tenant_context(tenant):
        USER_MODEL = get_user_model()
        # Create a superuser for the given tenant
        # we set a dummy password for now ...
        # we should also send an activation mail, as we set no password
        
        try:    
            u = USER_MODEL.objects.get(email=old_email)
            u.is_superuser = True
            u.email = email
            u.save()

        except USER_MODEL.DoesNotExist:
            try:
                u = USER_MODEL.objects.get(email=email)
                u.is_superuser = True
                u.email = email
                u.save()
            except USER_MODEL.DoesNotExist:
                USER_MODEL.objects.create_superuser(email=email, password="admin123")