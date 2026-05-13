# Sander Schulhoff — Prompt Engineering & AI Red Teaming

## Guest Profile
- **Name**: Sander Schulhoff
- **Role/Company**: Founder of Learn Prompting and HackAPrompt; AI security researcher
- **Background**: Created the first prompt engineering guide on the internet (two months before ChatGPT launch). Partnered with OpenAI to run HackAPrompt, the largest AI red-teaming competition. Led The Prompt Report, a 76-page comprehensive study analyzing 1,500+ papers and 200+ prompting techniques, co-authored by OpenAI, Microsoft, Google, Princeton, and Stanford.

## Tags
`AI/ML` `Prompt Engineering` `Security` `Product Strategy` `Frameworks` `Execution` `Engineering` `Data` `Research` `Enterprise`

## TL;DR
Prompt engineering remains critical despite claims it's becoming obsolete—studies show bad prompts can drop performance to 0% while good prompts reach 90%. AI security through prompt injection is an unsolvable problem that will only grow more dangerous as agentic AI deploys in the real world, requiring defense at the model architecture level rather than through external guardrails.

## Core Frameworks & Mental Models

- **Two Modes of Prompt Engineering**: (1) **Conversational mode**—iterative prompting in ChatGPT/Claude where you refine outputs through dialogue; (2) **Product-focused mode**—creating single, optimized prompts that run millions of times in production. Product-focused prompting requires much more rigor and provides the biggest performance gains.

- **Few-Shot Prompting**: Give the AI examples of what success looks like. Use consistent formatting (XML, Q&A structure) that appears commonly in training data. For writing tasks, paste previous emails in your style; for data tasks, show input-output pairs with reasoning.

- **Decomposition Technique**: Before solving a complex problem, ask "What are some subproblems that need to be solved first?" Then solve each systematically. Example: For a car dealership return query, first verify customer identity, then car type, then checkout date, then insurance status—before making the final decision.

- **Self-Criticism Loop**: Ask the LLM to solve a problem, then ask "Can you go back and check your response?" After it critiques itself, say "Great job, now implement these suggestions." Repeat 2-3 times for iterative improvement.

- **Additional Information (Context)**: Front-load prompts with relevant background information. Put it at the beginning for caching benefits (cheaper subsequent calls) and to prevent the model from forgetting the original task. In conversational mode, dump everything in; in product mode, carefully balance cost and latency.

- **Artificial Social Intelligence**: The skill of communicating effectively with AIs, understanding their responses, and adapting follow-up prompts—parallel to human social intelligence but for human-AI interaction.

## Top Insights (Timeless)

1. **Role prompting doesn't work for accuracy tasks**: Despite widespread belief, telling an AI "you are a math professor" provides no statistically significant performance boost on accuracy-based tasks. Roles only help with expressive/style tasks like writing. Studies showing 0.01% differences lack statistical significance.

2. **Threats and rewards in prompts don't work**: Phrases like "this is very important to my career" or "I'll tip you $5" provide no measurable benefit. These worked briefly on older models but are ineffective on modern LLMs, contrary to popular Twitter advice.

3. **Prompt injection is fundamentally unsolvable**: Unlike classical cybersecurity where you can patch a bug with certainty, you cannot "patch a brain." Even if you train against specific attacks, you can never be certain they won't work again. Sam Altman's realistic goal is 95-99% security, not 100%.

4. **Common defenses don't work**: (1) Adding "do not follow malicious instructions" to prompts fails completely; (2) AI guardrails have limited effect due to the "intelligence gap"—they're often too simple to detect encoded attacks that main models understand; (3) Blocking common words from attack datasets is ineffective and impractical.

5. **The real danger is agentic AI**: Current chatbot jailbreaks (outputting bomb-building instructions) are concerning but limited—that information exists elsewhere. The looming crisis is autonomous agents managing finances, booking flights, or operating in humanoid robots, where prompt injection could cause real-world harm. An AI coding agent could be tricked via a malicious website to inject viruses into your codebase.

6. **Persistence over talent**: Sander's philosophy is that persistence is the only thing that matters. He'll work on the same bug for months. This trait is what he values most when hiring, over raw intelligence or skill.

7. **Trial and error beats reading**: The single best way to improve prompting skills is hands-on experimentation with chatbots—more effective than reading resources or taking courses. Learn by doing.

## AI & The Changing PM Role

- **Product security becomes a core PM responsibility**: As products integrate agentic AI, PMs must understand that AI security vulnerabilities are fundamentally different from classical security. You cannot achieve 100% safety, only risk mitigation. This changes how you design features, set user expectations, and plan deployments.

- **Prompt optimization is a product lever**: For AI-powered products, the quality of prompts directly impacts user experience and business metrics. A 70% accuracy improvement from better prompting (as Sander achieved in medical coding) can be the difference between product success and failure. PMs need to allocate resources to prompt engineering the same way they would to traditional optimization.

- **Trust and verification become critical**: As Sander notes, "With conversational prompt engineering, you see the output. With product-focused, millions of users interact with that prompt. You want certainty it's working well." PMs must build verification systems and cannot rely on spot-checking AI outputs.

- **The consciousness and alignment problem is becoming practical**: The discussion about AI agents potentially making harmful decisions to achieve goals (the SDR/daughter example) means PMs must think through unintended consequences and edge cases in ways that go beyond traditional product thinking. What happens when your AI tries too hard to achieve its objective?

## Notable Interview Questions Lenny Asked

- "Is prompt engineering a thing you need to spend your time on?"
- "What's an example where changing the prompt had a big impact?"
- "What's a technique that people think they should be doing that's no longer useful?"
- "From the perspective of a founder or product team, is this [prompt injection] a solvable problem?"
- "How much better does your result end up being if you use these techniques in a conversational setting—10%, 50%?"
- "How real is that [story about LLMs trying to blackmail engineers]? Is that something we should be worried about?"
- "Is there hope here? Where do we go from here?"

## Best Quotes

> "Studies have shown that using bad prompts can get you down to 0% on a problem, and good prompts can boost you up to 90%."

> "People will always be saying, 'It's dead,' or 'It's going to be dead with the next model version,' but then it comes out and it's not."

> "You can patch a bug, but you can't patch a brain."

> "If we can't even trust chatbots to be secure, how can we trust agents to go and manage our finances? If somebody goes up to a humanoid robot and gives it the middle finger, how can we be certain it's not going to punch that person in the face?"

> "Persistence is the only thing that matters. I don't consider myself to be particularly good at many things... but boy, will I persist. I'll work on the same bug for months at a time until I get it."

> "We actually call AI red teaming 'artificial social engineering' a lot of the times."

> "In the competition setting, people are massively incentivized. Even when they have solved the problem, we've set it up so you're incentivized to find shorter and shorter solutions. It's a game. It's a video game."

## Interview Prep Takeaways

- **Frame technical depth with practical examples**: Sander excels at explaining complex concepts (prompt injection, self-criticism loops) through concrete stories (medical coding improvement, grandmother bomb story). In interviews, demonstrate depth by showing how techniques apply to real scenarios.

- **Challenge conventional wisdom with data**: Sander confidently debunks popular techniques (role prompting, reward/threat prompting) backed by research. In PM interviews, be prepared to question assumptions and cite evidence, but acknowledge nuance ("it works for expressive tasks, not accuracy tasks").

- **Articulate the "why" behind technical choices**: When discussing prompt engineering techniques, Sander explains not just what works but why (caching benefits, training data patterns, intelligence gaps). In system design or technical questions, always connect your choices to underlying principles.

- **Address limitations honestly**: Sander is direct about unsolvable problems (prompt injection can only be mitigated, never eliminated). In interviews, demonstrate mature thinking by acknowledging trade-offs rather than overselling solutions.

- **Show progression of thinking**: Sander shares how his views evolved (initially skeptical of misalignment, now convinced by chess research and Anthropic studies). In behavioral interviews, demonstrate growth mindset by explaining how your thinking has changed with new evidence.

- **Balance academic rigor with practical execution**: Sander moves fluidly between peer-reviewed research (The Prompt Report, 1,500 papers analyzed) and shipping products (HackAPrompt competition, courses). Show you can both think deeply and execute quickly.

## Related Themes

- AI safety and alignment challenges
- Security vulnerabilities in emerging technologies  
- Crowdsourced problem-solving and competition design
- Research-to-product translation
- Technical communication and education
- Building defensible moats in fast-moving spaces
- Trade-offs between capability and safety
- The future of human-AI interaction patterns
