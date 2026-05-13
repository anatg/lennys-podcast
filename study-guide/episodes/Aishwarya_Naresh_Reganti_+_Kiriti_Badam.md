# Aishwarya Naresh Reganti + Kiriti Badam — AI product builders & Maven instructors

## Guest Profile
- **Name**: Aishwarya (“Ash”) Naresh Reganti; Kiriti Badam
- **Role/Company**: Ash: early AI researcher (Alexa, Microsoft), published 35+ papers, consulting on AI deployments. Kiriti: works on OpenAI’s coding agent product (referred to in the episode as both “Kodex” and “Codex” in the transcript); previously Google and Kumo; decade in AI/ML infrastructure. Together they teach a highly rated Maven course on building enterprise AI products and maintain a popular GitHub learning repo (~20K stars per episode discussion).
- **Background**: As a pair they have led or supported 50+ AI product deployments across Amazon, Databricks, OpenAI, Google, startups, and enterprises. The episode focuses on avoiding common failure modes when shipping AI products and agents.

## Tags
`AI/ML` `Product Strategy` `Execution` `Enterprise` `Experimentation` `Leadership` `Culture` `Platform` `Career` `Frameworks`

## TL;DR
Ash and Kiriti argue that AI products differ from traditional software in two fundamental ways: **non-determinism** (unpredictable users in natural language plus a probabilistic “LLM API”) and the **agency–control tradeoff** (more autonomy for the system means less direct control for you). Their antidote is to ship **incrementally**: start with **high human control and low agency**, log behavior, tighten reliability, then increase agency over time—paired with a **continuous calibration / continuous development** loop that blends scoped evals with rich production monitoring rather than treating “evals” as a magic wand.

## Core Frameworks & Mental Models

- **Non-determinism (input + process + output)**: Unlike a mapped UI workflow, users can express intent many ways; the model’s outputs also shift with phrasing and context—so you must design for behavior you cannot fully specify up front.

- **Agency–control tradeoff**: Autonomy is not free. Before expanding what the AI can decide or execute, the system must **earn trust** through demonstrated reliability in narrower scopes.

- **Half Dome training / “start small”**: Like training for a hard hike, don’t begin with a maximal agent on day one. Build muscle on constrained slices so you learn true model and workflow limits.

- **Problem-first (not tool-first)**: AI hype makes it easy to obsess over solution complexity and forget the user problem; forcing smaller autonomy scopes keeps the team anchored on the actual job-to-be-done.

- **Success triangle (people, not only tech)**: **Leaders** who relearn intuitions and go hands-on (example: a CEO blocking early mornings for AI learning); **culture** that augments experts instead of threatening them with replacement; **technical** obsession with real workflows and the right mix of ML, LLM, and deterministic code.

- **Evals vs production monitoring (complementary)**: Eval sets encode what you already believe matters; production surfaces **implicit signals** (regenerate vs thumbs-down, tool errors, silent drop-offs) and novel failure modes. High-throughput systems need monitoring to prioritize which traces to inspect; discoveries feed new eval slices—neither alone covers the space.

- **Semantic diffusion (“evals,” “agents”)**: The same word means different things (benchmarks vs PM-written suites vs expert annotations). Align on the underlying goal: an **actionable feedback loop** suited to the product.

- **Continuous Calibration, Continuous Development (CCCD)**: An AI-native lifecycle (they relate it to CI/CD): scope capability, curate starter datasets, define **evaluation metrics** (dimensions, not vibes alone), deploy, then **calibrate** against emerging real-world patterns—while stepping through versions that move along **agency up / control down** (e.g., support: suggest → draft → act with expanding tools).

- **When to advance a stage**: Move forward when calibration cadence shows **fewer new data distribution surprises**—but expect resets (model upgrades, shifting user behavior).

- **Pain is the new moat (individual + company)**: Advantage comes from enduring the messy iteration to learn non‑negotiables and tradeoffs in a field with few textbooks—not from being first with a flashy demo.

## Top Insights (Timeless)

1. **Design for probabilistic behavior**: Treat the LLM as a non-deterministic dependency; plan for monitoring, guardrails, and staged rollout—not only “happy path” UX.

2. **Earn autonomy in layers**: Customer support can progress from AI **suggestions** to human-reviewed **drafts** to broader actions (e.g., refunds)—each stage builds logs that fuel the next.

3. **Keep UX trust while learning**: Early versions should avoid eroding customer trust while still capturing what humans do so you can improve (human-in-the-loop is a data flywheel).

4. **Reliability is the enterprise bottleneck**: Citing a Berkeley/Databricks-related survey discussed in-episode, a large majority of enterprises cite **reliability** as the top blocker to customer-facing AI—explaining why many deployments stay in “productivity” (lower autonomy) modes.

5. **Leaders must re‑learn publicly**: Top-down skepticism or magical thinking both break execution; leaders who schedule real learning time and admit “I might be wrong” set the pace for the org.

6. **Experts must feel safe**: If SMEs fear replacement, they won’t collaborate—and AI quality depends on their judgment of “correct” behavior.

7. **Workflow literacy beats “one-click agent” marketing**: Messy taxonomies and undocumented rules dominate real enterprises; expect **months** of pipeline work to replace critical workflows even with strong data foundations.

8. **Don’t let “evals” become theater**: Benchmark leaderboards are not your product eval; align language and invest in loops that match risk.

9. **Multi-agent hype, supervisor realism**: Orchestrated supervisor/sub-agent patterns can work; unconstrained peer-to-peer agent chatter is hard to control—especially customer-facing.

10. **Taste and judgment scale when execution gets cheap**: As implementation commodifies, differentiation shifts to problem selection, design, end-to-end ownership, and willingness to persist through iteration.

## AI & The Changing PM Role

- PMs, engineers, and data folks increasingly share **one feedback loop** (e.g., reviewing **agent traces** together) instead of siloed optimizations—collaboration tightens materially.
- PMs contribute heavily to **aligning expected behavior** early (starter datasets / scenarios) and to deciding **how** autonomy should be constrained by topic, risk, or number of actions.
- “Writing evals” may mean anything from scenario lists to review rubrics—not always production LLM judges; PMs should clarify **metrics** and **signals**, not just ship prompts.
- Ash emphasizes that strong AI PM/engineer time is often spent **understanding workflows and data**, not building the flashiest model stack.

## Notable Interview Questions Lenny Asked

- “What are you seeing on the ground within companies trying to build AI products? What’s going well? What’s not going well?”
- “What are the two very big differences between building AI products and non-AI products?”
- “What other patterns and ways of working do you see in companies that do this well—and what are the most common pitfalls?”
- “What’s your take on evals? How far does that take people?”
- “What can you share on how the Codex/Kodex team approaches evals?” (wording per transcript)
- “What is overhyped in AI right now—and what is underhyped?”
- “From a product point of view, what do you think the next year of AI is going to look like by end of 2026?”
- “If someone wants to get better at building AI products, what one or two skills should they lean into?”

## Best Quotes

> “Most people tend to ignore the non-determinism. You don't know how the user might behave with your product, and you also don't know how the LLM might respond to that.”

> “Every time you hand over decision-making capabilities to agentic systems, you're kind of relinquishing some amount of control on your end.”

> “When you start small, it forces you to think about what is the problem that I'm going to solve… one easy, slippery slope is to keep thinking about complexities of the solution and forget the problem that you're trying to solve.”

> “It's not about being the first company to have an agent among your competitors. It's about have you built the right flywheels in place so that you can improve over time.”

> “Leaders have to get back to being hands-on… you must be comfortable with the fact that your intuitions might not be right. And you probably are the dumbest person in the room and you want to learn from everyone.”

> “Pain is the new moat.”

> “Be obsessed with your customers. Be obsessed with the problem. AI is just a tool… 80% of so called AI engineers, AIPMs spend their time actually understanding their workflows very well.”

## Interview Prep Takeaways

- Use **non-determinism + agency/control** as a crisp answer for “How is AI product development different?”
- Tell a **staged rollout story** (suggest → review → automate) for reliability, risk reduction, and learning velocity.
- When asked about **evals**, articulate a **dual-loop**: offline/holdout checks for known requirements + production monitoring for unknown failure modes and implicit signals.
- For org questions, cite the **leader learning + psychological safety for SMEs + workflow depth** triangle.
- For “moats,” discuss **organizational learning** and iteration cost honestly versus feature-first narratives.

## Related Themes

- “staged autonomy and human-in-the-loop”
- “evals vs production monitoring”
- “enterprise data messiness and taxonomies”
- “AI transformation and leadership buy-in”
- “coding agents and developer workflows”
- “multi-agent orchestration vs chaos”
