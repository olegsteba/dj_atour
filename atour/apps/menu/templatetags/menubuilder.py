from apps.menu.models import Menu, MenuItem
from django import template
from django.core.cache import cache


register = template.Library()


def build_menu(parser, token):
    """
    {% menu menu_name %}
    """
    try:
        tag_name, menu_name = token.split_contents()
    except:
        raise template.TemplateSyntaxError("%r tag requires exactly one argument" % token.contents.split()[0])
    return MenuObject(menu_name)


class MenuObject(template.Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name

    def render(self, context):
        try:
            current_path = context['request'].path
            user = context['request'].user
        except KeyError:
            current_path = None
            user = None

        context['menuitems'] = get_items(self.menu_name, current_path, user)
        return ''
  

def build_sub_menu(parser, token):
    """
    {% submenu %}
    """
    return SubMenuObject()


class SubMenuObject(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        current_path = context['request'].path
        user = context['request'].user
        menu = False
        for m in Menu.objects.filter(base_url__isnull=False):
            if m.base_url and current_path.startswith(m.base_url):
                menu = m

        if menu:
            context['submenu_items'] = get_items(menu.slug, current_path, user)
            context['submenu'] = menu
        else:
            context['submenu_items'] = context['submenu'] = None
        return ''


def get_items(menu_name, current_path, user):
    """
    Если возможно, используйте кэшированный список элементов, чтобы избежать постоянных повторных запросов к базе данных.
    Ключ содержит название меню, аутентификацию пользователя и текущий путь.
    Отключите кэширование, установив значение MENU_CACHE_TIME равным -1
    """
    from django.conf import settings
    cache_time = getattr(settings, 'MENU_CACHE_TIME', 1800)
    debug = getattr(settings, 'DEBUG', False)

    if user:
        is_authenticated = user.is_authenticated
        is_anonymous = user.is_anonymous
    else:
        is_authenticated = False
        is_anonymous = True

    if cache_time >= 0 and not debug:
        cache_key = 'django-menu-items/%s/%s/%s'  % (menu_name, current_path, is_authenticated)
        menuitems = cache.get(cache_key, [])
        if menuitems:
            return menuitems
    else:
        menuitems = []
        

    menu = Menu.objects.filter(slug=menu_name).first()

    if not menu:
        return []

    for i in MenuItem.objects.filter(menu=menu).order_by('position'):
        if current_path:
            current = ( i.url != '/' and current_path.startswith(i.url)) or ( i.url == '/' and current_path == '/' )
            if current_path != i.url:
                current = False
        else:
            current =False

        show_anonymous = i.anonymous_only and is_anonymous
        show_authorized = i.authorized_only and is_authenticated
        if (not (i.authorized_only or i.anonymous_only)) or (i.authorized_only and show_authorized) or (i.anonymous_only and show_anonymous):
            menuitems.append({'url': i.url, 'title': i.title, 'current': current,})

    if cache_time >= 0 and not debug:
        cache.set(cache_key, menuitems, cache_time)
    return menuitems


register.tag('menu', build_menu)
register.tag('submenu', build_sub_menu)
