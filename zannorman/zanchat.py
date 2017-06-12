from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from zannorman.util import *
from zannorman.models import *
from zannorman.forms import *

def report(request):
	if request.method == "POST":
		muv_form = MyUserVoiceForm(request.POST)
		if muv_form.is_valid(): # User successfully entered email + password after selecting "is_teacher"
			ip = get_ip(request)
			email = muv_form.cleaned_data['email']
			name = muv_form.cleaned_data['name']
			message = muv_form.cleaned_data['message']
			try: nickname = request.POST['user_nickname']
			except: nickname = 'no nickname'
			class_session = str(get_recent_sessions_for_class(request.user))[:1024]
			nickname_session = str(get_recent_sessions_for_nickname(nickname))[:1024]
			
			if request.user.is_authenticated():
				username = request.user.username
			else:
				username = "anonymous"
			report = MyUserVoiceReport(ip=ip,email=email,name=name,message=message,nickname=nickname,class_session=class_session,nickname_session=nickname_session)
			if request.user.is_authenticated():
				report.user = request.user
	
			report.save()
			try:
				s = "SuperMathWorld user voice report from: "+name
				m = name + """ had this to say:

""" + message + """

ip: """ + str(ip) + """
email: """ + email + """

nickname: """ + nickname + """
username: """ + username + """
class session: """ + class_session + """
nickname_session: """ + nickname_session + """

SuperMathWorld is a platform for playing, creating, and sharing math games online.

"""
				fr = "robot@zannorman.com"
				to = "charlie@zannorman.com"
				send_mail_threaded(s,m,fr,[to])
				return json_response({"success":True})
			except:
				return json_response({"success":False})
		else: #form not valid.
			obj = {}
			obj['success'] = False
			obj['errors'] = muv_form.errors
			return json_response(obj)
	else:
		print 'MyUserVoice.py was not called with post data. Request body: ' +str(request)
		return json_response({"success":False})	

		

