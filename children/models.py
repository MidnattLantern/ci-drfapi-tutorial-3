from django.db import models
from django.contrib.auth.models import User


NATAL_SEX = ((0, "Intersex"), (1, "Female"), (2, "Male"))
CHOOSEN_SEX = ((0, "Cis"), (1, "MTF"), (2, "FTM"), (3, "NB"))


class Child(models.Model):
    """
    Child model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
#    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    register_date = models.DateTimeField(auto_now_add=True)
    register_update_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    natal_sex = models.IntegerField(choices=NATAL_SEX, default=0)
    choosen_sex = models.IntegerField(choices=CHOOSEN_SEX, default=0)


    class Meta:
        ordering = ['-register_date']
    

    def  __str__(self):
#        return f"{self.parent}'s child {self.name}"
        return f"{self.owner}'s child {self.name}"
