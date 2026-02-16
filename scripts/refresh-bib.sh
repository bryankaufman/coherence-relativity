#!/bin/bash
# Refresh master.bib from Zotero Better BibTeX
# Collection: Coherence-relativity (DZX5AAD3)
#
# Usage: ./scripts/refresh-bib.sh
#
# For persistent auto-export, configure in Zotero GUI:
#   Zotero > Preferences > Better BibTeX > Automatic Export
#   Collection: Coherence-relativity
#   Format: Better BibTeX
#   Path: ~/Library/CloudStorage/Dropbox/Mac/Documents/coherence-relativity/bibliography/master.bib

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
TARGET="$PROJECT_DIR/bibliography/master.bib"
BBT_URL="http://localhost:23119/better-bibtex/export/collection?/DZX5AAD3.bibtex"

# Check Zotero is running
if ! curl -s --max-time 2 "http://localhost:23119/better-bibtex/cayw?probe=true" >/dev/null 2>&1; then
    echo "ERROR: Zotero/BBT not running on port 23119"
    exit 1
fi

# Export and filter junk entries
curl -s --max-time 15 "$BBT_URL" > "$TARGET.raw"

python3 -c "
import re, sys
with open('$TARGET.raw') as f:
    content = f.read()
entries = re.split(r'\n(?=@)', content)
clean = [e.strip() for e in entries if e.strip() and 'zotero-item' not in e]
with open('$TARGET.tmp', 'w') as f:
    f.write('\n\n'.join(clean) + '\n')
print(len(clean))
" > /tmp/bib_count.txt 2>/dev/null

ENTRIES=$(cat /tmp/bib_count.txt)
rm -f "$TARGET.raw" /tmp/bib_count.txt

if [ "$ENTRIES" -eq 0 ]; then
    echo "ERROR: Export returned 0 entries"
    rm -f "$TARGET.tmp"
    exit 1
fi

mv "$TARGET.tmp" "$TARGET"
echo "Exported $ENTRIES entries to bibliography/master.bib"
