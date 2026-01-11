from django import template

register = template.Library()


@register.filter
def split(value, delimiter):
    return value.split(delimiter) if value else []


@register.filter
def offset(dt):
    if dt.utcoffset() is not None:
        offset = dt.utcoffset()
        return offset
    return None
