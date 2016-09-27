"""Get doc strings from modules."""
import inspect
import htmllib
import conf

EXCLUDE_PRIVATE = conf.EXCLUDE_PRIVATE


def describe_builtin(obj):
    """Describe a builtin function."""
    """
    Built-in functions cannot be inspected by
    inspect.getfullargspec. We have to try and parse
    the __doc__ attribute of the function.
    """
    ret = htmllib.tag('h2', 'Built-in Function')
    docstr = obj.__doc__
    name = obj.__name__
    args = ''
    if docstr:
        items = docstr.split('\n')
        if items:
            func_descr = items[0]
            s = func_descr.replace(name, '')
            idx1 = s.find('(')
            idx2 = s.find(')', idx1)
            if idx1 != -1 and idx2 != -1 and (idx2 > idx1 + 1):
                args = s[idx1 + 1: idx2]
    argstring = ""
    for a in args:
        argstring += str(a) + ", "
    argstring = argstring[:-2]
    ret += htmllib.tag('p', name + "(" + argstring + ")")
    ret += htmllib.tag('h2', 'Documentation')
    ret += htmllib.tag('p', docstr)
    return htmllib.tag('div', ret, {'class': 'builtin'})


def describe_function(obj, method=False):
    """Describe a function."""
    """
    Describe the function object passed as argument.
    If this is a method object, the second argument will
    be passed as True.
    """
    if method:
        ret = htmllib.tag('h2', 'Method')
    else:
        ret = htmllib.tag('h2', 'Function')
    name = obj.__name__
    try:
        arginfo = inspect.getfullargspec(obj)
    except TypeError:
        return
    args = arginfo[0]
    argstring = ""
    for a in args:
        argstring += str(a) + ", "
    argstring = argstring[:-2]
    ret += htmllib.tag('p', name + "(" + argstring + ")")
    ret += htmllib.tag('h2', 'Documentation')
    docstring = str(obj.__doc__)
    ret += htmllib.tag('p', docstring)
    return htmllib.tag('div', ret, {'class': 'function'})


def describe_class(obj):
    """Describe a class."""
    """
    Describe the class object passed as argument,
    including its methods.
    """
    ret = htmllib.tag('h2', 'Class')
    name = obj.__name__
    cl = name + '(' + ')'  # TODO
    ret += htmllib.tag('p', cl)
    ret += htmllib.tag('h2', 'Documentation')
    docstring = str(obj.__doc__)
    ret += htmllib.tag('p', docstring)
    for name in obj.__dict__:
        cobj = getattr(obj, name)
        ret += _inspect(cobj, name, True)
    return htmllib.tag('div', ret, {'class': 'class'})


def describe_module(module):
    """Describe a module."""
    """
    Describe the module object passed as argument
    including its classes and functions
    """
    ret = htmllib.tag('h1', 'Module: ' + module.__name__)
    ret += htmllib.tag('h2', 'Documentation')
    docstring = str(module.__doc__)
    ret += htmllib.tag('p', docstring)
    return ret


def document(module):
    """Get doc strings of the module, module's functions, classes, etc."""
    ret = describe_module(module)
    for name in dir(module):
        obj = getattr(module, name)
        ret += _inspect(obj, name)
    return ret


def _isprivate(name):
    """Check if object is prefixed with '_'."""
    name = str(name)
    if name[0] == '_':
        if name[1] == '_':
            return False
        else:
            return True
    else:
        return False


def _inspect(obj, name, method=False):
    """Inspect object passed by getattr."""
    ret = ""
    if EXCLUDE_PRIVATE:
        if _isprivate(name):
            return ""
    if inspect.isclass(obj):
        ret += describe_class(obj)
    elif (inspect.ismethod(obj) or inspect.isfunction(obj)):
        ret += describe_function(obj, method)
    elif inspect.isbuiltin(obj):
        ret += describe_builtin(obj)
    return ret


if __name__ == '__main__':
    import importlib
    while True:
        module = input("Import: ")
        mod = importlib.import_module(module)
        print(document(mod))
