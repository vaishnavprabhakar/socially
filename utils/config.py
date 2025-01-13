import os
from jinja2 import Environment,FileSystemLoader
from django.templatetags.static import static
from django.urls import reverse
from django.template.loader import select_template

def get_environment(**options):
	
	env = Environment(
		**options,
	)
	env.globals.update({
		"static": static,
		"url": reverse,
	})
	return env
