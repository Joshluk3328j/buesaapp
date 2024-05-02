from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(("name"), max_length=50)
    matric_number = models.CharField(("matric_number"), max_length=11)
    email = models.EmailField(("email"))
    otp = models.IntegerField(("otp"),)
    loggedin = models.BooleanField(("loggedin"))
    voted = models.BooleanField(("voted"))

    def __str__(self):
        return f"{self.id} -{self.name}- {self.matric_number} - {self.email} - {self.otp} - {self.loggedin} - {self.voted} "


# class candidates(models.Model):
#     name = models.CharField(max_length=50)
#     gmail = models.EmailField()
#     # image = models.ImageField(upload_to='candidate/')
#     description = models.TextField(max_length=150)
