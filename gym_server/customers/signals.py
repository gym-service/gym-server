from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from customers.models import Client
from .utils import create_superuser, create_or_update_superuser
from tenant_schemas.utils import tenant_context

@receiver(pre_save, sender=Client, dispatch_uid="pre_save_client_create_superuser")
def model_pre_save(sender, **kwargs):
    instance = kwargs['instance']
    #we manage the public instance by ourselves..
    # todo: reference settings...
    if instance.schema_name == 'public':
        return

    if not instance.pk:
        create_superuser(instance, instance.email)
    else:
        old_tenant_pk = instance.pk
        with tenant_context(instance):
            old_tenant = Client.objects.get(pk=old_tenant_pk)
            create_or_update_superuser(instance, old_tenant.email, instance.email)
        