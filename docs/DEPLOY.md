# Deploying to GitHub & Releasing Updates

## First-time publish (about 5 minutes)

1. **Create the repo** on GitHub named `get-found-os` (public or private). Do *not* initialize it with a README.
2. **Unzip this package** and open a terminal in the `get-found-os/` folder.
3. **Set your GitHub username** in all links and install commands:
   ```bash
   bash scripts/set-github-owner.sh YOUR_REAL_USERNAME
   ```
4. **Push:**
   ```bash
   git init -b main
   git add .
   git commit -m "Get-Found OS v1.0.0"
   git remote add origin https://github.com/YOUR_REAL_USERNAME/get-found-os.git
   git push -u origin main
   ```
5. **Cut the first release** (GitHub Actions builds and attaches `get-found-os.plugin` automatically):
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
6. Check **Actions** → both *Validate plugin* and *Release plugin* are green, and **Releases** shows `get-found-os.plugin`.
   The README's "Download the plugin" link now works.

No GitHub CLI? You can also drag the unzipped folder's contents into GitHub's "uploading an existing file" page, then create a
release named `v1.0.0` from the Releases page — the release workflow attaches the plugin file.

## Shipping an update

1. Edit files under `plugins/get-found-os/`.
2. Bump the version (semver) in **both** `plugins/get-found-os/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
3. `python3 scripts/build_catalog.py` (if skills changed) and `python3 scripts/validate.py`.
4. Add a `CHANGELOG.md` entry, commit, then `git tag vX.Y.Z && git push --tags`.

Claude Code users get the update with `/plugin marketplace update get-found`; desktop users download the new `.plugin` file.

## What CI checks

`.github/workflows/validate.yml` runs `scripts/validate.py` on every push and pull request:

- `marketplace.json` and `plugin.json` are valid; plugin name is kebab-case; version is semver
- every one of the 103 skill folders has a `SKILL.md` whose frontmatter `name` matches the folder and has a description
- ranks 1–100 are each used exactly once
- every referenced `references/` file exists
- all 9 agents have valid frontmatter with `<example>` blocks and only reference real skills
- every ranked skill is owned by an agent; every skill named in the command center and heartbeat exists
- the version in `plugin.json` matches `marketplace.json`
