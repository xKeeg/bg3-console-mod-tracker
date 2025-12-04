# BG3 Console Mod Tracker

A changelog tracker for Baldur's Gate 3 console mods. Automatically monitors the mod.io API for new and updated mods available on console.

**[View the live site →](https://xkeeg.github.io/bg3-console-mod-tracker/)**

## Features

- 📦 Tracks **new mods** added to the console mod platform
- 🔄 Tracks **mod updates** with version changes
- 📅 Browse changes by date with easy navigation
- ⏰ Automatically checks for updates every hour
- 📱 Mobile-friendly responsive design

## How It Works

1. **Hourly Scrape** - A GitHub Action fetches the latest mod data from the mod.io API
2. **History Tracking** - Changes are tracked using [git-history](https://github.com/simonw/git-history) to detect new and updated mods
3. **HTML Generation** - A static HTML page is generated with the changelog
4. **GitHub Pages** - The site is automatically deployed to GitHub Pages
