"""Tab components for the mod tracker interface."""

from typing import Optional


def tab_bar(new_count: int, updated_count: int, active_tab: str = "new") -> str:
    """
    Generate the tab bar with New and Updated tabs.

    Args:
        new_count: Number of new mods
        updated_count: Number of updated mods
        active_tab: Which tab is active ('new' or 'updated')

    Returns:
        HTML string for the tab bar
    """
    new_active = "active" if active_tab == "new" else ""
    updated_active = "active" if active_tab == "updated" else ""

    return f"""
        <div class="tab-bar">
            <div class="tab-group">
                <button class="tab-button {new_active}" data-tab="new" onclick="switchTab('new')">
                    <span>New</span>
                    <span class="tab-count">{new_count}</span>
                </button>
                <button class="tab-button {updated_active}" data-tab="updated" onclick="switchTab('updated')">
                    <span>Updated</span>
                    <span class="tab-count">{updated_count}</span>
                </button>
            </div>
        </div>
    """


def mod_card(
    title: str,
    summary: str,
    image_url: Optional[str] = None,
    profile_url: Optional[str] = None,
    timestamp: Optional[str] = None,
) -> str:
    """
    Generate a compact mod row.

    Args:
        title: Mod name
        summary: Mod description
        image_url: URL to the mod's thumbnail
        profile_url: URL to the mod's page
        timestamp: Formatted timestamp string

    Returns:
        HTML string for the mod row
    """
    fallback_image = "https://placehold.co/80x45/e2e8f0/64748b?text=No+Image"
    img_src = image_url or fallback_image

    # Build as a link if profile_url exists
    tag = "a" if profile_url else "div"
    href = (
        f'href="{profile_url}" target="_blank" rel="noopener noreferrer"'
        if profile_url
        else ""
    )

    # Link icon (external link)
    link_icon = (
        """<svg class="mod-link-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M6 10L14 2m0 0h-5m5 0v5M8 4H3a1 1 0 00-1 1v8a1 1 0 001 1h8a1 1 0 001-1V9"/></svg>"""
        if profile_url
        else ""
    )

    return f"""<{tag} class="mod-row" {href}>
            <img class="mod-thumb" src="{img_src}" alt="" loading="lazy" onerror="this.src='{fallback_image}'">
            <div class="mod-info">
                <div class="mod-title">{title}</div>
                <div class="mod-summary">{summary}</div>
            </div>
            {link_icon}
        </{tag}>"""


def tab_panel(tab_id: str, content: str, is_active: bool = False) -> str:
    """
    Generate a tab panel container.

    Args:
        tab_id: The ID for the tab panel ('new' or 'updated')
        content: The HTML content for the panel
        is_active: Whether this panel is active

    Returns:
        HTML string for the tab panel
    """
    active_class = "active" if is_active else ""

    return f"""
        <div class="tab-panel {active_class}" id="panel-{tab_id}">
            {content}
        </div>
    """


def empty_state(message: str = "No mods to display") -> str:
    """
    Generate an empty state message.

    Args:
        message: The message to display

    Returns:
        HTML string for the empty state
    """
    return f"""
        <div class="empty-state">
            <div class="empty-state-icon">📦</div>
            <div class="empty-state-text">{message}</div>
        </div>
    """


def tabs_script() -> str:
    """
    Generate the JavaScript for tab and date switching.

    Returns:
        JavaScript code for the tab and date navigation functionality
    """
    return """
        <script>
            let currentDateIndex = 0;
            let currentTab = 'new';
            
            function switchTab(tabId) {
                const activeSection = document.querySelector('.date-section.active');
                if (!activeSection) return;
                
                // Check if the tab is disabled
                const tabBtn = activeSection.querySelector(`.tab-button[data-tab="${tabId}"]`);
                if (tabBtn && tabBtn.disabled) {
                    tabId = 'new'; // Fall back to 'new' if requested tab is disabled
                }
                
                currentTab = tabId;
                
                // Update tab buttons within the active date section
                activeSection.querySelectorAll('.tab-button').forEach(btn => {
                    btn.classList.toggle('active', btn.dataset.tab === tabId);
                });
                
                // Update panels within the active date section
                activeSection.querySelectorAll('.tab-panel').forEach(panel => {
                    panel.classList.toggle('active', panel.dataset.panel === tabId);
                });
                
                // Save preference
                localStorage.setItem('activeTab', tabId);
            }
            
            function getDaysAgoText(dateStr) {
                const today = new Date();
                today.setHours(0, 0, 0, 0);
                
                // Parse date like "December 02, 2025"
                const entryDate = new Date(dateStr);
                entryDate.setHours(0, 0, 0, 0);
                
                const diffTime = today - entryDate;
                const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
                
                if (diffDays === 0) return 'Today';
                if (diffDays === 1) return '1 day ago';
                return `${diffDays} days ago`;
            }
            
            function updateDateDisplay() {
                const sections = document.querySelectorAll('.date-section');
                const currentLabel = document.querySelector('.date-nav-current');
                const badge = document.querySelector('.date-nav-badge');
                const prevBtn = document.querySelector('.date-nav-btn.prev');
                const nextBtn = document.querySelector('.date-nav-btn.next');
                
                if (!sections.length) return;
                
                // Update visible section
                sections.forEach((section, i) => {
                    section.classList.toggle('active', i === currentDateIndex);
                });
                
                // Update label - show "Start Tracking" for the oldest entry
                const activeSection = sections[currentDateIndex];
                if (currentLabel && activeSection) {
                    const isFirstEntry = currentDateIndex === sections.length - 1;
                    const isMostRecent = currentDateIndex === 0;
                    
                    currentLabel.textContent = isFirstEntry ? 'Started Tracking' : activeSection.dataset.date;
                    
                    // Update badge separately
                    if (badge) {
                        if (isMostRecent && !isFirstEntry) {
                            const daysAgo = getDaysAgoText(activeSection.dataset.date);
                            badge.textContent = `Latest · ${daysAgo}`;
                            badge.style.display = '';
                        } else {
                            badge.style.display = 'none';
                        }
                    }
                }
                
                // Update button states (prev=older, next=newer)
                if (prevBtn) prevBtn.disabled = currentDateIndex === sections.length - 1;
                if (nextBtn) nextBtn.disabled = currentDateIndex === 0;
                
                // Disable Updated tab if no updated entries
                if (activeSection) {
                    const updatedCount = parseInt(activeSection.dataset.updatedCount) || 0;
                    const updatedBtn = activeSection.querySelector('.tab-button[data-tab="updated"]');
                    if (updatedBtn) {
                        updatedBtn.disabled = updatedCount === 0;
                    }
                }
                
                // Restore tab state for the new section
                switchTab(currentTab);
            }
            
            function prevDate() {
                const sections = document.querySelectorAll('.date-section');
                if (currentDateIndex < sections.length - 1) {
                    currentDateIndex++;
                    updateDateDisplay();
                }
            }
            
            function nextDate() {
                if (currentDateIndex > 0) {
                    currentDateIndex--;
                    updateDateDisplay();
                }
            }
            
            function formatTimeAgo(date) {
                const now = new Date();
                const diffMs = now - date;
                const diffMins = Math.floor(diffMs / 60000);
                const diffHours = Math.floor(diffMs / 3600000);
                const diffDays = Math.floor(diffMs / 86400000);
                
                if (diffMins < 1) return 'just now';
                if (diffMins < 60) return `${diffMins} minute${diffMins !== 1 ? 's' : ''} ago`;
                if (diffHours < 24) return `${diffHours} hour${diffHours !== 1 ? 's' : ''} ago`;
                return `${diffDays} day${diffDays !== 1 ? 's' : ''} ago`;
            }
            
            function fetchLastChecked() {
                const el = document.getElementById('last-checked');
                if (!el) return;
                
                fetch('https://api.github.com/repos/xKeeg/bg3-console-mod-tracker/actions/workflows/main.yml/runs?status=success&per_page=1')
                    .then(r => r.json())
                    .then(data => {
                        if (data.workflow_runs && data.workflow_runs.length > 0) {
                            const lastRun = new Date(data.workflow_runs[0].updated_at);
                            el.textContent = `Last checked: ${formatTimeAgo(lastRun)}`;
                        } else {
                            el.textContent = 'Checked hourly';
                        }
                    })
                    .catch(() => {
                        el.textContent = 'Checked hourly';
                    });
            }
            
            // Initialize on load
            document.addEventListener('DOMContentLoaded', function() {
                const savedTab = localStorage.getItem('activeTab');
                if (savedTab && ['new', 'updated'].includes(savedTab)) {
                    currentTab = savedTab;
                }
                
                // Calculate total mods
                const sections = document.querySelectorAll('.date-section');
                let totalMods = 0;
                sections.forEach(section => {
                    totalMods += parseInt(section.dataset.newCount) || 0;
                });
                const totalModsEl = document.getElementById('total-mods');
                if (totalModsEl) {
                    totalModsEl.textContent = totalMods.toLocaleString();
                }
                
                updateDateDisplay();
                fetchLastChecked();
            });
        </script>
    """
