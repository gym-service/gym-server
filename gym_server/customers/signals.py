from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from tenant_schemas.utils import tenant_context
from customers.models import Client
from .utils import create_superuser, create_or_update_superuser

@receiver(post_save, sender=Client, dispatch_uid="post_save_client_create_superuser")
def model_post_save(sender, **kwargs):
    instance = kwargs['instance']
    #we manage the public instance by ourselves..
    public_schema_name = getattr(settings, 'PUBLIC_SCHEMA_NAME', 'public')
    if instance.schema_name == public_schema_name:
        return

    if not instance.pk:
        create_superuser(instance, instance.email)
    """
    else:
        old_tenant_pk = instance.pk
        with tenant_context(instance):
            old_tenant = Client.objects.get(pk=old_tenant_pk)
            create_or_update_superuser(instance, old_tenant.email, instance.email)
    """