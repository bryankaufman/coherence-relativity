You’re right to treat your workflow text as an outline, not a fixed spec. I’ll treat it as the *requirements skeleton* and layer in (a) a more engineered workflow, (b) a first-pass Component Purpose Index, and (c) candidate missing components.

---

## A. Engineered Radiology Workflow v0.2 (brainstorm draft)

Below is a tightened version of your closed-loop workflow, organized for concept‑mapping. Think of each phase as a “lane” where specific components plug in.

### 1. Order Intent, CDS, and Indication Capture

**Purpose:** Ensure the *right* study is ordered with sufficient clinical context.

- **Activities**
  - Referrer enters indication, urgency, constraints (renal function, pregnancy, allergies).
  - Clinical decision support (ACR AC, local rules) suggests modality + exam family.
  - System validates minimal clinical content (no “rule out headache” with no red flags, etc.).

- **Key artifacts**
  - Order + indication (structured where possible).
  - CDS log (appropriateness score, overrides).

- **Candidate owners in your stack**
  - `ai-imaging-platform`  
    - GraphRAG + ACR AC integration to suggest modality/protocol and capture rationale.
  - FHIR / CDS‑Hook MCP servers (FHIR MCP, healthcare MCP)  
    - To plug decisions into EHR/order entry in a standards‑based way.

**Potential gaps**
- No single “CDS Gateway” service clearly defined as the entry point between EHR ↔ AI imaging platform.
- No explicit representation of CDS override logging and analytics.

---

### 2. Scheduling, Protocol Selection, and Patient Prep

**Purpose:** Convert an approved order into an executable, safe imaging plan.

- **Activities**
  - RIS scheduling (time, modality, room, radiologist).
  - Protocoling team (or AI) maps order → standardized protocol (RadLex Playbook / local catalog).
  - Checks labs/allergies/devices; chooses contrast, sedation, etc.
  - Generates modality‑facing protocol instructions.

- **Artifacts**
  - Scheduled order + accession.
  - Chosen protocol ID + parameters.
  - Preparation instructions to staff/patient.

- **Candidate owners**
  - `ai-imaging-platform`  
    - Protocol recommendation engine; protocol catalog; RadLex / LOINC / SNOMED crosswalks.
  - DICOM ecosystem  
    - To eventually exercise Assisted Protocol Setting / SWF‑b.

**Gaps**
- No dedicated “Protocol Governance Service” that owns the protocol catalog, versions, approvals, and ties back to AC/standards.
- No explicit tech‑facing UI/workflow for protocoling (only implied via docs).

---

### 3. Prior Data Aggregation and Normalization

**Purpose:** Ensure all relevant priors and external content are ready before imaging and reading.

- **Activities**
  - Prefetch prior images/reports (local PACS, external HIE).
  - Normalize external studies (ID reconciliation, basic QC).
  - Aggregate clinical data (problem list, meds, labs) into a common view.

- **Candidate owners**
  - `dicom-ecosystem` + `dicom-rag-integration`  
    - DICOM imports, XDS‑I, SR flows, bridging into GraphRAG for knowledge extraction.
  - `ai-imaging-platform` terminology + GraphRAG layers  
    - To reason over prior imaging narratives and structured SR.

**Gaps**
- A clear “Clinical Context Aggregator” service that turns all this into a single structured bundle per order (e.g., FHIR Composition + pointers to DICOM).

---

### 4. Check-in, Modality Worklist, and Acquisition

**Purpose:** Acquire images safely and correctly with minimal data errors.

- **Activities**
  - Arrival & identity verification.
  - Modality Worklist provisioning; tech selects the correct scheduled step.
  - Protocol execution, dose logging, contrast tracking.
  - Tech notes on deviations, complications.

- **Candidate owners**
  - `dicom-ecosystem`
    - Orthanc/DCM4CHEE/DICOMcloud + Modality Worklist + DICOM networking.
  - SR tools under `dicom-ecosystem/sr-tools`
    - For dose reports, technical SRs, and later clinical SR.

**Gaps**
- Dose registry integration (e.g., sending to registries or ACR Dose Index).
- Structured technologist worksheet UX—it’s implied but not yet a distinct component.

---

### 5. Image Management, Worklists, and Triage

**Purpose:** Get the right studies to the right radiologist at the right time, with AI‑assisted triage.

- **Activities**
  - Image routing + archiving.
  - Worklist creation by subspecialty, site, urgency.
  - Optional AI triage (e.g., stroke, PE) to bump priority and add flags.

- **Candidate owners**
  - `dicom-ecosystem` + viewers (OHIF, Orthanc UI).
  - `dicom-mcp`, `dicom-rag-integration`, AI services
    - To run triage models and attach SR/flags.

**Gaps**
- A dedicated “AI Triage/Worklist Orchestrator” that:
  - Scores studies, updates priority, attaches structured alerts, and writes back to RIS/PACS.

---

### 6. Reading Workspace and Interpretation

**Purpose:** Provide a coherent environment for radiologists to interpret with full context.

- **Activities**
  - Side‑by‑side current + priors, key images, labs, clinical notes.
  - Measurements, structured templates (TI‑RADS, LI‑RADS, etc.).
  - Real‑time assistance: summarization, checklists, second‑look.

- **Candidate owners**
  - `dicom-ecosystem` viewers (OHIF) as image core.
  - `radiology-assistant-desktop`
    - For PHI‑safe LLM assistance, template prompting, TI‑RADS, etc.
  - Potential MCP layer integrating the desktop with DICOM SR + FHIR.

**Gaps**
- A unified “Reading Workspace Orchestrator” concept that ties viewer, AI assistant, and SR generation together in one logical app.
- Formalized DICOM SR templates for each reporting standard, wired into this workspace.

---

### 7. Report Creation, Finalization, and Distribution

**Purpose:** Produce structured, standards‑compliant reports that flow cleanly into EHR and downstream systems.

- **Activities**
  - Draft generation (speech recognition + AI; structured templates).
  - DICOM SR generation, mapping to FHIR and/or CDA where needed.
  - Sign‑off, locking, distribution; critical results pathways.

- **Candidate owners**
  - `radiology-assistant-desktop`
    - Narrative generation; priority classification; PHI handling.
  - DICOM SR tools in `dicom-ecosystem` and `ai-imaging-platform` tech‑protocol modules
    - SR creation, validation, and upload to PACS.
  - FHIR MCP / reporting MCP
    - To translate SR + narrative into FHIR DiagnosticReport, Observations, etc.

**Gaps**
- A production‑grade “Report Orchestration Service” that:
  - Accepts findings (structured + free text).
  - Ensures DICOM SR + FHIR + billing codes are all consistent.
  - Manages signing/locking and pushes to EHR / referrer inbox.

---

### 8. Billing, Analytics, QA, and Governance

**Purpose:** Close the loop with quality, compliance, and financial integrity.

- **Activities**
  - Code selection (CPT/HCPCS/ICD‑10) with AI assist, plus audit trails.
  - Peer review, discrepancy tracking, protocol adherence.
  - Analytics on turnaround time, queue lengths, CDS overrides, AI impact.

- **Candidate owners**
  - `ai-imaging-platform`
    - Already encodes CPT/ICD‑10 mappings and AC logic; can become core of a billing/QA engine.
  - Analytics notebooks + docs under `tt_platform/docs` and AI‑imaging docs.

**Gaps**
- A centralized “Radiology Quality & Analytics Service” that:
  - Ingests logs/events across the entire loop.
  - Surfaces dashboards & alerts (e.g., chronic delays, protocol drift, frequent CDS overrides).

---

## B. Component Purpose Index v0.1 (draft)

Here’s a first pass at a purpose mapping for key components, in terms of the engineered workflow phases above.

I’ll keep this high‑level and focused on the big pieces:

1. **`tier1-product/ai-imaging-platform`**
   - **Workflow phases:** 1, 2, 3, 7, 8  
   - **Purpose:** Core clinical knowledge and decision engine for imaging:
     - Takes order indications and patient context to recommend modalities/protocols.
     - Encodes ACR AC, CPT/ICD‑10, and terminology crosswalks.
     - Provides GraphRAG‑based reasoning over protocols and narratives.
     - Serves as a future hub for billing/QA logic and CDS analytics.

2. **`tier1-product/radiology-assistant-desktop`**
   - **Workflow phases:** 6, 7  
   - **Purpose:** Radiologist‑facing AI report assistant:
     - PHI‑safe prompting, report templates, TI‑RADS and other schemas.
     - Streaming report generation, priority classification, recommendation sections.
     - Optional text‑to‑speech and summarization for reading workflows.

3. **`tier1-product/dicom-ecosystem`**
   - **Workflow phases:** 3, 4, 5, 6, 7  
   - **Purpose:** Local DICOM “lab” for imaging infrastructure:
     - Implements Orthanc/DCM4CHEE/DICOMcloud/OHIF combo for PACS + viewer.
     - Handles Modality Worklist, DICOM networking, DICOMweb, and SR round‑trip.
     - Provides SR tooling (TID 1500, validation) to support structured reporting.

4. **`dicom-rag-integration`**
   - **Workflow phases:** 3, 5, 6, 8  
   - **Purpose:** Bridge between DICOM artifacts (images/SR) and GraphRAG:
     - Extracts entities/relationships from imaging data.
     - Enables knowledge‑graph‑driven reasoning about protocols, findings, and QA.

5. **`dicom-mcp`**
   - **Workflow phases:** 3, 5, 6, 7  
   - **Purpose:** MCP server for DICOM operations:
     - Lets agents/tools interact with PACS, run queries, fetch/send SRs, drive DICOM workflows through standardized tools.

6. **`radiology-report-generator`**
   - **Workflow phases:** 6, 7  
   - **Purpose:** More focused report‑generation engine:
     - Provides programmatic APIs/MCP interfaces to construct structured reports (possibly DICOM SR) from findings.

7. **Healthcare MCP servers (e.g., `fhir-mcp-server`, `typeform-mcp-server`, `notion-mcp-server`, `macos-automator-mcp`)**
   - **Workflow phases:** 1, 2, 7, 8 (supporting)  
   - **Purpose:** Glue between radiology stack and the rest of your environment:
     - FHIR/EHR access, data collection (Typeform), documentation/notes (Notion), local automations.

8. **`tools/warp-documentation-automation`**
   - **Workflow phases:** meta / governance  
   - **Purpose:** Keep documentation and WARP rules aligned with actual workflows:
     - Journaling and handoff templates that can be extended to encode workflow changes over time.

This is intentionally incomplete; we can extend it to specific MCP servers and side‑projects, but it should be enough to start your concept map.

---

## C. Suggested Missing / Future Components (brainstorm)

Given the refined workflow and your existing stack, here are some candidate components to **design or acquire**:

1. **CDS Gateway / Order Entry Bridge**
   - **Role:** A small, well‑defined service that:
     - Exposes ACR AC / `ai-imaging-platform` decisions via FHIR CDS Hooks or a REST API.
     - Logs every recommendation + override.
   - **Why:** Makes phase 1 explicit and gives you a single place to monitor/optimize CDS impact.

2. **Protocol Governance & Catalog Service**
   - **Role:**
     - Owns the authoritative protocol catalog (RadLex Playbook + local variants).
     - Provides APIs for protocol selection, versioning, approval workflows, and linkage to ACR AC.
   - **Why:** Centralizes what is otherwise spread across docs + AI prompts.

3. **Clinical Context Aggregator**
   - **Role:**
     - Aggregates priors, reports, labs, meds, and external imaging into a per‑order “context package” (e.g., FHIR Composition + DICOM links).
   - **Why:** Simplifies AI reasoning and viewer integration; reduces duplication in each downstream tool.

4. **AI Triage & Worklist Orchestrator**
   - **Role:**
     - Orchestrates inference jobs (e.g., stroke, PE, incidental findings).
     - Updates worklist priorities in RIS/PACS; attaches flags and structured alerts.
   - **Why:** Turns your AI capabilities into measurable improvements in phase 5.

5. **Reading Workspace Orchestrator**
   - **Role:**
     - Logically binds a case’s images (OHIF/Orthanc), AI assistant session (desktop app or web), and SR templates into a coherent session.
     - Manages session state, context, and output artifacts (SR, narrative, codes).
   - **Why:** Clarifies how the viewer, assistant, and SR tools are meant to act together in phase 6–7.

6. **Report & SR Orchestration Service**
   - **Role:**
     - Consumes findings from AI + human edits.
     - Produces: DICOM SR, narrative report, FHIR DiagnosticReport/Observations, CPT/ICD‑10 bundle.
     - Ensures internal consistency and enforces required checks before finalization.
   - **Why:** Makes report correctness and multi‑format output a first‑class concern.

7. **Radiology Quality & Analytics Service**
   - **Role:**
     - Ingests logs/events from CDS, scheduling, PACS, SR, and AI triage.
     - Provides dashboards for TAT, discrepancy rates, protocol adherence, override patterns.
   - **Why:** Gives you a systematic way to evaluate whether your engineered workflow is actually working.

---

## D. Next steps (still in brainstorming mode)

Given where we are, here’s a pragmatic order of operations:

1. **Refine this engineered workflow text**  
   - You mark anything that feels off, missing, or over‑specified.
   - We adjust the phases and responsibilities until they accurately reflect your intent.

2. **Promote the Component Purpose Index into a real doc**  
   - Once you’re comfortable, we can drop a `COMPONENT_PURPOSE_INDEX.md` (or similar) into `tt_platform/docs/` and link it from `WARP.md` and `SYSTEM_ARCHITECTURE_GUIDE.md`.

3. **Create a concept‑map diagram**  
   - Using this refined workflow and the index, I can synthesize a Mermaid (or similar) diagram representing:
     - Phases 1–8,
     - Main actors,
     - Your concrete components,
     - And the core data flows (DICOM, SR, FHIR, MPC/tool calls).

If you agree, the next thing I’ll do is propose a compact “Component Purpose Index” markdown snippet suitable for inclusion under `tt_platform/docs/`, plus a draft concept‑map node/edge list that we can convert into a diagram.