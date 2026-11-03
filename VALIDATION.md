# Validation · 2026-11-03

## Automated checks

Passed `node tests/model.cjs`, JavaScript syntax checks, and `git diff --check`.

Verified all 17 records, 16 source image paths, 85 airport reports and exact archive request links. Checked reconciled 2010/2012/2014/2018/2021/2024 totals; preserved 2017/2022 disagreements; preserved 2016's untimed 13. Confirmed missing annual figures stay null, 2015/2025 estimates remain approximate, 2026 sum is 505, and uncertain source notes remain present.

Checked duration normalization, line breaks across gaps, cumulative interval-end timing, old/new backup import, CSV parsing/validation, mismatched year rejection, negative count rejection, and unsafe image-reference rejection.

## Browser interaction checks

Served from `/park-st-halloween/`, the same subpath used by the public site.

- All four navigation destinations and year selection work.
- Checked arrivals, running totals, temperature overlays, and numeric readouts. The last running totals are 341 / 331 / 505 for 2021 / 2024 / 2026.
- Inspected 2022's 286 written total beside the full 293 time-row sum and airport source links.
- Added temporary year 2199 with two intervals, saved, refreshed, and verified persistence.
- Downloaded backup, removed the temporary year, restored it through the import review, and refreshed to verify persistence again.
- Added a source-sheet image to the temporary year and verified its notebook attachment.
- Removed temporary year and picture; real archive remains 17 years.
- Bad backup with a negative total rejected without changes.
- CSV with two 20-minute intervals previews 8 counted visitors before import; canceled preview without changing records.
- Inspected phone form at 320px; it remains within the dialog without horizontal overflow.
- Inspected all views at requested viewport widths 320, 375, 430 and 1200. No persistent horizontal overflow. A transient 5px measurement during the 320px resize settled to exact client width; rechecked before proceeding.
- Inspected full desktop story, phone comparison and phone editor screenshots. The chart is touch selectable; the range slider provides an accessible time control.
- No browser console warnings/errors during these checks.

Native Safari automation did not respond, so engine-specific Safari and physical iPhone testing are **not verified**. The layout uses Safari-supported SVG, native form controls, safe-area padding, responsive typography and a standard HTML dialog. Browser viewport testing is not represented as physical device testing.

## Data limitations

`DATA_AUDIT.md` and each year's on-screen notes identify unresolved handwriting, incomplete time coverage, and cadence assumptions. The subsequently supplied 2026 original (IMG_8848.JPEG) was visually reviewed and linked. All 19 nonblank time rows match the retained counts and sum to 505; the blank 9:30 row is no longer represented as a measured zero. The published image was verified byte for byte against the supplied file. Weather is cached at the airport, not measured at the house. Device-local edits do not synchronize automatically or republish the shared archive.


## Three-edition update

- Confirmed the existing data/model checks still pass; the dataset, scans and airport files are unchanged by this update.
- Tested 72 combinations: three styles × four views × 320/375/1200px widths × dark system appearance/light visual fixture. Two narrow notebook-selector overflows were found and fixed; the affected cases were rechecked.
- Dark mode was tested against the actual system preference. Light mode used a local-only fixture that disables dark media rules and provides the matching light chart palette; no Mac settings were changed. These fixtures are not published.
- Verified the logo opens the three-style chooser, the chosen edition is highlighted, Escape closes it and focus returns to the logo.
- Verified changing styles preserves the comparison mode, chosen years, time slider and displayed 341/331/505 cumulative counts. Refresh preserves the chosen style and direct URLs select the requested edition.
- Verified the selected 2026 notebook year survives a style change, the original source image remains linked, and its edit form fits at 320px.
- Added a temporary year with 7 visitors in one edition, verified it in another, then removed it. The real notebook remains unchanged.
- Verified reduced-transparency/increased-contrast and reduced-motion fallbacks in a local visual fixture: header/nav backdrop blur is `none` and view animation is `none`.
- No browser console errors or warnings during the layout checks. Physical iPhone Safari remains unverified; glass effects use web CSS with explicit solid fallbacks.
