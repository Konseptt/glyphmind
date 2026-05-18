# GLYPHMIND — Fully offline / zero setup

**No internet at runtime**, **no npm**, **no Python**, **no build step.** Copy this entire folder (USB, lab machine, air‑gapped PC), keep relative paths, and open **`index.html`** in a modern browser.

What ships locally:

- **`lib/`** — Three.js + SheetJS (already bundled).
- **`fonts/`** — Cinzel, Cinzel Decorative, Noto Egyptian Hieroglyphs (required so glyphs render; see **`fonts/FONT_NOTICE.txt`**).

Do **not** move **`index.html`** without **`lib/`** and **`fonts/`** beside it (paths are relative).

## Folder layout

```
├── index.html           ← double‑click this
├── lib/
│   ├── three.min.js     ← Three.js r128
│   └── xlsx.full.min.js ← SheetJS (Excel export)
└── fonts/
    ├── FONT_NOTICE.txt
    ├── NotoSansEgyptianHieroglyphs-Regular.woff2
    ├── Cinzel-*.woff2
    └── CinzelDecorative-*.woff2
```

## Browser

Use a current **Chrome**, **Firefox**, **Safari**, or **Edge**. Internet Explorer / Edge Legacy will not work.

## Running

1. **Primary:** **Double‑click `index.html`** (opens as `file://…`). That is enough for typical lab machines.
2. **Fallback:** If a browser blocks scripts or fonts from disk (rare), serve the folder once locally — still **no internet**:

   ```bash
   cd "/path/to/glyph-mind-offline"
   python3 -m http.server 8080
   ```

   Then open `http://localhost:8080`.

## Per-participant workflow

1. Enter **Participant ID** on the title screen (required). Optionally **Session ID**, **Condition**, **Phase**, and **N-back** mode.
2. Run the task (intro cutscene and tutorial can be skipped).
3. After each block, **Export Data** saves trial rows, or use **`SAVE & NEXT PARTICIPANT`** (pause or results): exports **`.xlsx`**, clears IDs and trial buffer, returns to title.

## Multiple blocks, one participant

1. Complete a block (70 scored trials after **N** warm-up paintings).
2. On the results screen, under **NEXT BLOCK (same IDs)**, choose **1-BACK** / **3-BACK** / **CUSTOM**, then **RUN NEXT BLOCK**.
3. **`block`** increments in the spreadsheet; **PID / Session / Condition / Phase** stay the same until you **SAVE & NEXT PARTICIPANT**.
4. Export when finished so **one `.xlsx`** can contain several blocks.

Example filename when both N=1 and N=3 were run:

`glyphmind_P001_tDCS_pre_n1+3_2026-05-05.xlsx`

## Workbook structure

Two sheets:

| Sheet | Contents |
|-------|-----------|
| **Trials** | Long-format trial rows (header row frozen). |
| **Meta** | Keys such as `exportedAt`, `sessionStartISO`, design counts (`scoredTrialsPerBlock_design`, `matchTargetsPerBlock_design`), row counts, RSI notes. |

### Rows per block

Each block adds **N** **warm-up** rows (`trialType = warmup`) plus **70** **scored** rows (`trialType = scored`). Example: **3-back** → **73** rows per block; **1-back** → **71**.

### Trials sheet columns (order)

`PID`, `Session`, `Condition`, `Phase`, `sessionStartISO`, `exportedAt`, `block`, `N`, `trialType`, `painting`, `warmupIndex`, `trial`, `tc`, `CRESP`, `Resp`, `ACC`, `RT`, `RSI`, `rsiAnchor`, `TriggerCondition`, `TriggerResponse`, `Stimulus`, `StimulusName`, `StimulusUnicode`, `Target`, `TargetName`, `TargetUnicode`

- **`trial`**: blank on warm-up; **1–70** on scored rows.  
- **`tc` / `CRESP`**: target coding for analysis (see Meta **`RSI_ms_meaning`** for RSI interpretation).  
- **`RSI`**: milliseconds from **`rsiAnchor`** to this stimulus onset on **every** row (warm-up = onset-to-onset; scored trial 1 = after last warm-up onset; scored trials 2–70 = after prior response). Use **`rsiAnchor`** when analyzing.

### Quick Excel checks

- Accuracy by **N**: pivot **N** × average **ACC** (filter **`trialType = scored`**).  
- RT (correct only): same, filter **ACC = 1**, average **RT**.  
- Hits / false alarms: filter **`trialType = scored`**; cross-tab **tc** × **Resp**.

## Data-loss safeguards

The app warns when leaving or restarting if there are **unexported** trials (confirm to discard). Prefer **Export Data** or **SAVE & NEXT PARTICIPANT** before starting a new participant or closing the tab.

## Downloads folder

Point the browser’s default download location at your study folder (Chrome: Settings → Downloads).

## Smoke test before real data

1. Open the page; title glyphs should render (not empty boxes).  
2. **PID = TEST**, run a short session, **Export Data** or **SAVE & NEXT PARTICIPANT**.  
3. Open the `.xlsx`: confirm **Trials** + **Meta**, warm-up + scored rows, and columns above.

If any step fails, fix paths or browser before collecting data.
