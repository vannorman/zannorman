import json
import uuid
import urllib
import datetime
import re 
import requests # for setting cookies

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from django.utils import timezone
from django.contrib import auth
#from django.forms.util import ErrorList
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

#import requests

from charlievannorman.util import *
def simple_page(template):
	def handler(request):
		return renderWithNav(request, template)
	return handler


def home(request):
	obj = {}
	obj['portfolio'] = []
	obj['portfolio'].append({
		"title" : "Super Math World",
		"year" : "2016 - 2017",
		"subtitle" : "An online math sandbox using WebGL",
		"description" : """
			At Super Math World, I built a game creation kit on top of a 3D math puzzler-platformer game. The editor is accessible from the game and takes you to a sky view where you can place and modify objects. In this way, users can use the same tools we use to create content.
<br />
<br /> 
The WebGL executable is hosted by Amazon S3, served by Apache on Ubuntu. I built the backend using python/django, including the save and load flow (using MySQL on RDS on the back end, and a javascript layer between the game executable and the django server.) 
<br />
<br />
""",
		"my_roles" : ["Unity/c# developer","game designer","c# platform architect","python/django"],
		"videos" : [
				{ "source": "https://player.vimeo.com/video/219464062", "image" : "smw_1.jpg" }
		],
		"images" : ["smw_2.jpg","smw_4.jpg","smw_3.jpg"],	
		"link" : "https://supermathworld.com"
		})
	obj['portfolio'].append({
		"title" : "Mathbreakers",
		"year" : "2013 - 2015",
		"subtitle" : "A downloadable math puzzle platformer for grades 2 - 8",
		"description" : "An advnture puzzle game that teaches fundamental concepts in a playful, visual, and low-pressure way.",
		"my_roles" : ["Unity/c# developer","game designer"],
		"videos" : [
				{ "source": "https://player.vimeo.com/video/73754523", "image" : "mb_1.jpg" }
		],
		"images" : ["mb_2.jpg","mb_3.jpg","mb_4.jpg"],	
		"link" : "https://mathbreakers.com"
		})
	obj['portfolio'].append({
		"title" : "Mouse Brain Explorer VR",
		"year" : "2015",
		"subtitle" : "Fly through a real mouse brain",
		"description" : "Use XBOX controller and Oculus VR to pilot an imaginary ship through a real mouse brain. The one cubic centimeter brain was imaged by 3Scan.",
		"my_roles" : ["Unity/c# developer","game designer"],
		"videos" : [
				{ "source": "https://player.vimeo.com/video/117482417", "image" : "3scan_1.jpg" }
		],
		"images" : [],	
		"link" : "https://3scan.com"
		})



	return renderWithNav(request,'home.html', obj)

def file_a(request):
	return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")

def file_b(request):
	return HttpResponse("Z9DF236bXRfXjvGlUflaI98PMWAKsG9qpGnrDXllb2o.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")	



