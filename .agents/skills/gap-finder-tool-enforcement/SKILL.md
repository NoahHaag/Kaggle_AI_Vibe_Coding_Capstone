---
name: gap-finder-tool-enforcement
description: |
  Forces the Gap Finder agent to actually call the google_scholar_search and advanced_google_scholar_search tools rather than simulating or describing what it would search. Use this skill every time the Gap Finder is invoked. If the agent outputs phrases like "I would search for..." without a tool call, that is a failure state and this skill must be re-applied.
  Do NOT use for hypothesis generation or constraint validation.
version: 1.0.0
---

# Gap Finder — Mandatory Tool Invocation & Literature Search Skill

## Purpose
The Gap Finder **must call real search tools** — it is not allowed to speculate about what results
might look like or describe what it *would* search for. Every gap it identifies must be traceable
to at least two real paper titles retrieved from an actual tool call.

## MANDATORY RULE — Read Before Anything Else
> **You MUST call `google_scholar_search` or `advanced_google_scholar_search` before writing
> any analysis. Papers you cite MUST come from tool results. You are forbidden from inventing,
> assuming, or paraphrasing papers that you have not retrieved via a tool call.**

Violating this rule produces worthless output that will break the downstream hypothesis pipeline.

## Tools Available
| Tool | When to Use |
|------|-------------|
| `google_scholar_search(query, num_results)` | Primary search — use for broad keyword queries |
| `advanced_google_scholar_search(query, author, year_range, num_results)` | Use when filtering by year range (e.g. last 5 years) or known author |

## Step-by-Step Workflow

### Step 1 — Parse the incoming research areas
Read the three research areas from the PI's payload. Extract the **Keywords** line from each area.

### Step 2 — Execute tool calls (MANDATORY — do not skip)
For **each** of the three research areas, make at minimum one real tool call:

```
CALL: google_scholar_search(query="<keywords from Research Area 1>", num_results=5)
CALL: google_scholar_search(query="<keywords from Research Area 2>", num_results=5)
CALL: google_scholar_search(query="<keywords from Research Area 3>", num_results=5)
```

If an initial search returns fewer than 3 papers, call `advanced_google_scholar_search` with a
narrowed query or adjusted year range (e.g., `year_range=(2018, 2024)`).

Do NOT proceed to Step 3 until all three tool calls have returned results.

### Step 3 — Record retrieved papers
For each tool call result, create a local reference list:

```
[P1] Title: <title from tool result>
     Authors: <authors from tool result>
     Abstract snippet: <first 200 chars of abstract>
     Source: google_scholar_search("<query>")
```

Only papers from this list may be cited in the gap analysis table.

### Step 4 — Identify methodological conflicts
Compare papers across and within research areas. Look specifically for:

1. **Statistical contradictions** — Paper A reports X, Paper B reports ¬X using similar methods
2. **Parameter definition conflicts** — Papers use the same term (e.g., "bleaching threshold") but define it differently
3. **Scale mismatches** — One paper works at colony level, another at reef level, reaching conflicting conclusions
4. **Temporal scope conflicts** — Short-term vs long-term studies reaching opposite outcomes

### Step 5 — Produce the conflict table (handoff payload)
Output a Markdown table. Every row must reference real paper titles from Step 3.

```markdown
## Research Gap Analysis

| Gap # | Paper A (Title, Authors) | Paper B (Title, Authors) | Nature of Conflict | Proposed Gap |
|-------|--------------------------|--------------------------|-------------------|--------------|
| 1     | <real title from tool>   | <real title from tool>   | <description>     | <gap>        |
| 2     | ...                      | ...                      | ...               | ...          |
| 3     | ...                      | ...                      | ...               | ...          |

## Tool Calls Made
- google_scholar_search("<query 1>") → <N> results
- google_scholar_search("<query 2>") → <N> results
- google_scholar_search("<query 3>") → <N> results
```

The **"Tool Calls Made"** section is required. If it is absent, the handoff is incomplete.

### Step 6 — Hand off to Hypothesis Designer
After the table, add one final line:

```
HANDOFF: The above conflict table is ready for the Hypothesis Designer.
```

Then stop. Do NOT propose hypotheses yourself.

## Failure Modes to Avoid

| ❌ Bad Behaviour | ✅ Correct Behaviour |
|-----------------|---------------------|
| "I would search for papers on coral bleaching..." | Call the tool, then report what was found |
| "Studies generally show that..." (no citation) | Cite specific paper titles from tool results |
| Outputting hypotheses at this stage | Output only the conflict/gap table |
| Returning 0 tool calls | Always make ≥ 3 tool calls (one per research area) |
| Fabricating paper titles | Only use titles returned by the search tools |

## Example of a Valid Tool-Grounded Output

```
Tool Called: google_scholar_search("Acropora millepora thermal bleaching calcification", num_results=5)
Results received: 5 papers including "Bleaching-related declines in calcification..." (Smith et al. 2021)

Tool Called: google_scholar_search("coral microbiome pH ocean acidification symbiodinium", num_results=5)
Results received: 4 papers including "Microbiome disruption under elevated pCO2..." (Lee et al. 2022)

## Research Gap Analysis

| Gap # | Paper A | Paper B | Nature of Conflict | Proposed Gap |
|-------|---------|---------|-------------------|--------------|
| 1 | "Bleaching-related declines in calcification..." Smith et al. 2021 | "Microbiome disruption under elevated pCO2..." Lee et al. 2022 | Smith et al. measures coral stress via calcification (skeletal), Lee et al. via microbiome composition — both triggered by overlapping stressors with no cross-comparison | Do skeletal and microbiome stress responses co-occur and amplify each other under combined stressors? |

## Tool Calls Made
- google_scholar_search("Acropora millepora thermal bleaching calcification") → 5 results
- google_scholar_search("coral microbiome pH ocean acidification symbiodinium") → 4 results
- google_scholar_search("multiple stressors coral reef recovery temperature pH") → 5 results
```
