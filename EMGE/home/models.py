from django.db import models

# Create your models here.

class Company(models.Model):
    logo = models.ImageField(null=True,upload_to='images')
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True)
    organisation = models.CharField(max_length=200)
    Intro = models.TextField(max_length=200)
    selfie = models.ImageField(null=True,upload_to='images')
    document = models.FileField(upload_to='documents')
    contact = models.BigIntegerField(null=True)
    CIN = models.BigIntegerField(null=True)
    password = models.CharField(max_length=200, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Company #{}'.format(self.organisation)
    
    class Meta:
        verbose_name_plural = 'companies'

class Post(models.Model):

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    
    Company_Type_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]

    Industry = models.ForeignKey(Company, null=True, on_delete=models.CASCADE,)
    Brand = models.CharField(max_length=200,null=True)
    company_type = models.CharField(max_length=200,choices=Company_Type_CHOICES,default=FRESHMAN,)
    Locations = models.CharField(max_length=250, null=True)
    phone = models.BigIntegerField(null=True)
    email = models.CharField(max_length=200, null=True)
    website = models.CharField(max_length=200)
    selfie = models.ImageField(null=True,upload_to='images')
    #story= models.TextField(max_length=200)
    #contact = models.BigIntegerField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Post #{}'.format(self.Industry)
    
    class Meta:
        verbose_name_plural = 'posts'

class Contact(models.Model):

    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200)
    mssg= models.TextField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Contact #{}'.format(self.name)
    
    class Meta:
        verbose_name_plural = 'contacts'
"""
class KidApparel(models.Model):
    product_image = models.ImageField()
    product_name = models.TextField()
    product_price = models.CharField(max_length=200, null=True)
    product_offer = models.FloatField(null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'kidapparels'

"""