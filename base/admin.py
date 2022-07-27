from django.contrib import admin
from .models import *

# @admin.register(Message)
class messageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'body')

# @admin.register(Room)
class roomAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'host')

# @admin.register(Topic)
class topicAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register your models here.
admin.site.register(Room, roomAdmin)
admin.site.register(Topic, topicAdmin)
admin.site.register(Message, messageAdmin)