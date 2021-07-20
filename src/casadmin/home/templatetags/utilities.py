import datetime
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def order_by_for_header_table(object_list, args):
    object = object_list.first()
    order_by = object_list.query.order_by[0]
    table_head = ''
    for field in args.split(','):
        field = field.strip()
        icon = ''
        title = object._meta.get_field(field).verbose_name.title() if (field in object.__dict__) else '{0} No es un campo de {1}'.format(field, object._meta.model_name.title())
        if order_by == field:
            field = "-" + field
            icon = "<i class='material-icons'>arrow_drop_up</i>"
        elif order_by == "-" + field:
            icon = "<i class='material-icons'>arrow_drop_down</i>" 
        table_head += "<th><a href='?order-by={0}'>{1}{2}</a></th>".format(field, title, icon)
    
    return mark_safe(table_head)

@register.filter
def detail_row(object, field):
    title = object._meta.get_field(field).verbose_name.title() if (field in object.__dict__) else 'ERROR'
    value = object.__dict__[field] if (field in object.__dict__) else '<strong> {0} </strong> No es un campo de <strong> {1} </strong>'.format(field, object._meta.model_name.title())

    if isinstance(value, bool):
        value = iconyesno(value)

    elif isinstance(value, datetime.datetime):
        value = value.strftime('%d-%m-%Y %H:%M:%S')
    
    elif value == None:
        value = ''
    response = '<div class="row mb-3" style="border-bottom: 1px solid #f1f1f1"><div class="col-sm col-md-5 col-xl-4"><h5>' + title + '</h5></div><div class="col-sm col-md-7 col-xl-8">' + value + '</div></div>'
    return mark_safe(response)


@register.filter
def iconyesno(bool):
    if bool:
        icon = "<i class='material-icons text-success'>done</i>"
    else:
        icon = "<i class='material-icons text-danger'>close</i>"
    return mark_safe(icon)