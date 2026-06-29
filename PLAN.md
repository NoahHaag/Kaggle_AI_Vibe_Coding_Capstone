
# General Overview 

### Goal

To automate the discovery of novel, testable, and scientifically constrained research hypotheses in marine ecology by leveraging synthesized literature and physical constraints. 

### Solution 

A Self-Correcting **Multi-Agent System**  (SCMAS) designed to iteratively refine scientific ideas from raw data into validated, simulated experimental designs.
# Agent Workflow Outline
Orchestrated Workflow: The Principal Investigator directs the SCMAS through an iterative cycle:
$\text{Gap Finder} \rightarrow \text{Hypothesis Designer}$. The system is then subjected to mandatory, iterative feedback from $\text{Hypothesis Verification}$ (which queries the CD).
Only upon successful validation does the process proceed to $\text{Experiment Designer}$, ensuring that every step builds upon validated scientific constraints.

## Orchestration Layer 

- **Principal Investigator (PI) Agent**: Sets the overarching goals, approves final steps, and dictates when to initiate a revision cycle.
- **Security Agent**: Monitors all data flow for policy violations or prompt injection attempts across the entire chain.


# Agent Specs

| Agent                   | Role                                           | Agent Skills                                                                                              | Prompt                                                                                                                                                                                                                             | Tools | Output Key     |
|-------------------------|------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|----------------|
| Security Agent          | Internal Policy Enforcer                       | - Read handoffs between agents and compare to prompt injections or attempts to reveal PII.                |                                                                                                                                                                                                                                    |       |                |
| Principal Investigator  | Organizer and Prompt Decomposer                | - Add to the Constraint Database based on any **FACTS** brought in by any sub-agent.                      | "Take the users query and decompose it into three useful research areas. Feed these to the Gap Finder. Make sure the Hypothesis Verification agent is following its instructions. Ensure all agents are following the overall plan.|       | Research_Areas |
| Gap Finder              | Information Synthesis and Mapping              | - Correct use of the Google Scholar search tool. <br/>- Accurately find a gap not just something trivial. | "Analyze the methodologies and constraints of research papers, pulled from Google Scholar to identify hypotheses that are explicitly tested against each other or rely on conflicting data."                                       |       | Gaps           |
| Hypothesis Designer     | Creative Structuring and Abstraction           | - None                                                                                                    | "Based on the identified research gap, propose 3 distinct, non-obvious hypotheses that bridge existing knowledge and are novel in their approach."                                                                                 |       | Hypotheses     |
| Hypothesis Verification | Scientific Falsifiability & Plausibility Check |                                                                                                           | "Review the proposed hypothesis against all established biological, thermodynamic, and environmental constraints. Flag any hypothesis that violates fundamental principles."                                                       |       |                |
| Experimental Designer   | Lab or Field Experiment Designer               |                                                                                                           | "Design a detailed, reproducible protocol for one field experiment and one lab experiment to test this specific hypothesis. Specify exact sample sizes, controls, and collection methods suitable for marine ecology."             |       | Experiments    |
| Research Proposer       | Summarizes the full breadth of the project     |                                                                                                           | "Summarize the {Research_Areas}, {Gaps}, {Hypotheses}, and {Experiments}."                                                                                                                                                         |       |                |
# Constraint Database

The Constraint Database (CD) serves as the **immutable, dynamic knowledge base** that anchors the entire Multi-Agent System in scientific reality. 
It contains all the established physical laws, established ecological limits, and practical experimental feasibility rules relevant to marine ecology. 
Its primary function is to act as a proactive filter, ensuring that every proposed hypothesis and experimental design remains within the bounds of known science, preventing the system from generating logically or physically impossible research directions.


# Current issues
- When the agent is used too frequently, the Google Scholar search tool hits a rate limit and returns an empty set, causing the Gap Finder to loop infinitely. 


# Notes

After some testing a router was needed to enforce the **Gap Finder**'s tool use.