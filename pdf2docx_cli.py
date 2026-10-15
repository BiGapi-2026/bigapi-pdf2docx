# SPDX-License-Identifier: AGPL-3.0-or-later
# PDF zu Word für bigapi-engine. Ruft pdf2docx (MIT) und damit PyMuPDF (AGPL-3.0) unverändert auf.
# Dieses kleine Programm wird von der Engine als eigener Prozess gestartet und steht unter AGPL,
# weil es PyMuPDF einbindet. Quelltext: dieses Skript, unverändert pdf2docx und PyMuPDF von PyPI.
# Aufruf: python3 pdf2docx_cli.py eingabe.pdf ausgabe.docx [erste_seite] [letzte_seite]
import json, sys, logging
logging.disable(logging.CRITICAL)
from pdf2docx import Converter

def main():
    src, dst = sys.argv[1], sys.argv[2]
    first = int(sys.argv[3]) - 1 if len(sys.argv) > 3 else 0
    last = int(sys.argv[4]) if len(sys.argv) > 4 else None
    cv = Converter(src)
    try:
        cv.convert(dst, start=first, end=last, multi_processing=False)
        pages = len(cv.fitz_doc)
    finally:
        cv.close()
    print(json.dumps({"ok": True, "pages_total": pages}))

if __name__ == "__main__":
    main()
