from django import apps 

class OrderConfig(apps.AppConfig):
    name                = 'sw_order'
    verbose_name        = 'Замовлення'
    verbose_name_plural = verbose_name


default_app_config = 'sw_order.OrderConfig'

