# Simon Willison — Co-creator of Django, AI Security Researcher, and Creator of Datasette

## Guest Profile
- **Name**: Simon Willison
- **Role/Company**: Independent open source developer and AI security researcher; Creator of Datasette
- **Background**: 25-year software engineering career; co-created Django (web framework powering Instagram, Pinterest, Spotify); coined the term "prompt injection"; popularized "AI slop" and "agentic engineering"; maintains 100+ open source projects; builds tools for data journalism

## Tags
`AI/ML` `Engineering` `Product Strategy` `Leadership` `Career` `Frameworks` `Execution` `Data` `Startup` `Communication` `Culture` `Vision`

## TL;DR
In November 2024, coding AI agents crossed a threshold from "mostly working" to "almost always doing what you tell them to do," enabling experienced engineers like Simon to produce 95% of their code through AI while using every inch of their 25 years of expertise to direct it effectively. However, this shift creates a dangerous gap where mid-career engineers lack both the beginner's onboarding advantage and the senior engineer's ability to amplify their skills, while the normalization of "vibe coding" without proper testing practices threatens a Challenger-level disaster in software engineering.

## Core Frameworks & Mental Models

- **Agentic Engineering**: The discipline of using coding agents to build professional-quality software that can be deployed to production. Distinct from "vibe coding" where you don't look at or care about the code. Requires applying professional practices and quality expectations to code you're not directly reviewing—what Simon calls the "dark factory pattern."

- **Red/Green TDD (Test-Driven Development)**: Write the test first, watch it fail (red), implement code, then watch it pass (green). This programming jargon is understood by AI agents and produces significantly better results. AI agents excel at maintaining test suites because they don't get bored with testing, making TDD practices that frustrated human programmers work exceptionally well with agents.

- **Start New Projects with Good Templates**: Coding agents are phenomenally good at sticking to existing patterns in code, so a thin skeleton template gives enough hints for the agent to maintain your preferred style throughout the project.

- **The Lethal Trifecta (Prompt Injection Security)**: Three required elements for a dangerous prompt injection attack: (1) access to private information, (2) exposure to malicious instructions, and (3) an exfiltration mechanism. All three must be present for serious security consequences.

- **CaMeL Paper Solution**: Split agents into a privileged agent that can execute actions and a quarantined agent exposed to malicious instructions but can't act directly, with human approval required for high-risk activities tracked through tainted data flows.

## Top Insights (Timeless)

1. **Code is the easiest problem for AI to solve** because code is obviously right or wrong—you run it and either it works or it doesn't. This makes software engineers the bellwether for other information workers; AI came for them first, and other knowledge work will follow similar patterns.

2. **Using coding agents well takes every inch of expertise** from Simon's 25 years as a software engineer and is mentally exhausting. Running four agents in parallel and managing them can leave you wiped out by 11 AM, despite the popular narrative that AI makes work easier.

3. **Mid-career engineers are in the most trouble right now**—not beginners (who get huge onboarding boosts from AI assistants) and not super senior engineers (who can amplify their skills). Mid-level engineers lack both the beginner's advantage and the senior's ability to effectively direct and verify AI output.

4. **Prototyping is now almost free**, allowing you to knock out three different UI prototypes quickly to experiment and see which works best. Since the thing that used to take the most time (writing code) now takes way less time, all other bottlenecks become more important—decision-making, design choices, and strategic direction.

5. **25 years of experience in estimating how long things take to build is now completely obsolete**. Simon can churn out 10,000 lines of code now in the time it would take him to write 100, fundamentally changing project planning and capacity forecasting.

6. **The AI labs focused all their 2025 training efforts on coding** because people were willing to pay $200/month for it, creating a strong commercial incentive. There's a strong correlation between how well a model draws a Pelican riding a bicycle in SVG and how good it is at everything else—coding capability is a general intelligence proxy.

7. **Once you start vibe coding for other people where bugs might harm them, you need to take a step back**—that's irresponsible. Understanding what's responsible and what isn't is itself an expert-level skill that many practitioners lack.

8. **The normalization of deviance will catch up with us**. Simon's prediction: "We've been using these systems in increasingly unsafe ways, this is going to catch up with us. My prediction is that we're going to see a Challenger disaster" in software engineering from inadequate testing practices.

9. **AI agents have no agency at all**—they can never decide what makes sense to act on next because they lack human motivations. People use agency to decide what problems to take on and where to go; the one thing AI can never have is agency because it doesn't have human desires, fears, or goals.

10. **The only universal skill right now is being able to roll with the changes**. The recruitment market has been driven completely crazy by AI—job ads are AI-written, resumes are AI-written—making it harder than ever to filter and hire, even as open roles approach record numbers.

## AI & The Changing PM Role

Simon's insights have direct implications for product managers:

- **StrongDM's swarm of agent testers** simulate end users in fake Slack channels 24/7, spending $10,000/day on tokens to test their access management software. They built simulated versions of Slack, Jira, and Okta using API documentation to avoid rate limits, with a policy where nobody reads the code—relying entirely on automated testing.

- **Cloudflare and Shopify both hired 1,000 interns in 2025** because AI assistants reduced onboarding time from a month to a week, fundamentally changing hiring strategies and team composition.

- **Some companies are introducing policies where nobody writes any code**—it all must be written by AI, representing an extreme version of the dark factory pattern.

- **The recruitment and hiring crisis** means PMs need new ways to evaluate candidates when both job descriptions and applications are AI-generated, making traditional screening methods obsolete.

- **OpenClaw demonstrates enormous demand** for personal digital assistants despite security concerns—hundreds of thousands of people set it up despite non-trivial technical requirements, showing product-market fit even in risky categories.

- **Journalists are well-equipped to work with AI** because they're trained to deal with unreliable sources—they can treat AI as yet another source that needs verification. This verification mindset is increasingly essential for PMs evaluating AI-generated insights.

## Notable Interview Questions Lenny Asked

- How are you thinking about your own career and how you work with these tools?
- What percentage of code that you write today did you not type yourself?
- Can you describe a typical day or typical week for you now?
- Why can't we just solve prompt injection with more AI detection?
- What's your take on OpenClaw and the security implications?
- How do you think about the job market and career advice for people listening?

## Best Quotes

> "A lot of people woke up in January and February and started realizing, 'Oh wow, I can churn out 10,000 lines of code in a day.'"

> "Today probably 95% of the code that I produce I didn't type it myself."

> "Using coding agents well is taking every inch of my 25 years of experience as a software engineer."

> "By 11:00 AM, I am wiped out."

> "We've been using these systems in increasingly unsafe ways, this is going to catch up with us. My prediction is that we're going to see a Challenger disaster."

> "AI's supposed to make us more productive. It feels like the people that are most AI-pilled are working harder than they've ever worked."

> "The thing that used to take the time takes way less time."

> "I write so much of my code on my phone, it's wild. I can get good work done walking the dog along the beach."

> "People, human beings have agency and we use that agency to decide what problems to take on and where to go. I think agents have no agency at all."

> "The one thing AI can never have is agency because it doesn't have human motivations."

> "I hate doing this [TDD]. There are a lot of programmers believe that this is the one true way to write software. I tried it for a couple of years. It just slowed me down and frustrated me."

> "If you can build safe OpenClaw, if you can deploy a version of OpenClaw that does all the things people love about it and won't randomly link people's data and delete their files, that's a huge opportunity."

## Interview Prep Takeaways

_How to apply lessons from this episode to your own PM interviews:_

- **Demonstrate you understand the productivity paradox**: Don't just say "AI makes us more productive"—show you understand that while AI reduces coding time, it increases cognitive load, shifts bottlenecks to decision-making, and requires deep expertise to use responsibly. Reference how the thing that used to take the time now takes way less time, making other factors more important.

- **Know the difference between vibe coding and agentic engineering**: In interviews discussing AI tools, distinguish between irresponsible "vibe coding" and professional "agentic engineering" that maintains quality standards. Show you understand when each is appropriate and the risks of using AI irresponsibly in production.

- **Use concrete examples of AI in production**: Reference real implementations like StrongDM's $10,000/day agent testing swarm or Cloudflare's 1,000-intern hiring surge. These demonstrate you follow how leading companies actually deploy AI, not just theoretical possibilities.

- **Address the mid-career gap thoughtfully**: When discussing team composition or hiring, acknowledge that AI creates different advantages for junior (faster onboarding) and senior (skill amplification) engineers, while mid-career engineers face unique challenges. Show you've thought about supporting all career levels.

- **Speak to security and safety concerns**: Reference prompt injection, the normalization of deviance, and the predicted "Challenger disaster" in software to show you think critically about AI risks, not just benefits. Understanding the lethal trifecta shows technical depth.

- **Demonstrate adaptability as your universal skill**: When asked about career advice or personal growth, emphasize rolling with changes rather than mastering specific tools. The landscape is shifting too fast for fixed expertise; adaptability is the only constant.

## Related Themes

- Engineering productivity and velocity measurement
- AI coding assistants and developer tools
- Hiring and onboarding in the AI era
- Security and responsible AI deployment
- Career development for software engineers
- Test-driven development and quality practices
- Open source development and community building
- Data journalism and investigative reporting tools
