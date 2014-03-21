from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response

def main (request) :
	title = _('Welcome to my site.')
	return render_to_response('index/base.html', {
		'title': title
	})