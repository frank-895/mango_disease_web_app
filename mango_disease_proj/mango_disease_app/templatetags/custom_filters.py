from django import template
from datetime import date, timedelta

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

LOW_THRESHOLD = 0.45
MODERATE_THRESHOLD = 0.7

@register.filter
def check_frequency_format(risk_score):
    if risk_score < LOW_THRESHOLD:
        return f"Once per week."
    elif risk_score < MODERATE_THRESHOLD:
        return f"Every 3 days."
    else:
        return f"Every day."
    
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
    
@register.filter #I THINK THIS CAN BE DELETED
def next_dates(risk_score, time_last_check):
    time_last_check = int(time_last_check) if str(time_last_check).isdigit() else 99
    today = date.today()

    # calculate frequency days
    if risk_score < LOW_THRESHOLD:
        frequency_days = timedelta(days=7)
    elif risk_score < MODERATE_THRESHOLD:
        frequency_days = timedelta(days=3)
    else:
        frequency_days = timedelta(days=1)
    
    last_check_date = today - timedelta(days=time_last_check)
    next_date = last_check_date + frequency_days
    
    if next_date < today:
        next_date = today
        
    next_next_date = next_date + frequency_days
    next_next_next_date = next_next_date + frequency_days

    return f"{next_date.strftime('%B %d, %Y')} | {next_next_date.strftime('%B %d, %Y') } | {next_next_next_date.strftime('%B %d, %Y') }"

@register.filter #Remade to have the dates organised into a list
def next_dates_list(risk_score, time_last_check):
    time_last_check = int(time_last_check) if str(time_last_check).isdigit() else 99
    today = date.today()

    # calculate frequency days
    if risk_score < LOW_THRESHOLD:
        frequency_days = timedelta(days=7)
    elif risk_score < MODERATE_THRESHOLD:
        frequency_days = timedelta(days=3)
    else:
        frequency_days = timedelta(days=1)
    
    last_check_date = today - timedelta(days=time_last_check)
    first_date = last_check_date + frequency_days
    second_date = first_date + frequency_days
    third_date = second_date + frequency_days

    return [first_date, second_date, third_date]

