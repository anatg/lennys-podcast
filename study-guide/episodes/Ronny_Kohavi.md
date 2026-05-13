# Ronny Kohavi — The World Expert on A/B Testing and Experimentation

## Guest Profile
- **Name**: Ronny Kohavi
- **Role/Company**: Former VP and Technical Fellow of Relevance at Airbnb; Former Corporate VP at Microsoft (led Experimentation Platform); Former Director of Data Mining and Personalization at Amazon; Currently full-time advisor and instructor
- **Background**: Widely recognized as the world's leading expert on A/B testing and experimentation. Author of the definitive book "Trustworthy Online Controlled Experiments." Built experimentation platforms at scale at Microsoft (20-25,000 experiments/year), and led search relevance teams at both Microsoft and Airbnb. Teaches cohort-based courses on experimentation via Maven.

## Tags
`Experimentation` `A/B Testing` `Data` `Metrics` `Platform` `Product Strategy` `Leadership` `Culture` `Frameworks` `Execution` `Enterprise` `Consumer` `SaaS`

## TL;DR
Most product ideas fail—80-92% of experiments show no improvement or hurt metrics—making controlled experimentation essential for data-driven decisions. Building trust in your experimentation platform through rigorous checks (like sample ratio mismatch detection) is more important than speed, and requires defining clear OECs (overall evaluation criteria) that balance short-term gains with long-term user value.

## Core Frameworks & Mental Models

- **Overall Evaluation Criterion (OEC)**: Define what you're optimizing for by combining revenue/conversion metrics with countervailing user experience metrics to ensure long-term value, not just short-term gains. Frame as constraint optimization (e.g., "increase revenue within a fixed ad real estate budget") or include guardrail metrics that predict lifetime value.

- **Twyman's Law**: "Any figure that looks interesting or different is usually wrong." When results look too good to be true (e.g., 10% improvement when typical is <1%), investigate for bugs before celebrating. Nine out of ten times, surprisingly large results indicate experimental flaws.

- **Sample Ratio Mismatch (SRM)**: If your 50/50 experiment shows 50.2/49.8 split with a million users, calculate the probability this happened by chance. If it's one-in-half-million odds, something is wrong (often bots, data pipeline issues, or traffic assignment problems). This catches ~8-10% of invalid experiments.

- **Portfolio Approach to Experimentation**: Allocate ~80% of efforts to incremental improvements and ~20% to high-risk, high-reward ideas. Expect the big bets to fail 80% of the time, but recognize breakthroughs when they occur.

- **Hierarchy of Evidence**: Trust levels from lowest to highest: anecdotal → observational studies → natural experiments → controlled experiments → multiple replicated controlled experiments. Always ask where evidence comes from before trusting it.

- **False Positive Risk vs. P-value**: P-value of 0.05 doesn't mean 5% chance of error. At Airbnb search (8% success rate), a p<0.05 result had 26% false positive risk. Use Bayes' rule with historical success rates to calculate true risk. Recommend p<0.01 threshold and replication for borderline results.

## Top Insights (Timeless)

1. **Most ideas fail—and that's normal**: 66% of ideas failed at Microsoft overall, 85% at Bing, 92% at Airbnb search. This isn't poor PM judgment—it's the reality at Google, Booking, and other top companies. Success comes from running many experiments and accepting most will fail.

2. **Small changes can have massive impact**: Bing's biggest revenue win (12% increase, $100M value) came from moving two lines in ad display—an idea that languished in the backlog for months. Opening links in new tabs consistently wins across companies (MSN, Bing, Airbnb). You can't predict which small changes will be breakthrough wins.

3. **Trust is the foundation of experimentation culture**: An experimentation platform serves as both safety net (abort bad changes quickly) and oracle (trustworthy results). Early statistical mistakes (like Optimizely's real-time p-value monitoring inflating false positives to 30%) destroy organizational trust and can "almost get you fired."

4. **Big redesigns usually fail**: Large redesigns with 17 simultaneous changes typically hurt metrics. The sunk cost fallacy ("we invested 6 months") leads to shipping negative results. Instead, decompose into smaller changes tested incrementally, or accept 80% failure rate for big bets.

5. **Test everything, even bug fixes**: Any code change can have surprising impact. The platform should make marginal cost of experiments approach zero. At Microsoft, after initial investment, nobody questioned that everything should be experimented—the cost was negligible.

6. **Countervailing metrics prevent short-term thinking**: You can always increase revenue by adding more ads or sending more emails, but you'll hurt long-term user value. Model the cost of negative actions (e.g., "unsubscribe = $X lost lifetime value") and include in your OEC to optimize for sustainable growth.

7. **Institutional memory requires active documentation**: Run quarterly meetings on "most surprising experiments" (not just winners—surprising losers teach too). Build searchable experiment history. Document patterns like "opening in new tab works" across domains. Without this, organizations forget and repeat experiments.

8. **Start experimenting at 200k users**: Below tens of thousands of users, statistics don't work. At 200k users, you can detect 5-10% effects (appropriate for startups—don't focus on 1% gains early). Build culture and platform as you scale toward this threshold.

9. **Platforms require investment but pay off**: At Microsoft, running 100+ new experiments daily only worked because platform investment drove marginal cost to near-zero. At Airbnb, weaker platforms required many data scientists to compensate. Invest in automation to reduce analyst dependency.

10. **Social features consistently fail**: Microsoft spent 100 person-years on Bing social integration (Twitter, Facebook) with hundreds of negative-to-flat experiments before aborting. Netflix and Airbnb also failed with social features. Document these categorical learnings.

## AI & The Changing PM Role
*(Not a focus of this episode.)*

## Notable Interview Questions Lenny Asked

- "What is maybe the most unexpected A/B test you've run or the most surprising result from an A/B test?"
- "How often do you find one of these gold nuggets just lying around?"
- "What percentage should people expect [experiments] to fail?"
- "Can you be too experiment-driven in your experience?"
- "Is there anything that you ever don't think is worth A/B testing?"
- "When should we start running A/B tests?"
- "What are signs that what you're doing may not be valid if you're starting to run experiments?"
- "What advice do you have for people to actually remember these surprises?"
- "Is there anything you recommend for helping people run experiments faster?"

## Best Quotes

> "I'm very clear that I'm a big fan of test everything, which is any code change that you make, any feature that you introduce has to be in some experiment. Because again, I've observed this sort of surprising result that even small bug fixes, even small changes can sometimes have surprising, unexpected impact."

> "If you go for something big, try it out, but be ready to fail 80% of the time."

> "The key thing is [the Bing ad title experiment] didn't hurt the user metrics. So it's very easy to increase revenue by doing theatrics. Displaying more ads is a trivial way to raise revenue, but it hurts the user experience."

> "We are often humbled by how bad we are at predicting the outcome of experiments."

> "The key word is lifetime value, which is you have to define the OEC such that it is causally predictive of the lifetime value of the user."

> "If in peace time you're wrong two thirds to 80% of the time, why would you be subtly right in wartime, in Covid time?"

> "Trust builds up, it's easy to lose. And so to me, it is very important that when you present this and say, 'This is science, this is a controlled experiment, this is the resolve,' you better believe that this is trustworthy."

> "You don't ship on flat, unless it's a legal requirement. When legal comes along and says, 'You have to do X or Y,' you have to ship on flat or even negative... But legal gave you a framework that you have to work under. Try three different things, and ship the one that hurts the least."

> "Your normal movement of an experiment is under 1% and you suddenly have a 10% movement, hold the celebratory dinner... Nine out of 10, when we call it Twyman's law, it is the case that we find some flaw in the experiment."

## Interview Prep Takeaways
*How to apply lessons from this episode to your own PM interviews:*

- **Demonstrate data-driven humility**: Share stories where your hypothesis failed in an A/B test and what you learned. Interviewers value PMs who accept that most ideas fail and use data to course-correct rather than defend their intuition.

- **Explain how you balance metrics**: Describe how you've thought about short-term conversion vs. long-term retention, or revenue vs. user experience. Use the OEC framework to show strategic thinking about trade-offs.

- **Show platform thinking**: If asked about scaling impact, discuss how you'd invest in experimentation infrastructure to enable the team to run more experiments with less overhead, not just individual feature wins.

- **Reference Twyman's Law**: When discussing experiment results, show you know to investigate surprisingly good results for bugs before celebrating. This demonstrates technical credibility and scientific rigor.

- **Quantify your learning velocity**: Be ready to discuss what % of your experiments succeeded, how you documented learnings, and how you shared surprising results across the org. This shows you build institutional knowledge, not just ship features.

- **Discuss replication and statistical rigor**: If you've run experiments, mention how you handled borderline statistical significance, whether you replicated, and how you thought about false positive rates given your baseline success rate.

## Related Themes
- Data-driven decision making and metrics
- Building experimentation culture and platforms
- Product-market fit validation through testing
- Balancing innovation with incremental optimization
- Statistical literacy for product managers
- Organizational learning and knowledge management
- Platform investment vs. feature development
- Long-term thinking vs. short-term metrics
