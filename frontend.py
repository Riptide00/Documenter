"""Webface frontend."""
import bottle
import htmllib
import documenter as doc
import importlib
import pip


STYLE = htmllib.tag_open('link', {'href': '/theme.css',
                                  'rel': 'stylesheet',
                                  'type': 'text/css'})
ICON = htmllib.tag_open('link', {'rel': 'icon', 'href': 'favicon.ico'})
PAGES = ['document_webface']


def error(text):
    """Return default page on errors."""
    ret = htmllib.tag('h1', text, {'class': 'error'})
    return ret


def navigation():
    """Return a navigation bar based on installed packages."""
    installed_packages = pip.get_installed_distributions()
    list_items = ""
    for i in installed_packages:
        itm = str(i.key) + " " + str(i.version)
        link = htmllib.tag('a', itm, {'href': '/' + i.key})
        list_items += htmllib.tag('li', link)
    return htmllib.tag('ul', list_items, {'id': 'navigation'})


def footer():
    """Returna footer."""
    footer = '<img src="/bottle.png"></img><br>'
    footer += 'Powered by <a href="http://bottlepy.org">Bottle.py</a>'
    return htmllib.tag('footer', footer)


@bottle.get('/bottle.png')
def bottle_logo():
    """Serve an image file."""
    return bottle.static_file('bottle.png', root='images/')


@bottle.get('/theme.css')
def stylesheet():
    """Serve a static css file."""
    return bottle.static_file('theme.css', root='css/')


@bottle.route('/favicon.ico')
def favicon():
    """Reroute default favicon requests."""
    return bottle.static_file('favicon.ico', root='images/')


@bottle.route('<module:path>')
def document_webface(module='/random'):
    """Display documenter in webface w/ dynamicly looked up modules."""
    page = htmllib.HTMLPage()
    page.add_head(STYLE)
    page.add_head(ICON)
    page.add_content(navigation())
    if module:
        module = module.lower()
        if len(module) == 1:
            module = 'random'
        if module[0] == "/":
            module = module[1:]
    else:
        module = 'random'
    m = None
    try:
        m = importlib.import_module(module)
    except:
        page.add_content(error('Module not found!'))
    try:
        page.add_content(doc.document(m))
    except:
        page.add_content(error('Failed to built docs!'))
    page.add_content(footer())
    return page.contents
