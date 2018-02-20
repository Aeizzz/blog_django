from django import template

from blog_django.settings import owner,repo,client_id,client_secret

register = template.Library()

@register.simple_tag
def get_comment():
    return {'owner':owner,'repo':repo,'client_id':client_id,'client_secret':client_secret}
