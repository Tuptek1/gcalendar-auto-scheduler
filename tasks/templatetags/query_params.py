from django import template
from urllib.parse import urlencode, parse_qs

register = template.Library()

@register.simple_tag(takes_context=True)
def toggle_query_param(context, key, value):
    request = context['request']
    query_params = request.GET.copy()

    if query_params.get(key) == value:
        query_params.pop(key, None)
    else:
        query_params[key] = value
    
    return f"?{urlencode(query_params)}"
