"""CSS styles for the mod tracker."""

STYLES = """
        /* Fonts */
        @font-face {
            font-family: 'Inter';
            font-style: normal;
            font-weight: 400;
            font-display: swap;
            src: url(assets/fonts/inter-400.ttf) format('truetype');
        }
        @font-face {
            font-family: 'Inter';
            font-style: normal;
            font-weight: 500;
            font-display: swap;
            src: url(assets/fonts/inter-500.ttf) format('truetype');
        }
        @font-face {
            font-family: 'Inter';
            font-style: normal;
            font-weight: 600;
            font-display: swap;
            src: url(assets/fonts/inter-600.ttf) format('truetype');
        }
        @font-face {
            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-display: swap;
            src: url(assets/fonts/inter-700.ttf) format('truetype');
        }

        /* Variables */
        :root {
            --bg-primary: #1a1614;
            --bg-secondary: #252120;
            --bg-tertiary: #2d2825;
            --text-primary: #e8dcc8;
            --text-secondary: #a89880;
            --border-color: #3d352f;
            --gold-primary: #c9a227;
            --gold-secondary: #8b6914;
            --gold-light: #e6c453;
            --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.3);
            --shadow-md: 0 1px 3px 0 rgb(0 0 0 / 0.4), 0 1px 2px -1px rgb(0 0 0 / 0.3);
            --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.4), 0 4px 6px -4px rgb(0 0 0 / 0.3);
        }

        /* Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Hide scrollbar */
        ::-webkit-scrollbar {
            display: none;
        }

        html {
            scrollbar-width: none;
            -ms-overflow-style: none;
        }

        /* Base */
        html {
            font-size: 110%;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.4;
            min-height: 100vh;
            padding: 0;
            background-image: 
                url("assets/img/d20.svg"),
                radial-gradient(ellipse at top, rgba(201, 162, 39, 0.08), transparent 60%),
                radial-gradient(ellipse at bottom, rgba(139, 105, 20, 0.05), transparent 60%);
        }

        /* Header */
        .app-header {
            padding: 1.5rem 1.5rem 0;
            position: sticky;
            top: 0;
            z-index: 100;
            background: linear-gradient(180deg, var(--bg-primary) 0%, transparent 100%);
            pointer-events: none;
        }

        .header-content {
            max-width: 600px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            padding: 0.625rem 1.25rem;
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 9999px;
            box-shadow: var(--shadow-lg), 0 0 0 1px rgba(201, 162, 39, 0.1);
            pointer-events: auto;
        }

        .header-logo {
            height: 2rem;
            width: auto;
            opacity: 0.9;
        }

        .header-title {
            font-size: 0.9375rem;
            font-weight: 600;
            color: var(--text-primary);
            letter-spacing: 0.01em;
        }

        .header-stat {
            display: flex;
            align-items: center;
            gap: 0.375rem;
            font-size: 0.8125rem;
            color: var(--text-secondary);
        }

        .header-stat-value {
            font-weight: 600;
            color: var(--gold-primary);
        }

        .header-subtext {
            max-width: 600px;
            margin: 0.5rem auto 0;
            text-align: center;
            font-size: 0.75rem;
            color: var(--text-secondary);
            opacity: 0.7;
        }

        /* Layout */
        .changelog-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1.5rem;
        }

        .changelog-stack {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        h1 {
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            color: var(--text-primary);
            letter-spacing: -0.03em;
            text-align: center;
        }

        .hero-image {
            width: 100%;
            max-width: 220px;
            margin: 0 auto 1rem;
            display: block;
        }

        /* Date Navigation - Pill Style */
        .date-nav {
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0.75rem 0;
            position: relative;
        }

        .date-nav::before {
            content: '';
            position: absolute;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--border-color), transparent);
            z-index: 1;
        }

        .date-nav-pill {
            display: flex;
            flex-direction: column;
            align-items: center;
            background: var(--bg-primary);
            padding: 0.375rem 0.75rem;
            border: 1px solid var(--border-color);
            border-radius: 9999px;
            z-index: 2;
            box-shadow: var(--shadow-sm);
            gap: 0.125rem;
        }

        .date-nav-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 1.75rem;
            height: 1.75rem;
            border: 1px solid var(--border-color);
            background: var(--bg-primary);
            border-radius: 9999px;
            cursor: pointer;
            color: var(--text-secondary);
            transition: all 0.15s ease;
            z-index: 2;
            box-shadow: var(--shadow-sm);
        }

        .date-nav-btn.prev {
            margin-right: 0.5rem;
        }

        .date-nav-btn.next {
            margin-left: 0.5rem;
        }

        .date-nav-btn:hover:not(:disabled) {
            background: var(--bg-tertiary);
            color: var(--text-primary);
        }

        .date-nav-btn:disabled {
            opacity: 0.3;
            cursor: not-allowed;
        }

        .date-nav-btn svg {
            width: 0.875rem;
            height: 0.875rem;
        }

        .date-nav-current {
            font-size: 0.875rem;
            font-weight: 500;
            color: var(--text-secondary);
            padding: 0 2rem;
            text-align: center;
        }

        .date-nav-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            padding: 0.125rem 0.75rem;
            font-size: 0.6875rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.03em;
            color: var(--gold-primary);
            background: rgba(201, 162, 39, 0.15);
            border: 1px solid rgba(201, 162, 39, 0.3);
            border-radius: 9999px;
        }

        /* Date Sections */
        .date-section {
            display: none;
        }

        .date-section.active {
            display: block;
        }

        /* Date Content Card */
        .date-content {
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 0.75rem;
            padding: 0.75rem;
            margin-top: 0.5rem;
            box-shadow: var(--shadow-sm);
        }

        /* Tab Bar */
        .tab-bar {
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0.75rem 0;
        }

        .tab-group {
            display: flex;
            align-items: center;
            background: var(--bg-primary);
            border: 1px solid var(--border-color);
            border-radius: 9999px;
            box-shadow: var(--shadow-sm);
            padding: 0.25rem;
            gap: 0.25rem;
        }

        .tab-button {
            display: flex;
            align-items: center;
            gap: 0.375rem;
            padding: 0.25rem 0.75rem;
            border: none;
            background: transparent;
            border-radius: 9999px;
            cursor: pointer;
            font-family: 'Inter', sans-serif;
            font-size: 0.875rem;
            font-weight: 500;
            color: var(--text-secondary);
            transition: all 0.2s ease;
        }

        .tab-button:hover {
            background: var(--bg-tertiary);
            color: var(--text-primary);
        }

        .tab-button.active {
            background: linear-gradient(135deg, var(--gold-primary), var(--gold-secondary));
            color: var(--bg-primary);
        }

        .tab-button.active .tab-count {
            background: rgba(0, 0, 0, 0.2);
            color: inherit;
        }

        .tab-button:disabled {
            opacity: 0.4;
            cursor: not-allowed;
            pointer-events: none;
        }

        .tab-button:disabled:hover {
            background: transparent;
            color: var(--text-secondary);
        }

        .tab-count {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 1.5rem;
            height: 1.25rem;
            padding: 0 0.375rem;
            font-size: 0.75rem;
            font-weight: 600;
            background: var(--bg-tertiary);
            border-radius: 9999px;
            transition: all 0.2s ease;
        }

        /* Tab Panels */
        .tab-panels {
            position: relative;
        }

        .tab-panel {
            display: none;
            animation: fadeIn 0.2s ease;
        }

        .tab-panel.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Mod List */
        .mod-list {
            display: flex;
            flex-direction: column;
        }

        /* Mod Row */
        .mod-row {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.5rem 0.75rem;
            text-decoration: none;
            color: inherit;
            border-bottom: 1px solid var(--border-color);
            transition: background 0.15s ease;
        }

        .mod-row:last-child {
            border-bottom: none;
        }

        .mod-row:hover {
            background: var(--bg-tertiary);
        }

        .mod-thumb {
            width: 64px;
            height: 36px;
            object-fit: cover;
            border-radius: 0.25rem;
            background: var(--bg-tertiary);
            flex-shrink: 0;
        }

        .mod-info {
            flex: 1;
            min-width: 0;
            display: flex;
            flex-direction: column;
            gap: 0.125rem;
        }

        .mod-title {
            font-size: 0.875rem;
            font-weight: 500;
            color: var(--text-primary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .mod-summary {
            font-size: 0.75rem;
            color: var(--text-secondary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .mod-link-icon {
            width: 1rem;
            height: 1rem;
            color: var(--text-secondary);
            flex-shrink: 0;
            opacity: 0.5;
            transition: opacity 0.15s ease;
        }

        .mod-row:hover .mod-link-icon {
            opacity: 1;
        }

        /* Empty State */
        .empty-state {
            text-align: center;
            padding: 3rem 1rem;
            color: var(--text-secondary);
        }

        .empty-state-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            opacity: 0.5;
        }

        .empty-state-text {
            font-size: 1rem;
            font-weight: 500;
        }
"""
