from django.db import models
class ContactForm1(models.Model):
    fullname= models.CharField(max_length=100)
    email= models.EmailField()
    contact= models.CharField(max_length=50)
    message= models.CharField(max_length=200)

class ContactForm(models.Model):
    fullname = models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False)
    contact = models.CharField(max_length=50)
    message = models.CharField(max_length=200)


class Member(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    class Meta:
        db_table: "contacthtml"

class Contactt(models.Model):
            fullname = models.CharField(max_length=100)
            email = models.EmailField()
            contact = models.CharField(max_length=50)
            message = models.CharField(max_length=200)

            class Meta:
                db_table: "contacthtml"

class ContactLess(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

class Details(models.Model):
    username = models.CharField(max_length=20,default='',null=False)
    password = models.CharField(max_length=30, default='', null=False)

class Details1(models.Model):
        username = models.CharField(max_length=20, default='', null=False)
        password = models.CharField(max_length=30, default='', null=False)


class Details2(models.Model):
    username = models.CharField(max_length=20, default='', null=False)
    password = models.CharField(max_length=30, default='', null=False)
class User(models.Model):
# username field
     username = models.CharField(max_length=30, blank=False, null=False)
# password field
     password = models.CharField(max_length=8, blank=False, null=False)