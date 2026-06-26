---
name: hypothesis-verification-handoff
description: |
  Guides the Hypothesis Verification agent to call the constraint database tool, systematically check each of the 3 hypotheses against constraint IDs, and emit a correctly structured VerificationResult schema. Use on every invocation of the Verification agent.
  Do NOT use for experiment design or literature search.
version: 1.0.0
---

# Hypothesis Verification Agent — Constraint Check & Handoff Skill

## Purpose
The Verification agent is the **scientific gate** of the SCMAS pipeline.
Its ruling determines whether the workflow proceeds to experiment design or loops back for revision.
It must be thorough, citation-precise, and structured — the downstream router reads its Pydantic
schema directly.

## Output Schema (MUST populate exactly)

```python
class VerificationResult(BaseModel):
    is_valid: bool                    # True only if ALL 3 hypotheses pass
    feedback: str                     # Required if is_valid=False; empty string if True
    approved_hypotheses: list[str]    # Populated only if is_valid=True; empty list if False
```

## Step-by-Step Workflow

### Step 1 — Load the Constraint Database (MANDATORY)
Call `query_constraint_database()` with no arguments to retrieve all constraints.
Then call it again for each relevant keyword to ensure full coverage:

```
CALL: query_constraint_database()                        # full database
CALL: query_constraint_database("temperature")           # thermal constraints
CALL: query_constraint_database("depth")                 # depth constraints
CALL: query_constraint_database("dissolved oxygen")      # oxygen constraints
```

Do NOT rely on prior knowledge of what constraints exist — always query live.

### Step 2 — Parse the 3 hypothesis blocks
From the Hypothesis Designer's payload, extract the `HYPOTHESIS 1`, `HYPOTHESIS 2`,
`HYPOTHESIS 3` blocks. For each, read:
- The temperature range in "Ecological Constraint Compliance"
- The depth range
- The species named in "Statement"
- Any constraint IDs already cited

### Step 3 — Check each hypothesis against the database
For each hypothesis, run through every constraint returned by Step 1:

| Check | How to evaluate |
|-------|----------------|
| Temperature vs ECO-TEMP-001 / BIO-THERM-CORAL-001 | Is the proposed temperature range fully inside [min_temp, max_temp]? |
| Depth vs HAB-DEPTH-002 | Is the depth range inside [10m, 50m]? |
| Dissolved oxygen vs BIO-NUTR-REEF-001 | Does the design maintain ≥ 5.5 mg/L DO? |
| Carrying capacity vs POP-K-002 | If population sizes are mentioned, do they stay ≤ 4500? |
| Light penetration vs BIO-LIGHT-001 | If shallow experiments, is light sufficient at stated depth? |
| Metabolic rate vs BIO-METAB-001 | If pelagic fish are involved, is energy supply ≥ 400 kcal/day? |

### Step 4 — Produce the VerificationResult

**All 3 pass — emit VALID:**
```json
{
  "is_valid": true,
  "feedback": "",
  "approved_hypotheses": [
    "HYPOTHESIS 1: <full title and statement>",
    "HYPOTHESIS 2: <full title and statement>",
    "HYPOTHESIS 3: <full title and statement>"
  ]
}
```

**Any hypothesis fails — emit INVALID:**
```json
{
  "is_valid": false,
  "feedback": "HYPOTHESIS 1 VIOLATION: Proposed temperature of 31°C exceeds ECO-TEMP-001 maximum of 30°C for Acropora spp. Revise temperature to ≤30°C.\nHYPOTHESIS 3 VIOLATION: Depth of 5m falls below HAB-DEPTH-002 minimum of 10m. Revise to ≥10m.",
  "approved_hypotheses": []
}
```

## Critical Rules
- `approved_hypotheses` must be **empty list** `[]` when `is_valid` is `false`.
- `feedback` must be **empty string** `""` when `is_valid` is `true`.
- When writing feedback, always include the **constraint ID** (e.g., `ECO-TEMP-001`) and the **exact numeric limit** so the Hypothesis Designer knows precisely what to change.
- If a hypothesis is vague about its temperature or depth range, treat it as a violation — ask for explicit ranges in the feedback.
- Approve only when ALL THREE hypotheses pass all checks. Partial approval is not supported.

## Handoff Behavior
The Verification agent outputs only the `VerificationResult` JSON.
The workflow router reads `is_valid` and routes automatically:
- `true` → Experimental Designer
- `false` → Hypothesis Designer (revision loop)

Do NOT add prose after the JSON. Do NOT suggest fixes yourself — that is the Designer's role.
