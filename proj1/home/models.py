from django.db import models

#makemigrations - create changes and store in a file
#migrate - apply pending changes made by makemigrations



# Create your models here.
class Contact(models.Model):   #here Contact is table in database
    name=models.CharField(max_length=122)  #here name email phone desc are columns of table Contact
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField()
    data=models.DateField()

#to change the name in contact table in admin panel
    def __str__(self):
        return self.name
