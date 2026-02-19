# arXiv Submission Guide
## Coherence Relativity I: Coherence Frames, Frame Invariance, and the Born Rule

**Recommended Timing:** Submit to arXiv on the same day as journal submission to Foundations of Physics

---

## arXiv Categories

**Primary Category:** `quant-ph` (Quantum Physics)

**Cross-list Categories (choose 1-2):**
- `gr-qc` (General Relativity and Quantum Cosmology) - for geometric framework
- `math-ph` (Mathematical Physics) - for information geometry aspects
- `physics.hist-ph` (History and Philosophy of Physics) - for foundational aspects

**Recommendation:** Primary: quant-ph, Cross-list: gr-qc

---

## Title and Abstract

**Title:** (exactly as in paper)
```
Coherence Relativity I: Coherence Frames, Frame Invariance, and the Born Rule
```

**Abstract:** (copy from LaTeX file, ~250 words)
- Use plain text (no LaTeX commands except basic math like $|c_i|^2$)
- Keep under 1920 characters (arXiv limit)
- Current abstract is suitable as-is

---

## Files to Upload

### Required Files:
1. **main.tex** - Primary LaTeX file
2. **mainNotes.bib** - Bibliography file (or .bbl if using compiled bibliography)
3. **All figure files:**
   - fig1_g_lambda.pdf
   - fig2_quasipotential.pdf
   - fig3_frame_transformation.pdf
   - fig4_born_rule_invariant.pdf
   - fig5_double_slit_frames.pdf
   - fig6_cr_vs_standard.pdf
   - fig7_experimental_setup.pdf
   - (fig1b_dlam_ds.pdf if used)

### Optional but Recommended:
4. **00README.txt** - Processing instructions for arXiv (see below)

### Do NOT Upload:
- main.pdf (arXiv will compile it)
- .aux, .log, .out files
- .DS_Store or other system files

---

## 00README.txt (Optional)

Create a file called `00README.txt` with compilation instructions:

```
This is the LaTeX source for "Coherence Relativity I: Coherence Frames, Frame Invariance, and the Born Rule"

Compilation:
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

Document class: revtex4-2 (Physical Review D style)

All figures are in PDF format and should be in the same directory as main.tex.

Contact: bryankaufman@mac.com
```

---

## Submission Steps

### 1. Create arXiv Account (if needed)
- Go to: https://arxiv.org
- Click "register"
- Verify email
- Request endorsement for quant-ph (if first submission)
  - Typically granted quickly for well-formatted physics papers

### 2. Prepare Submission Package

**Option A: Web Upload (Recommended for First Submission)**
- Package all files into a single .zip or .tar.gz
- Name it something clear: `coherence_relativity_paper1.zip`
- Include: main.tex, mainNotes.bib, all figure PDFs, 00README.txt

**Option B: Direct Upload**
- Upload each file individually through web interface

### 3. Submit via Web Interface

1. Go to: https://arxiv.org/submit
2. Click "Start New Submission"
3. Choose license:
   - **Recommended:** arXiv.org perpetual, non-exclusive license to distribute
   - **Alternative:** CC BY 4.0 (if you want explicit open access)
4. Select categories:
   - Primary: quant-ph
   - Cross-list: gr-qc
5. Upload files (ZIP or individual)
6. arXiv will compile automatically
7. Review compiled PDF
8. If errors, fix and re-upload
9. Fill in metadata:
   - Title (copy exactly from paper)
   - Authors: Bryan Kaufman
   - Abstract (plain text version)
   - Comments: "41 pages, 8 figures. Submitted to Foundations of Physics"
10. Submit

### 4. Announcement Schedule

arXiv has daily announcement cutoffs (Eastern Time):
- Submit before 14:00 ET (2 PM) → announces next day
- Submit after 14:00 ET → announces day after tomorrow

**Recommendation:** Submit early in day to get announced quickly

---

## After arXiv Posting

### 1. Note Your arXiv Identifier
Will be in format: `arXiv:YYMM.#####` (e.g., `arXiv:2602.12345`)

### 2. Update Journal Submission
Add arXiv number to:
- Cover letter notes
- Foundations of Physics submission system (if there's a field)

### 3. Share
- Add to your website/CV
- Share on Twitter/LinkedIn with arXiv link
- Email to colleagues interested in quantum foundations

### 4. Future Updates
If paper is revised after peer review:
- Submit updated version to arXiv
- Include note: "v2: Revised version accepted by Foundations of Physics"
- Add journal reference when published

---

## Common Issues and Solutions

### Issue: "TeX compilation errors"
**Solution:** 
- Test compile locally first with same command sequence
- Check all figure files are included
- Ensure .bib file is present
- Remove any local-path dependencies

### Issue: "File too large"
**Solution:**
- Compress figures (but keep quality ≥300 DPI)
- arXiv limit is 10MB total (you're well under at ~2-3MB)

### Issue: "Missing endorsement"
**Solution:**
- Request endorsement from someone who has published in quant-ph
- Alternatively, include your institutional affiliation (if applicable)
- For independent researchers: explain background in endorsement request

### Issue: "Figures not appearing"
**Solution:**
- Check \graphicspath command points to correct location
- Use relative paths, not absolute paths
- Ensure all figure files are in submission package

---

## Metadata for Reference

**Author:** Bryan Kaufman (Independent Researcher)  
**Email:** bryankaufman@mac.com  
**ORCID:** (register at https://orcid.org if you don't have one)

**Comments Field Suggestion:**
```
41 pages, 8 figures. Introduces coherence relativity, a geometric framework 
treating quantum measurement as frame transformation. Derives Born rule from 
frame invariance. Makes six testable predictions. Submitted to Foundations of Physics.
```

**MSC/PACS Codes:** (if requested)
- 03.65.Ta (Foundations of quantum mechanics)
- 03.67.-a (Quantum information)
- 04.60.-m (Quantum gravity - for geometric aspects)

---

## Timing Strategy

**Recommended:** Submit to arXiv the same day as journal submission

**Advantages:**
- Establishes priority
- Allows community feedback
- Increases visibility
- No embargo issues with Foundations of Physics (they allow arXiv preprints)

**Alternative:** Wait for journal acceptance
- More conservative
- Ensures peer-reviewed version is first public version
- Less common in theoretical physics

**My Recommendation:** Submit to arXiv immediately. Physics community expects this, and Foundations of Physics has no objection.

---

## After Acceptance

Once paper is accepted by Foundations of Physics:

1. Update arXiv with revised version (if changes were made)
2. Add journal reference in arXiv metadata:
   ```
   Published in Foundations of Physics, Vol. XX, No. Y (2026)
   DOI: [will be provided by journal]
   ```
3. arXiv will automatically add journal reference banner

---

**You're ready!** The paper is strong, figures are publication-quality, and submission materials are prepared. Good luck with both submissions!
