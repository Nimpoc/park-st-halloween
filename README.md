# Park St Halloween Lab

A dependency-free, static dashboard of trick-or-treater records from 2420 Park St, Bellingham, Washington (2010–2026). Open `index.html` directly or serve this directory with any static HTTP server. No install, build, API key, or external assets are required.

## Data and provenance

The embedded `BUNDLED` records come from the project brief's historical transcriptions; source sheet images are not included. Each record separates `sourceTotal`, `estimate`, `sourceApproximate`, `computedInterpretation`, `intervals`, `confidence`, `handwrittenWeather`, `externalWeather`, `status`, and `notes`. The annual chart uses a source total first, an explicitly approximate estimate second, and otherwise a gap. The average includes all available totals, including approximate values; missing years never count as zero.

2013 and 2020 have no source sheets. 2015 has no verified total. 2011 is approximately 138 from a damaged sheet; 2025 is a low-confidence reconstruction of approximately 231. 2017 preserves source total 174 and possible computed interpretation 178 without inventing interval times. Only 2026 has supplied interval data: twenty 15-minute counts summing to 505. Earlier-year confidence is conservatively medium unless a specific low/high designation was supplied. Some historical notes are paraphrases, identified in their text. External weather is unpopulated, separate from porch observations, and can later contain `{ "source": "...", "location": "...", "observations": "..." }`.

## Editing and backups

Use **Data → Edit** or **Add / edit a year**. A blank numeric field means unknown, not zero. Interval JSON uses chronological, non-overlapping same-day 24-hour start times, integer counts, and explicit durations: `[{"time":"17:00","count":12,"minutes":15}]`. Source totals and interval sums remain separate when they disagree.

Changes are validated and saved under `park-st-halloween.overrides.v1` in this browser's localStorage. Immutable bundled records are merged with local overrides for display, and local records are labeled. Private browsing, storage restrictions, clearing browser data, or changing origin may prevent persistence or remove edits; export backups. Restore removes only that year's override. To update the shared defaults, edit the embedded source records in `index.html`, commit and push.

**Export JSON** includes `schemaVersion: 1`, the original bundled records for reference, and a separate `overrides` object keyed by year. Edit values inside `overrides` for import. Import validates the entire override collection before changing storage, asks before merging, and replaces only matching local years. The export's `bundled` field is informational and is never imported over built-in defaults. Notes are rendered as text, never executable HTML.

## GitHub Pages

In **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, branch **main**, folder **/ (root)**, then **Save**. The empty `.nojekyll` file disables Jekyll processing. Expected URL: https://nimpoc.github.io/park-st-halloween/

All CSS and JavaScript are embedded in the root HTML. There are no root-relative asset paths, so GitHub project subpaths work. The responsive SVG charts use their viewBox to resize, support touch selection and keyboard activation, and require no hover. iPhone safe areas, 44px controls, and Add to Home Screen metadata are included. Large tables scroll inside their own container rather than expanding the page.
