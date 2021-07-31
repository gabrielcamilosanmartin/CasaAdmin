import datetime
from django.utils.safestring import mark_safe
from django import template

register = template.Library()


@register.filter
def order_by_for_header_table(object_list, args):
    """Create header for table list

    Args:
        object_list (Queryset): List of object
        args (str): string with field for headers separate for ,

    Returns:
        string: html with table head and link for order
    """
    meta = object_list.model._meta
    order_by = object_list.query.order_by[0]
    table_head = ''
    for field in args.split(','):
        field = field.strip()
        icon = ''
        title = '{0} No es un campo de {1}'.format(
            field, meta.model_name.title())
        if field in [x.name for x in meta.get_fields()]:
            title = meta.get_field(field).verbose_name.title()
        if order_by == field:
            field = "-" + field
            icon = "<i class='material-icons'>arrow_drop_up</i>"
        elif order_by == "-" + field:
            icon = "<i class='material-icons'>arrow_drop_down</i>"
        table_head += "<th><a href='?order-by={0}'>{1}{2}</a></th>".format(
            field, title, icon)
    return mark_safe(table_head)


@register.filter
def detail_row(object, field):
    """Create row with field verbose name and value

    Args:
        object (modelObject): modelObjet with data
        field (string): field name of modelObject

    Returns:
        string: html with field verbose name and value
    """
    title = "ERROR"
    if field in [x.name for x in object._meta.get_fields()]:
        title = object._meta.get_field(field).verbose_name.title()
    value = '<strong>{0}</strong> No es un campo de' \
        ' <strong>{1}</strong>'.format(field, object._meta.model_name.title())
    if field in [x.name for x in object._meta.get_fields()]:
        value = object.__dict__[field]

    if isinstance(value, bool):
        value = iconyesno(value)

    elif isinstance(value, datetime.datetime):
        value = value.strftime('%d-%m-%Y %H:%M:%S')
    elif value is None:
        value = ''
    response = '<div class="row mb-3" style="border-bottom: 1px solid'\
        '#f1f1f1"><div class="col-sm col-md-5 col-xl-4"><h5>{0}</h5></div>'\
        '<div class="col-sm col-md-7 col-xl-8">{1}</div></div>'.format(
            title, value)
    return mark_safe(response)


@register.filter
def iconyesno(bool):
    """return html icon positive or negative for a bool

    Args:
        bool (bool): bool for return icon

    Returns:
        string: html with icon success or danger depending of bool
    """
    if bool:
        icon = "<i class='material-icons text-success'>done</i>"
    else:
        icon = "<i class='material-icons text-danger'>close</i>"
    return mark_safe(icon)
