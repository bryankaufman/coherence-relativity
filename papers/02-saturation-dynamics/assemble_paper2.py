#!/usr/bin/env python3
"""
Paper 2 Assembly Script
Concatenates all section drafts/patched files into one working manuscript.
Run from: /Users/bryankaufman/Library/CloudStorage/Dropbox/Mac/Documents/coherence-relativity/
Usage: python3 papers/02-saturation-dynamics/assemble_paper2.py
"""

import os

BASE = "/Users/bryankaufman/Library/CloudStorage/Dropbox/Mac/Documents/coherence-relativity/papers/02-saturation-dynamics"

SECTIONS = [
    ("§1 Introduction",
     "sections/drafts/paper2_section_1_introduction_MERGED.md"),
    ("§2.1 T_MΣ Derivation",
     "sections/patched/paper2_section_2.1_T_MSigma_PATCHED.md"),
    ("§2.2 δλ Formalism",
     "sections/drafts/paper2_section_2.2_delta_lambda_DRAFT.md"),
    ("§2.3 Pilot Wave Connection",
     "sections/drafts/paper2_section_2.3_pilot_wave_DRAFT.md"),
    ("§2.3 Pilot Wave Completion (§2.3.8-2.3.9 + Appendix C.6)",
     "sections/drafts/paper2_section_2.3_pilot_wave_COMPLETION.md"),
    ("§2.4 Mixed-State Born Rule",
     "sections/patched/paper2_section_2.4_mixed_state_born_PATCHED.md"),
    ("§2.5 Left-Right Generator Decomposition",
     "sections/drafts/paper2_section_2.5_left_right_generators_DRAFT.md"),
    ("§2.6 Markov Transition Criterion",
     "sections/drafts/paper2_section_2.3_markov_transition_DRAFT.md"),
    ("§3.1 Century of Assumed Topology",
     "sections/patched/paper2_section_3.1_historical_PATCHED.md"),
    ("§3.2 Topology as Output",
     "sections/patched/paper2_section_3.2_topology_as_output_PATCHED.md"),
    ("§3.3 What Derived Compactification Constrains",
     "sections/drafts/paper2_section_3.3_constraints_DRAFT.md"),
    ("§4 KK-Cone Model",
     "sections/patched/paper2_section_4.0_KK_Cone_model_PATCHED.md"),
    ("§4.4 C1 Regularity",
     "sections/patched/paper2_section_4.4_C1_regularity_PATCHED.md"),
    ("§5 Holographic Conjecture Abstract Layer",
     "sections/drafts/paper2_section_5_holographic_conjecture_DRAFT.md"),
    ("§5.1-5.2 SC1 and SC2",
     "sections/drafts/paper2_section_5.1_5.2_SC1_SC2_DRAFT.md"),
    ("§5.3 SC3 Casimir Cosmological Constant",
     "sections/drafts/paper2_section_5.3_SC3_Casimir_DRAFT.md"),
    ("§6 Geometric Dark Matter",
     "sections/patched/paper2_section_6_geometric_dark_matter_PATCHED.md"),
    ("§7 Equations of Motion on MxSigma",
     "sections/drafts/paper2_section_7.0_EoM_MxSigma_DRAFT.md"),
    ("§8 Holographic Conjecture KK-Cone",
     "sections/drafts/paper2_section_8.0_holographic_conjecture_DRAFT.md"),
    ("§9 Discussion",
     "sections/drafts/paper2_section_6_discussion_MERGED.md"),
    ("§10 Open Problems",
     "sections/drafts/paper2_section_7_open_problems_MERGED.md"),
    ("Appendix A Block Inverse",
     "sections/patched/paper2_appendix_A_block_inverse_PATCHED.md"),
    ("Appendix B Geff KK Tower",
     "sections/patched/paper2_appendix_B_Geff_KK_tower_PATCHED.md"),
]

output_lines = []
output_lines.append("# Coherence Relativity II — Working Draft (Assembled 2026-03-23)\n\n")
output_lines.append("*Assembled from individual section drafts per ASSEMBLY_MANIFEST_2026-03-23.md*\n")
output_lines.append("*Status: Working manuscript — NOT submission-ready. See manifest for per-section statuses.*\n\n")
output_lines.append("---\n\n")

found = 0
missing = []

for label, relpath in SECTIONS:
    fullpath = os.path.join(BASE, relpath)
    output_lines.append(f"\n\n---\n\n<!-- ===== SECTION: {label} ===== -->\n")
    output_lines.append(f"<!-- Source: {relpath} -->\n\n")
    if os.path.exists(fullpath):
        with open(fullpath, encoding="utf-8") as f:
            content = f.read()
        output_lines.append(content)
        found += 1
        print(f"OK  {label}")
    else:
        output_lines.append(f"> **[SECTION NOT FOUND: {relpath}]**\n")
        missing.append(label)
        print(f"MISSING  {label}")

out_path = os.path.join(BASE, "paper2_ASSEMBLED_2026-03-23.md")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("".join(output_lines))

print(f"\nAssembled {found}/{len(SECTIONS)} sections")
if missing:
    print(f"Missing sections:")
    for m in missing:
        print(f"  - {m}")
print(f"Output: {out_path}")
print(f"Size: {os.path.getsize(out_path):,} bytes")
