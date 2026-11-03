# After dark on Park Street

A responsive visual almanac of Halloween arrivals in Bellingham, Washington. Published at https://nimpoc.github.io/park-st-halloween/ through the repository's existing GitHub Pages setup.

## Experience

- Editorial story with annual lollipops, a fifteen-year ridgeline portrait, cumulative overlays and a weather/turnout scatterplot.
- Compare any combination of years: arrivals normalized per 15 minutes, known cumulative counts, actual airport temperature. Tap the chart or use its keyboard-accessible time slider. All numeric observations have table alternatives.
- Browse every year's notes, original scans, tally reconciliation and raw airport METAR reports.
- Add or edit years with ordinary time/count inputs and optional source pictures. CSV import and notebook-backup restoration require a review before saving.

No runtime dependencies, API keys or installation. Open `index.html` directly, or serve the parent directory and visit `/park-st-halloween/`. All paths are relative for GitHub Pages compatibility. No live network call is needed to render the data. Original images load only when opened in the notebook.

## Data and uncertainty

`data/records.json` contains 2010–2026. Fifteen source scans cover fourteen years; the second 2011 image is a detail of the same sheet. 2013 and 2020 have no sheets. 2026 is supplied chat transcription, with no scan in the folder. All original scans are retained under `sources/`.

Time labels are interpreted as interval starts. Explicit durations take precedence; otherwise sheet cadence is used and documented. Blank rows are **unknown**, not zero, and break the curves. No missing visitors are interpolated. Running totals include only transcribed time rows. Rate comparisons normalize 20- and 30-minute observations to visitors per 15 minutes; this does not create 15-minute measurements.

Written annual totals and interval sums are separate. See `DATA_AUDIT.md` for discrepancies and unresolved handwriting. In particular, 2015 and 2025 annual figures are estimates, 2011 is partly illegible, and 2023's written total does not reconcile with its visible rows. Dashed curves identify low-confidence transcriptions.

## Weather

`data/weather.json` caches 85 routine hourly KBLI Bellingham International Airport METARs, five reports per Halloween from 2010 through 2026, archived by Iowa Environmental Mesonet. Full daily downloads are retained in `data/airport-YEAR.csv`; every year links to its exact request URL. Retrieval script: `python3 scripts/fetch-weather.py` (network required). It currently requests the archive range 2010–2026; extend that range when publishing a later edition.

Evening means and ranges use reports timestamped 17:00–21:59 in `America/Los_Angeles`, not whole-day weather. Precipitation is the preceding-hour amount in routine hourly reports; traces remain distinct. Airport conditions describe the airport, not the porch. The scatterplot is descriptive; it makes no causal claim.

## Saving records

The website's built-in archive stays separate from browser-local edits. Edits save under `park-st-halloween.overrides.v2`; earlier `v1` edits are readable and preserved. A failed storage write leaves the prior saved collection intact. The interface explains that edits do not sync to other devices or update the shared website. Backup JSON contains local edits and attached local pictures, with the bundled archive included for reference. Restoration imports only the explicitly editable `overrides` collection. Old v1 backups remain accepted.

To add a year without programming: **Add & save → Add a Halloween**. To update the shared edition, provide the saved backup to the site maintainer, merge reviewed records into `data/records.json`, then run `node scripts/bundle.mjs` and publish. This deliberate review keeps uncertain handwriting out of shared defaults until checked. The original scan transcription helper is archival and accepts the original scan folder as its argument; edit the reviewed JSON for routine updates instead of rerunning it.

CSV requires `year,time,count` and optional `minutes` (default 15). Times use 24-hour format. Rows must be chronological and nonoverlapping. Import replaces the matching year's time rows only, retaining its other fields; the review shows the total before saving. Choose **Save a backup** before replacing local records.

## Validation

`node tests/model.cjs` checks data/source reconciliation, all image paths, airport records, missing totals, gap behavior, interval normalization, v1/v2 backup round trips, CSV ingest and invalid input rejection. `node --check app.js` and `node --check model.js` check syntax.

The browser QA log in `VALIDATION.md` records responsive and interaction checks. Browser viewport tests are not a substitute for physical iPhone Safari testing.
