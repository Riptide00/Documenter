"""Extract css classes and id's and generate a skeleton css file."""
from html.parser import HTMLParser


class CssGenerator(HTMLParser):
    """Extract classes and id's with python HTMLParser."""

    def __init__(self):
        """Initiation."""
        HTMLParser.__init__(self)
        self._css = ""
        self._classes = list()
        self._ids = list()

    def handle_starttag(self, tag, attrs):
        """Parser has found a start tag."""
        css_string = ""
        for att in attrs:
            if att[0] == 'class':
                if att[1] not in self._classes:
                    self._classes.append(att[1])
                    css_string += "." + str(att[1]) + " {\n\n}\n\n"
            elif att[0] == 'id':
                if att[1] not in self._ids:
                    self._ids.append(att[1])
                    css_string += "#" + str(att[1]) + " {\n\n}\n\n"
        self._css += css_string

    @property
    def css(self):
        """Return currently generated css skeleton."""
        return self._css


def extract_css(frontend):
    """Extract css classes and id's from the frontend."""
    cg = CssGenerator()
    for page in frontend.PAGES:
        content = eval("frontend." + page + "()")
        cg.feed(content)
    _write_file(cg.css)


def _write_file(css: str()=""):
    """Write a css file."""
    file = open("theme.css", "w")
    file.write(css)
    file.close()
