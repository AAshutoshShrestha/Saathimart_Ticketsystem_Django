from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages


branch = (("Headoffice", "Headoffice"),("Maitidevi", "Maitidevi"),("Kathmandu Warehouse", "Kathmandu Warehouse"),("BIRTAMOD WAREHOUSE", "BIRTAMOD WAREHOUSE"),("Tokha", "Tokha"),("Sanepa", "Sanepa"),("Itahari Store & WH", "Itahari Store & WH"))
selectchoices = (
        ('Emergency', 'Emergency'),
        ('High', 'High'),
        ('Low', 'Low'),
        ('Very low', 'Very low'),
        )
option = (
        ('Pending', 'Pending'),
        ('On Process', 'On Process'),
        ('ON Hold', 'ON Hold'),
        ('Completed', 'Completed'),
        )


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Employe(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    EmpID = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.EmpID

class OrgDepartment(models.Model):
    name = models.CharField(max_length=200, null=True)
    tags = models.ManyToManyField(Tag)
    description = models.CharField(max_length=1000,null=True)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class supervisor(models.Model):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    name = models.CharField(max_length=200, null=True)
    empID = models.ForeignKey(Employe,null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.name)
        
class Workers(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    empID = models.ForeignKey(Employe,null=True, on_delete=models.SET_NULL)
    Profile = models.ImageField(upload_to ='',default='profile.png')

    name = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=200, null=True)

    joining_date = models.DateField(null=True)
    branch = models.CharField(max_length=100, choices=branch,default='Headoffice')
    Designation = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)

    TeamHead = models.ForeignKey(supervisor,null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(OrgDepartment,null=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name

class CouponType(models.Model):
    name = models.CharField(max_length=200, null=True)
    validationTime = models.IntegerField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)

class Case(models.Model):
	user = models.ForeignKey(Workers,null=True, on_delete=models.SET_NULL)
	topic = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=1000, null=True)
	Category = models.ForeignKey(CouponType,null=True, on_delete=models.SET_NULL)
	Department = models.ForeignKey(OrgDepartment,null=True, on_delete=models.SET_NULL)
	Priority = models.CharField(max_length=25, null=True,choices=selectchoices, default='High')
	Status = models.CharField(max_length=25, null=True,choices=option, default='Pending')
	note = models.CharField(max_length=1000, null=True,blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

def __str__(self):
        return self.topic
    
