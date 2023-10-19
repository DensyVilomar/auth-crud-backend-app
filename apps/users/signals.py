from .models import UserAccount
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save

### SIGNALS ###


@receiver(pre_save, sender=UserAccount)
def calc_age(sender, instance, **kwargs):
    if instance.date_of_birth:
        today = timezone.now().date()
        age = today.year - instance.date_of_birth.year - ((today.month, today.day) <
                                                          (instance.date_of_birth.month, instance.date_of_birth.day))
        instance.age = age
