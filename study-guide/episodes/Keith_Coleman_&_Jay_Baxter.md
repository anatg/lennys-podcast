# Keith Coleman & Jay Baxter — Community Notes at X

## Guest Profile
- **Name**: Keith Coleman & Jay Baxter
- **Role/Company**: Keith Coleman is Product Lead for Community Notes at X; Jay Baxter is Founding ML Engineer and Researcher for Community Notes
- **Background**: Keith joined Twitter in December 2016 during the company turnaround when Jack Dorsey returned as CEO. He worked under Kayvon Beykpour who approved the Thermal team structure. After paternity leave, Keith proposed working full-time on misinformation solutions, starting the project with just himself doing research and prototyping before building a five-person team. Jay was one of the founding members focused on the ML and research aspects of the algorithm.

## Tags
`Product Strategy` `AI/ML` `Platform` `Execution` `Frameworks` `Org Design` `Leadership` `Growth` `Consumer` `Data` `Culture` `Psychology`

## TL;DR
Community Notes solves misinformation at internet scale by having users write context notes that only show to everyone if rated helpful by people who normally disagree with each other—a bridging-based consensus algorithm that creates neutral, accurate information while being fully transparent with all code and data published openly. The product survived four different leaders (including Jack and Elon) by sticking to core principles: voice of the people not the company, complete transparency, and openness to all humanity, while maintaining extremely high quality bars by showing only ~8% of proposed notes.

## Core Frameworks & Mental Models

- **Community Notes Three-Step Process**: Anyone on X can propose a note on posts they think are misleading; other people then rate that note; notes show to everyone only if found helpful by people who normally disagree with each other. This bridging-based agreement provides strong anti-manipulation properties and creates neutral, accurate content.

- **Thermal Team Structure**: Small focused teams with one clear driver/founder, one clear senior decision-maker, 100% focus on their mission, and freedom to set their own process. The Community Notes team started with just five people: one each for ML, backend, frontend, design, and research—proving that small teams can accomplish more than standard management tracks.

- **Progressive Validation**: Prove the product at every step before proposing expansion. First prove people can find notes helpful, then prove people can write quality notes, then expand from there. Started with Figma mockups tested first, then MTurk pilot, then 1000-person public pilot with low expectations to manage risk.

- **Quality-First Threshold Setting**: Set conservative quality thresholds even if it means not showing some good notes. The worst possible mistake is showing a bad note because that undermines trust in the system. Community Notes shows approximately 8% of notes that get proposed to maintain a very high quality bar—the team lives or dies based on note quality.

- **Bridging-Based Consensus Algorithm**: Uses matrix factorization to identify notes rated helpful by people who have disagreed in the past. When contributors consistently rate notes counter to bridging-based consensus, their ratings stop counting. The algorithm uses a threshold of 0.4 on an arbitrary scale calibrated through user feedback.

- **Milestone-Based Goal Setting**: Set goals for the next milestone that matters, not quarterly or annual cycles. The team meets daily and runs off a single long-running Google Doc for coordination—no Jira, no Asana. Deleting code is more important than writing it when forced to have a small team.

- **Note Matching at Scale**: Notes can be matched to multiple posts with the same image/video—one note can match thousands of posts, enabling the system to work at internet scale even with volunteer contributors.

## Top Insights (Timeless)

1. **Agreement from disagreement proves neutrality**: Looking for agreement from people who have disagreed in the past makes notes neutral, accurate, and well-written. This surprising agreement is what gives Community Notes its power and why it's trusted across the political spectrum.

2. **Transparency enables trust at scale**: All code, data, and ratings are published openly so anyone can replicate and audit the entire system. Back in 2020, most ML engineers would say you have to keep it closed source to prevent manipulation, but openness actually strengthens the system. Vitalik Buterin wrote a blog post verifying the algorithm works as claimed by running it himself.

3. **No exemptions maintains integrity**: Every post is eligible for notes—no exemptions for Elon, government figures, or even advertisers. There is no button at the company to change the status of a note; if it's showing because people rated it helpful, it shows. This principle helped the product survive four different leaders.

4. **Notes dramatically reduce misinformation spread**: Notes cause 30-40% engagement rate drops for likes and reposts in A-B tests; 50-60% drop in total reposts overall. Authors become 80% more likely to delete their post after receiving a note. If a post with a note appears, engagement drops so dramatically (50-60% per generation) that virality quickly goes to zero.

5. **Speed through decentralization beats centralized fact-checking**: During the Israel-Hamas conflict start, 500 notes appeared in first three days covering out-of-context imagery and fake footage. Median time from post to note showing was five hours, versus typical fact-checking taking 2-4 days. The system produced more notes than professional fact-checkers could have in weeks.

6. **Self-selection and small teams drive exceptional results**: Everyone on the team opted in and was interviewed; no one was assigned. Working in a small focused team allows accomplishing much more than through standard management tracks. The team shipped every week during the acquisition period despite many opportunities for distraction.

7. **External validation proves effectiveness**: External studies show people's agreement with core claims in posts changes when they see it with or without a Community Note. A White House tweet was deleted and reissued with updated statement after receiving a Community Note, demonstrating real-world impact.

8. **Contributor motivation is intrinsic**: Approximately 950,000 contributors around the world participate as volunteers, motivated by intrinsic desire to have better information in the world. Contributors need verified phone numbers but selection is otherwise random to anyone who signs up. Contributors must earn the ability to write notes by demonstrating they can identify notes helpful to a broad range of people.

9. **Pseudonymity enables crossing partisan boundaries**: People are more willing to cross partisan boundaries when anonymous or pseudonymous than when using their real names. Pseudonymity allows freedom for honesty while maintaining quality through other mechanisms in the system, similar to how making likes private enables more authentic engagement.

10. **The 80% agreement insight**: While society feels polarized, there's probably an 80% set of people who agree on quite a lot of things, even on controversial topics. Community Notes proves that facts matter and there are facts people can agree on even on the most controversial topics, countering the belief that everything has become subjective.

## AI & The Changing PM Role

- **Supernotes uses LLMs strategically**: Instead of having AI write notes from scratch, Supernotes uses LLMs to generate variants of existing proposed notes, then simulates the community notes rating process with a representative jury of contributors to predict ratings. This creates notes likely to be rated helpful while maintaining human judgment as the quality bar.

- **AI agents as verification assistants**: There's potential for AI agents to assist by browsing the web and checking whether notes are supported by sources, but this requires careful design so raters remain diligent and verify before rating helpful. The human verification step remains critical to maintain quality.

- **The dream of open-source AI contributions**: The team envisions the product being built by the people, not just contributed to by them—potentially having the scoring algorithm significantly or entirely written by the public through open source contributions, extending the community-driven model to the product itself.

## Notable Interview Questions Lenny Asked

- "How does Community Notes actually work?" (prompting explanation of the three-step process)
- "What is a Thermal team?" (uncovering the organizational structure that enabled success)
- "How do you prevent manipulation of the system?" (exploring the anti-gaming mechanisms)
- "What happened during major events like the Israel-Hamas conflict?" (testing the system under pressure)
- "Why did you decide to make everything open source?" (challenging conventional wisdom about transparency)
- "How did the product survive multiple leadership changes?" (understanding resilience through principles)

## Best Quotes

> "We actually look for agreement from people who have disagreed in the past. And what we see is when people actually have that sort of surprising agreement, that's what makes the notes so neutral and accurate and well-written, really, overall."

> "Every post is eligible for notes. We shouldn't exempt Elon. We shouldn't exempt government figures. We should be like everyone... Even advertisers can get notes."

> "If I were to start a company in that company, it would be even leaner than I would've made it before. I've been amazed with just how much the team is able to accomplish with a small group."

> "We live or die based on the quality of the notes at the end of day."

> "We view the worst possible mistake as showing a bad note because that's going to undermine trust and the trust is why people like the product."

> "There is no button at the company to change the status of a note. If it's showing because people rated it helpful, it shows."

> "Community Notes proves that facts matter and there are facts people can agree on even on the most controversial topics."

> "Imagine being the person who wrote that. You probably have 12 followers. Your posts probably get a couple likes. And here, you just put a note on the White House and they changed their public talking points based on what you did."

> "Back in 2020 before we started building anything here, I think a room of ML engineers would say, 'Oh, you have to keep it closed source. People are going to be manipulating this all the time.'"

> "The goal is just to get people more information about what they're seeing so they can make better decisions in their lives."

## Interview Prep Takeaways

**How to apply lessons from this episode to your own PM interviews:**

- **Demonstrate quality-first thinking**: When discussing product decisions, emphasize how you set conservative quality bars and prioritize trust over short-term metrics. Explain trade-offs where you chose to show less content or fewer features to maintain quality standards.

- **Show progressive validation methodology**: Walk through how you proved a product concept at each step before expanding. Use phrases like "first we proved X, then we proved Y" to demonstrate rigorous validation thinking that reduces risk.

- **Explain anti-manipulation design**: When discussing platform or social products, articulate how you thought about preventing abuse and gaming. Show you consider adversarial users and design systems that are robust against manipulation.

- **Quantify impact with A/B test results**: Use concrete numbers like "30-40% engagement drop" or "80% more likely to delete" to show you measure real behavioral changes, not just vanity metrics. This demonstrates rigorous experimentation culture.

- **Articulate team structure philosophy**: Be ready to discuss optimal team sizes and structures. Reference concepts like clear decision-makers, 100% focus, and freedom to set process—showing you understand how organizational design enables execution.

- **Balance transparency with pragmatism**: Discuss when you'd make systems open versus closed, and why. Show you can challenge conventional wisdom (like "keep ML closed to prevent gaming") when evidence supports a different approach.

- **Connect product principles to survival**: Explain how sticking to core principles (like "no exemptions") helps products survive organizational changes and builds long-term trust, even if it creates short-term friction with stakeholders.

- **Describe milestone-based planning**: Show you can work outside rigid quarterly planning cycles when appropriate. Demonstrate flexibility in goal-setting while maintaining clear focus on what matters most.

## Related Themes

- Platform integrity and trust & safety systems
- Crowdsourced content moderation and community-driven products
- ML algorithm design for social good and bridging divides
- Small team execution and organizational design
- Misinformation and media literacy at internet scale
- Open source transparency in sensitive systems
- Pseudonymity versus real names in online communities
- Progressive validation and risk management in product development
