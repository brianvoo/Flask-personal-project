from flask import Blueprint, render_template
from flask import current_app as app


# Blueprint Configuration
faq_bp = Blueprint(
    'faq_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@faq_bp.route('/faq', methods=['GET', 'POST'])
def home():
    """Homepage."""
    return render_template(
        'faq.jinja2',
        title="FAQ",
        description="FAQs"
    )