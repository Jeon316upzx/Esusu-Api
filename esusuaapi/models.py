from django.db import models
from django.contrib.auth.models import User, Group
from uuid import uuid4


class EsusuGroup(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    group_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    group_description = models.CharField(max_length = 300, default="")
    group_limit = models.PositiveIntegerField()
    group_limit = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    amount_to_save = models.PositiveIntegerField()
    is_public = models.BooleanField()
    g_users = models.ManyToManyField(User)

# sets the plural name of the EsusuGroup model
    class Meta:
        verbose_name_plural = "Esusu Groups"
# returns a string representation of the model EsusuGroup
    def __str__(self):
        return self.group.name

# class Userprofile(models.Model):
#     user = models.OneToOneField(User, related_name='user',on_delete=models.CASCADE)
#     account_no = models.CharField(max_length=11,blank=True)
#     phone_no = models.CharField(max_length=11,blank=True)
#     city = models.CharField(max_length=100,blank=True)
#     groups = models.ManyToManyField(EsusuGroup)
#
#
#     def __str__(self):
#         return self.user.username
