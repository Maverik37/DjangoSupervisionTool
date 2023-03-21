from django import template

register = template.Library()

@register.filter
def duration(timedelta):
    """
    Format a duration field
    "2h and 30 min" or only "45 min" for example

    :rtype: str
    """
    total_seconds = int(timedelta.total_seconds())
    hours = total_seconds // 3600
    minutes = round((total_seconds % 3600) / 60)
    if minutes == 60:
        hours += 1
        minutes = 0
    if hours and minutes:
        # Display both
        return f'{hours}h and {minutes} min'
    elif hours:
        # Display only hours
        return f'{hours}h'
    # Display only minutes
    return f'{minutes} min'
