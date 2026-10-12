"""Read-only CV content reconciliation. Run from the workspace root."""
from pathlib import Path
from zipfile import ZipFile
import difflib
import hashlib
import re
import sys
import xml.etree.ElementTree as ET
from pypdf import PdfReader

sys.stdout.reconfigure(encoding="utf-8")
root = Path(__file__).resolve().parent.parent
files = sorted(p for p in root.iterdir() if p.suffix.lower() in {".pdf", ".docx"})

def extract(path):
    if path.suffix.lower() == ".pdf":
        return "\n".join(page.extract_text() or "" for page in PdfReader(path).pages)
    with ZipFile(path) as doc:
        tree = ET.fromstring(doc.read("word/document.xml"))
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    return "\n".join("".join(p.itertext()) for p in tree.findall(".//w:p", ns))

contents = {p.name: extract(p) for p in files}
baseline = "Abdellah_Bouhaddi_Backend_Developer_CV_v14.pdf"
words = lambda s: re.findall(r"\S+", s)
reference = words(contents[baseline])
print(f"ROOT FILES: {len(files)}; PDFs: {sum(p.suffix == '.pdf' for p in files)}; DOCX: {sum(p.suffix == '.docx' for p in files)}")
for path in files:
    print(path.name, "characters:", len(contents[path.name]), "sha256:", hashlib.sha256(path.read_bytes()).hexdigest())
print("\nLATEST PDF FULL TEXT\n", contents[baseline])
seen = set()
for name, content in contents.items():
    if name == baseline:
        continue
    candidate = words(content)
    changes = []
    for tag, i, j, k, l in difflib.SequenceMatcher(None, reference, candidate, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        old, new = " ".join(reference[i:j]), " ".join(candidate[k:l])
        key = (old, new)
        if key in seen:
            continue
        seen.add(key)
        changes.append(f"LATEST: {old}\nTHIS VERSION: {new}")
    print(f"\n{name}: previously unseen text differences from latest\n" + ("\n".join(changes) or "None beyond differences already printed."))
copy = root / "portfolio/assets/Abdellah_Bouhaddi_CV.pdf"
print("\nPORTFOLIO PDF MATCHES V14:", copy.read_bytes() == (root / baseline).read_bytes())
