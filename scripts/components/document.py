"""HTML document wrapper component."""

from .styles import get_all_styles

COLLAPSIBLE_SCRIPT = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('.section-header').forEach(function(header) {
                header.addEventListener('click', function() {
                    const content = this.nextElementSibling;
                    const isExpanded = this.getAttribute('aria-expanded') === 'true';
                    
                    this.setAttribute('aria-expanded', !isExpanded);
                    content.classList.toggle('collapsed', isExpanded);
                });
            });
        });
    </script>
"""


def html_document(title: str, body_content: str) -> str:
    """Generate a complete HTML document."""
    styles = get_all_styles()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>{styles}
    </style>
</head>
<body>
{body_content}
{COLLAPSIBLE_SCRIPT}
</body>
</html>
"""
