# Ben Williams — VP of Product (Snyk)

## Guest Profile
- **Name**: Ben Williams
- **Role/Company**: VP of Product at Snyk (developer security company, $8.6B valuation, 2,000+ customers, 1,300 employees, ~70 in product org); formerly VP Product at CloudBees; leadership roles at IBM Rational software
- **Background**: Built Snyk's growth organization from scratch after joining as its first dedicated growth leader. Computer science background, career rooted in developer tooling. Deep expertise in PLG, growth loops, product-led sales, and structuring growth teams in B2B developer-focused companies.

## Tags
`Growth` `PLG` `Developer Tools` `B2B` `Freemium` `Org Design` `Experimentation` `Data` `Loops` `Product-Led Sales`

## TL;DR
Snyk's growth story is a textbook PLG case study with critical lessons about what doesn't work: self-serve monetization failed before breadth, governance features, and sales were added. Ben's three-pillar growth team framework (people/process, strategy, data) and his growth loop model operationalize what most companies try to build ad-hoc. His activation metric design process and learning culture practices are directly applicable to any growth-stage B2B team.

## Core Frameworks & Mental Models

- **Narrow, Deep, Community-First Launch Strategy**: Snyk's first users came from hyper-focus on a single persona (Node.js developers using open source components), a single compelling hook ("Do you have known vulnerabilities in your code? So now you know."), and deep community presence at in-person conferences (Velocity in Amsterdam). The depth-first approach validated the solution before expanding to adjacent languages and ecosystems. A JavaScript developer won't care if you support Golang, but will absolutely care if automated package upgrades aren't available for their ecosystem. NPM had 200,000 packages downloaded 2.5 billion times/month — narrow enough to build a compelling solution quickly, wide enough to be viable.

- **Snyk's Growth Loop Architecture**:
  1. **GitHub PR Loop** (company-generated, company-distributed): Developer signs up → connects GitHub → Snyk scans code → creates branded fix PRs → other devs in the repo see PRs → some click through → sign up → connect their own repos → loop continues. First-of-its-kind integration. Key: Snyk controls the content (educates users about the vulnerability, branded, CTA to sign up). Functions as both an acquisition loop and an engagement loop simultaneously.
  2. **Snyk Advisor (programmatic SEO)**: Sidecar product indexing all open source package managers with health scores (security vulnerability data + maintenance activity + GitHub metadata). Hundreds of thousands of auto-generated pages. Developers searching Google for packages land on Snyk pages with CTAs to protect their apps. One brilliant SEO expert drives the strategy; engineers and PMs write the content.
  3. **Security Education Content**: Free, bite-size security lessons for developers — no paywall. Content loop that drives awareness, trust, and return visits.
  4. **Referral and Invite Loops**: Intra-company virality as developers within the same organization spread usage.

  Key insight: map all loops qualitatively, understand how they compound, and identify the biggest constraints in the overall growth model at any given time.

- **What Didn't Work (and Why)**: Snyk had developer adoption, strong free user growth, and good retention — but early self-serve monetization only converted individual developers at $100/month. Larger company purchases didn't happen. Root cause: (1) needed governance/compliance features (user management, reporting at scale) that enterprise buyers expected; (2) supporting only Node.js wasn't sufficient for security teams accountable for the entire application estate; (3) CISOs and AppSec leaders (the actual enterprise buyers) weren't being reached through a developer-only motion.
  
  Fix: hired first sales and marketing people, broadened language support, added table stakes governance features. Self-serve only customers now exist and scale — the motion evolved over time. The product always played a key role in the sales process even during the sales-led phase.

- **Three Pillars of an Effective Growth Team**:

  **1. People and Process**
  - Balanced, cross-functional teams: engineers, engineering manager, PM, designer, growth marketer, decision scientist (data science oriented toward action). Including a growth marketer embedded in each team is uncommon but powerful — creates a broader idea palette and bigger execution toolbox; allows marketing experiments (SEO pages, landing pages, email sequences) to run without consuming engineering capacity.
  - Match people to the growth context: the best growth engineers move fast, aren't attached to their code, embrace imperfection as part of the process, readily discard ideas, are curious and close to users. Excellent deep-technical engineers often struggle in growth — they're motivated differently. Test for this explicitly when building teams from internal moves, not just external hires.
  - Growth process must be well-documented with clear working cadences. Learnings must be actively socialized — without process, they gather dust and produce no durable organizational value.

  **2. Strategy: Loop-Based Growth Model**
  - Use a qualitative loop model (Reforge framework) to document all micro and macro acquisition/retention/expansion loops, how they connect, and the roles different teams play in fueling them.
  - Augment with quantitative model to understand where the biggest constraints are in the growth model at any given time.
  - This model guides quarter-to-quarter focus decisions. Strategy tells you where to invest amidst the sea of ideas.
  - Revisit the model continuously as loops mature, new features launch, and market context shifts.

  **3. Data**
  - Invest early in behavioral data infrastructure — before you need it. Retention data and activation data take time to accrue; the earlier you start collecting, the better.
  - Snyk had too much data but couldn't trust it. Solution: event tracking plans + schema conformance testing in CI pipeline. Now has absolute confidence in behavioral data.
  - "Decision scientists" (not just data scientists) — build predictive models that feed product experiences and guide decisions, not just dashboards.

- **Vision/Mission Framework (Scalable to Team Level)**:
  - **Vision**: The nirvana state you aim to enable for users in 5-10 years. Agnostic of your company, product, or solution — could theoretically be achieved by a competitor. Prefix with "In the future...". Bound to your target market. Not too wide, not too narrow.
  - **Mission**: How you'll relentlessly iterate toward the vision. Encodes your fundamental approach and unique differentiating advantage.
  - Snyk growth group: Vision = "Every developer securely unleashes their creativity"; Mission = "Connect every developer and their organizations to the value of the Snyk platform with frictionless self-serve adoption and expansion."
  - Applies at company level and individual team level. Provides clear answer to "why am I here?" for every team member.

- **Impact and Learnings Reviews (Most Important Growth Meeting)**:
  - Teams continuously document learnings from data exploration, experiments, and user research in a weekly impact/learnings document.
  - Meeting is PM-facilitated; each contributor presents their learning and facilitates discussion on implications, follow-up work, and cross-team relevance.
  - No time reviewing what the team has been doing (that's not the point). Most time on learnings and their implications.
  - Key metrics reviewed but often split into a separate meeting.
  - Monthly group-level version: directors run it; each team shares their most cross-relevant learnings; user research team presents "developer insights" as a standing agenda item; recorded and socialized company-wide.
  - Enthusiastic, voluntary cross-team learning sharing is the signal you've gotten the culture right.

- **Experiment Plan Reviews**:
  - Ad hoc, called when teams plan to experiment on surfaces they don't own (growth teams work on core product surfaces owned by other teams).
  - Include stakeholders from affected teams — ideally in co-designing the experiment plan before planning is complete.
  - A product change from an uninformed team mid-experiment can entirely invalidate the experiment. Prevention is critical.

- **Activation Metric Design Process**:
  - Activation at Snyk = a *team* (not individual user) forming a habit around fixing vulnerabilities — within 30 days of team creation. Not logging in, not finding vulnerabilities — *fixing* them.
  - Team-level definition because security is a team sport; different people fulfill different roles in the activation journey.
  - 30-day window chosen via ML analysis: significant correlation with 3-month retention (still fixing at 3 months, not just logging in).
  - Process: collect baseline data → huge amount of quantitative analysis + ML models + qualitative call research → identify retention metric → find habit moment most strongly predicting long-term retention → work backward to aha moments and setup moments → map individual steps teams need to complete.

- **Freemium Design Principles**:
  - Things that promote your growth model → go in free.
  - Things with high cost of service or that add friction → behind paywall.
  - Paid plan triggers at Snyk: governance, compliance, user management, reporting at scale (when you need to secure business-critical code organization-wide).
  - Trial design: question whether time-based trials are right — enterprise companies need longer evaluation periods; usage-based trial lengths may be more appropriate.
  - "Product-driven revenue" metric: all revenue from customers where meaningful in-product activity preceded any sales contact. Product-driven cohort has higher net retention than non-product-driven.

- **Product-Led Sales Integration**:
  - Growth platform team makes behavioral signals available to GTM teams in actionable ways — which users/teams/accounts show high engagement, what signals indicate readiness for a conversation.
  - This powers the PLS motion: large pipeline of highly qualified leads fed to sales from the product itself.

## Top Insights (Timeless)

1. **Start narrow, go deep, then expand.** Snyk launched for one persona in one language ecosystem. Every expansion came after nailing the initial use case. The lure of a larger TAM is always tempting — resist until the narrow case is bulletproof.

2. **Build growth loops into the product from day one, before PMF.** Snyk's GitHub PR loop was designed as both an acquisition and engagement loop while the company was still finding product-market fit. Founders should have strong hypotheses about how their product will acquire users before declaring PMF.

3. **PLG requires layering multiple loops, not just one.** The GitHub PR loop was powerful, but Snyk also built SEO loops, education loops, and referral loops. Each one compounds the others. Mapping your full loop architecture and identifying constraints within each is the work of growth strategy.

4. **Product adoption ≠ monetizable product.** Snyk had thousands of free users and great retention before self-serve monetization worked. The missing pieces were breadth, governance features, and sales to reach enterprise decision-makers. Adoption and revenue are different problems.

5. **Build learnings infrastructure as seriously as you build product.** Without a process to generate, document, socialize, and act on learnings, experiments produce no durable organizational value. The impact/learnings review is the most important meeting in a growth org.

6. **Activation is the right metric to anchor on.** Not logins, not page views, not even sign-ups. Find the moment that most strongly predicts long-term retention, define it precisely with data, and orient the entire activation journey around getting users there.

7. **Trust your behavioral data or don't use it.** Snyk collected everything but couldn't trust it. Schema conformance testing in CI, event tracking plans, and intentional instrumentation design fixed this. Untrustworthy data produces confident wrong decisions.

## AI & The Changing PM Role

- Snyk's developer security platform is directly adjacent to where AI will have the most impact: AI-generated code still carries vulnerabilities and open source risks; the developer security problem grows as AI generates more code faster
- The loop-based growth strategy framework is highly applicable to AI products: growth loops must be designed into the product from day one; the GitHub PR loop is a model for how AI products can create value for adjacent users without requiring explicit sign-up
- Decision science (ML-powered analysis informing product decisions) will become a standard function within growth teams as behavioral data volumes grow and decisions become more complex
- Activation metric methodology applies directly to AI features: the right activation metric for an AI feature is the moment a user derives real value from AI output — not just uses the feature once

## Notable Questions Lenny Asked
- "How did Snyk get its first 100 users?"
- "Walk me through what worked and didn't work in early monetization."
- "How do you structure a growth team? What teams do you have?"
- "What are the three most important things to get right when building a growth team?"
- "How do you define and measure activation for Snyk?"
- "What do you put in free vs. behind a paywall in freemium?"

## Best Quotes
> "Being able to identify the various micro and macro loops, how they're all connected, being able to document them in a qualitative model to communicate a shared understanding of how you grow — it's really powerful. You're never going to have a shortage of ideas in a high-performing growth team. Knowing where to focus amidst that sea of ideas is a really important role of the strategy."

> "Experimentation is not about delivering outcomes — it's about generating learnings that the organization can leverage effectively to deliver outcomes."

> "If you focus on the user's path to value and not on monetization, the latter will follow."

> "We collected absolutely everything. The problem was we weren't intentional enough about the data we were collecting and how we collected it, which made the data hard to trust. That becomes a big problem."

> "Activation is a team fixing a vulnerability within their first 30 days. Not logging in. Not finding vulnerabilities. Fixing them. That's the moment that predicts everything downstream."

> "The learnings made in growth teams, even from mistakes or failures, we socialize them widely and visibly. People can't know if something is useful to them if you haven't shared it."

## Interview Prep Takeaways
- **"How did you get your first users?"**: Narrow focus — single persona, single use case, single platform. Hook that triggered genuine concern. Deep community presence where that persona actually was (conferences, not digital ads). Bake growth loops into the product from day one.
- **"How do you structure a growth team?"**: Balanced cross-functional teams (PM, engineer, designer, growth marketer, decision scientist). Outcomes-based structure (acquisition, activation, monetization + growth platform). Core product teams are domain/function-based. Growth teams work on surfaces they don't own — requires transparent experiment planning with affected teams.
- **"How do you think about freemium design?"**: Things that promote growth loops → free. Governance/compliance/scale triggers → paid. Track "product-driven revenue" as the integrating metric for PLG + sales efficiency.
- **"How do you define activation?"**: Find the in-product moment most strongly correlated with long-term retention using ML analysis. At Snyk: team fixing a vulnerability within 30 days. Work backward from habit moment to aha moment to setup moment.
- **"How do you build a learning culture in a growth team?"**: Weekly impact/learnings review (PM-facilitated, team presents learnings not status). Monthly group-level version. Learnings socialized across the organization. Experiment plans co-designed with stakeholder teams. The signal you've done it right: enthusiastic voluntary sharing of learnings from failures, not just wins.

## Related Themes
- "Snyk PLG developer security growth loop"
- "GitHub PR loop company generated distributed content"
- "programmatic SEO developer tools Snyk Advisor"
- "growth team structure activation metric B2B"
- "freemium design product led sales PLG"
