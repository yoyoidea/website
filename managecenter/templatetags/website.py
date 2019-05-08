from django import template

register = template.Library()


def list_range(data, step):
    return range(0, len(data), step)


register.filter('list_range', list_range)


@register.filter
def get_at_index_url(list, index):
    return list[index].url


@register.filter
def get_at_index_logo_url(list, index):
    return list[index].logo_url


@register.filter
def get_at_index_title(list, index):
    return list[index].title


@register.filter
def get_at_index_describe(list, index):
    return list[index].describe


@register.filter
def add_index(num1, num2):
    return num1 + num2
