from django.urls import reverse
from django.templatetags.static import static
from jinja2 import Environment

def get_environment(**options):
	env = Environment(
		**options,
	)
	env.globals.update({
		"static": static,
		"url": reverse,
	})
	return env
