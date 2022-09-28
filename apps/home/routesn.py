from apps.home import blueprint
from flask import render_template, has_request_context
from jinja2 import TemplateNotFound


@blueprint.route('/index')
def index():

    return render_template('home/home.html', segment='index')


@blueprint.route('/<template>')
def route_template(template):

    try:
        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template(f"home/{template}", segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except Exception:
        return render_template('home/page-500.html'), 500
