"""Changelog container component."""


def changelog_container(title: str, content: str, hero_image_url: str = None) -> str:
    """Generate the main changelog container with pill-style header."""
    logo_html = f'<img src="{hero_image_url}" alt="Logo" class="header-logo">' if hero_image_url else ''
    
    return f"""    <header class="app-header">
        <div class="header-content">
            {logo_html}
            <span class="header-title">{title}</span>
            <div class="header-stat">
                <span class="header-stat-value" id="total-mods">--</span>
                <span>mods</span>
            </div>
        </div>
    </header>
    <main class="changelog-container">
        <div class="changelog-stack">
{content}
        </div>
    </main>"""
