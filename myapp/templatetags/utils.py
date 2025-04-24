from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_domain(context):
    request = context['request']
    return f"{request.scheme}://{request.get_host()}"
