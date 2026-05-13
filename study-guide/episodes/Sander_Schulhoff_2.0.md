# Sander Schulhoff — AI Security Researcher & Red Teaming Expert

## Guest Profile
- **Name**: Sander Schulhoff
- **Role/Company**: AI Security Researcher; Creator of Learn Prompting; Organizer of the world's largest AI red teaming competition (HackaPrompt); Instructor at MATS (ML Alignment & Theory Scholars)
- **Background**: Seven years in AI research focused on prompt engineering and adversarial robustness. Created the first comprehensive guide on prompt engineering (Learn Prompting). Ran the first-ever generative AI red teaming competition, which produced a dataset now used by all Frontier Labs and most Fortune 500 companies. His paper on prompt injection won Best Theme Paper at EMNLP 2023 out of ~20,000 submissions. Works with leading AI labs (OpenAI, Anthropic, Google DeepMind) on model defenses and teaches the leading course on AI red teaming and security.

## Tags
`AI/ML` `Security` `Risk Management` `Product Strategy` `Enterprise` `Engineering` `Frameworks` `Execution` `Data` `Platform` `Startup` `B2B` `SaaS`

## TL;DR
AI guardrails and current defenses against prompt injection and jailbreaking fundamentally do not work—the attack space is effectively infinite (one followed by a million zeros), and even state-of-the-art models can be tricked by determined attackers in under an hour. The only reason we haven't seen massive damage yet is limited AI adoption and capability, but as agents gain more power and robotics deploy LLM-powered systems, the risk will escalate rapidly without real solutions beyond classical cybersecurity practices like proper data permissioning and techniques like CAMEL.

## Core Frameworks & Mental Models

- **Jailbreaking vs. Prompt Injection**: Jailbreaking = directly tricking a model (user + model only) to output harmful content. Prompt Injection = tricking a model that has developer instructions/system prompts to ignore those instructions and do something malicious (user + model + developer prompt). Understanding this distinction is critical for evaluating risk.

- **"You can patch a bug, but you can't patch a brain"**: In classical cybersecurity, fixing a bug gives 99.99% certainty it's solved. In AI systems, applying a fix gives 99.99% certainty the problem still exists. AI vulnerabilities can't be eliminated through traditional patching—the model can always be tricked in novel ways.

- **Attack Success Rate (ASR) and Adversarial Robustness**: How to measure AI security. If 100 attacks are thrown at a system and one succeeds, ASR = 1% and the system is 99% adversarially robust. However, with effectively infinite possible attacks (1 followed by a million zeros), even 99% defense leaves infinite vulnerabilities.

- **Adaptive Evaluation**: The only meaningful way to test AI defenses is through adaptive attacks—systems (including humans) that learn and improve their attacks over time. Static datasets of attacks are insufficient because they weren't designed for newer models. Humans remain the most effective adaptive attackers, breaking defenses in 10-30 attempts.

- **CAMEL (Capability-Access Model Enforcement Layer)**: A framework from Google that restricts agent permissions based on user intent ahead of time. If you ask an AI to "send an email to my boss," CAMEL only grants send permissions, not read permissions, preventing prompt injection attacks that try to make it read your inbox. Works when read/write can be separated; fails when both are needed simultaneously.

- **The Intersection of Classical Cybersecurity and AI Security**: The future of security jobs. Classical security focuses on permissioning and containment; AI security understands that models can be tricked into anything. The critical skill is applying both lenses: "Assume this AI is an angry God that wants to hurt you—how do we keep it contained while making it useful?"

## Top Insights (Timeless)

1. **AI guardrails fundamentally don't work and create dangerous overconfidence**. Companies selling guardrails claim 99% effectiveness, but with an attack space of 1 followed by a million zeros, 99% still leaves effectively infinite attacks. In Sander's competitions and research (including work with OpenAI, Anthropic, Google DeepMind), all state-of-the-art defenses get broken by human attackers in under an hour.

2. **The smartest AI researchers at Frontier Labs haven't solved this problem in years—enterprise guardrail companies certainly can't**. OpenAI, Anthropic, and Google employ the world's best AI researchers and haven't achieved meaningful adversarial robustness. If they can't solve it, third-party enterprise vendors claiming to solve it with LLM-based guardrails are making implausible claims.

3. **Automated red teaming "works too well"—it always finds vulnerabilities because all transformer-based systems are vulnerable**. Every chatbot can be tricked into saying something harmful. Running automated attacks just confirms what's already known: the models are breakable. This creates false urgency that drives guardrail sales but doesn't represent novel insights.

4. **Most AI deployments don't actually need security measures**. If you're deploying read-only chatbots that can only affect the user interacting with them, prompt injection isn't a real problem—malicious users can only hurt themselves, and they could get the same harmful outputs from ChatGPT directly. Security only matters when AI systems can take actions or access data beyond the current user.

5. **The real danger emerges with agents, AI browsers, and robotics**. As AI systems gain the ability to send emails, modify databases, browse the internet autonomously, or control physical robots, prompt injection becomes genuinely dangerous. The ServiceNow vulnerability (allowing database CRUD operations and email exfiltration via prompt injection) demonstrates this emerging threat.

6. **Classical cybersecurity techniques (proper permissioning, sandboxing, CAMEL) are the only working defenses**. The MathGPT attack succeeded because code execution happened on the same server as the application. Dockerizing it would have solved the problem completely. Similarly, restricting AI permissions ahead of time (CAMEL) prevents many attacks. Security comes from containment, not from trying to make the AI unbreakable.

7. **The absence of major attacks is due to limited adoption, not security**. Per Alex Komoroske (confirmed by Sander): "The only reason there hasn't been a massive attack yet is how early the adoption is, not because it's secured." As agents proliferate, damage will follow.

8. **Market correction coming for AI security companies**. Many AI security vendors were acquired by classical cybersecurity firms for large sums despite doing little revenue. As enterprises realize guardrails don't work and can be bypassed, and that open-source solutions are better than proprietary ones, the market will correct.

9. **Static datasets and non-adaptive evaluations are meaningless for measuring AI security**. Testing new models with attacks designed for older models doesn't prove robustness. Only adaptive evaluations—where attackers learn and refine their approach—reveal true vulnerabilities.

10. **Offensive adversarial research is no longer helpful—defensive research is desperately needed**. We already know models can be broken in infinite ways. Publishing new jailbreak techniques just gives attackers more tools without improving defenses. The field needs breakthroughs in making models actually robust, not more proof they're vulnerable.

## AI & The Changing PM Role

- **PMs must now think like AI alignment researchers**: When deploying AI features, especially agents, PMs need to adopt the mindset of "assume this AI is a malicious God trying to hurt us—how do we contain it?" This is fundamentally different from traditional product security thinking.

- **The capabilities vs. security tradeoff is shaping product roadmaps**: Frontier Labs prioritize making models smarter over making them more secure because intelligence drives revenue. PMs must navigate this tension—more capable agents create more value but also more risk.

- **PM interviews will increasingly include AI security scenarios**: Understanding prompt injection, jailbreaking, and mitigation strategies (CAMEL, permissioning) is becoming table stakes. Expect questions like "How would you prevent prompt injection in an email-writing agent?"

- **Product permissioning architecture is now an AI security concern**: What used to be a backend/security team problem is now a PM problem. Deciding which actions an AI feature can take, what data it can access, and how to implement CAMEL-like restrictions is product design work.

- **Education and awareness are critical PM skills**: Because technical teams, executives, and security teams may not understand AI's unique vulnerabilities ("you can't patch a brain"), PMs must evangelize these risks and push back against overconfident security claims from vendors.

## Notable Interview Questions Lenny Asked

- "Give us an example of, say, a jailbreak and then maybe a prompt injection attack."
- "Why can't you just add some code in front of this thing of just like, 'Okay, if it's telling someone to write a bomb, don't let them do that'?"
- "How do these companies work with AI products? So say you hire one of these companies to help you increase your adversarial robustness... how do they work together?"
- "This all sounds really great so far... What is the issue?"
- "What can they [CISOs] do? What are some things you recommend?"
- "Is there value in creating friction and making it harder to find the holes?... Why not make it 10% harder, 50% harder, 90% harder?"

## Best Quotes

> "AI guardrails do not work. I'm going to say that one more time. Guardrails do not work."

> "You can patch a bug, but you can't patch a brain. If you find some bug in your software and you go and patch it, you can be maybe 99.99% sure that bug is solved. Try to do that in your AI system. You can be 99.99% sure that the problem is still there."

> "Not only do you have a God in the box, but that God is angry, that God is malicious, that God wants to hurt you. Can we control that malicious AI and make it useful to us and make sure nothing bad happens?"

> "When these guardrail providers say, 'We catch everything,' that's a complete lie... 99% of one followed by a million zeros, there's just so many attacks left. There's still basically infinite attacks left."

> "If someone is determined enough to trick GPT-5, they're going to deal with that guardrail. No problem."

> "If the smartest AI researchers in the world can't solve this problem, why do you think some random enterprise who doesn't really even employ AI researchers can?"

> "The only reason there hasn't been a massive attack yet is how early the adoption is, not because it's secured." *(Alex Komoroske, quoted by Lenny)*

> "Any data that AI has access to, the user can make it leak. Any actions that it can possibly take, the user can make it take."

> "It's easier to tell the model, 'Never do this,' than with emails and stuff, 'Sometimes do this.'"

> "Do not write that jailbreak paper... We know the models can be broken, we know they can be broken in a thousand million ways. We don't need to keep knowing that."

## Interview Prep Takeaways

- **Demonstrate AI security literacy**: In PM interviews, especially for AI products, show you understand the difference between jailbreaking and prompt injection, and that current defenses are limited. This signals sophisticated thinking about risk.

- **Apply the "angry God in a box" framework**: When asked how you'd design an AI feature, especially an agent, walk through: (1) What actions can it take? (2) What data can it access? (3) How do we restrict permissions to minimize damage if it's compromised? (4) Can we use CAMEL-like patterns to separate read/write permissions?

- **Know when NOT to deploy AI**: A strong PM answer is sometimes "we shouldn't build this with AI." If the risk (e.g., agentic access to sensitive data) outweighs the benefit and can't be mitigated with proper permissioning, that's a valid conclusion. Shows judgment.

- **Understand the capabilities vs. security tradeoff**: Be prepared to discuss how you'd prioritize speed-to-market and feature capabilities against security concerns, especially in fast-moving AI markets. Reference that even Frontier Labs prioritize capabilities first.

- **Use technical precision**: Don't say "we'll add a guardrail" as a hand-wavy solution. If asked about AI security, reference specific techniques: proper data permissioning, sandboxing/dockerization, CAMEL for permission restriction, monitoring and logging, human-in-the-loop for high-risk actions.

- **Cite real examples**: The ServiceNow vulnerability, MathGPT API key exfiltration, Comet browser data leaking, Claude Code cyber attacks, Vegas Cybertruck bombing (ChatGPT use) are all recent, real-world examples you can reference to show you're tracking the space.

- **Advocate for cross-functional expertise**: Suggest hiring or partnering with people at the intersection of classical cybersecurity and AI security—this shows you understand resource allocation and team building for emerging risks.

## Related Themes

- AI Risk Management & Governance
- Adversarial ML & Model Robustness  
- Agent Security & Autonomous Systems
- Product Security Architecture
- Enterprise AI Deployment
- AI Alignment & Control Problems
- Emerging Tech Risk Assessment
- Security vs. Velocity Tradeoffs
