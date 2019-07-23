from django.contrib import admin
from .models import EsusuGroup,Group
import random
from datetime import timedelta


# The admin layout Configuration
@admin.register(EsusuGroup)
class EsusuGroupAdmin(admin.ModelAdmin):
    list_display = ('group','group_description','member_turn','group_members','amount_to_save','group_limit','is_public')
    list_filter = ('is_public','g_users','group_limit','amount_to_save','group')

# //returns a string of users joined as  string
    def group_members(self, obj):
        return " , ".join([str(u) for u in obj.g_users.all()])


# this function is supposed to return the turn of each member of the group but is not working :(
    def member_turn(self, obj):
        myuserdate = [str(u) + ' ' + str(obj.date_created + timedelta(days=30)) for u in obj.g_users.all()]
        return ' , '.join(myuserdate)
        # return obj.date_created.strftime('%B')
