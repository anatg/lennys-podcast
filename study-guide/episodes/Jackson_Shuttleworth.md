# Jackson Shuttleworth — Group PM at Duolingo (Streaks Deep Dive)

## Guest Profile
- **Name**: Jackson Shuttleworth
- **Role/Company**: Group Product Manager, Retention Team at Duolingo
- **Background**: Former management consultant who flew weekly for 6 years. Joined Duolingo ~4 years ago, leading the team responsible for the company's most impactful feature: streaks. Oversees 600+ experiments on streaks over 4 years. Based in Kansas City, proud Midwesterner learning French on Duolingo.

## Tags
`Product Strategy` `Growth` `Experimentation` `Consumer` `Metrics` `Psychology` `Retention` `Gamification` `Culture` `Frameworks` `Data` `Execution` `PLG`

## TL;DR
Jackson Shuttleworth reveals how Duolingo's streak feature—the most impactful driver of the company's $14B valuation after the core product—was built through relentless experimentation (600+ tests in 4 years). The key insights: simplicity beats complexity, revealed behavior trumps stated preferences, loss aversion is powerful but must be balanced with flexibility, and users care about features proportionally to how much the company signals they matter.

## Core Frameworks & Mental Models

- **CURR (Current User Retention Rate)**: Duolingo's north star engagement metric measuring users who aren't new or resurrected returning tomorrow. Percentage changes in CURR drive the most DAU growth. Focus retention work on this metric rather than vanity metrics.

- **Flexibility vs. Perfection Balance (The Serenity Prayer Framework)**: "Grant me the serenity to accept the flexibility I need, the courage to reach perfection when I can, and the wisdom to celebrate regardless." Balance giving users flexibility (streak freezes) with celebrating perfection (perfect streak status) to avoid cheapening the core mechanic.

- **Unit of Use Clarity**: Define the atomic unit of meaningful engagement in your product (for Duolingo: one lesson). Build streaks around this unit, not arbitrary metrics like experience points. The unit must be comprehensible and actually represent the habit you're building.

- **0-7 Day Onboarding Window**: Loss aversion kicks in at day 7. Invest disproportionately in getting users from 0-7 days (where retention jumps are massive with each day) vs. optimizing for long-streak users where gains plateau.

- **Test It vs. Debate It Philosophy**: When you have sufficient user base, run the experiment rather than debate in conference rooms. Copy tests are especially cheap—translate strings and test constantly. About 50% of Duolingo experiments lose, but they learn from all of them.

- **Simplest V1 Hypothesis Testing**: Strip away all bells and whistles to test core hypothesis first. Add complexity iteratively only after validating the foundation. This enables faster shipping, clearer learning, and easier pivots.

## Top Insights (Timeless)

1. **Streaks are engagement hacks layered on core value**: The streak only works because people genuinely want to learn languages. Don't build streaks to solve fundamental product-market fit problems. If users don't want to use your app daily, a streak won't save you—fix the core experience first.

2. **Simplicity drives comprehension drives retention**: The shift from XP-based streaks to "do one lesson" was a massive win. The calendar needs to look like a calendar. The number matters more than the flame metaphor. Every design choice should clarify "what is this feature tracking?" Don't sacrifice clarity for cleverness.

3. **Revealed behavior > stated preferences**: Users said they wanted to set their own practice reminder times. But 23.5 hours after their last session (when they actually practiced yesterday) beat any self-selected time. Similarly, removing user-set XP goals for simple "one lesson" goals won big.

4. **Making streaks easier to extend doesn't always win**: Testing "one exercise extends streak" (vs. one full lesson) was flat on DAUs—it captured the least engaged users who wouldn't stick anyway and dumbed down the meaningful unit of use. Sometimes making things "too easy" backfires.

5. **Intentionality creates commitment**: Adding an opt-out button to streak goals (letting users say "no") was a huge win even though it meant some users didn't engage. The act of consciously choosing "yes, I want to commit to 30 days" created much stronger engagement than a passive "continue" button.

6. **Give more flexibility early, less flexibility later**: Two streak freezes (insurance days) beat one or three. Give new users (days 0-7) more flexibility to prevent early abandonment. Long-streak users need less flexibility—they're committed, and too much flexibility trains them to take unnecessary time off.

7. **Users care about what you signal matters**: "The reason users care about your streak so much is because you care about your streaks so much." Big animated celebration screens, push notifications, prominent placement—all signal importance. If you hide a feature in a corner, users won't care about it.

8. **Micro-copy changes drive massive wins**: Changing "Continue" to "Commit to My Goal" was a massive DAU win. Eight words explaining how streaks work when users start one was Jackson's first major win at Duolingo. Test copy constantly—it's cheap and high-impact.

9. **23.5-hour timing unlocks daily habits**: Send practice reminders 23.5 hours after last use (not at user-selected times). This catches users when they're likely available based on revealed behavior and creates true daily rhythm.

10. **Animation and haptics increase feature investment**: Celebrations make users pause and soak in the moment (vs. rushing through). The longer they linger on the streak screen appreciating the milestone, the more they care about maintaining it tomorrow.

11. **Process enables velocity**: Running 600+ experiments in 4 years (every other day) requires heavy Jira automation, detailed roadmaps mapping dependencies across functions months out, and design/engineering/product synchronized to eliminate idle cycles.

12. **Protect feature sanctity with a "keeper"**: Have someone (Jackson's co-lead Antonia) who guards against cheapening the core mechanic. It's easy to win short-term by making streaks easier, but you risk a "one-way door" where millions of engaged users suddenly stop caring.

## AI & The Changing PM Role
*(Not a focus of this episode.)*

## Notable Interview Questions Lenny Asked

- "For people that don't know anything about what Duolingo streaks are, can you just first give a brief explanation of what is this feature all about?"
- "Give people a sense of the impact that this one feature has had on Duolingo's success and growth."
- "Talk about how this feature originally came to be. What was the original version of it? What was the original insight?"
- "Let's get into the motherload of learnings from the journey of streaks, talk about the key lessons, insights, and also wrong turns along the way."
- "Is there an example of an experiment that was positive that you all decided, no, we don't actually think this is what we want in the product, they ended up not shipping?"
- "What are some maybe lessons or advice you'd have for folks that want to work more like this, from your team's experience?"

## Best Quotes

> "Streaks is the most impactful feature. We have, right now, over 9 million users with a year plus streak... I think it's been our biggest growth lever."

> "Getting user come back the next day is the biggest problem to solve."

> "The easiest way not to learn on Duolingo is not to come back the next day."

> "We've run in the last four years over 600 experiments on the streaks, so every other day... I'd say test everything."

> "The reason why users care about your streak so much is because you care about your streaks so much."

> "Streaks are an engagement hack... But if your app is not something that users want to use every day, you're just going to waste a lot of time."

> "Don't get too caught up in the philosophy of everything... my recommendation is just try things. This is as much human psychology as anything."

> "We'd much rather test it than debate it for days and days."

> "The streak, it just counts up, you guys have been testing on it for years, how much more work can we do on the streak? And [Anton] was like, Jackson, you child... we're not even 30% of the way optimized."

> "Form should follow function... don't get too caught up into what is the beautiful story that you're trying to tell, at the expense of it being a really comprehensible feature."

## Interview Prep Takeaways

- **Demonstrate metric-driven thinking**: When discussing features you've built, lead with the business metric impact (e.g., "drove X DAUs" or "improved 7-day retention by Y%") and the metric you were optimizing for, not just feature descriptions.

- **Show experimentation rigor**: Discuss your hypothesis testing approach—how you stripped down to simplest V1, what you learned from losses (not just wins), and how you iterated. "We run 50% loss rate on experiments but learn from all of them" shows mature product thinking.

- **Explain user psychology depth**: Go beyond surface-level "users liked it"—discuss behavioral insights like loss aversion, revealed vs. stated preferences, intentionality creating commitment. Shows you understand *why* things work.

- **Balance flexibility and conviction**: Demonstrate you test aggressively ("test it vs. debate it") but also have conviction about protecting core value (the "keeper" role, knowing when not to ship a win that cheapens the experience).

- **Quantify everything**: Don't say "it was a big win"—say "10,000+ DAUs" or "top 3 CURR win." Interviewers want to see you think in absolute numbers and can translate percentages to business impact.

- **Show cross-functional orchestration**: Describe how you coordinated design, engineering, product roadmaps to maintain velocity. Process isn't sexy but enables 600 experiments in 4 years—that's a competitive advantage.

## Related Themes

- Retention mechanics and loss aversion psychology
- Metric-driven product development (CURR optimization)
- Experimentation culture and velocity at scale
- Consumer product gamification strategies
- Simplicity vs. complexity in feature design
- Behavioral nudges and habit formation
- Copy testing and micro-optimizations
- Product review processes and founder involvement
- Cross-functional team orchestration for speed
