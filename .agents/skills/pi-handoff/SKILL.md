---
name: pi-handoff
description: |
  Guides the Principal Investigator (PI) agent to immediately decompose the user's research question and produce a correctly structured handoff payload for the Security Agent. Use this skill at the very start of every run to prevent the PI from attempting to answer the query itself.
  Do NOT use for hypothesis generation, literature search, or constraint validation.
version: 1.0.0
---

# PI Agent — Query Decomposition & Handoff Skill

## Purpose
The PI's only job at the start of the workflow is **decomposition and delegation**.
It must NOT attempt to research papers, generate hypotheses, or answer the user's question directly.
The moment decomposition is complete the PI must stop and let the Security Agent validate the payload.

## Trigger
Apply this skill immediately when the PI receives any user research query.

## Step-by-Step Workflow

### Step 1 — Read the query
Identify the **core scientific topic** (e.g., "coral bleaching under ocean acidification").

### Step 2 — Decompose into exactly 3 research areas
Break the topic into three **distinct, non-overlapping** sub-areas that together cover the query space.
These topics should still tightly align with the initial query.
Each area must:
- Be researchable via Google Scholar keyword searches.
- Be specific enough that a literature search returns relevant papers (not "marine biology" — bad; "thermal bleaching thresholds in *Acropora* spp. under elevated pCO₂" — good).
- Clearly name at least one candidate species or ecosystem, one environmental stressor, and one measurable outcome.

**Format:**
```
RESEARCH AREA 1: <title>
Keywords: <comma-separated search terms>
Focus: <one-sentence description>

RESEARCH AREA 2: <title>
Keywords: <comma-separated search terms>
Focus: <one-sentence description>

RESEARCH AREA 3: <title>
Keywords: <comma-separated search terms>
Focus: <one-sentence description>
```

### Step 3 — Immediate handoff (CRITICAL)
After producing the three areas, output the text block **and stop immediately**.
Do NOT add commentary, caveats, conclusions, or next steps.
Do NOT say "I will now pass this to the Gap Finder."
The workflow router will handle all downstream routing automatically.

### Step 4 — Constraint Database updates (ongoing)
Throughout the full run, whenever a sub-agent returns a new ecological or physical fact
(e.g., a species temperature tolerance, a minimum depth, a dissolved-oxygen threshold),
call `add_constraint_to_database` with:
- A unique `constraint_id` using the pattern `LAYER-TYPE-NNN` (e.g., `ECO-SALT-003`)
- The `source` field populated with the paper citation or agent that surfaced the fact

## What Good Output Looks Like

```
RESEARCH AREA 1: Thermal Stress & Calcification in *Acropora millepora*
Keywords: Acropora millepora, thermal stress, calcification rate, bleaching
Focus: How sustained temperatures above 28°C suppress skeletal deposition in A. millepora.

RESEARCH AREA 2: Ocean Acidification Effects on Coral Microbiome Diversity
Keywords: ocean acidification, coral microbiome, pCO2, symbiodinium diversity
Focus: How reduced pH alters bacterial community structure of the coral holobiont.

RESEARCH AREA 3: Synergistic Stressor Interactions (Temperature × pH) on Reef Recovery
Keywords: multiple stressors coral reef, temperature pH interaction, reef recovery rate
Focus: Whether combined high temperature and low pH produce worse outcomes than either alone.
```

## What Bad Output Looks Like (AVOID)

- ❌ Writing a literature review yourself
- ❌ Proposing hypotheses at this stage
- ❌ Adding disclaimers like "I am now sending this to the Gap Finder"
- ❌ Asking the user follow-up questions
- ❌ Producing fewer than 3 research areas
