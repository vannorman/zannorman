from functools import partial

from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.contrib.auth.models import User
from django.forms import widgets
from django.utils.html import conditional_escape, format_html

from zannorman.models import *
from django.core.validators import RegexValidator
alphanumeric = RegexValidator(r'^[_\s0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# from https://djangosnippets.org/snippets/1956/
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
	"""renders horizontal radio buttons.
	found here:
	https://wikis.utexas.edu/display/~bm6432/Django-Modifying+RadioSelect+Widget+to+have+horizontal+buttons
	"""

	def render(self):
		return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class ZanChatForm(forms.Form):
	name = forms.CharField(max_length=100, required = True, label="Your name")
	email = forms.EmailField(required=True, label="Your email")
	message = forms.CharField(max_length=2048, widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}), required=True, label = "Comment or suggestion")



