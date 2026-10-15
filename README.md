# bigapi-pdf2docx

The small program behind **PDF to Word** on [bigapi.dev](https://bigapi.dev) (`/v1/pdf/to-docx`) and [gatefrog.com](https://gatefrog.com/pdf-zu-word/).

It converts a PDF into an editable Word document using [pdf2docx](https://github.com/ArtifexSoftware/pdf2docx) (MIT) and [PyMuPDF](https://github.com/pymupdf/PyMuPDF) (AGPL-3.0). Because it uses PyMuPDF, this program is licensed under the **GNU Affero General Public License v3.0 or later** (see `LICENSE`).

## How it runs

The BiGapi engine starts `pdf2docx_cli.py` as a separate process for each request and only exchanges files with it:

```
python3 pdf2docx_cli.py input.pdf output.docx [first_page] [last_page]
```

It prints one line of JSON, for example `{"ok": true, "pages_total": 3}`.

pdf2docx and PyMuPDF are installed unmodified from PyPI in the versions listed in `requirements.txt`:

```
pip install -r requirements.txt
```

This repository is the complete corresponding source of the program as it runs in production. The version in use is the latest commit on `main`.

## Contact

Artoption GmbH, Hamburg, Germany. Questions about this source code: via the contact details on [bigapi.dev](https://bigapi.dev).

---

## Kurz auf Deutsch

Dieses kleine Programm steckt hinter **PDF zu Word** bei bigapi.dev und gatefrog.com. Es nutzt pdf2docx und PyMuPDF unverändert von PyPI. Weil PyMuPDF unter AGPL steht, steht auch dieses Programm unter der **GNU AGPL v3.0 oder später**. Dieses Repository ist der vollständige Quelltext, so wie er im Betrieb läuft.
