# MOC — HCR Agent Session Logs
*Index of all agent session logs in `memory/kb/`. The Dataview block auto-updates when the Dataview plugin is installed. The static index below is manually maintained.*

---

## Auto-Index (requires Dataview plugin)
```dataview
TABLE file.mtime as "Last Modified", file.size as "Size"
FROM "memory/kb"
WHERE file.name != "INDEX"
SORT file.mtime DESC
LIMIT 30
```

---

## Session Log Index (static, see also [[memory/kb/INDEX]])

### 2026-04 (most recent)
- [[memory/kb/SESSION_2026-04-26_SYNTHESIS_AND_SPINE]] — synthesis and spine
- [[memory/kb/SESSION_2026-04-26_REVISED_STATUS_ASSESSMENT]] — revised P2A status
- [[memory/kb/PAPER1_V6_CONFLICT_AUDIT_2026-04-26]] — P1 v6 conflict audit
- [[memory/kb/SESSION_2026-04-20_SCF_FIXED_POINT_SUBSTITUTION]] — SCF fixed point
- [[memory/kb/SESSION_2026-04-19_T_MSigma_HOLOGRAPHIC_BORN_RULE]] — T_MΣ holographic Born rule
- [[memory/kb/SESSION_2026-04-19_YTV_UNENTANGLED_BELL_CONTEXTUALITY]] — YTV / unentangled Bell
- [[memory/kb/SESSION_2026-04-19_COV_CHECK_CANDIDATE_SCF]] — covariance check SCF candidate
- [[memory/kb/SESSION_2026-04-14_ORTHOVERSE_SINGULARITY_DARK_MATTER]] — orthoverse / dark matter
- [[memory/kb/SESSION_2026-04-14_T25B_CMB_BOUNDARY]] — T25B CMB boundary
- [[memory/kb/SESSION_2026-04-13_CONSCIOUSNESS_INFORMATION_HARD_PROBLEM]] — consciousness / hard problem
- [[memory/kb/SESSION_LOG_2026-04-13]]
- [[memory/kb/SESSION_2026-04-10_GEOMETRIC_LAMBDA_ANALYSIS]] — geometric lambda analysis
- [[memory/kb/SESSION_LOG_2026-04-12]]
- [[memory/kb/HANDOFF_TO_CLAUDE_2026-04-13]] — handoff document
- [[memory/kb/CONCEPT_MAP_2026-04-11]] — concept map (key reference)

### 2026-03
- [[memory/kb/SESSION_2026-03-19_REFEREE_REVISION]] — EGY reparameterization, 10 fixes

### 2026-02
- [[memory/kb/SESSION_2026-02-14_PUBLICATION]] — OSF publication milestone
- [[memory/kb/SESSION_2026-02-12_ESTIMATE_AUDIT]] — R_Σ=8, s*=0.72, geodesic cutoff
- [[memory/kb/SESSION_2026-02-07_FIGURE_AUDIT]] — U-shape metric, ChatGPT edits

### 2026-01–early 2026-02
- See [[memory/kb/INDEX]] for full list

---

## Usage Notes
- New sessions: name as `SESSION_YYYY-MM-DD_TOPIC.md`
- Append entry to [[memory/kb/INDEX]] after each session
- Templates: [[_vault/templates/session-log]]
