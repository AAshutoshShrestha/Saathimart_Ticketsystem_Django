from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.dispatch import Signal,receiver

from .models import Employe,Workers,Case
#fsdgsd
def Employe_profile(sender, instance, created, **kwargs):
	if created:
		Employe.objects.create(
                user=instance,
                name=instance.username,
			)
		print('Employe instance created!')

post_save.connect(Employe_profile, sender=User)

def Workers_profile(sender, instance, created, **kwargs):
	if created:
		Workers.objects.create(
                user=instance,
                name=instance.username,
			)
		print('Workers instance created!')

post_save.connect(Workers_profile, sender=User)


# def post_case_save(sender,instance,created,**kwargs):
# 	if created:
# 		context={
# 			'Message':"New Ticked has been created",
# 			'Department':instance.Department,		
# 			'Priority':instance.Priority
# 		}
# 	else:
# 		context ={
# 			'message' : "changes made on coupon",
# 			'user' : instance.user,
# 			'topic' :instance.topic,
# 			'status': instance.Status

# 		}
# 	print(context)
# post_save.connect(post_case_save,sender=Case)

# signal creation

notification = Signal("request")

# Receiving signal
@receiver(notification)
def show_notification(sender,**kwargs):
	
	extra = f'{kwargs}'
	msg = f"Your case has been updated: {sender}"
	return(msg)