from django.db import models

# Create your models here.
class TelecomAdmin(models.Model):
    ism = models.CharField(max_length=250)
    familiya = models.CharField(max_length=250)
    ochistiva = models.CharField(max_length=250)
    mahalla = models.CharField(max_length=250)


    def __str__(self):
        return f'{self.ism}-{self.familiya}-{self.ochistiva}'


class TelecomUser(models.Model):
    post = models.ForeignKey(TelecomAdmin,on_delete=models.CASCADE)
    router_name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.router_name}'