"""Html builder library for Webface frontend."""


class HTMLPage(object):
    """Basic html page object."""

    def __init__(self):
        """Initiation."""
        self._contents = ""
        self._head = ""

    def add_content(self, content):
        """Add content to a page."""
        bt = tag_open('br')
        content = content.replace("\n", bt)
        self._contents += content

    def add_head(self, content):
        """Add content to a page."""
        self._head += content

    @property
    def head(self):
        """Return page header."""
        ret = tag_open('head')
        ret += self._head
        ret += tag_close('head')
        return ret

    @property
    def body(self):
        """Return page body."""
        ret = tag_open('body')
        ret += self._contents
        ret += tag_close('body')
        return ret

    @property
    def contents(self):
        """Get page contents."""
        ret = '<!DOCTYPE html>'
        ret += tag_open('html')
        if self._head:
            ret += self.head
        ret += tag_open('body')
        if self._contents:
            ret += self._contents
        ret += tag_close('body')
        ret += tag_close('html')
        return ret

    def clear(self):
        """Clear page contents and header."""
        self._contents = ""
        self._head = ""

    def clear_contents(self):
        """Clear page contents."""
        self._contents = ""

    def clear_head(self):
        """Clear page header."""
        self._head = ""


def tag_open(tag: str, tag_properties: dict=None):
    """Start a tag."""
    ret = '<' + tag
    if tag_properties:
        ret += " "
        for tag_property_key in tag_properties.keys():
            ret += (str(tag_property_key) + '="' +
                    str(tag_properties.get(tag_property_key)) + '" ')
    ret += '>'
    return ret


def tag_close(tag: str):
    """End a tag."""
    return '</' + tag + '>'


def tag(tag: str, content: str=None, tag_properties: dict=None, ):
    """Create a node."""
    ret = tag_open(tag, tag_properties)
    if content:
        ret += content
    ret += tag_close(tag)
    return ret
