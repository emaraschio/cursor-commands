# Demo and social assets

## demo.gif

Illustrative mock (not a live IDE screen recording): `/` autocomplete → `/define-agent-goal` → six-part Goal. ~126 KB, 960x540.

Regenerate:

```bash
# uses the same script pattern as the advertising rollout (Pillow in a venv)
python3 -m venv /tmp/social-preview-venv
/tmp/social-preview-venv/bin/pip install -q Pillow
# then re-run the generator from the advertising session, or ask the agent to rebuild
```

Optional: replace with a real Cursor capture later. Compress under ~5 MB:

```bash
gifski -o docs/assets/demo.gif --width 960 --quality 80 capture/*.png
```

## social-preview.png

Exact 1280x640 card for GitHub Settings → Social preview (manual upload).
