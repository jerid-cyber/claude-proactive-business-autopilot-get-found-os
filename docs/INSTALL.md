# Installing Get-Found OS

Get-Found OS is a standard Claude plugin (`plugins/get-found-os/`) inside a Claude plugin marketplace repo
(`.claude-plugin/marketplace.json`). Pick the path that matches where you use Claude.

## 1. Claude desktop app / Cowork — upload the plugin file

1. Download **`get-found-os.plugin`** from the [latest release](https://github.com/YOUR-GITHUB-USERNAME/get-found-os/releases/latest)
   or from `dist/` in this repo. (A `.plugin` file is a zip of the `plugins/get-found-os/` folder.)
2. In Claude, go to **Customize → Plugins → Upload plugin** (menu names can vary by app version), or drop the file into a chat.
3. Review and accept. You should see skills such as `get-found-os:get-found-command-center` and agents such as `get-found-os:scout`.
4. Start with: **"Set up Get-Found for my business."**

**Tip:** connect a folder (desktop app) or use a Claude Project so the `get-found/` work files persist between sessions.

## 2. Claude Code — install from this GitHub marketplace

```bash
/plugin marketplace add YOUR-GITHUB-USERNAME/get-found-os
/plugin install get-found-os@get-found
```

- `get-found` is the marketplace name (from `.claude-plugin/marketplace.json`); `get-found-os` is the plugin name.
- Update: `/plugin marketplace update get-found`
- Remove: `/plugin uninstall get-found-os@get-found`
- Local test without GitHub: `/plugin marketplace add ./path/to/this/repo`

**Private repo?** Claude Code uses your existing git credentials. Make sure `git clone https://github.com/YOUR-GITHUB-USERNAME/get-found-os`
works in your terminal (e.g. `gh auth login`) before adding the marketplace.

## 3. Organization / team marketplace

Owners/admins on Team or Enterprise plans can add this repository as a GitHub-synced plugin marketplace in the
organization's plugin settings. Members then install `get-found-os` from the org catalog and receive updates when you push
a new version.

## 4. Manual install (any Claude Code environment)

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/get-found-os.git
claude --plugin-dir ./get-found-os/plugins/get-found-os
```

## Verify the install

Ask Claude: **"What Get-Found skills do you have?"** — it should list 103 skills and 9 agents. Or run
`python3 scripts/validate.py` from the repo root.

## Recommended connectors after install

Supermetrics (Google Ads, Meta, GA4, Search Console), Google Drive, Gmail, Google Calendar, your CRM (GoHighLevel, Lofty or
HubSpot), your website CMS, and a Google Business Profile connector. See the Connectors table in the [README](../README.md#connectors).

## Troubleshooting

| Problem | Fix |
| --- | --- |
| Upload rejected | Make sure you uploaded the `.plugin` file (zip of the plugin folder with `.claude-plugin/plugin.json` at its root), not the whole repo zip |
| `marketplace add` fails | Confirm the repo path is `owner/repo` and `.claude-plugin/marketplace.json` is on the default branch |
| Skills don't trigger | Use the trigger phrases in each skill description (e.g. "run Get-Found", "next best move") or name the skill directly |
| Work files disappear | Connect a folder or use a Claude Project; otherwise files live only in that session |
| Scheduled runs don't happen | Scheduled tasks are created by `get-found-heartbeat`; check them in Claude's scheduled tasks list |
