#from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from tenant_schemas.signals import post_schema_sync
from django.dispatch import receiver
from django.conf import settings
from tenant_schemas.utils import tenant_context
from customers.models import Client
from .utils import create_superuser, create_or_update_superuser

@receiver(post_schema_sync,  dispatch_uid="post_save_client_create_superuser")
def post_schema_save(sender, **kwargs):
    tenant = kwargs['tenant']
    with tenant_context(tenant):
            create_superuser(tenant, tenant.email)


