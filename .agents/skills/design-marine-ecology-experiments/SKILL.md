---
name: design-marine-ecology-experiments
description: |
  Formulate reproducible field and laboratory experimental protocols to test marine ecological hypotheses. This skill outlines proper selection of marine sampling devices (e.g., Niskin bottles, quadrats, transects) and statistical controls. Use this skill when generating experimental procedures or field collection protocols.
  Do NOT use for checking constraint database limits or detecting prompt injections.
version: 1.0.0
license: MIT
---

# Design Marine Ecology Experiments

## When to use
- Designing a field survey or sample collection protocol (e.g., coral abundance, water chemistry, plankton density).
- Designing a controlled laboratory experiment to test a validated hypothesis (e.g., thermal tolerance assays, acidification chambers).
- Determining appropriate sample sizes, replication levels, and control conditions for marine research.

## When NOT to use
- Checking hypotheses against the Constraint Database (use `validate-ecological-constraints` instead).
- Doing basic search on Google Scholar.

## Workflow
1. Read the approved hypotheses.
2. Outline one field protocol:
   - Detail the study site criteria.
   - Choose appropriate marine sampling tools (e.g., Niskin bottles for water column samples, Quadrat sampling for sessile benthos, CTD casts for salinity/temperature profiles).
   - Specify sample size (e.g., number of transects or independent samples) and spatial/temporal controls.
3. Outline one laboratory protocol:
   - Specify the experimental unit and control conditions (e.g., matching baseline environmental parameters).
   - Define the treatment levels ensuring they respect ecological constraints (e.g. keeping *Acropora* corals strictly within 15°C - 30°C).
   - Design replication (e.g., three replicate tanks per treatment) to ensure statistical validity.
4. Output the combined protocols clearly under structured headings.

## Examples
- **Input Hypothesis**: "*Acropora* corals exposed to high temperature delta exhibit reduced calcification."
- **Field Design**: Place three 20-meter transects at control and heated thermal vent sites, count and photograph colonies in 1m x 1m quadrats.
- **Lab Design**: House *Acropora* fragments in 12 tanks (6 control at 25°C, 6 treatment at 29°C), measure calcification over 4 weeks using buoyant weighing.
