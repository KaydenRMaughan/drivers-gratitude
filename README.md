# Drivers: A Reflection on Gratitude

A short scrollytelling piece in the style of a newspaper graphics article. It has **one D3 graphic that changes state** as the story moves through 13 beats. Three evidence charts are drawn over the map (the George Bailey effect, gratitude and well-being, and gratitude and hope); the headwinds/tailwinds finding is drawn on the map itself. Text sits on the left and the graphic stays fixed on the right. You can present it live or send it to read afterward.

**The story:** in our work we're skeptical of single-driver explanations. But when we explain our own lives, we narrow the lens to what we have done, and we account for headwinds and tailwinds unevenly. Gratitude is acknowledging the different aspects of our lives, attributing them honestly, and appreciating what they mean to us. Just as hope is more than optimism, gratitude is more than positive thinking: it helps build the stabilizing and mobilizing hope Caleb described.

## Files

| File | What it is |
|---|---|
| `Drivers.html` | **The deliverable.** One self-contained file (~385 KB) with D3 and the heading font embedded. Works offline. |
| `Drivers-script.md` | Speaker script, beat by beat, plus how the graphic carries each beat. |
| `Drivers-v2.html` | An earlier, more interactive version, kept for reference. |
| `source/` | Editable source, `build.py` and the vendor files (D3 v7.9.0 under the ISC license, Fraunces under the SIL OFL). |

## Present it on Teams or Zoom

1. Open `Drivers.html` in Edge or Chrome and press **P** for presenter mode. The toolbar hides itself; move the mouse to bring it back.
2. Press **N** for **speaker notes in a separate window**, with the script, the next beat and a timer. Allow pop-ups if the browser asks.
3. Share the **browser window** in Teams. Press **F** for full screen if you like.
4. Advance with **→**, **PageDown**, **Space** or a clicker. Each beat's animation takes about 1–3 seconds, so let it finish before you speak over it.

**Timing:** about 720 spoken words, roughly 6 minutes. Four acts: the habit (1–2), the narrow lens (3–4), gratitude (5–10: acknowledge, attribute, appreciate), and hope (11–13). Beats 2 and 9 animate in two phases (the second starts about 6 seconds in; in beat 9 it is the George Bailey effect chart), so speak through the first before advancing.

## Share it afterward

Send the file. Opened normally, it reads as a scrolling article. **R** gives a read/print version, and **Ctrl+P** prints it. The page has no tracking and cannot make network requests.

## Change the content

Everything is in the `window.CONTENT = { ... }` block near the top of `Drivers.html`. You can edit it in any text editor without rebuilding.

| To change… | Edit |
|---|---|
| On-screen line / reading text / script for a beat | `steps[n].headline` / `.body` / `.notes` |
| The drivers of a life (labels, kinds) | `drivers`. Add, remove or reword freely; the layout adapts. Kind `self` sits inside the narrow lens |
| Kinds and their colors | `kinds` (color shows kind only, never strength) |
| Work outcomes in beat 1 | `outcomeLabels` |
| Center labels | `lifeCenter`, `lifeCenterClear` |
| Evidence charts (titles, numbers, captions) | `charts` (`removal`, `effects`, `hope`) |
| Interaction arcs (beat 7, illustrative) | `interactions` (pairs of driver ids; `label` shows on the arc) |
| Headwinds labels (beat 4) | `winds` |
| Imagine-it-absent driver and notes (beat 9) | `absent` |
| Hope path labels and the drivers that feed it (beat 11) | `hopeMap` |
| Which drivers are lit in the narrow lens | `headwind: true` on a driver (plus everything of kind `self`) |
| Sources and notes | `sources`, `about` |

If you'd rather edit `source/Drivers.src.html`, run `python build.py` in `source/` to regenerate `Drivers.html`.

## Guardrails built in
- The map is labeled illustrative. Position, size and line width carry no meaning. Beat 8 makes this part of the story: the lines dissolve.
- Hard drivers (a hard year, a mistake, a setback) appear alongside the good ones, so gratitude is never shown as spin.
- Research is used only where it carries the argument: why tailwinds fade (Davidai & Gilovich), how to notice them (Koo et al.), what gratitude practices do, modestly (Kirca et al., with Davis et al. noted), and the link to hope (Witvliet et al.). Numbers are shown as reported. Counter-evidence the piece was designed around is listed at the end of `Drivers-script.md`.
- Gratitude is never directed at the organization or leadership, and every invitation is optional.
- Keyboard navigation, screen-reader descriptions for each beat, and `prefers-reduced-motion` support.
