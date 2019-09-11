from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
from io import BytesIO     # for handling byte strings
from io import StringIO

""" This requires: reportlab, xhtml2pdf, html5lib, pypdf """


def render_to_pdf(template, context):
    template = get_template(template)
    context = Context(context)
    html = template.render(context)
    result = StringIO()

    pdf = pisa.pisaDocument(StringIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Errors Encountered: <pre>%s</pre>' % escape(html))
