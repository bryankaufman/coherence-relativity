# Zenodo v4 Upload Checklist
Use this checklist for the Paper 1 Zenodo v4 release.

## Before upload
- [ ] `main.tex` identifies the manuscript as v4
- [ ] `main.pdf` has been rebuilt from the current sources
- [ ] `releases/v4/main_v4.pdf` exists and matches the rebuilt `main.pdf`
- [ ] `releases/v4/coherence-relativity-paper1-v4-source.zip` exists
- [ ] `releases/v4/RELEASE_MANIFEST.md` is current
- [ ] manuscript references use the Zenodo concept DOI where a stable DOI is needed

## Zenodo action
- [ ] create a new version from the existing Zenodo record
- [ ] upload `main_v4.pdf`
- [ ] upload the matching source bundle
- [ ] publish the new version

## After Zenodo assigns the DOI
- [ ] record the new version DOI in `releases/v4/RELEASE_MANIFEST.md`
- [ ] record the new Zenodo record URL in `releases/v4/RELEASE_MANIFEST.md`
- [ ] refresh any version-specific references that should point to the newly minted v4 DOI
