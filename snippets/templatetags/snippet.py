from django import template
from django.utils.html import linebreaks

from snippets.models import Snippet

register = template.Library()

class SippetRenderer(template.Node):
    def __init__(self, name, resolve_var=False):
        if resolve_var:
            self.name = template.Variable(name)
        else:
            self.name = name
        self.resolve_var = resolve_var
        
    def render(self, context):
        if self.resolve_var:
            try:
                name = self.name.resolve(context)
            except template.VariableDoesNotExist:
                return """<!-- Cannot resolve variable `%s`. Did you forget to add quotes? -->""" % self.name
        else:
            name = self.name
        try:
            snippet = Snippet.objects.get(name=name, is_active=True)
        except Snippet.DoesNotExist:
            return ''
        if snippet.is_html:
            return snippet.content # output as is
        else:
            return linebreaks(snippet.content, True) # True for autoescape


@register.tag
def get_snippet(parser, token):
    try:
        tag_name, snippett_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "get_snippet tag requires a single argument"
    if snippett_name[0] in ('"', "'"):
        # quoted string
        if not (snippett_name[0] == snippett_name[-1]):
            raise template.TemplateSyntaxError, "%r tag's argument must be prpoperly quoted" % tag_name
        return SippetRenderer(snippett_name[1:-1])
    else:
        # this must be a variable
        return SippetRenderer(snippett_name, True)
