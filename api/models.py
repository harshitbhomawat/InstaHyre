from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator

class Contact(models.Model):
    cid=models.AutoField(primary_key=True)
    contact_name=models.CharField(max_length=32)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    contact_phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16)    
    spam=models.BooleanField(default=False)
    

class PersonManager(BaseUserManager):
    def create_user(self,phone_number=None,email=None,name=None,password=None,contact_id=None):
        if not phone_number:
            raise ValueError('Users must have an phone number')
        if not name:
            raise ValueError('Users must have a name')
        person=self.model(
            name=name,
            phone_number=phone_number,
            password=password,
            email=email,
            contact_id=contact_id
        )
        person.save()
        return person

    def create_superuser(self,phone_number=None,email=None,name=None,password=None):
        if not phone_number:
            raise ValueError('Users must have an phone number')
        if not name:
            raise ValueError('Users must have a name')
        person=self.model(
            name=name,
            phone_number=phone_number,
            password=password,
            email=email,
            is_staff=True,
            is_superuser=True,
            is_admin=True
        )
        person.save()
        return person



class Person(AbstractBaseUser, PermissionsMixin):
    contact_id=models.IntegerField(default=-1)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=30, null=False)
    email=models.EmailField(null=True,blank=True)
    # phone_number=PhoneNumberField(unique=True,null=False,blank=False)
    contacts=models.ManyToManyField('Contact',blank=True,db_constraint=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    objects = PersonManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Person, self).save(*args, **kwargs)