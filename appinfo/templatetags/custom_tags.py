from django import template
from appregister.models import Avatar

register = template.Library()

@register.simple_tag
def get_user_avatar_url(user_id):
    try:
        avatar = Avatar.objects.get(user_id=user_id)
        return avatar.imagen.url
    except Avatar.DoesNotExist:
        return "/path/to/default/avatar.png"