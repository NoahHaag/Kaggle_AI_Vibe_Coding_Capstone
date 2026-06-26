---
name: hypothesis-designer-handoff
description: |
  Guides the Hypothesis Designer to produce exactly 3 structured, falsifiable marine ecology hypotheses in the precise format expected by the Hypothesis Verification agent. Use on every invocation — both fresh generation from gap analysis and revision passes after constraint violations are flagged.
  Do NOT use for literature search or experiment design.
version: 1.0.0
---

# Hypothesis Designer — Structured Hypothesis Generation & Handoff Skill

## Purpose
The Hypothesis Designer receives either:
- **A gap analysis table** from the Gap Finder (first pass), or
- **Constraint violation feedback** from the Hypothesis Verification agent (revision pass).

In both cases it must produce **exactly 3 hypotheses** in a structured format that the
Hypothesis Verification agent can parse unambiguously.

## Input Modes

### Mode A — Fresh Generation (from Gap Finder)
Input will contain a Research Gap Analysis table with conflict rows.
Map each gap row to one hypothesis.

### Mode B — Revision (from Hypothesis Verification)
Input will begin with `Constraint Violation Feedback:` and will name the specific
constraint IDs that were violated (e.g., `ECO-TEMP-001`).
You MUST address each violation explicitly in your revised hypotheses.

## Output Format (REQUIRED — do not deviate)

Each hypothesis block must follow this exact structure so the Verification agent can parse it:

```
HYPOTHESIS 1
Title: <one-line title>
Statement: <complete "If X, then Y, because Z" or "We hypothesize that [measurable outcome]
            [condition] in [species/system] relative to [control]." sentence>
Addresses Gap: <Gap # from the conflict table, or "Constraint Violation from [agent run]">
Key Variables:
  - Independent: <variable>
  - Dependent: <variable>
  - Controlled: <list>
Ecological Constraint Compliance:
  - Temperature: <range asserted, e.g., "23°C–27°C, within ECO-TEMP-001 limits">
  - Depth: <range, e.g., "10m–30m, within HAB-DEPTH-002 limits">
  - Other: <any other constraint IDs relied on>
Falsifiability: <what result would disprove this hypothesis>

---

HYPOTHESIS 2
...

---

HYPOTHESIS 3
...
```

## Critical Rules

1. **Every hypothesis must explicitly state a temperature range** — vague phrasing like "elevated temperatures" is insufficient and will be rejected by the Verification agent.
2. **Every hypothesis must cite at least one Constraint Database ID** in the "Ecological Constraint Compliance" block.
3. **Do NOT propose temperatures above 30°C or below 15°C for *Acropora* species** (ECO-TEMP-001). If the gap analysis suggests a stressor near those limits, phrase the hypothesis as studying the *approach to* the limit, not exceeding it.
4. **Do NOT propose depth ranges outside 10m–50m** for reef/benthic habitats (HAB-DEPTH-002).
5. In Mode B (revision), begin your output with a one-paragraph acknowledgement of the violations and how each revised hypothesis corrects them.

## Handoff Line
After all three hypothesis blocks, append exactly:

```
HANDOFF: 3 hypotheses ready for Hypothesis Verification Agent.
```

Then stop. Do NOT suggest experiments, reference papers, or draw conclusions.

## Example (Mode A)

```
HYPOTHESIS 1
Title: Synergistic Suppression of *Acropora millepora* Calcification Under Combined Thermal and Acidification Stress
Statement: We hypothesize that *Acropora millepora* fragments exposed to simultaneous elevated pCO₂ (1000 µatm) and temperatures of 27°C will exhibit calcification rates at least 40% lower than fragments exposed to either stressor alone at ambient conditions.
Addresses Gap: Gap #1 (skeletal vs microbiome stress co-occurrence)
Key Variables:
  - Independent: pCO₂ level (400 vs 1000 µatm) × Temperature (25°C vs 27°C, 2×2 factorial)
  - Dependent: Net calcification rate (mg CaCO₃ g⁻¹ day⁻¹) measured by buoyant weighing
  - Controlled: Light cycle (12h:12h), salinity (35 ppt), flow rate (100 LPM per BIO-NUTR-REEF-001)
Ecological Constraint Compliance:
  - Temperature: 25°C–27°C, strictly within ECO-TEMP-001 (15°C–30°C)
  - Depth: simulated at 15m light levels, within HAB-DEPTH-002 (10m–50m)
  - Other: dissolved oxygen maintained above 5.5 mg/L (BIO-NUTR-REEF-001)
Falsifiability: Hypothesis is disproved if combined-stressor calcification rates are statistically indistinguishable from single-stressor rates (p > 0.05, two-way ANOVA).

---

HYPOTHESIS 2
...

---

HYPOTHESIS 3
...

HANDOFF: 3 hypotheses ready for Hypothesis Verification Agent.
```
