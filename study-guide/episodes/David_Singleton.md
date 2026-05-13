# David Singleton — CTO of Stripe

## Guest Profile
- **Name**: David Singleton
- **Role/Company**: Chief Technology Officer at Stripe (5+ years in role)
- **Background**: VP of Engineering at Google for over a decade before joining Stripe. Responsible for guiding Stripe's engineering and design teams, overseeing a company that moves as much money as all of e-commerce did when Stripe started, with 99.999% uptime and 16.4 deployments per day.

## Tags
`Engineering` `Product Strategy` `Hiring` `Culture` `Execution` `Leadership` `AI/ML` `Developer Tools` `Infrastructure` `Org Design` `Operational Excellence` `Craft` `User Research`

## TL;DR
David Singleton shares how Stripe built a highly product-minded engineering culture by co-creating products with users like Figma and Slack, operationalizing craft through practices like friction logging and "walking the store," and maintaining 99.999% uptime while deploying 16+ times daily. He reveals Stripe's patient, personal hiring approach, their practice of "engineer-cations" for leaders to stay technical, and how operating principles like "users first" and "meticulous in craft" translate into systematic practices that compound into 10.5% revenue improvements.

## Core Frameworks & Mental Models

- **Co-creation with Early Users**: Find the right set of early users (companies like Figma, Slack for Stripe Billing) and build in shared Slack channels, showing product regularly. Only launch when this alpha group is "super, super happy." This ensures product-market fit before broader release.

- **Friction Logging**: Put yourself in a specific user's shoes, go through the entire product flow end-to-end, and keep meticulous stream-of-consciousness notes of every friction point. Focus investment on removing friction for the most critical user moments. Used across functions and done regularly (David does Stripe onboarding monthly).

- **Inverted W Planning Process**: Teams surface initial ideas → product leaders synthesize into draft strategy → back to teams to adjust plans → back up for final synthesis → down for distribution with full context. Balances bottom-up insight with top-down coordination.

- **Engineer-cations**: Leaders clear 3-4 days to join a team as an IC, pick up a feature, and ship it through the full process. Keep a friction log throughout. This maintains technical credibility, reveals tooling gaps, and provides lasting context for prioritization decisions.

- **Selective Test Execution**: As test suites grow, use systems to determine which tests are material for each specific change rather than running everything. Stripe's distributed test environment is their largest distributed system.

## Top Insights (Timeless)

1. **Meticulousness compounds dramatically**: Stripe's obsession with details like error messages linking to docs, removing checkout latency, and optimizing every step resulted in 10.5% revenue improvement for users—measured in hundreds of basis points where others measure single basis points. Small changes compound when you're systematic about where craft matters.

2. **Reserve time for polish in your roadmap**: Teams must think hard about how much bandwidth to reserve for friction log fixes and incident remediations. There's no company-wide percentage—it varies by team and product stage—but Stripe prioritizes most incident remediations before roadmap work because operating principles demand it.

3. **The first PM hire isn't about skill—it's about when**: Stripe waited until ~200 employees because every early engineer was product-minded enough to talk to users, synthesize feedback, and drive strategy. When building developer-focused products, technical PMs (often former engineers) are essential, and engineering teams can fulfill PM functions if structured correctly.

4. **References trump interviews for conviction**: Eight hours of interviews give you limited signal. Talking to people who've worked with a candidate for thousands of hours provides far better insight. Ask smart questions to get real signal, not just confirmations.

5. **Your experience of the product IS the strategy**: Stripe puts tremendous care into explaining products through beautiful websites and demos because for infrastructure (payment engines, treasury networks), users can't inspect the product directly. The meticulousness of explanation signals the meticulousness of execution.

## AI & The Changing PM Role

- **Stripe has used ML/AI at its core for years**: Radar (fraud detection) has used machine learning since inception. Transformers were integrated into fraud systems over a year ago with profound impact.

- **LLMs unlock non-developer productivity**: Stripe built internal GPT-4 integration with presets (shared prompts) that marketing, support, and other teams use. Writing effective prompts is accessible across job families, democratizing AI value.

- **Documentation + LLMs = instant answers**: GPT-4 reads all Stripe docs as embeddings and answers developer questions directly in documentation, significantly reducing time to integration.

- **Natural language to SQL**: Stripe Sigma (revenue analytics) now accepts natural language queries that generate SQL automatically, making powerful analytics accessible to non-technical users.

- **GitHub Copilot accelerates through boilerplate**: Stripe ran rigorous trials before rollout. Biggest gains: generating comprehensive test suites. Engineers focus on "what should this test" rather than boilerplate, improving both productivity and code quality. David personally loves coding with Copilot—it lets him focus on what matters.

## Notable Interview Questions Lenny Asked

- "What is it that you all do that allows you to attract, hire, close, and keep people of that caliber?"
- "How do you operationalize this principle [be meticulous in your craft]?"
- "What are some lessons you've learned about managing people and/or managing engineers?"
- "Has AI impacted the way you all build product yet?"
- "What does it take to achieve [99.999% uptime with 16.4 deployments/day]?"

## Best Quotes

> "The way we think about product development at Stripe, it really is to find the correct set of early users to kind of co-create the product with... we had shared Slack channels, we'd actually show them product on a very regular basis, get their feedback on it. And only when that original kind of Alpha group was super, super happy with the product did we then think it might be ready to go to a broader audience."

> "There's one way to be very reliable, which is to try to change things as infrequently as possible. Never change anything than you have many fewer opportunities for things to break. But we don't take that approach."

> "Most people wouldn't do that [more code for error handling than main flow], but it turns out not only was it something I was impressed with, but when I talk to Stripe users, this is very frequently something they tell me and delights them about the product."

> "As I've been responsible for bigger and bigger teams over time, one of the things that just I repeatedly learn is I personally will not be involved in really any of the decisions that matter and happen."

> "Don't tell us it's great. What bugs you?" (David's response when Lenny praised Stripe)

> "The name is, it's often the hardest thing about [engineer-cations] is finding the time to clear your calendar for that many days... when you're on vacation, the world goes on and it's all fine."

## Interview Prep Takeaways

- **Demonstrate user-first thinking**: Be ready to discuss specific users you've built relationships with and how their needs shaped your product decisions. Stripe values PMs who can name specific companies and individuals they've learned from.

- **Show systematic craft, not just craft**: Don't just say "I care about quality." Describe processes you've implemented (like friction logging) that systematically identify where quality matters most and how you operationalize that at scale.

- **Expect questions about learning from users**: Be prepared to walk through how you identify the right early users to co-create with, how you structure that feedback loop, and when you knew something was ready for broader release.

- **Technical fluency matters for developer products**: If interviewing for developer-focused products, demonstrate you can read code, understand APIs, and speak credibly about developer experience. Stripe PMs are often former engineers or deeply technical.

- **Ask about operating principles in interviews**: When interviewing, ask how the company's values translate into actual practices and rituals. Stripe shows this translates abstract values into concrete behaviors like friction logging, walk the store sessions, and instant remediations.

## Related Themes

- User Research & Co-creation
- Engineering Culture & Developer Productivity  
- Operational Excellence at Scale
- Hiring for Mission-Driven Companies
- Systematic Approaches to Quality
- Leadership in High-Growth Technical Organizations
- Internal Tools & Developer Experience
- Planning & Prioritization Frameworks
