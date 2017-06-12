import math

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
import datetime





class ZanChatReport(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	username = models.CharField(max_length=64) 
	ip = models.IPAddressField()
	email = models.CharField(max_length=64) # maybe they used a diff email than their login email?
	name = models.CharField(max_length=64) 
	message = models.CharField(max_length=1024)  
