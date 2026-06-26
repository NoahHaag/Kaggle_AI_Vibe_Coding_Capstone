---
name: validate-ecological-constraints
description: |
  Validate marine ecological research hypotheses and experimental designs against established thermal thresholds, salinity bounds, depth limits, and thermodynamic/physical constraints. Use this skill when checking if a hypothesis complies with known biological limits (such as Acropora spp. temperature limits) or environmental thresholds in the Constraint Database.
  Do NOT use for general literature search or non-constrained creative brainstorming.
version: 1.0.0
license: MIT
---

# Validate Ecological Constraints

## When to use
- Checking if proposed marine ecology hypotheses violate known limits.
- Confirming that simulated or laboratory temperature, salinity, or chemical parameters lie within viable ecological thresholds (e.g., keeping *Acropora* coral species between 15°C and 30°C).
- Evaluating physical/thermodynamic constraints on nutrient cycling, solar irradiance, or ocean currents.

## When NOT to use
- Generating new hypotheses from scratch.
- Searching for papers on Google Scholar.

## Workflow
1. Identify the key species, locations, and physical variables (e.g., temperature, pH, depth) mentioned in the hypothesis.
2. Query the Constraint Database using the `query_constraint_database` tool with relevant keywords (e.g., "Acropora", "temperature", "ECO-TEMP-001").
3. Compare the parameters proposed in the hypothesis or experiment to the parameters returned by the Constraint Database.
4. If a parameter falls outside the tolerance range (e.g., proposed temperature of 35°C vs tolerance max of 30°C), flag it as a violation, specify the constraint ID (e.g., ECO-TEMP-001), and formulate actionable correction feedback.
5. If no constraints are violated, approve the hypothesis.

## Examples
- **Input Hypothesis**: "Investigating the thermal resilience of *Acropora* corals by exposing them to stable 32°C water."
- **Constraint Found**: *Acropora* max temperature is 30°C (ECO-TEMP-001).
- **Result**: REJECTED. Violation: Water temperature exceeds the 30°C viable limit. Feedback: "Revise temperature below 30°C."
