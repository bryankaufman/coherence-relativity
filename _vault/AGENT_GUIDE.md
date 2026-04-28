# HCR Agent Guide — Authoritative Path Registry
*All agents (Warp, Claude, Perplexity) should read this file before working in the HCR repo.*
*This file is the single source of truth for where things live and where to put new things.*

---

## Project Identity
- **Full name**: HCR — Holographic Coherence Relativity
- **Short name**: HCR (formerly "CR"; do not use "CR" in new documents)
- **Canonical repo**: `~/Library/CloudStorage/Dropbox/Mac/Documents/coherence-relativity/`
- **GitHub remote**: `https://github.com/bryankaufman/coherence-relativity.git`
- **Preprint (P1)**: https://osf.io/preprints/metaarxiv/3g8ub_v1

---

## Before You Do Anything
```bash
REPO=~/Library/CloudStorage/Dropbox/Mac/Documents/coherence-relativity
cd "$REPO"
git --no-pager log --oneline -3   # Know current HEAD
git --no-pager status              # Confirm clean working tree
git pull origin main               # Sync if needed
```

---

## Where to Write — By Output Type

| Output Type | Write To | Notes |
|-------------|---------|-------|
| Session log | `memory/kb/SESSION_YYYY-MM-DD_TOPIC.md` | Use template: `_vault/templates/session-log.md` |
| Paper section draft | `papers/0X-PAPERNAME/sections/drafts/` | Use template: `_vault/templates/paper-section.md` |
| Derivation note | `notes/derivations/TOPIC.md` | Use template: `_vault/templates/derivation-note.md` |
| Figure (PDF/PNG) | `figures/` | Naming: `figN_description.pdf` + `.png` |
| Numerical data | `data/` or `analysis/` (JSON, CSV) | |
| Literature note | `literature/perplexity/` (Perplexity) or `literature/` | |
| Bibliography entry | `bibliography/master.bib` via Zotero | Run `scripts/refresh-bib.sh` |
| New analysis script | `code/` or `analysis/` | uv-managed venv |
| Inbox / unsorted | `_vault/inbox/` | For items awaiting classification |

---

## Where NOT to Write

| Location | Why Off-Limits |
|----------|---------------|
| `~/Desktop/coherence-relativity*/` | Non-canonical scratch; not git-tracked authoritatively |
| `~/Desktop/paper2_section_*.md` | Stale Desktop drafts; consolidate to `papers/02-saturation-dynamics/sections/` instead |
| `papers/01-coherence-frames/main.tex` | Paper 1 is PUBLISHED; do not edit without explicit instruction from Bryan |
| `_vault/*.md` (MOC files) | Human-curated navigation; agents do not write here |
| Any path outside canonical repo | All HCR work must go through the git repo |

---

## Paper Status (quick reference)

| ID | Folder | Status | Action |
|----|--------|--------|--------|
| P1 | `papers/01-coherence-frames/` | ✅ PUBLISHED | Read-only unless explicitly instructed |
| P2A | `papers/02-saturation-dynamics/` | 🔄 ACTIVE | Primary writing target |
| P2B | `papers/02-saturation-dynamics/` | 🔄 ACTIVE | Split from P2A |
| P2C | `papers/02C-holographic-structure/` | 🔄 ACTIVE | Holographic structure |
| P3 | `papers/03-gr-unification/` | 🔲 SCOPED | Scope only, no drafting yet |
| P4 | `papers/04-holography/` | 🔲 SCOPED | Scope only, no drafting yet |

---

## Key Files Every Agent Should Know

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Instructions for Claude agents |
| `WARP.md` | Instructions for Warp agent |
| `COORDINATION.md` | Society of Mind coordination log |
| `TASKS.md` | Project-wide task tracker |
| `VERSION_CONTROL_PROTOCOL.md` | **MANDATORY** git workflow rules |
| `notes/EQUATIONS_REFERENCE.md` | Master equation list with LaTeX labels |
| `bibliography/master.bib` | Single master bibliography |
| `memory/kb/INDEX.md` | Session log index |
| `_vault/00-HOME.md` | Vault home page |
| `context/HOW-I-WORK.md` | Author preferences and working style |
| `system/SYSTEM-RULES.md` | Operating rules for this workspace |

---

## Non-Canonical Locations (reference only)

These exist and may be browsed, but are NOT the source of truth:

| Location | Type | Notes |
|----------|------|-------|
| `~/Desktop/coherence-relativity/` | Old working copy | Stale |
| `~/Desktop/coherence-relativity-v3/` | Scratch | Stale |
| `~/Desktop/coherence-relativity-revised/` | Scratch | Has old paper2_outline.md |
| `~/Desktop/coherence-relativity-zenodo-v4/` | Zenodo v4 archive | Read-only reference |
| `~/Downloads/Coherence*.zip` | Archives | Extract only if needed |
| `~/Downloads/perplexity/` | Perplexity outputs | Move to `literature/perplexity/` |
| `~/.unified-mcp-manager/KB/RESEARCH_ARCHIVE_coherence-relativity-I.md` | Old KB entry | Points here now |

---

## Agent-Specific Notes

### Warp Agent
- Primary path: `~/Library/CloudStorage/Dropbox/Mac/Documents/coherence-relativity/`
- Read: `WARP.md` first, then this file
- Write session logs to: `memory/kb/SESSION_YYYY-MM-DD_TOPIC.md`
- Numerical work: `analysis/` and `code/`

### Claude Web / Claude Code
- Read: `CLAUDE.md` first, then this file
- Paper editing: explicit instruction required; never modify `papers/01-coherence-frames/main.tex` without being asked
- Draft sections: `papers/0X-*/sections/drafts/`
- Write session logs: `memory/kb/SESSION_YYYY-MM-DD_TOPIC.md`
- Content posted to conv-log → Warp applies to canonical repo

### Perplexity
- Research outputs: `literature/perplexity/TOPIC_YYYY-MM-DD.md`
- Bibliography additions: via Zotero (not directly to master.bib)
- Report findings in conv-log for other agents to consume

---

## Session Log Protocol
1. At session start: read `memory/kb/INDEX.md` to know recent context
2. During session: accumulate notes in working memory
3. At session end: write `memory/kb/SESSION_YYYY-MM-DD_TOPIC.md`
4. Append one-line entry to `memory/kb/INDEX.md`: `- YYYY-MM-DD — TOPIC — [brief summary]`
5. Commit: `git add memory/kb/ && git commit -m "session: TOPIC (YYYY-MM-DD)"`

---

## Obsidian MCP Integration (added 2026-04-28)

Two MCP servers are configured to give agents live read/write access to the vault through Obsidian:

### Server 1 — `obsidian-hcr` (cyanheads, stdio)
**Tool**: `obsidian-mcp-server` (installed globally via npm)
**Requires**: Obsidian running + Local REST API plugin enabled (port 27123)
**Use for**: File reads, writes, search, frontmatter, tags during Warp sessions

| Tool | Purpose |
|------|---------|
| `obsidian_read_note` | Read note content + metadata |
| `obsidian_update_note` | Append / prepend / overwrite note |
| `obsidian_global_search` | Vault-wide text/regex search |
| `obsidian_list_notes` | Directory tree listing |
| `obsidian_manage_frontmatter` | Get/set/delete YAML frontmatter |
| `obsidian_manage_tags` | Add/remove/list tags |
| `obsidian_search_replace` | In-note search-and-replace |
| `obsidian_delete_note` | Delete a note |

**Key env vars** (set in shell or Warp Drive env):
```bash
export OBSIDIAN_API_KEY=<from Local REST API plugin settings>
export OBSIDIAN_BASE_URL=http://127.0.0.1:27123
```

**Activate Local REST API**: open Obsidian → Settings → Community Plugins → Local REST API → copy API key.

### Server 2 — `obsidian-hcr-semantic` (aaronsb, HTTP)
**Plugin**: `semantic-vault-mcp` v0.11.16 (installed in `.obsidian/plugins/obsidian-mcp-plugin/`)
**Requires**: Plugin enabled in Obsidian; starts HTTP server on port 3001
**Use for**: Graph traversal, semantic search, backlinks, cross-paper concept navigation

| Tool Group | Purpose |
|------------|---------|
| `vault.*` | File operations + semantic search |
| `graph.*` | Link traversal, paths, backlinks, tag analysis |
| `edit.*` | Structure-aware content modification |
| `dataview.*` | DQL query execution (Dataview plugin required) |
| `workflow.*` | Contextual next-action hints |

**Setup** (one-time, in Obsidian GUI):
1. Open Obsidian → Settings → Community Plugins → enable "Semantic Notes Vault MCP"
2. Open plugin settings → copy the generated API key
3. Set in shell: `export OBSIDIAN_MCP_API_KEY=<key from plugin settings>`

**Connection test**:
```bash
curl -s -H "Authorization: Bearer $OBSIDIAN_MCP_API_KEY" http://localhost:3001/mcp
```

### Activation Checklist
- [ ] Obsidian is open with the HCR vault loaded
- [ ] Local REST API plugin enabled → `OBSIDIAN_API_KEY` set in env
- [ ] Semantic Notes Vault MCP plugin enabled → `OBSIDIAN_MCP_API_KEY` set in env
- [ ] Warp detects both servers (Settings → MCP → Detected from Warp)

---

## Build Commands
```bash
# Python environment
source .venv/bin/activate        # or: uv run python ...

# Regenerate figures
python3 code/calculate_g_lambda.py
python3 code/calculate_v_lambda.py
python3 code/generate_figures.py

# Build P1 PDF (from papers/01-coherence-frames/)
/Library/TeX/texbin/pdflatex main.tex && \
/Library/TeX/texbin/bibtex main && \
/Library/TeX/texbin/pdflatex main.tex && \
/Library/TeX/texbin/pdflatex main.tex

# Sync bibliography from Zotero
bash scripts/refresh-bib.sh
```
