from django import template
import calendar

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

LOW_THRESHOLD = 0.8
MODERATE_THRESHOLD = 0.9

@register.filter
def check_frequency_format(risk_score):
    if risk_score < 0.8:
        return f"Check this orchard once per week."
    elif risk_score < 0.9:
        return f"Check this orchard once every 3 days."
    else:
        return f"Check this orcahrd once per day."
    
@register.filter
def risk_factor_format(risk_score):
    if risk_score < LOW_THRESHOLD:
        return f"Low Risk ({risk_score:.2f})"
    elif risk_score < MODERATE_THRESHOLD:
        return f"Moderate Risk ({risk_score:.2f})"
    else:
        return f"High Risk ({risk_score:.2f})"

@register.filter
def risk_factor_class(risk_score):
    if risk_score < LOW_THRESHOLD:
        return "low"
    elif risk_score < MODERATE_THRESHOLD:
        return "medium"
    else:
        return "high"