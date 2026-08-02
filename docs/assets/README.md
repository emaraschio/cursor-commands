# Demo and social assets

Place media here before uncommenting README embeds.

## demo.gif (manual capture)

1. Open Cursor agent chat in a clean window.
2. Type `/` and show catalog autocomplete.
3. Run `/define-agent-goal` with a tiny `service-a` task.
4. Show the six-part Goal output (~20 seconds total).
5. Compress under ~5 MB:

```bash
# gifski (preferred)
gifski -o docs/assets/demo.gif --width 1280 --quality 80 capture/*.png

# or ffmpeg palette two-pass
ffmpeg -i capture.mov -vf "fps=12,scale=1280:-1:flags=lanczos,palettegen" palette.png
ffmpeg -i capture.mov -i palette.png -lavfi "fps=12,scale=1280:-1:flags=lanczos[x];[x][1:v]paletteuse" docs/assets/demo.gif
```

Then remove the HTML comment around the README embed.

## social-preview.png

1280x640 card for GitHub Settings → Social preview. Commit lives in-repo; upload is manual (no API).
