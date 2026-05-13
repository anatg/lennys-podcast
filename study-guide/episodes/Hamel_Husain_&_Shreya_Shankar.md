# Hamel Husain & Shreya Shankar — Building AI Evals: The Most Important New PM Skill

## Guest Profile
- **Name**: Hamel Husain & Shreya Shankar
- **Role/Company**: Instructors of the #1 Maven course on AI Evals; taught over 2,000 PMs and engineers across 500+ companies including OpenAI and Anthropic teams
- **Background**: Hamel Husain is a machine learning engineer and consultant specializing in AI application development. Shreya Shankar is a researcher focused on AI systems and evaluation methodologies. Both are recognized experts in systematic evaluation of AI products and have developed definitive methodologies for building evals.

## Tags
`AI/ML` `Product Strategy` `Frameworks` `Data` `Experimentation` `Execution` `Engineering` `User Research` `Metrics` `B2B` `SaaS` `Enterprise`

## TL;DR
Evals (systematic evaluation of AI applications) have emerged as the most critical new skill for AI product builders, combining data analytics, error analysis, and iterative testing to measure and improve AI product quality. The key insight is that effective evals start with manual error analysis of real user traces—not automated testing—to ground improvements in actual failures, then progressively automate measurement through code-based tests and LLM-as-judge evaluators.

## Core Frameworks & Mental Models

- **Error Analysis Process (Open Coding → Axial Coding → Automated Evals)**: Start by manually reviewing 100+ production traces, writing quick notes (open codes) on first error seen in each trace. Use LLMs to categorize these notes into failure modes (axial codes). Count occurrences to prioritize, then build automated evaluators for top issues. This systematic approach grounds all testing in real problems rather than hypothetical ones.

- **Benevolent Dictator Model**: Appoint one domain expert (often the PM) to own initial error analysis rather than forming committees. This prevents the process from becoming too expensive or slow. The key is trusting one person's taste while keeping the process tractable.

- **LLM-as-Judge with Binary Scoring**: When code-based tests aren't sufficient, create narrow, specific prompts that ask an LLM to evaluate one failure mode with pass/fail output only. Avoid 1-5 or 1-7 scales—they're "weasel ways of not making a decision" and create meaningless averages (e.g., 4.2). Always validate judge alignment with human labels using a confusion matrix before deploying.

- **Theoretical Saturation**: Stop error analysis when you're no longer discovering new types of problems. This typically happens after 40-100 traces depending on application complexity, not at an arbitrary number.

- **Evals as Systematic Quality Measurement**: Evals encompass all methods of systematically measuring AI application quality—unit tests, data analysis, LLM judges, A/B tests, and monitoring. It's fundamentally applied data science for AI products, not a separate discipline.

## Top Insights (Timeless)

1. **The highest ROI activity in AI product development is looking at actual production traces**. Most teams skip straight to writing tests, but you must ground evals in real errors through manual data analysis first. This prevents building evaluators for hypothetical problems while missing actual issues.

2. **Agreement percentage is a dangerous metric for LLM judges**. If errors occur only 10% of the time, a judge that always says "pass" achieves 90% agreement while catching zero problems. Instead, examine the confusion matrix to see false positive and false negative rates for each type of error.

3. **Most AI product errors are not what you'd hypothetically predict**. In the real estate assistant example, the team discovered issues like text message conversation flow problems and missing human handoff triggers—problems they never would have anticipated without examining real traces.

4. **You need surprisingly few targeted evals (4-7) for most applications**. Many problems are obvious prompt fixes that don't require ongoing evaluation. Reserve LLM-as-judge evals for persistent, subjective failure modes that you can't easily test with code.

5. **The initial eval setup takes ~3-4 days, then only 30 minutes per week to maintain**. This is a one-time investment that provides continuous returns through automated monitoring and iterative improvement. The process becomes addictive once teams see how much they learn.

## AI & The Changing PM Role

- **Evals represent PMs' evolving PRD responsibility**: The LLM-as-judge prompts shown are essentially executable product requirements documents—they specify exactly how the AI should behave in concrete, testable ways. Unlike traditional PRDs that describe desired behavior, eval prompts continuously enforce and measure that behavior.

- **Domain expertise becomes more critical, not less**: PMs and domain experts must be "in the loop" for error analysis because LLMs cannot assess product quality without business context. For example, an LLM would miss that failing to offer a virtual tour follow-up loses leads—it needs the PM's understanding that lead nurturing matters.

- **Data literacy is now a core PM skill**: PMs must be comfortable reviewing traces, writing open codes, interpreting confusion matrices, and making decisions about eval coverage. This isn't optional—it's how you know if your AI product works.

- **Coding agents are different because developers are the domain experts**: Products like Claude Code can rely more on developer dogfooding because engineers immediately recognize bad code. Most AI products lack this built-in expertise loop, making systematic evals essential.

## Notable Interview Questions Lenny Asked

- "What the heck are evals? For folks that have no idea what we're talking about, give us just a quick understanding."
- "What are a couple of the most common misconceptions people have with evals?"
- "Just to make very real, so imagining this real estate agent...how do you know if it's giving them good advice, good answers?"
- "How do they know this is happening? Watching this happening, I'm like, 'How could you not do this to your product?'"
- "Do you have thoughts on what Statsig [acquisition by OpenAI] means? Is there anything there that's interesting?"
- "What's cool about this is you don't need to do this many, many times. For most products, you do this process once and then you build on it, I imagine?"

## Best Quotes

> "To build great AI products, you need to be really good at building evals. It's the highest ROI activity you can engage in." — Lenny Rachitsky

> "The goal is not to do evals perfectly, it's to actionably improve your product." — Shreya Shankar

> "The top [misconception] is, 'We live in the age of AI. Can't the AI just eval it?' But it doesn't work." — Hamel Husain

> "You're never going to know what the failure modes are going to be upfront, and you're always going to uncover new vibes that you think that your product should have. You don't really know what you want until you see it with these LLMs." — Shreya Shankar

> "When you're doing this open coding, a lot of teams get bogged down in having a committee do this...You can appoint one person whose taste that you trust. It should be the person with domain expertise. Oftentimes, it is the product manager." — Hamel Husain

> "Everyone that does this immediately gets addicted to it. When you're building an AI application, you just learn a lot." — Hamel Husain

> "People have been burned by evals in the past. People have done evals badly, so then they didn't trust it anymore, and then they're like, 'Oh, I'm anti evals.'" — Shreya Shankar

## Interview Prep Takeaways

- **Demonstrate systematic thinking about quality**: When discussing AI products in interviews, show you understand the full eval lifecycle—not just "we'll test it" but "we'll analyze production traces, identify failure patterns, prioritize based on business impact, and build targeted automated checks."

- **Show data-driven decision-making**: Reference confusion matrices, theoretical saturation, and the importance of grounding tests in real errors. Avoid hand-waving about "we'll use AI to evaluate AI"—show you know that requires careful validation.

- **Emphasize domain expertise value**: Position yourself as the necessary human in the loop who brings product judgment and business context. LLMs can't determine what "good" means without someone who understands the user problem and business goals.

- **Know when to automate vs. when to stay manual**: Demonstrate judgment about cost-benefit tradeoffs—when code-based tests suffice, when LLM judges are worth the complexity, and when manual review remains essential.

- **Use concrete examples**: If asked about ensuring AI quality, walk through a simplified version of the error analysis process rather than speaking abstractly about testing. Reference real failure modes like conversation flow, hallucinations, or inappropriate handoffs.

## Related Themes

- Foundation model evaluation and benchmarks (MMLU, HumanEval)
- AI observability and monitoring tools (Braintrust, Phoenix Arize, LangSmith)
- Product analytics and data analysis for non-deterministic systems
- A/B testing in AI product development
- The debate between systematic evals vs. vibe-based development
- Cost optimization for LLM applications while maintaining quality
- Building custom tooling for error analysis
- User research methods adapted for AI (open coding, axial coding from social science)
