# Installing Get-Found OS

## Option 1: Claude Cowork (upload the plugin file)

1. Download `get-found-os-1.1.0.plugin` from the `dist/` folder of this repository (or from the Releases page).
2. In Claude, open the plugins area of Cowork and upload the file, or drag it into a Cowork chat and accept the plugin
   when prompted.
3. Start a new task and say: **"Set up Get-Found for my business."**

## Option 2: Claude Code (from GitHub)

```
/plugin marketplace add jerid-cyber/get-found-os
/plugin install get-found-os@get-found
```

Restart Claude Code if the skills don't appear right away. To update later:

```
/plugin marketplace update get-found
```

## Option 3: Install from a local folder (for testing)

```
/plugin marketplace add /path/to/get-found-os
/plugin install get-found-os@get-found
```

## After installing

1. **Connect your tools** (optional but recommended). The more you connect, the more it can do on its own. See
   `plugins/get-found-os/CONNECTORS.md`. Most useful first: Google Drive (for memory between runs), your CRM, and
   Google Business Profile or analytics.
2. **Choose where Get-Found keeps its files.** Setup asks for this. Pick Google Drive, a connected folder, or a Claude
   project. Scheduled runs start fresh each time, so the files must live somewhere lasting.
3. Say **"Set up Get-Found for my business,"** then **"Run my Visibility Audit,"** then **"Put Get-Found on a
   schedule."**

## Updating from 1.0.0

Install 1.1.0 over 1.0.0. Your existing `get-found/` files keep working. The first run creates
`get-found/autopilot.md` in shadow mode and asks you to confirm where the folder lives.

## Repository layout

```
get-found-os/
├── .claude-plugin/marketplace.json      # lets Claude Code install from GitHub
├── plugins/get-found-os/                # the plugin itself
│   ├── .claude-plugin/plugin.json
│   ├── agents/                          # 9 department agents
│   ├── skills/                          # 103 skills (100 + command center, heartbeat, setup)
│   ├── CONNECTORS.md
│   ├── LICENSE.md
│   └── README.md
├── dist/get-found-os-1.1.0.plugin       # ready-to-upload file for Cowork
├── README.md · INSTALL.md · CHANGELOG.md · LICENSE.md
```

## Publishing a new version (for the maintainer)

1. Bump `version` in `plugins/get-found-os/.claude-plugin/plugin.json` and in `.claude-plugin/marketplace.json`.
2. Add an entry to `CHANGELOG.md`.
3. Rebuild the upload file from inside the plugin folder:
   `cd plugins/get-found-os && zip -r ../../dist/get-found-os-<version>.plugin . -x "*.DS_Store"`
4. Commit, push, and attach the `.plugin` file to a GitHub Release tagged `v<version>`.
