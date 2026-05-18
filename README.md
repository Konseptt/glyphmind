# GLYPHMIND

**GLYPHMIND** is a browser-based **first-person corridor** task: a **spatial visual N-back** with **Egyptian hieroglyph** stimuli. It targets **working-memory / DLPFC-oriented research** (participant ID, condition, phase, trial-level export).

This build is **fully offline**: **`index.html`** plus **`lib/`** (Three.js, SheetJS) and **`fonts/`** (webfonts + hieroglyphs). **No internet**, **no npm**, **no install** — double‑click `index.html` or open it from disk. Optional local HTTP server only if `file://` is restricted on a locked‑down machine.

---

## Task (what the participant does)

1. **Walk** down a corridor. Wall paintings reveal **one hieroglyph** when you get close, **in order**.
2. **Warm-up:** The first **N** paintings are **observe only** (no match / no-match response).
3. **Scored trials:** **70** trials per block. Each time, decide whether the current glyph **matches the one from N paintings back**.
   - **Match:** **F**, **Space**, or **left click**
   - **No match:** **J** or **right click**
4. The sequence is generated so **30** of the 70 scored trials are **targets** (true N-back matches) and **40** are **non-targets**.

You can run **another block** at the same or different **N** from the end-of-block screen (**RUN NEXT BLOCK**) while keeping one continuous export session.

---

## Running locally

1. Copy the **whole project folder** so **`index.html`**, **`lib/`**, and **`fonts/`** stay together.
2. Open **`index.html`** (double‑click or drag into **Chrome**, **Firefox**, **Safari**, or **Edge**). Nothing needs to be downloaded at runtime.

If a lab policy blocks **`file://`** scripts or fonts, serve the folder locally (still offline):

```bash
python3 -m http.server 8080
# http://localhost:8080
```

Use **`README_OFFLINE.md`** for workstation setup, multi-block workflow, and export column details.

---

## Controls

| Action | Desktop |
|--------|---------|
| Move | **W A S D** / arrows; **Shift** sprint |
| Look | **Mouse** after pointer lock (click canvas or lock hint) |
| Match | **F**, **Space**, **left click** |
| No match | **J**, **right click** |
| Pause | **Esc** |

**Touch:** joystick, drag to look, on-screen **MATCH** / **NO MATCH**, pause button.

---

## Research fields and export

On the **title screen**, set **Participant ID** (required), **Session ID**, **Condition** (tDCS / Sham / Control), **Phase** (Pre / During / Post), and **N-back** (1, 3, or custom).

**Pause → Export Data** or the results screen downloads an **`.xlsx`** with:

- **`Trials`** — one row per warm-up or scored event; includes **`trialType`** (`warmup` | `scored`), **`trial`** (1–70 on scored rows only), accuracy, RT, RSI / **`rsiAnchor`**, stimulus and target IDs.
- **`Meta`** — session timestamps, design constants (70 scored trials, 30 targets), and short notes for analysts.

See **`README_OFFLINE.md`** for column list and participant workflow.

---

## Stimuli

**12** hieroglyphs from the Unicode Egyptian Hieroglyphs range; Gardiner-style IDs and names appear in exports. Local **`fonts/NotoSansEgyptianHieroglyphs-Regular.woff2`** is required for correct glyphs offline.

---

## Tech notes

- **Three.js** (r128) and **SheetJS** ship under **`lib/`**
- **Web Audio API** for UI / feedback
- **Pointer Lock** for desktop look (with fallbacks described in code)

---

## License

Add a **`LICENSE`** file if you distribute this build under explicit terms.
