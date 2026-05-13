# Chapter 13: AI & The Future of Product

## Overview

Artificial intelligence is not a single disruption—it is a stack of shifts that land at different depths in different organizations. Across Lenny's Podcast, practitioners who ship AI in production (not just demo it) keep returning to the same uncomfortable truths: probabilistic systems break the mental model of deterministic software; autonomy trades off against control; and the winning teams are those that treat AI as a **product discipline**—workflow understanding, evaluation, monitoring, culture, and leadership—not as a model pick or a chatbot bolt-on.

This chapter weaves together themes from dedicated AI episodes and from scattered “AI & The Changing PM Role” sections across the corpus. Names that appear repeatedly in these threads include **Aishwarya Naresh Reganti and Kiriti Badam** (enterprise AI deployments and teaching), **Tomer Cohen** (LinkedIn’s org-wide AI transformation), **Varun Mohan** and **Zevi Arnovitz** (how coding agents change who ships), **Wes Kao** (delegation and judgment with LLM partners), **Tobi Lütke** (first-principles and “expired assumptions”), and **Simon Willison** and other practitioners who stress shipping safely in public. The goal is not prediction—it is **orientation**: what changes, what does not, and how to stay valuable as the tooling layer commoditizes.

---

## What Changes: Non-Determinism and the Agency–Control Tradeoff

Reganti and Badam articulate a clean pair of differences between classic software and AI products. First, **non-determinism on both sides of the interface**: users can express intent in natural language in many ways you did not design for, while the “API” you call—the model—is sensitive to phrasing and context in ways you cannot fully specify. Second, the **agency–control tradeoff**: every time you give an agent more autonomy to decide or act, you give up direct control. The product task is not “maximize autonomy”; it is **earn autonomy in stages** while preserving user trust and organizational safety.

Their prescription is deliberately incremental: start with **high human control and low agency** (e.g., support copilots that *suggest* before they *act*), log what humans change, and only widen the agent’s decision surface when behavior is calibrated. They call this behavior **continuous calibration / continuous development**—an AI-native lifecycle analogous to CI/CD, where evaluation metrics and production signals feed each other rather than pretending one offline eval suite captures reality.

That framing connects directly to org reality: PMs, engineers, and data scientists increasingly sit in the **same feedback loop**—reviewing traces, debating failure modes, and aligning on what “good” means when “good” is statistical. The PM contribution shifts toward **defining expected behavior**, choosing where autonomy is safe, and clarifying what “evals” even mean in a given context (benchmarks vs. labeled sets vs. implicit production signals).

---

## What Does Not Change: Problems, Taste, and Workflow Literacy

Across guests, the anti-pattern is consistent: **tool-first thinking**—starting from “we need an agent” instead of “we need to remove a specific pain in a workflow.” Reganti and Badam use the phrase **problem-first** as a guardrail against the hype cycle. LinkedIn’s story under Tomer Cohen reinforces the same point at company scale: when LLMs arrived in force, leadership asked teams to return to **core customer problems** and temporarily loosen rigid roadmaps in favor of exploration—then converge on a small number of bets with weekly review. AI first became a **capability expectation for PMs** (training on objectives, data, fine-tuning—not delegating “AI” to a corner of engineering).

Varun Mohan’s field observations echo a structural shift: when PMs and domain experts can ship with coding agents, the scarce resource becomes **what to build** and **whether it is good**—taste, judgment, domain understanding—not raw implementation throughput. Zevi Arnovitz describes titles and responsibilities **collapsing toward “builder”** as more people can cross traditional boundaries—again raising the premium on clarity, narrative, and responsible scope.

None of that repeals classic product craft. It intensifies it: **workflow literacy** (where does value accrue, where does risk live), **stakeholder alignment**, and **sequencing** matter more when the system can do damage at machine speed.

---

## Evaluation, Monitoring, and the “Semantic Diffusion” of Words

Reganti and Badam argue against false dichotomies: **offline evals** encode what you already believe matters; **production monitoring** surfaces what you did not anticipate (implicit signals like regenerations, tool-call failures, silent abandonment). High-volume systems need monitoring to prioritize which traces deserve human review; discoveries there become new eval slices. “Evals” as a buzzword has suffered **semantic diffusion**—benchmark leaderboards, PM-written scenarios, and expert annotations all get called “evals,” but they solve different slices of the problem.

For PM interviews, the durable sound bite is: **build an actionable feedback loop appropriate to risk**, not a religion of either vibes-only or eval-maxing.

---

## Organization and Culture: Leaders Go Hands-On Again

Several threads converge on leadership behavior. Reganti and Badam describe leaders who schedule **real learning time** (one CEO blocked early mornings for AI catch-up) and who model intellectual humility—“your intuitions might be wrong”—because prior career intuitions were formed in a pre-LLM world. Separately, Tomer Cohen describes **AI literacy as a baseline for PMs** at LinkedIn-scale, not an elective.

The cultural failure mode is fear: subject-matter experts avoid helping train models if they believe the project exists to **replace** them. Successful teams message **augmentation** and create incentives for experts to improve behavior, not hide institutional knowledge.

---

## Multi-Agent Hype vs. Orchestration Reality

Reganti and Badam caution that **peer-to-peer multi-agent** fantasies are hard to control in customer-facing settings; patterns with a **supervisor** and constrained sub-agents tend to be more reliable. That is less about “never use multiple agents” and more about **limiting the state space** of what can go wrong—consistent with the agency–control theme.

---

## How PMs Stay Relevant: Judgment, Delegation, and Communication

Wes Kao’s second-episode thread on using Claude as a thought partner is a useful microcosm: AI rewards **clear context, point of view, and iteration**—the same skills that make PMs effective with humans. Delegation frameworks (she discusses CEDAF-style steps in the episode notes) map cleanly onto prompting: comprehension, alignment, feedback loops.

At the macro level, Ash and Kiriti argue that as **implementation gets cheap**, differentiation moves to **design, judgment, taste, and ownership of end-to-end outcomes**—including willingness to endure the “pain” of iteration that competitors skip. That is the individual analogue of organizational moats built from real deployment experience.

---

## Chapter Takeaways

- **Treat AI products as probabilistic systems.** Design for monitoring, staged autonomy, rollback, and human-in-the-loop where stakes are high— not only happy-path demos.

- **Earn agency in layers.** Suggest → draft with review → limited actions → broader autonomy is a repeatable pattern for support, coding assistants, marketing workflows, and internal ops.

- **Pair evals with production signals.** Offline suites catch regressions you can name; live traffic teaches you what you did not know to test.

- **Keep problem-first discipline.** Model choice and “agentiness” are downstream of a crisp customer/workflow problem; otherwise you ship complexity without value.

- **Lead visibly and reduce fear.** Leaders who learn in public and frame AI as augmentation unlock the SME collaboration that makes quality possible.

- **Invest in taste and end-to-end thinking.** When more people can ship code and content, the PM’s edge is choosing the right bets and defining “good enough to widen scope.”

- **Prefer constrained orchestration over agent soup.** Control surfaces and supervisor patterns beat unconstrained multi-agent chatter for most real customer workflows.

---

## Where to Go Deeper in This Repo

- Episode notes with rich AI sections include **`study-guide/episodes/Aishwarya_Naresh_Reganti_+_Kiriti_Badam.md`**, **`study-guide/episodes/Tomer_Cohen.md`**, **`study-guide/episodes/Tomer_Cohen_2.0.md`**, **`study-guide/episodes/Varun_Mohan.md`**, **`study-guide/episodes/Zevi_Arnovitz.md`**, **`study-guide/episodes/Wes_Kao_2.0.md`**, and **`study-guide/episodes/Simon_Willison.md`** (among others—grep `## AI & The Changing PM Role` under `study-guide/episodes/` for the full set).

- For non-AI foundations that become *more* important as execution cheapens, cross-read **Chapter 1 (PM role)**, **Chapter 2 (strategy)**, **Chapter 4 (discovery)**, and **Chapter 5 (metrics)** in `study-guide/themes/`.
