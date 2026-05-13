# Bill Carr — Co-author (Working Backwards), Former VP Digital Media (Amazon)

## Guest Profile
- **Name**: Bill Carr
- **Role/Company**: Co-author of *Working Backwards* (with Colin Bryar); formerly VP of Digital Media at Amazon (launched and managed Amazon Music, Prime Video, and Amazon Studios globally); joined Amazon in 1999 (5 years after founding), stayed 15 years; previously executive in residence at Maveron VC and COO at OfferUp; now runs Working Backwards LLC consulting firm
- **Background**: One of the most authoritative voices on Amazon's operating practices — the mechanisms behind its product innovation, org design, and decision-making. Personally led the launch of major Amazon products and has systematized and taught these practices to dozens of growth-stage and public companies.

## Tags
`Amazon` `Working Backwards` `Product Development` `PR/FAQ` `Org Design` `Single-Threaded Leader` `Input Metrics` `Decision-Making` `Hiring` `Leadership`

## TL;DR
Bill's episode is the canonical source on Amazon's operational playbook: the Working Backwards PR/FAQ process, single-threaded leaders, input vs. output metrics, disagree and commit, and Bar Raiser hiring. These practices were developed in a 4-year window (2003-2007) as Amazon scaled from zero-to-one to a highly complex multi-business company. They're systematic answers to recurring failure modes — not philosophy, but mechanisms.

## Core Frameworks & Mental Models

- **Amazon's Innovation Burst (2003-2007)**: All of Amazon's major product innovations (Kindle, AWS, Alexa/Echo, Prime, digital media businesses) AND its major process innovations were developed in a single 4-year window. This happened because the company had become too complex for the CEO to be in every meeting. Jeff Bezos, applying a scientific, quantitative mindset, experimented with processes the same way he experimented with products: form a hypothesis, implement, measure, iterate. This is why Amazon's process innovations are unusually systematic — they were designed that way.

- **Working Backwards (Customer-Obsession as a Process)**: Amazon's guiding principle: start with the customer's need and work backward to the solution. The mechanism that operationalizes this is the PR/FAQ process. The typical failure mode is "working forward" — starting from financial constraints, existing resources, or "I need to grow revenue" and projecting out to potential solutions. Amazon took "if we serve customers well, revenue will follow" as an article of faith and built a repeatable process to ensure they always started with the customer.

- **PR/FAQ Process**: The Working Backwards method for deciding what to build. Before writing code, write a press release. The press release has:
  1. **Headline**: Clear single-sentence statement of what the product is
  2. **Customer problem**: Who is the customer (specific, not "all restaurants")? What is their specific, quantifiable problem?
  3. **Solution statement**: What is the product, and how does it solve the problem?
  4. **FAQ**: Questions that internal and external stakeholders will ask — business case, technical approach, financial projections, risks
  
  The press release is NOT a real press release (no hyperbole, full of internal confidential data). The date in the press release is meaningful — it signals the author's expectation for launch timing. The concentric circle review process: author → small group → larger group → CEO level. Not every PR/FAQ survives — some get killed at author stage, some at director level. The goal is a product funnel (many ideas, few survive), not a product tunnel (everything that goes in comes out).
  
  Key function: forces teams to articulate who the customer is (not "everyone") and what the problem is (specific and quantifiable) before any engineering resources are committed. The writing surfaces fatal flaws in ideas before they're funded.

- **Single-Threaded Leader (Program vs. Project Orientation)**:
  - **Problem it solves**: At scale, multiple departments compete for centralized engineering resources. Teams spend more time in resource-fighting meetings than building. Accountability is diffuse — nobody fully owns anything.
  - **The model**: One leader owns a cross-functional team with all the resources needed to execute (engineering, design, marketing, biz dev — either direct reports or dedicated dotted-line). That leader is responsible for the outcomes, not just the roadmap.
  - **Program vs. project**: A project-oriented team forms and dissolves around specific initiatives. A program-oriented team always works on search (or payments, or mobile apps) — they own the full remit continuously, set their own priorities within it, and are accountable for those metrics.
  - **Benefit**: Teams can sprint fast knowing they're aligned with senior leadership. CEOs move from refereeing every roadmap item to refereeing team resource allocation (a once/twice/three-times-a-year decision).
  - **Prerequisite**: Service-based architecture with defined APIs so teams can own their code with clear endpoints. Monolithic codebases make this impossible.
  - **Countermeasures for functional excellence**: When engineers or designers are spread across single-threaded teams and no longer have a C-level function head, functional excellence can erode. Amazon's solution: create functional roles embedded inside the org — engineering VPs who, in addition to their day job, sit on promotion panels, do code reviews for other teams, set companywide standards.

- **Disagree and Commit (Correctly Understood)**: One of the most misunderstood Amazon leadership principles. The correct interpretation:
  - **Disagree**: An obligation — if you disagree with a decision direction, you MUST voice it, all the way up the chain if necessary. Disagreement is about bringing new information, new data, or a new point of view that hasn't been considered. It's NOT about relitigating things already considered.
  - **Commit**: Once you've voiced your disagreement and the decision-maker acknowledges they've heard and considered your point — that's the commit trigger. If they say "I hear you, and we've considered that factor, but here's why we're going this way anyway," it's time to commit.
  - **What commit really means**: Not "I'll grudgingly do this." Ideally: "I've now heard the reasoning, I understand why we're going this way, and I can reflect that reasoning back to my team." Commitment based on understanding. Going through the motions of commitment while privately still disagreeing is not commitment and hurts execution.
  - **When you still disagree after committing**: Find the kernel — what is the core of why the person making the decision thinks it's right? Focus on that kernel and ask: how can I take this concept and try to make it viable? Don't just stomp through something you don't believe in.

- **Leaders Are Right A Lot**: Judgment can't be delegated and can't always be data-driven (data can be framed to support any position). "Right a lot" is explicitly not "right all the time." It's a quality you develop through experience: making decisions, seeing the results, learning from mistakes. Teams need leaders who are directionally correct enough that they're worth following. Being wrong too often destroys followership. This quality develops through active learning — being a student of decisions you made and decisions you observed.

- **Input vs. Output Metrics**: Origin: Amazon had quarterly revenue shortfalls and responded with promotional fire drills — extra emails, price cuts, last-minute ad spend. These fire drills didn't work (pulled future revenue forward, were a distraction, didn't move the needle on things that mattered). The realization: revenue is an output metric — you can't directly control it.
  
  Catalyst: Jeff and the S-Team read *Good to Great*, which helped them codify Amazon's growth flywheel. The flywheel identified the actual inputs to customer experience: broad selection, low prices, speed of delivery, ease of finding/buying. These are what customers will always want (nobody will ever prefer less selection, higher prices, slower shipping).
  
  **Input metrics**: Things the team controls that, if improved, drive the outputs. Must touch the customer experience or affect it causally. Examples: "what % of searches result in a click on a top 3 result?" "page load time in milliseconds by browser/device type." They're not perfect — measuring selection was done wrong for years, had to be refined.
  
  **Output metrics**: Revenue, active customers, free cash flow. The article of faith: if we focus on inputs, outputs will take care of themselves. Amazon's S-Team goals were ~500 items, only 10 of which had financial metrics.
  
  **How to identify input metrics**: Map the end-to-end customer experience step by step. At each step, ask: how do I measure the speed, quality, and ease of this step? Which of these measurements can we control? Which correlate most with downstream retention and revenue? Iterate through measurement → observation → improvement → check output effects.
  
  **Compound metrics are wrong**: Amazon experimented with "fitness functions" — weighted index of multiple important metrics. Abandoned them because they become meaningless. You can't understand what's driving good or bad outcomes when metrics are combined. Keep each metric separate and manage each individually.

- **PRFAQ as a Product Funnel, Not Product Tunnel**: The goal of writing PR/FAQs is not to launch everything — it's to have a corpus of well-thought-out ideas, compare them against each other, and select the best ones. Think like a VC: a VC doesn't fund every company they meet. You should have many PR/FAQs that were great ideas but didn't get built because others had higher potential impact. The tunnel mentality (everything goes in, everything comes out) is how you end up building things you shouldn't have built.

- **Fire Phone Lesson**: Despite having the PR/FAQ process, Amazon shipped a failed product. Bill's analysis: Fire Phone started from a technology (3D effects) in search of a problem. The PR/FAQ process is a tool that helps you make better decisions, not one that makes decisions for you. When you start with "we have this cool technology," you're working forward, not backward. The correct PR/FAQ starts with a customer problem — "what are customers frustrated by when using their phone?" If you can't name a specific, meaningful customer problem that the 3D effects solve, that's the signal.

- **Bar Raiser Hiring Process**: Created in 1999 to solve a "new people hiring new people hiring new people" problem in hypergrowth. Every interview loop includes a Bar Raiser — an interviewer who is NOT the hiring manager, does NOT report to the hiring manager, is NOT the recruiter, is not even in the department. The Bar Raiser:
  - Runs the debrief meeting (not the hiring manager, not the recruiter)
  - Has technical veto power over the hiring manager's decision (almost never actually used — it's a Socratic process of surfacing concerns, not a dictate)
  - Is an expert in behavioral interview methodology and Amazon's leadership principles as objective evaluation criteria
  
  Why it works: prevents urgency bias (hiring managers under pressure to fill seats), ensures consistent objective criteria across all hires (not "they seem like a good culture fit"), makes the hiring manager's decision better rather than blocking it.
  
  Time cost: up to 10 hours/week for active Bar Raisers. Worth it — the cost of a wrong hire far exceeds the cost of the process. Final decision: always the hiring manager. Bar Raiser is advisory with a rarely-used veto.

- **Innovation Organizational Requirements**: For companies that want to enable real innovation:
  1. **Compensation decoupled from short-term financial performance**: Amazon had no performance bonuses tied to quarterly numbers. Compensation was equity (stock price, long-term). This meant moving from a successful P&L to a risky zero-revenue new venture didn't change your comp — you had incentive to do what was right for the company long-term.
  2. **CEO must be deeply engaged, not delegate**: For digital media and AWS, Amazon put two of its smartest leaders (Steve Kessel and Andy Jassy) on these efforts AND had Jeff meeting with them regularly. Senior sponsorship creates runway for new ventures to overcome bureaucratic friction.
  3. **Separate organizational structures**: Most structures inside a large company are designed to crush small innovative teams. You need different approval processes, different decision-making structures, different timelines for the innovative team. (*Loonshots* by Safi Bahcall.)
  4. **OK to launch something that fails**: But you need the org design, comp structure, and leadership example to make this culturally real — not just stated.

- **"Slow Is Smooth, Smooth Is Fast"**: Bill's personal motto (from Marine Corps Scout Snipers). Most people confuse speed with velocity. Velocity has both speed and a direction (destination). You can go extremely fast and still end up nowhere useful. Going slow first — being very clear on where you're going and what you're doing — is often what enables you to go fast after. Jeff Bezos embodied this: the upfront clarity is what makes the downstream execution fast.

## Top Insights (Timeless)

1. **Start with the customer problem, not the technology or the revenue goal.** The PR/FAQ process exists to force this. Fire Phone failed because Amazon started from a technology (3D) and worked forward to find a problem. Every failed product can usually be traced back to this error.

2. **Input metrics, not output metrics, are what your team can actually control.** Revenue is an output. Find the 3-6 inputs to your customer experience that, if improved, cause better outputs — then obsess over those inputs. Measuring the output and trying to move it directly causes fire drills, not durable growth.

3. **Single-threaded leadership is not about one person's genius — it's about clear accountability.** The organizational structure ensures someone is fully responsible for a small list of things rather than half-responsible for a long list of things. When nobody's fully accountable, CEOs push on strings.

4. **Disagree and commit means voice disagreement completely, then actually commit.** Commitment based on understanding the reasoning is sustainable. Going through the motions of commitment while privately still disagreeing undermines execution. Find the kernel of why the decision-maker believes they're right, then try to make it work.

5. **The PR/FAQ process is a product funnel, not a product tunnel.** Great ideas that don't get built are evidence the process is working — they were outcompeted by better ideas. If everything you PR/FAQ gets built, you don't have a selection mechanism.

6. **The conditions for innovation are organizational, not inspirational.** You can want innovation and have employees who want it, but if your compensation system punishes quarterly misses, your CEO doesn't sponsor the new venture, and your approval processes are designed for the core business, you won't get it.

7. **Functional excellence and autonomous teams can coexist — but you have to design countermeasures.** Single-threaded teams without functional leaders lose engineering standards, design standards, hiring standards. Amazon's solution: engineers and designers in teams also have "second jobs" contributing to company-wide functional standards. It's designed in, not assumed.

## AI & The Changing PM Role

- The PR/FAQ process becomes more important as AI tools make prototyping easier: the temptation to jump to building is stronger than ever. Writing the press release forces articulation of the customer problem before any code (or AI-generated code) is written — a more valuable forcing function in an era when the cost of building a prototype is near zero
- Input metrics will increasingly be AI-computed: customer experience signals that used to require manual instrumentation can now be auto-detected and tracked — but the discipline of identifying which signals to track (and which are most causal) remains a PM skill
- Single-threaded leadership becomes more important as AI creates more surface area: when one team can build in a week what took a month, the number of viable product directions explodes; clear ownership and focused mandates are more necessary, not less
- Bar Raiser methodology is directly applicable to AI hiring: as AI capability grows, the urgency to hire AI talent is high — urgency bias is the enemy of quality hiring, and the Bar Raiser process was designed specifically to counter it

## Notable Questions Lenny Asked
- "What is it about Amazon that enabled so many new ways of working, and why did they proliferate?"
- "What does single-threaded leadership actually mean and why is it so effective?"
- "How does disagree and commit actually work? People often use it incorrectly."
- "What does it mean to work backwards versus working forwards?"
- "How do you actually implement the PR/FAQ process? Walk me through steps."
- "What's the difference between input and output metrics? Give me an example."
- "How do you actually enable a culture of innovation where failing is genuinely okay?"
- "What is the Bar Raiser program and how can other companies implement it?"

## Best Quotes
> "Jeff would say, we took it as an article of faith. If we served customers well, if we prioritized customers and delivered for them, things like sales, things like revenue and active customers and things like the share price and free cash flow would follow."

> "Once the disagreer is hearing back from the leader that they understand their point of view... that is the point for them to commit."

> "You want to create this corpus of ideas that are well-thought-out and select the best ones. Think of yourself as a venture capitalist."

> "What problem did you solve? If it wasn't poor execution, what was wrong with the concept? 9 times out of 10, that's where the answer is."

> "You know it's an input metric if it is measuring something with respect to the customer experience and if it is something you can control."

> "Velocity has both speed and a vector — a specific destination. A lot of people are going very fast, but the destination isn't very clear. Slow is smooth, smooth is fast."

> "Implementing a new process is not easy. If you go into it lightly and dip your toes into it and try it out, it's probably not going to work. It requires commitment and discipline to get through the hard part."

## Interview Prep Takeaways
- **"What is the Working Backwards process?"**: Customer-first product development. Start with who is the customer (specific persona) and what is their specific, quantifiable problem. Work backward to solution, without constraints. Mechanism: PR/FAQ. The press release surfaces fatal flaws in product ideas before engineering resources are committed.
- **"How do you set up a high-ownership product team?"**: Single-threaded leader model. One leader, one cross-functional team, clear metric ownership, program orientation (continuous ownership of a domain, not projects). Moves senior leadership from refereeing every roadmap decision to refereeing resource allocation.
- **"What makes a good metric? How do you think about metrics?"**: Distinguish input from output metrics. Output: revenue, customers, cash flow — you can't directly control these. Input: the customer experience elements that cause the outputs (selection, price, speed, ease of purchase). Obsess over inputs. Never create compound metrics — they're meaningless and obscure causality.
- **"How do you build an innovation culture?"**: Needs organizational design, not just permission to fail. Decouple compensation from short-term financial outcomes. Ensure the CEO is deeply engaged with innovation bets. Create separate structural protections for innovative teams from the bureaucracy of the core business.
- **"What is your hiring process / how do you ensure quality hiring at scale?"**: Bar Raiser program: dedicated non-hiring-manager interviewer with expertise in behavioral interviewing and objective criteria (Amazon's LPs). Runs the debrief. Counters urgency bias. Final decision with hiring manager. Pilots within one department before scaling.

## Related Themes
- "Amazon Working Backwards PRFAQ customer obsession"
- "single-threaded leader program orientation org design"
- "input output metrics flywheel Amazon"
- "disagree and commit leadership principles"
- "Bar Raiser hiring program Amazon"
