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

## ✨ Examples

> **Query:**
> lets look for some unique ways to raise damselfish, specifically new ways to breed them

> **Agent Response:**
> Phase 1: The Context (Setting the Stage)
> The survival of coral reef ecosystems hinges upon a delicate, multi-dimensional choreography of biological signals. Current marine conservation efforts are increasingly moving toward "Precision Husbandry"—an ambitious frontier that seeks to master the life cycles of keystone species, specifically within the family Pomacentridae (damselfish).
>
> To date, our foundational understanding has focused on three critical pillars: the use of multimodal sensory stimuli (lunar light spectra and reef soundscapes) to trigger spawning; the application of nutritional biotechnology to combat high larval mortality; and the implementation of AI-driven autonomous systems to monitor and adjust habitat parameters in real-time. We recognize that for a restocking program to succeed, we must not only provide the right "diet" and "signals" but also maintain a stable physical and chemical environment. However, as we attempt to engineer these micro-environments, we are confronted by a staggering ecological reality: the reef is not a collection of isolated variables, but a hyper-connected system of thermal, acoustic, and light-driven feedback loops.
>
> Phase 2: The Challenge (Defining the Gap)
> Despite our technological advancements, a profound "knowledge silo" exists that threatens the efficacy of restoration. Current literature is fragmented, focusing on single-stimulus stressors in isolation. We see studies on the benefits of acoustic enrichment (Dobson) existing alongside research on the disruptive nature of artificial light at night (Schligler), yet we lack a cohesive understanding of their synergistic or antagonistic effects.
>
> Furthermore, there is a critical conflict between active intervention and passive monitoring. As we deploy active acoustic tools to stimulate spawning, we risk masking the very passive biological signals required to assess biodiversity and biomass (Mooney et al.). Most significantly, we have ignored the multi-modal complexity of the environment. While we know fish respond to complex stimuli, our current models fail to account for the holistic physiological stress caused by the simultaneous convergence of light, sound, and thermal fluctuations. We are attempting to build high-tech nurseries on a foundation—the coral reef itself—whose breaking points under multi-modal stress remain dangerously unmapped.
>
> Phase 3: The Solution (Proposing the Path)
> To bridge the gap between high-tech fish husbandry and a collapsing natural habitat, we propose a revolutionary research trajectory. We must first establish the "biological floor"—the physiological limits of the coral architecture (Acropora spp.) that provides the essential habitat for the Pomacentridae we aim to restore.
>
> Our proposed research moves through three integrated experimental tiers designed to quantify the collapse of the reef foundation under environmental pressure:
>
> Tier 1: The Symbiotic Integrity Test (Addressing Thermal Variance) We hypothesize that increased thermal variance (22°C–26°C) significantly reduces the density of endosymbiotic dinoflagellates in Acropora spp. To test this, we will execute Protocol H1-FIELD-01, utilizing in-situ CTD profiling and quadrat-based extraction to map natural symbiont loss, complemented by lab-based PAM fluorometry to simulate 12-hour thermal cycles. This will reveal if even moderate fluctuations destabilize the coral’s primary energy source.
>
> Tier 2: The Metabolic Demand Assessment (Addressing Oxygen & Temperature) Building on the symbiont data, we must understand the energetic cost of rising temperatures. We hypothesize that metabolic oxygen consumption rates in Acropora will spike significantly at 25°C–28°C compared to baseline levels. Through Protocol H2-FIELD-01, we will combine deep-water (35m–50m) dissolved oxygen monitoring with closed-system respirometry. This will determine if rising temperatures push corals into a state of metabolic deficit that could jeopardize the entire reef food web.
>
> Tier 3: The Structural Collapse Model (Addressing Calcification Non-linearity) Finally, we must predict the physical disappearance of the reef. We hypothesize that skeletal calcification rates exhibit a non-linear, rapid decline as temperatures approach the critical 27°C–29°C threshold. Using Protocol H3-FIELD-01, we will employ buoyant weighing and non-linear thermal ramping in controlled environments to identify the exact "tipping point" where reef growth ceases to outpace erosion.
>
> Final Synthesis
> By integrating these three tiers, we move beyond simple observation. We are creating a predictive model that links coral physiological failure (the foundation) to the viability of Pomacentridae recruitment (the target species). Only by understanding the non-linear responses of the coral substrate to multi-modal stressors can we design AI-driven husbandry systems and nutritional protocols that are actually resilient to the realities of a changing ocean. We are not just studying fish; we are engineering the survival of an entire ecosystem.

> **Query:**
> What are some gaps in the research on 3D printed artificial reefs?

> **Agent Response:**
> Research Prospectus: Navigating the Chemical and Structural Paradoxes of 3D-Printed Marine Restoration
> Phase 1: The Context (Setting the Stage)
> As global coral reef ecosystems face unprecedented degradation, additive manufacturing (3D printing) has emerged as a transformative frontier in marine restoration. By utilizing high-resolution 3D printing, researchers can now engineer complex, micro-topographic architectures designed to optimize hydrodynamic flow, enhance sediment transport, and provide diverse niche availability for benthic recruitment. The promise is clear: to replace lost structural complexity with bio-compatible, engineered substrates that facilitate the rapid recovery of diverse marine taxa.
>
> However, this technological leap introduces a critical ecological tension. The transition from traditional stony substrates to synthetic, 3D-printed materials—ranging from biopolymers to calcium carbonate composites—shifts the restoration paradigm from passive structural support to active chemical interaction. As we introduce these engineered modules into sensitive marine environments, we must confront a fundamental reality: the very materials designed to save the reef may inadvertently alter the benthic water chemistry and the physiological health of the organisms they are intended to support.
>
> Phase 2: The Challenge (Defining the Gap)
> Current literature reveals a profound and unresolved conflict between the goals of structural innovation and the necessity of ecological safety. We have identified three high-potential research gaps that represent a "paradox of restoration":
>
> The Toxicity Paradox: While significant effort is being directed toward developing sustainable resins for coral restoration (Jia et al.), emerging evidence suggests that even bio-based polymers may exert immunological stresses similar to petrochemical plastics (Dara et al.). We currently lack a definitive understanding of how these resins affect the cellular health of key framework species like Acropora spp. during their degradation lifecycle.
>
> The Porosity-Leaching Paradox: To maximize biological recruitment, 3D-printed substrates are designed with high porosity and intricate surface complexities (Patil et al.). However, increasing the surface-area-to-volume ratio inherently increases the exposure of the substrate to seawater, potentially accelerating the leaching of additives and chemical agents (Jia et al.). The mathematical correlation between architectural complexity and chemical release remains unquantified.
>
> The Fragmentation Paradox: Marine-derived bioplastics are widely advocated as a sustainable alternative to ocean pollutants (Manaswini et al.). Yet, the long-term fragmentation kinetics of these materials remain a "black box." There is a critical need to determine whether these "green" materials truly mitigate microplastic pollution or if they simply create a secondary, more insidious cycle of bio-based microplastic fragmentation (Dara et al.).
>
> Phase 3: The Solution (Proposing the Path)
> To resolve these contradictions, we propose a multi-scalar research program that integrates field-based ecological monitoring with controlled laboratory stress testing. Our approach is structured around three interconnected pillars of inquiry:
>
> Pillar I: Validating Immunological Neutrality
> To address the Toxicity Paradox, we will test the hypothesis that engineered non-toxic resins will induce significantly lower immunological stress markers in Acropora spp. compared to standard bio-based polymers.
>
> Our methodology employs a dual-track approach:
>
> Field Component: We will deploy engineered vs. bio-based modules at a depth of 22m, utilizing Pulse-Amplitude Modulation (PAM) fluorometry to monitor the maximum quantum yield ($F_v/F_m$) of symbiotic zooxanthellae in situ.
> Lab Component: Controlled flow-through seawater systems (maintained at 27.5°C and 6.2 mg/L DO) will allow us to quantify precise physiological responses, ensuring that our restoration materials do not compromise the photosynthetic efficiency of the coral holobiont.
> Pillar II: Quantifying the Porosity-Leaching Correlation
> To resolve the Porosity-Leaching Paradox, we will investigate the hypothesis that there is a linear positive correlation between the increase in surface-area-to-volume ratio and the rate of chemical leachable agent release.
>
> This will be achieved through:
>
> Field Component: Deploying substrates with varying porosities (10%, 40%, and 70%) at 15m depth and utilizing Niskin bottles to capture water samples within the immediate benthic boundary layer.
> Lab Component: Using high-precision pressure chambers to simulate benthic depths, we will correlate calibrated geometric surface areas (250–1250 mm²) with spectrophotometric analysis of leachable concentrations, establishing the mathematical limits of safe architectural complexity.
> Pillar III: Assessing Fragmentation Kinetics
> Finally, to resolve the Fragmentation Paradox, we will test whether marine-derived bioplastics exhibit significantly slower fragmentation-induced microplastic production rates compared to petrochemical-based plastics.
>
> Our validation strategy includes:
>
> Field Component: Long-term immersion studies using mesh enclosures at 35m depth to monitor natural fragmentation and micro-fragment bypass in a real-world benthic environment.
> Lab Component: Accelerated degradation trials in high-flow tanks, utilizing buoyant weighing and fine-mesh sieving (10$\mu$m - 500$\mu$m) to provide a rigorous mass-balance of material loss and secondary microplastic production.
> Through this integrated framework, this research will move 3D-printed marine restoration from an era of "structural trial-and-error" to a period of "ecologically engineered precision," ensuring that the reefs of tomorrow are built on a foundation of chemical and biological stability.


## Known Bugs
- When the agent is used too frequently, the Google Scholar search tool hits a rate limit and returns an empty set, causing the Gap Finder to loop infinitely. 

