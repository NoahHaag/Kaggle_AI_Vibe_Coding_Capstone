# 🌊 Marine Ecology Research Hypothesis Generator 🌊

> A Self-Correcting Multi-Agent System (SCMAS) for automated discovery of novel, testable, and scientifically constrained research hypotheses in marine ecology.

## 🚀 Project Overview

The goal of this project is to leverage synthesized literature and physical constraints to generate and validate research hypotheses. The system is designed to iteratively refine scientific ideas, from raw data to simulated experimental designs, ensuring that each step is grounded in scientific reality.

## ⚙️ System Architecture

The system is built as a multi-agent workflow orchestrated by a **Principal Investigator (PI)** agent. The workflow is designed to be self-correcting, with feedback loops for hypothesis verification and revision.

The overall workflow is as follows:

1.  **Principal Investigator** 🕵️‍♀️: Decomposes a user's query into research areas.
2.  **Gap Finder** 🗺️: Identifies research gaps in the existing literature.
3.  **Hypothesis Designer** ✍️: Proposes novel hypotheses based on the identified gaps.
4.  **Hypothesis Verification** 🔬: Checks the proposed hypotheses against a Constraint Database of known scientific facts.
5.  **Revision Loop** 🔄: If a hypothesis is invalid, it is sent back to the Hypothesis Designer for revision.
6.  **Experimental Designer** 🧪: Designs experiments to test validated hypotheses.
7.  **Security Agent** 🛡️: Monitors the entire process for policy violations.
8.  **Research Proposer** 📝: Summarizes the entire research plan.

## 🤖 Agents

The system is composed of the following agents:

*   **Principal Investigator (PI)**: Sets the research goals and manages the Constraint Database.
*   **Security Agent**: Enforces internal policies and prevents prompt injections.
*   **Gap Finder**: Analyzes research papers to identify gaps in the current body of knowledge.
*   **Hypothesis Designer**: Generates novel and falsifiable hypotheses.
*   **Hypothesis Verification**: Validates hypotheses against the Constraint Database.
*   **Experimental Designer**: Designs detailed lab and field experiments.
*   **Research Proposer**: Summarizes the complete research plan.

## 🛠️ Tools

The agents use the following tools:

*   `google_scholar_search`: Performs a simple keyword search on Google Scholar.
*   `advanced_google_scholar_search`: Performs an advanced search on Google Scholar with filters for author and year.
*   `query_constraint_database`: Queries the Constraint Database for scientific constraints.
*   `add_constraint_to_database`: Adds new constraints to the Constraint Database.

## 📚 Constraint Database

The Constraint Database is a key component of the system. It serves as a dynamic knowledge base of established physical laws, ecological limits, and experimental feasibility rules relevant to marine ecology. This database ensures that all generated hypotheses and experiments are scientifically plausible.

## 🏃‍♀️ How to Run

The project is implemented as a workflow using the `google.adk` library. To run the workflow, you would typically execute the `root_agent` workflow defined in `agent.py`.

```python
# Example of how to run the workflow
from agent import root_agent

result = root_agent.run("Explore the impact of ocean acidification on coral bleaching.")
print(result)
```