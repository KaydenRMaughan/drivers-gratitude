"""Bundle Drivers.src.html + D3 + Fraunces font into one offline HTML file.

Usage:  python build.py  [path/to/d3.min.js]  [path/to/fraunces.woff2]
Output: ../Drivers.html
"""
import base64, pathlib, sys

here = pathlib.Path(__file__).parent
d3_path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else here / "vendor" / "d3.v7.9.0.min.js")
font_path = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else here / "vendor" / "fraunces-latin-600-normal.woff2")

src = (here / "Drivers.src.html").read_text(encoding="utf-8")
d3 = d3_path.read_text(encoding="utf-8")
assert "</script" not in d3.lower(), "d3 bundle contains a closing script tag"
font = base64.b64encode(font_path.read_bytes()).decode()
face = ("/* Fraunces 600 (SIL Open Font License 1.1), embedded for offline use */\n"
        "@font-face{font-family:'Fraunces';font-style:normal;font-weight:600;font-display:swap;"
        f"src:url(data:font/woff2;base64,{font}) format('woff2')}}")

out = src.replace("/*__D3__*/", "/* D3 v7.9.0 | (c) Mike Bostock | ISC license | https://d3js.org */\n" + d3, 1)
out = out.replace("/*__FONT__*/", face, 1)
dest = here.parent / "Drivers.html"
dest.write_text(out, encoding="utf-8")
print(f"wrote {dest} ({dest.stat().st_size/1024:.0f} KB)")
