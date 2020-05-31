from django import template

register = template.Library()


@register.filter
def order_by(queryset, args):
    return queryset.order_by(args)


@register.filter
def to_list(queryset):
    result = list()
    for i in queryset:
        result.append(i.name)
    result = ', '.join(result)
    return result


@register.filter
def to_time(time):
    return time.strftime('%d/%m/%y %H:%M:%S')