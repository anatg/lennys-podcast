# PM Interview Flashcards

Single-file deck derived from **`study-guide/themes/`** (the “book” chapters) and cross-checked against patterns in **`study-guide/episodes/`**. Use it as: read **Q** aloud → answer → reveal **Framework** / **Examples** / **Open with**.

**Visual deck:** open [`index.html`](index.html) in a browser (flip / filter / shuffle). After editing this file, run `python3 scripts/build_flashcard_app.py` from the repo root to refresh `index.html`.

---

## How to practice

- **90-second answers**: opener (one line) → framework (30s) → story (40s) → tradeoff/risk (20s).
- **One story, many questions**: mine your own wins; map each card’s “Examples” to *your* ship, not the guests’.
- **Deep links**: each category aligns with a book chapter—reread that chapter when a card feels thin.

| Category | Primary chapter |
|----------|------------------|
| Prioritization & roadmap | `themes/02_product_strategy.md` |
| Product sense / design | `themes/04_discovery_and_insight.md` |
| Strategy & vision | `themes/02_product_strategy.md` |
| Growth | `themes/03_growth_and_plg.md` |
| Metrics & success | `themes/05_metrics_and_data.md` |
| Execution & eng/design | `themes/01_the_pm_role.md`, `themes/06_org_design_and_leadership.md` |
| Influence / leadership | `themes/01_the_pm_role.md`, `themes/06_org_design_and_leadership.md` |
| Hiring & team | `themes/07_hiring_and_developing_pms.md` |
| Career & failure | `themes/12_career.md` |
| AI & future of product | `themes/13_ai_and_future_of_product.md` |

---

## Prioritization & roadmap

### Card 1: “How do you prioritize?”
**Q:** We have more ideas than capacity. How do you decide what ships first?  
**Framework:** Stack decisions: **strategy kernel** (diagnosis → guiding policy → coherent actions per Rumelt) → **outcome vs output** (empowered teams solve problems, not feature lists per Cagan) → **crux** (one hardest barrier; focus power there).  
**Examples:** (1) Cut roadmap items that don’t connect to company strategy stack (Ravi Mehta’s stack in Ch.2). (2) Reframe “priorities” as bets with explicit **non-goals**. (3) Use **input metrics** you control vs vanity outputs (Ch.5 / Carr).  
**Open with:** “I separate *strategy* from *backlog*—priorities are bets on a diagnosis, not whoever argued loudest.”

### Card 2: “Say no to a CEO”
**Q:** The CEO wants a feature that doesn’t align with strategy. What do you do?  
**Framework:** **Three realities** (intent / behavior / impact) + **viability + value risk** (Cagan’s frame): translate the request into customer/business risk tests. Offer cheaper validation paths before full build.  
**Examples:** (1) Propose a **time-boxed discovery** slice with success criteria. (2) Show opportunity cost against the crux initiative. (3) Offer a **scope ladder** (MVP vs full).  
**Open with:** “I’d align on what success would need to be true for both of us—then pick the smallest experiment that tests that.”

### Card 3: “Roadmap for the next quarter”
**Q:** Walk me through how you’d build a quarterly roadmap.  
**Framework:** **Mission → company strategy → product strategy → goals → roadmap** (avoid skipping layers). Mix **outcomes** with **inputs** (Ch.5). Leave capacity for unknowns.  
**Examples:** (1) Tie each theme to a **North Star** + leading inputs. (2) Book **unplanned buffer** for debt/legal surprises. (3) Publish **non-goals** in the doc header.  
**Open with:** “Roadmaps are communication tools for bets—mine start from strategy layers, not Jira tickets.”

### Card 4: “Technical debt vs features”
**Q:** Eng wants a quarter of debt paydown; sales wants features.  
**Framework:** Reframe as **risk**: value/usability/feasibility/viability. Debt is feasibility + velocity risk; connect it to revenue or incident risk in dollars or SLAs.  
**Examples:** (1) Pair each feature with a **quality gate**. (2) Quantify **incident / dev-hours tax**. (3) Alternate **tollgates**—no new surface area if SLO red.  
**Open with:** “I’d translate debt into forecastable delivery and reliability risk, then trade at the leadership level—not in a hallway fight.”

### Card 5: “Competing stakeholders”
**Q:** Sales, legal, and design disagree on a launch.  
**Framework:** PM owns **value + viability**; bring constraints into discovery **early** (Cagan’s sacred responsibilities). Use explicit **decision logs** and escalation paths.  
**Examples:** (1) Joint **PR/FAQ**-style narrative to expose conflicts. (2) **Pre-mortem** for launch failure modes. (3) **RACI** for who decides vs consults.  
**Open with:** “My job is to make tradeoffs explicit with data and risk, not to absorb every function’s max wish.”

### Card 6: “Kill a project”
**Q:** When do you stop investing in a live initiative?  
**Framework:** **Kill criteria** + **pre-mortem** (Duke-style discipline, Ch.12) paired with **hypothesis clarity**—is the core bet disproved, or is execution just hard (Weaver tension in Ch.12)?  
**Examples:** (1) Define **leading indicators** that should move by date X. (2) Separate “no traction” from “wrong channel.” (3) Sunset with **customer migration** plan.  
**Open with:** “I’d separate ‘hard execution’ from ‘disproven thesis’—kill criteria should be set when we start, not when we’re tired.”

---

## Product sense / design (“Design X for Y”)

### Card 1: “Design a grocery app for seniors”
**Q:** Design an app for seniors buying groceries.  
**Framework:** **Job map** + **constraints** (vision, motor, trust, payment) → **progressive disclosure** → **risk reversal** (support, refunds). State assumptions; pick a narrow beachhead day-one.  
**Examples:** (1) Default flows: **large type**, **one primary CTA**, **human help**. (2) Validate with **task completion**, not preference surveys. (3) Instrument **drop-off by step**.  
**Open with:** “I’d anchor on the job—get weekly staples reliably—then design for fear, not just efficiency.”

### Card 2: “What is good product sense?”
**Q:** How do you define product sense?  
**Framework:** Pattern recognition across **user pain**, **business model**, and **feasibility**; ability to predict **second-order effects** of a change.  
**Examples:** (1) “What breaks at 10× scale?” (2) “What metric games this?” (3) “What’s the **adjacent user** we’re not serving?” (Ch.4 themes).  
**Open with:** “Product sense is compressed causality—knowing which levers actually move outcomes for *this* user and model.”

### Card 3: “Improve onboarding”
**Q:** Activation is weak. Where do you start?  
**Framework:** **Activation is highest-leverage** once PMF exists (Ch.3); map **time-to-value**; remove steps that don’t correlate with retention.  
**Examples:** (1) **Session replay + funnel** by cohort. (2) **Remove** optional fields. (3) A/B **first-run checklist** vs empty state.  
**Open with:** “I’d map time-to-first-success, then cut anything that doesn’t predict retained users.”

### Card 4: “Delight vs complexity”
**Q:** Users ask for power features; the product is already complex.  
**Framework:** **DHM** (Delight, Hard-to-copy, Margin-enhancing—Ch.2/3)—delight without hard-to-copy or margin is fragile.  
**Examples:** (1) **Progressive complexity** for power users. (2) **Defaults + advanced**. (3) Measure **support tickets per feature**.  
**Open with:** “Delight that isn’t hard to copy or margin-positive becomes debt—I’d price the complexity in those terms.”

### Card 5: “Accessibility / inclusion”
**Q:** How do you prioritize accessibility?  
**Framework:** Risk (**viability**: legal), growth (**adjacent users**), and quality (**usability**). Tie to outcomes, not virtue.  
**Examples:** (1) **WCAG** as release gate for surfaces. (2) **Dogfood** with assistive tech. (3) Track **task success** with a11y cohorts.  
**Open with:** “I treat accessibility as a quality and risk requirement with measurable task success, not a backlog nice-to-have.”

### Card 6: “Innovation vs iteration”
**Q:** Should we bet big or iterate small?  
**Framework:** Match to **strategy stage** and **reversibility**; use **crux** to decide if a step-change bet is warranted.  
**Examples:** (1) **Optionality** via modular architecture. (2) **Platform-ize** only after 3rd use case. (3) **Kill** small bets that crowd the crux.  
**Open with:** “Innovation without a diagnosis of the crux is theater—I’d size the bet to what the strategy moment requires.”

---

## Strategy & vision

### Card 1: “What is strategy in one minute?”
**Q:** Define strategy vs goals vs roadmap.  
**Framework:** Rumelt: **diagnosis + guiding policy + coherent actions**. Martin: integrated choices that **compel customer behavior**. Helmer: **power** needs benefit + barrier.  
**Examples:** (1) “10 goals” is not strategy. (2) Roadmap without **where to play / how to win** is wishful. (3) Moats need **barriers**, not slogans.  
**Open with:** “Strategy is the smallest set of coherent choices that address the hardest barrier to winning.”

### Card 2: “Where to play / how to win”
**Q:** We’re considering three markets. How do you choose?  
**Framework:** Martin’s **cascade** + Moore **beachhead**: pick a pond you can **dominate** before expanding.  
**Examples:** (1) **30–50% share** plausible in 24 months test. (2) **Reference customers** in segment (Ch.1/4 B2B patterns). (3) Explicit **excluded segments**.  
**Open with:** “I’d pick the smallest market we can credibly win and earn the right to expand—concentration beats spray.”

### Card 3: “Competitive response”
**Q:** A competitor copied our core feature.  
**Framework:** Ask if you had real **power** (Helmer) or **UX-only delight**. Respond with **hard-to-copy** investments (data, workflow lock-in, ecosystem).  
**Examples:** (1) **Network / data flywheel** audit. (2) **Switching costs** via integrations. (3) **Narrative**: category story only you can tell (Ch.11).  
**Open with:** “If a copy killed us, we didn’t have a barrier—I’d invest in what compounds, not feature parity.”

### Card 4: “Vision vs execution”
**Q:** Founders want a 10-year vision; teams want clarity this month.  
**Framework:** Vision sets **constraints and taste**; strategy chooses **bets**; roadmaps communicate **sequencing**. Don’t conflate layers (Mehta stack).  
**Examples:** (1) **Quarterly narrative** tied to vision. (2) **Thematic OKRs** not task lists. (3) **Demo rhythm** to prove progress.  
**Open with:** “Vision tells us what world we’re building; strategy picks the next hill; the roadmap is how we take that hill without lying about dependencies.”

### Card 5: “Platform strategy”
**Q:** When do you build a platform vs point solutions?  
**Framework:** Third-use-case rule (common pattern): platformize when the same primitive repeats; else ship vertical slices faster.  
**Examples:** (1) **API adoption** metrics before “platform OKRs.” (2) **Developer time saved** as North Star for platform. (3) Guardrails on **breaking changes**.  
**Open with:** “I platformize when multiple teams would ship the same primitive anyway—otherwise it’s resume-driven architecture.”

### Card 6: “Pricing / packaging”
**Q:** How does strategy connect to pricing?  
**Framework:** Pricing is a **choice** in Martin’s cascade; it signals **where to play** and shapes **unit economics** and sales motion (Ch.9).  
**Examples:** (1) **Value metric** aligned to customer outcome. (2) **Good/better/best** to segment willingness to pay. (3) Test **packaging** before headline price.  
**Open with:** “Pricing is part of strategy—it’s how we capture value from the customer behavior we’re trying to compel.”

---

## Growth

### Card 1: “Growth is slowing—hire growth?”
**Q:** Growth slowed; should we hire a growth team?  
**Framework:** Elena Verna pattern (Ch.3): growth **amplifies** PMF; it rarely **fixes** core product or GTM strategy. Sequence: **PMF → activation → loops → acquisition**.  
**Examples:** (1) **Retention cohorts** before spend. (2) **PMF survey** filter. (3) Map **loops**, not funnel only.  
**Open with:** “If retention is weak, a growth team optimizes acquisition of churn—I’d prove PMF and activation first.”

### Card 2: “Build a growth model”
**Q:** How do you model growth for a B2B SaaS product?  
**Framework:** **Loops** (action → reaction) + identify **constraint**; engines vs fuel (race car framework in Ch.3).  
**Examples:** (1) **Viral / content / product / sales** loops map. (2) Instrument **activation → paid** conversion. (3) Find **bottleneck** stage quarterly.  
**Open with:** “I’d draw the loops, find the constraint, and only then pick tactics—otherwise we’re spraying fuel.”

### Card 3: “PLG vs sales”
**Q:** Should we be PLG or sales-led?  
**Framework:** Modern answer is **hybrid** (Ch.3/9): PLG for activation/expansion; sales for complexity, procurement, enterprise wedge.  
**Examples:** (1) **PQL** triggers for sales assist. (2) **Self-serve** first for ICP SMB. (3) **Enterprise SKUs** with services.  
**Open with:** “It’s rarely either/or—the question is where self-serve reduces friction and where humans close risk.”

### Card 4: “Referral program”
**Q:** Should we add referrals?  
**Framework:** Referrals are a **loop**, not a banner; they need **motivated senders + valuable recipients** + measurement of **quality** (Ch.3 distribution notes).  
**Examples:** (1) **Double-sided** incentives with fraud controls. (2) Referral **quality** vs volume. (3) Trigger at **moment of delight**.  
**Open with:** “Referrals work when the product moment naturally invites sharing—I’d validate quality before incentives.”

### Card 5: “International expansion”
**Q:** How do you approach international growth?  
**Framework:** Treat as **new beachhead**: localization, payments, compliance, and often **different loops**; don’t assume US PMF transfers.  
**Examples:** (1) **Country-level** retention parity goal. (2) **Local power users** interviews. (3) **Partners** for trust-heavy markets.  
**Open with:** “International is a strategy problem, not a translation problem—I’d pick a beachhead and prove retention there.”

### Card 6: “Viral loop design”
**Q:** What makes a viral loop actually work?  
**Framework:** **K-factor math** is necessary but insufficient—**retention of inviter and invitee** and **contextual fit** dominate (Ch.3 Instagram / consumer patterns).  
**Examples:** (1) **Recipient value** in first session. (2) **Frictionless** invite path. (3) **Social proof** surfaces.  
**Open with:** “Viral loops fail when invites feel spammy—I optimize recipient value first, inviter incentives second.”

---

## Metrics & success definition

### Card 1: “Define success for a new feature”
**Q:** How do you define success before shipping?  
**Framework:** **Outcome + input metrics** (Carr, Ch.5); avoid composite metrics; pre-register **OEC** for experiments when possible (Kohavi culture).  
**Examples:** (1) **Guardrail metrics** (latency, support load). (2) **Primary** customer outcome. (3) **Leading** input drivers.  
**Open with:** “I’d pair one customer-outcome primary with guardrails and leading inputs we control—no vague ‘engagement up.’”

### Card 2: “North Star metric”
**Q:** What’s a good North Star?  
**Framework:** Ellis criteria (Ch.5): reflects **customer value**, can grow, often **frequency**-linked; revenue is a **consequence**, not the star.  
**Examples:** (1) **Nights booked** vs bookings count. (2) **Successful tasks completed** vs clicks. (3) Align sub-metrics in a **tree**.  
**Open with:** “A North Star should track delivered value, not internal activity—otherwise we optimize theater.”

### Card 3: “Experiment says neutral”
**Q:** Your A/B test is flat. What now?  
**Framework:** **Segment** results; check **power**, **guardrails**, and whether the hypothesis was **value** vs **local max** (Ch.5 experimentation culture).  
**Examples:** (1) Slice by **new vs power** users. (2) **Qual** on “why flat.” (3) Try **step-function** change, not tweak.  
**Open with:** “Flat often means wrong segment, underpowered test, or small change—I’d diagnose which before shipping.”

### Card 4: “Goodhart / metric gaming”
**Q:** Teams are gaming the metric. What do you do?  
**Framework:** **Goodhart’s law**—add **guardrails**, **qualitative audits**, and **distributional** views (DoorDash lesson in Ch.5).  
**Examples:** (1) Pair **quality sampling** with volume KPIs. (2) **Fail-state** metrics. (3) Rotate **review** ownership.  
**Open with:** “Any single number will be gamed—I’d redesign incentives around a small bundle of hard-to-game signals.”

### Card 5: “Leading vs lagging”
**Q:** Board wants revenue; team needs actionable goals.  
**Framework:** Translate revenue into **inputs** you control (selection, speed, reliability—Amazon flywheel story, Ch.5).  
**Examples:** (1) **Conversion inputs** per funnel stage. (2) **Sales pipeline** health for B2B. (3) **Unit economics** bridge.  
**Open with:** “Revenue is a lagging scoreboard—I’d commit the org to customer inputs that historically move it.”

### Card 6: “AI / engagement metrics”
**Q:** How do you measure an AI feature?  
**Framework:** Blend **offline checks** for known failures with **production signals** (implicit + explicit) and staged autonomy (Ch.13 + Reganti/Badam episode).  
**Examples:** (1) **Task success rate** by scenario. (2) **Human edit distance** on drafts. (3) **Escalation rate** to humans.  
**Open with:** “AI features need probabilistic measurement—paired eval slices and live trace review, not one dashboard.”

---

## Execution & working with eng/design

### Card 1: “PM vs eng conflict”
**Q:** Engineering says your spec is wrong / infeasible.  
**Framework:** Pull engineers into **problem discovery** early; PM owns **value + viability**, eng owns **feasibility**—collaborate on tradeoffs (Cagan, Ch.1).  
**Examples:** (1) **Tech spike** time-boxed. (2) **Cut scope** ladder. (3) Joint **risk register**.  
**Open with:** “If they’re pushing back, I probably failed to bring them into the problem early—I’d reset to constraints, not argue the spec.”

### Card 2: “Working with design”
**Q:** How do you partner with design well?  
**Framework:** Shared ownership of **usability risk** + **customer access**; avoid design-as-service org (Ch.1 Chesky nuance).  
**Examples:** (1) **Joint research** sessions. (2) **Pair** on prototypes before PRD freeze. (3) **Design crits** with decision owner named.  
**Open with:** “Great partnerships pair on customer evidence and tradeoffs—design owns usability risk with me, not for me.”

### Card 3: “Estimates always slip”
**Q:** Deadlines slip every sprint.  
**Framework:** Separate **commitment** from **forecast**; reduce WIP; shrink batch size; surface dependencies; protect **discovery** time (Ch.6 execution themes).  
**Examples:** (1) **Rolling planning** with explicit buffers. (2) **Definition of ready**. (3) **Scope poker** with leadership.  
**Open with:** “Chronic slips usually mean hidden dependency or discovery debt—I’d make uncertainty visible and cut scope earlier.”

### Card 4: “Bugs in launch week”
**Q:** Launch is next week; bug backlog is huge.  
**Framework:** **Severity × reach** triage; explicit **launch criteria**; hotfix plan; communicate risk to stakeholders with options.  
**Examples:** (1) **S0/S1** definitions. (2) **Dark launch** / feature flag. (3) **Rollback** runbook.  
**Open with:** “Launch decisions are risk decisions—I’d quantify who’s harmed, how many, and whether we can roll back.”

### Card 5: “Agile / Scrum frustrations”
**Q:** Scrum feels bureaucratic.  
**Framework:** Scrum is a delivery skeleton; **product management** is broader (Perri critique in Ch.1)—keep ceremonies that reduce risk, drop theater.  
**Examples:** (1) **Outcome-based** sprint goals. (2) **Discovery cadence** outside sprint noise. (3) **Quarterly** strategy refresh.  
**Open with:** “Ceremonies should serve learning velocity—if they don’t, I’d simplify the process, not blame agile.”

### Card 6: “Remote / async collaboration”
**Q:** How do you run product in a remote org?  
**Framework:** **Write decisions**, **clear DRI**, **async artifacts** (PRDs, RFCs), synchronous for **high-bandwidth alignment** only.  
**Examples:** (1) **Decision log** in Slack/docs. (2) **Loom** for context. (3) **Office hours** for stakeholders.  
**Open with:** “Remote rewards written clarity and explicit ownership—I invest in artifacts so meetings are rare and decisive.”

---

## Leadership without authority / influence

### Card 1: “No authority—how do you lead?”
**Q:** How do you influence without being the boss?  
**Framework:** **Creator not facilitator** + **three sacred relationships** (customers, eng, stakeholders) + **trust as currency** (Ch.1).  
**Examples:** (1) Bring **customer clip** to debate. (2) **Pre-brief** allies before forums. (3) **Document** decisions crisply.  
**Open with:** “Influence comes from evidence and earned trust—I sell outcomes, not opinions.”

### Card 2: “Disagree with your manager”
**Q:** You disagree with your manager on direction.  
**Framework:** **Impact > optics** (Doshi) + **three realities** (Robin, Ch.12) + propose **cheap tests** instead of abstract debate.  
**Examples:** (1) **Write a one-pager** with options and recommendation. (2) Ask for **decision criteria**. (3) Commit or escalate once.  
**Open with:** “I’d translate disagreement into a decision memo with a test plan—disagree and commit beats passive resistance.”

### Card 3: “Cross-functional politics”
**Q:** Another team is blocking you politically.  
**Framework:** Map **incentives**; build **coalitions**; make their success metric visible (Pfeffer visibility lessons, Ch.12—use ethically).  
**Examples:** (1) **Shared OKR** slice. (2) **Exec sponsor** alignment. (3) **Trade** something they value.  
**Open with:** “Blockers are usually incentive misalignment—I’d find the win-win metric, not win the argument.”

### Card 4: “Crisis / incident”
**Q:** Major outage—what’s your role as PM?  
**Framework:** **Command clarity**: customer comms, scope triage, stakeholder updates; defer blame; protect eng focus; define **recovery success**.  
**Examples:** (1) **Status page** messaging. (2) **Customer outreach** for top accounts. (3) **Postmortem** with action owners.  
**Open with:** “In incidents I own narrative and customer impact while eng owns mitigation—I remove noise.”

### Card 5: “Stakeholder says ‘just ship it’”
**Q:** Legal/compliance is slow; business pressures ship.  
**Framework:** Reframe as **viability risk**; offer phased rollout, **beta cohort**, monitoring; escalate with **explicit risk acceptance** doc.  
**Examples:** (1) **Feature flag** + limited population. (2) **Legal review** checklist upfront next time. (3) **Rollback** plan.  
**Open with:** “I’d make risk binary and visible—either we accept it with signatures or we scope the release.”

### Card 6: “Motivate a tired team”
**Q:** Team is burned out after a crunch.  
**Framework:** Acknowledge reality; reduce WIP; protect **recovery**; align on meaningful **customer outcome** (inner work themes Ch.12 intersect execution).  
**Examples:** (1) **Cancel** low-value meetings. (2) **Celebrate** learning, not heroics. (3) **Repay** debt sprint.  
**Open with:** “Motivation returns when people see progress on meaningful work—I’d cut scope and protect recovery time.”

---

## Hiring & team building

### Card 1: “What do you look for in PM hires?”
**Q:** What traits matter most when hiring PMs?  
**Framework:** Blend **customer insight**, **strategy**, **execution**, **leadership** competencies (Mehta model in Ch.1/7); hire for **level-appropriate aperture**.  
**Examples:** (1) **Written case** + debrief quality. (2) **Reference depth** on influence. (3) **Role-play** stakeholder.  
**Open with:** “I hire for judgment in ambiguity and evidence of cross-functional traction—skills vary by level.”

### Card 2: “PM interview question you ask”
**Q:** What’s your favorite interview question?  
**Framework:** Pick questions that reveal **thinking process**: tradeoffs, metrics, customer discovery, conflict resolution—avoid trivia.  
**Examples:** (1) “Tell me about a **wrong** decision—what signal did you miss?” (2) “How did you **define success**?” (3) “How did you **say no**?”  
**Open with:** “I optimize for how they structure ambiguity—decision quality over polish.”

### Card 3: “Underperforming PM”
**Q:** A PM on your team is struggling.  
**Framework:** Clarify expectations; **SBI**-style feedback; **coaching plan** with measurable behaviors; document timeline (Ch.7 / management canon in themes).  
**Examples:** (1) Pair on **customer calls**. (2) **Written** spec reviews. (3) **Pre-firing** clarity if no change.  
**Open with:** “I’d treat it like a product bug—diagnose which competency gap, then coach with measurable milestones.”

### Card 4: “Team structure”
**Q:** Pods vs platforms vs components—how do you choose?  
**Framework:** Align structure to **strategy** (Conway’s law); **single-threaded** ownership for big bets where possible (Ch.6).  
**Examples:** (1) **Platform** when reuse is real. (2) **Pods** when speed to customer matters. (3) Avoid **matrix** without clear DRI.  
**Open with:** “Team topology should mirror what we need to learn fastest—structure is a strategy artifact.”

### Card 5: “Diversity & hiring pipeline”
**Q:** How do you build a diverse PM pipeline?  
**Framework:** Fix **top of funnel**, **rubrics**, **panel balance**, and **bias checks** in cases; measure conversion by stage.  
**Examples:** (1) **Blind** resume review where possible. (2) **Structured** questions. (3) **Sponsorship** for internal candidates.  
**Open with:** “Diversity is a system design problem in hiring—I’d instrument the funnel and standardize evaluation.”

### Card 6: “Scaling PM org from 3 to 30”
**Q:** How does PM org design change as you scale?  
**Framework:** Introduce **levels**, **craft ownership**, **principles**, and **lightweight processes**; avoid premature bureaucracy (Ch.6/7).  
**Examples:** (1) **PM principles** doc. (2) **Office hours** with leadership. (3) **Communities of practice** for domains.  
**Open with:** “Scaling is trading informal trust for explicit standards—I’d add the minimum process that preserves speed.”

---

## Career & failure

### Card 1: “Tell me about a failure”
**Q:** Describe a significant failure and what you learned.  
**Framework:** **STAR** with emphasis on **learning loop**: hypothesis → signal missed → behavior change. Avoid blame-only stories.  
**Examples:** (1) Shipped feature with **flat experiment**—learned wrong metric. (2) **Mis-scoped** platform—learned discovery gap. (3) **Conflict** mishandled—learned feedback timing.  
**Open with:** “I’ll share a failure where I misread a customer signal—and the specific habit I changed afterward.”

### Card 2: “Why leave your last job?”
**Q:** Why are you looking to move?  
**Framework:** Honest **inner scorecard** framing (Ch.12 themes) + growth vector; never trash-talk; show **agency**.  
**Examples:** (1) Seeking **scope** step-up. (2) Seeking **domain** fit. (3) Seeking **culture** aligned to learning.  
**Open with:** “I’m optimizing for X in my next chapter—this role maps because…”

### Card 3: “Career goals for 5 years”
**Q:** Where do you see yourself in five years?  
**Framework:** Connect to **competency depth** and **impact aperture**—avoid title-only answers; show **self-awareness** (Ch.12).  
**Examples:** (1) Lead **0→1** then **scale**. (2) Deepen **AI product** craft. (3) Build **org capability** as manager.  
**Open with:** “I’m building toward owning ambiguous problem spaces end-to-end—here’s the skill I’m deepening next…”

### Card 4: “Handling conflict with a peer”
**Q:** Tell me about conflict with a cross-functional peer.  
**Framework:** **Three realities** + focus on **shared goal** + specific behavior change requests (Ch.12 Robin themes).  
**Examples:** (1) Misaligned **success metrics** fixed via joint OKR. (2) **Design conflict** resolved with user study. (3) **Timeline** conflict resolved with scope ladder.  
**Open with:** “I separate intent from impact, then align incentives—most ‘people problems’ are goal problems.”

### Card 5: “Imposter syndrome / confidence”
**Q:** When have you doubted yourself?  
**Framework:** Reframe as **imposter phenomenon** + focus on **inputs you control**; growth mindset without toxic positivity (Ch.12 / Norton themes).  
**Examples:** (1) First **exec presentation** prep process. (2) **Mentor** feedback loop. (3) **Small wins** log.  
**Open with:** “I channel doubt into preparation and external validation with customers—feelings aren’t facts about competence.”

### Card 6: “Work-life balance”
**Q:** How do you handle intensity?  
**Framework:** **Energy management** + boundaries + sustainable pace; tie to **team outcomes** (Ch.12 nervous system / burnout themes).  
**Examples:** (1) **Calendar** blocks for deep work. (2) **Delegate** via clearer specs. (3) **Say no** to low-LNO tasks (Doshi).  
**Open with:** “Sustainable pace is a performance strategy—I protect deep work blocks and kill low-leverage meetings.”

---

## AI & the future of product

### Card 1: “How is building AI products different?”
**Q:** What’s different about AI-native product development?  
**Framework:** **Non-determinism** (user language × model variance) + **agency–control tradeoff**; ship **staged autonomy** with eval + monitoring loops (Ch.13).  
**Examples:** (1) Support: **suggest → draft → act**. (2) **Trace review** rituals with eng. (3) **Implicit signals** in prod.  
**Open with:** “It’s probabilistic software—you design for calibration, not for a fixed spec path.”

### Card 2: “PM job in 3 years with AI?”
**Q:** Will PMs exist / how does the role change?  
**Framework:** Execution commoditizes; **judgment, taste, problem selection, and cross-functional narrative** compound; more **builders** across disciplines (Tomer Cohen 2.0 / Zevi / Mohan threads in Ch.13).  
**Examples:** (1) PM ships **prototype** with agents + PR. (2) PM owns **eval scenarios** + risk tiers. (3) PM drives **workflow mapping** with SMEs.  
**Open with:** “The job shifts from writing tickets to owning outcomes and risk in a probabilistic stack—I’m leaning into that.”

### Card 3: “Evals: necessary or overrated?”
**Q:** How do you think about evals for LLM features?  
**Framework:** Avoid false dichotomy: **offline eval slices** + **production monitoring** + human review for high-stakes paths; define terms precisely (Ch.13 semantic diffusion).  
**Examples:** (1) **Golden sets** for regressions. (2) **Thumbs down + regenerate** as signals. (3) **Human edit distance** on drafts.  
**Open with:** “Evals are one instrument in a feedback orchestra—pair them with live signals or you’ll miss novel failures.”

### Card 4: “AI for productivity—how you use it?”
**Q:** How do you personally use AI tools as a PM?  
**Framework:** Treat as **thought partner** with tight context loops (Wes Kao 2.0 pattern): draft, critique, iterate; apply delegation rigor.  
**Examples:** (1) **Memo outlines** + devil’s advocate prompts. (2) **Meeting summaries** to decisions. (3) **SQL/exploratory** assistance with verification.  
**Open with:** “I use AI to shorten iteration time on writing and analysis—but I own verification and customer truth.”

### Card 5: “Responsible AI / risk”
**Q:** What risks worry you most with AI features?  
**Framework:** Wrong actions at scale, **privacy**, **security** (prompt injection noted in AI episodes), **bias**, and **trust erosion**—mitigate with scope, monitoring, and human gates (Ch.13).  
**Examples:** (1) **High-risk** actions require human approval. (2) **Red-team** prompts. (3) **Customer comms** on limitations.  
**Open with:** “Risk scales with autonomy—I match guardrails to what the agent can do, not to what the demo showed.”

### Card 6: “Org adoption of AI”
**Q:** How would you help a company adopt AI responsibly?  
**Framework:** Leader **hands-on learning**, SME **psychological safety**, and **workflow-first** automation; avoid FOMO buying (Ch.13 triangle).  
**Examples:** (1) **Training** + internal guild. (2) **Pilot** in ops before customer-facing. (3) **Executive** office hours on demos.  
**Open with:** “Adoption fails from fear and magical thinking—I’d pair education with narrow, measurable pilots tied to workflows.”

---

## Appendix: expand this deck

- Add cards from **`## Notable Interview Questions Lenny Asked`** in episodes you personally love—turn each into your own answer skeleton.  
- When an answer feels thin, reread the matching **`study-guide/themes/*.md`** chapter and paste **one** new story from your résumé beside the guest examples.
