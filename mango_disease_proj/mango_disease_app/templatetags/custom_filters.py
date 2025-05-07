from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''


@register.filter 
def meterclass(value):
    try:
        if value >= 7:
            return 'meter-high'
        elif value >= 4:
            return 'meter-med'
        else:
            return 'meter-low'
    except Exception:
        return ''