from django.db import models
from django.contrib.auth.models import User

branch = (("Headoffice", "Headoffice"),("Maitidevi", "Maitidevi"),("Kathmandu Warehouse", "Kathmandu Warehouse"),("BIRTAMOD WAREHOUSE", "BIRTAMOD WAREHOUSE"),("Tokha", "Tokha"),("Sanepa", "Sanepa"),("Itahari Store & WH", "Itahari Store & WH"))
Depart = (("Ecommerce", "Ecommerce"),("IT", "IT"),("Finance", "Finance"))

class employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Profile = models.ImageField(upload_to ='',default='profile.png')

    Emp_id = models.CharField(max_length=15)
    Fullname = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100, choices=branch,default='Headoffice')
    Department = models.CharField(max_length=100, choices=Depart,default='IT')
    Phonenum = models.IntegerField(blank=True,null=True,default=98023)
    Email = models.CharField(max_length=100)
    Joined = models.DateField(auto_now_add=True, null=True)
    
    Fb_id= models.URLField(max_length=200,default='www.facebook.com')
    Insta_id= models.URLField(max_length=200,default='www.Instagram.com')
    Linkedin_id= models.URLField(max_length=200,default='www.Linkedin.com')

    class Meta:
        ordering = ['Emp_id']
        
    def __str__(self):
        return self.Emp_id

