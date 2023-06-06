from django.db.models.signals import post_save
from django.contrib.auth.models import User

from ticket.models import Employes
from emp_details.models import employee


def Emp_profile(sender, instance, created, **kwargs):
    if created:
        employee.objects.create(
                user=instance,
                Fullname=instance.username,
            )
        print('Profile created!')

post_save.connect(Emp_profile, sender=User)


def Employes_profile(sender, instance, created, **kwargs):
	if created:
		Employes.objects.create(
                user=instance,
                name=instance.username,
			)
		print('Profile created!')

post_save.connect(Employes_profile, sender=User)
