# Wall Art Splitter

A browser tool for splitting flat 3D-printed wall art and logos into pieces that fit your printer bed.

Load an STL (exported from Tinkercad or anywhere else), or drop in a logo picture and the tool traces it into a model for you. It lays the design flat, quotes the filament, works out the fewest pieces it needs, and gives you a zip of print-ready STLs.

## What it does

- **Picture to model.** Drop a PNG, JPG or WebP logo. The tool finds the background (transparent, or the picture's most common colour), traces everything else with smooth edges, and builds a model at the width and thickness you set. Shapes touching the picture's edge, like screenshot frames, are left out. It warns about lines thinner than 2 mm and tiny loose bits. **Download full STL** gives you the whole model.
- **Filament and price.** Every design shows an estimated filament weight and length, worked out from its volume and outline. The formula is tuned to Orca totals from three past jobs and matches them within about 1%. Price buttons show grams × 0.5, × 1 and × 2. To retune it for different slicer settings, change `G_VOL` and `G_WALL` near the top of the script.
- **Cuts only where needed.** Oversized parts are cut one piece at a time at their thinnest joins (often where script letters connect), and the tool also tries the best grid with neighbouring pieces merged back together. It keeps whichever plan gives fewer pieces and cuts less of the art. A plain grid mode is still there.
- **Keeps loose parts whole.** Separate letters, words and shapes that fit the bed are left uncut. Only parts too big for the bed get split.
- **Seams follow the design.** Cuts run through gaps in the art and cross solid lines at their narrowest point. You can switch to straight seams.
- **Puzzle tabs.** Knob-and-socket joints go wherever a seam crosses art solid enough to hold one, with an adjustable fit gap.
- **No stray bits.** A small tip that a cut would leave on its own stays with the piece it is attached to.
- **Fits at an angle.** Each piece is checked against your bed at any rotation. Pieces that need an angle are exported already turned.
- **Named pieces.** Cut pieces are named A1, B2… (rows from the top, columns from the left). Whole parts are P1, P2… in reading order. The zip includes `layout.txt` and `layout.png`.

## Using it

Open the GitHub Pages link for this repo, drop an STL onto the page, check the preview, then click **Split into pieces** and **Download pieces (.zip)**.

Everything runs in your browser. Your files are never uploaded anywhere.

Tips:
- Set **Largest square you print on** a little under your real bed size (default 11.75 in for a 12 × 12 in bed).
- In Orca Slicer, turn off auto-rotate in the Arrange settings so angled pieces keep their angle.
- The STL must be watertight. If the tool reports holes, run Orca's **Fix model** on it and export again.

## Running it yourself

The page needs `index.html` and `manifold.wasm` in the same folder, served by a web server. Opening `index.html` straight from disk will not load the cutting engine. To try it locally:

```
python -m http.server 8000
```

Then open http://localhost:8000.

## Editing

`splitter/index.html` is the source. It is written for Claude's artifact viewer, which adds the `<html>` and `<head>` wrapper itself. After changing it, rebuild the GitHub Pages page with:

```
python tools/make-standalone.py
```

## Credits

- Geometry engine: [Manifold](https://github.com/elalish/manifold) (`manifold-3d` 3.3.2), Apache License 2.0. `manifold.wasm` is redistributed unmodified; see `licenses/manifold-3d-LICENSE.txt`.
- Zip export: [JSZip](https://stuk.github.io/jszip/) 3.10.1, loaded from cdnjs.
- Fonts: Barlow, Barlow Semi Condensed and JetBrains Mono from Google Fonts.
