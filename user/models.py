from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Profile(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    related_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s %s " % (self.name, self.last_name)


    

    
