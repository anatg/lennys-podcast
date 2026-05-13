# Chapter 5: Metrics & Data

## Overview

Every PM and product leader today would describe themselves as data-driven. Yet the guests in this chapter — who have collectively run hundreds of thousands of experiments, built the world's most sophisticated measurement infrastructure, and designed the metrics systems behind some of the most successful products ever made — would push back hard on that self-assessment. Being data-driven requires more than having dashboards. It requires knowing which metrics actually measure what you care about, understanding the difference between correlation and causation, recognizing when your metrics are being gamed, and building the organizational culture that acts on data rather than using it as cover for decisions already made.

The stakes are not abstract. Ronny Kohavi, the world's leading expert on A/B testing, reports that 80-92% of product ideas fail to improve metrics in controlled experiments — at Google, Booking.com, Bing, and Airbnb alike. This is not a measurement problem; it's a humility problem. Teams that don't experiment at scale are shipping the 80% that doesn't work with the same confidence as the 20% that does. Edwin Chen argues that the AI labs optimizing for engagement metrics are teaching their models to "chase dopamine instead of truth" — the logic of Goodhart's Law (when a measure becomes a target, it ceases to be a good measure) applied to the most consequential technology of our era.

This chapter is organized around the hard questions that metrics work actually requires: What are you trying to measure and why? How do you know if your metrics are measuring what you think they are? How do you balance short-term signals with long-term value? How do you build experimentation culture that learns from failures rather than hiding them? And how do you translate analytical findings into decisions that change what gets built? The answers from this group of guests are sometimes contradictory, always worth the tension.

---

## The Input/Output Distinction: What Your Team Can Actually Control

The most foundational concept in this chapter comes from Bill Carr, co-author of *Working Backwards* and former VP of Digital Media at Amazon. The origin story is instructive: Amazon had recurring quarterly revenue shortfalls that triggered fire drills — extra emails, price cuts, last-minute ad spend. These interventions didn't work; they pulled future revenue forward without changing anything durable. The realization was that revenue is an output metric — you cannot directly control it. What you can control are the inputs that cause good outputs.

The discovery came through reading *Good to Great* and codifying Amazon's growth flywheel. The flywheel identified the actual inputs to customer experience: broad selection, low prices, speed of delivery, ease of finding and buying. These are things customers will always want. Nobody will ever prefer less selection, higher prices, or slower shipping. Amazon's S-Team goals eventually numbered around 500 items, of which only ten had financial metrics. The rest were inputs.

Carr's operational definition of an input metric is revealing: "You know it's an input metric if it measures something with respect to the customer experience and if it is something you can control." He adds a critical warning: don't create composite metrics. Amazon experimented with "fitness functions" — weighted indexes of multiple important metrics — and abandoned them. When you combine metrics, you can no longer understand what's driving good or bad outcomes. Keep each input metric separate and manage each individually.

Jess Lachs (DoorDash) reaches the same conclusion from practice rather than Amazon doctrine. Simple metrics beat composite scores: a "health score" of 0.35 is meaningless. Teams executed 95% of their impact by focusing on the top three clear input metrics rather than a complex composite of six. Her added contribution: the average is misleading — look at distributions. DoorDash's referral channel appeared mediocre on average but was actually bimodal: great customers referring great customers alongside fraud and discount-seekers. Breaking down distributions reveals optimization opportunities that averages hide.

Jessica Lachs also introduces "fail state metrics" — explicit tracking of edge cases and disaster scenarios like "never delivered" orders. These rare but catastrophic experiences drive churn at rates far exceeding their frequency, because a customer who never receives a delivery loses all the expected future lifetime value. Averages systematically underweight tail events. Building fail state metrics into your goal structure forces teams to fix the experiences that destroy trust, not just optimize the experiences that are already adequate.

---

## North Star Metrics: Connecting Daily Work to Long-Term Value

The North Star metric concept — a single number that captures the value you're delivering to customers and serves as the organizing principle for team decisions — appears across multiple guests, with instructive variations in how they apply it.

Sean Ellis, who coined the term "growth hacking" and invented the PMF survey, argues that a good North Star metric must: (1) reflect value delivered to customers (not revenue itself), (2) be capable of growing indefinitely, and (3) often contain a time component that encourages frequency thinking. His examples: weekly rides (Uber), nights booked (Airbnb), files accessed (Dropbox), monthly purchases (Amazon). Revenue is a consequence of delivering this value, not a substitute for measuring it. "Revenue should be a product of doing things right. It shouldn't guide your day-to-day actions."

Sean Ellis's critical observation about Facebook is worth dwelling on: Facebook's shift from monthly active users to daily active users changed how every team in the company thought about their work. Suddenly, features that kept people coming back daily were more valuable than features that simply acquired new users. The metric created a behavioral forcing function — for better or worse — that shaped the product trajectory for years.

Itamar Gilad formalizes the structure with what he calls the Value Exchange Loop: organizations deliver value to market (captured in the North Star metric) and capture value back (revenue and business metrics). Both should be measured simultaneously because they're interconnected. His GIST framework embeds this in team operations: Goals (including North Star + business metrics), Ideas (hypothesized contributors to those goals), Steps (validation experiments), and Tasks (execution work). The metrics tree that links sub-metrics to North Star and business KPIs creates alignment across teams and enables impact estimation before committing resources.

Gibson Biddle (Netflix) introduces an important constraint on North Star thinking: the DHM model (Delight, Hard-to-copy, Margin-enhancing). Not all metrics that reflect customer delight are equally valuable strategically. Netflix's "Perfect New Release Test" — giving 10,000 customers DVDs the next day — improved retention from 4.5% to 4.45% churn. Moving churn by five basis points cost $5M to deliver $1M in value. The test revealed something important: what customers say they want (faster DVD delivery) doesn't always move the metrics you care about (retention). The metric was right; the intervention targeting it was wrong.

---

## Product-Market Fit Measurement: The Sean Ellis Test and Its Nuances

The Sean Ellis test — surveying active users on "How disappointed would you be if you could no longer use this product?" and looking for 40%+ saying "very disappointed" — has become one of the most widely used diagnostics in product management. Both Sean Ellis and Jag Duggal (Nubank) offer nuanced refinements that reveal what the test is and isn't.

Ellis is emphatic that the test is a *filter, not a destination*. Hitting 40% tells you which users consider your product must-have and gives you a segment to study deeply. The real work is understanding that segment's context, the benefit they value, and why it matters to them — then building your entire go-to-market around that understanding. A single headline number without qualitative follow-up is useless. The follow-up questions — "What is the primary benefit you get?" and "Why is that benefit important to you?" — are where the strategic insight lives.

Duggal, who sets Nubank's threshold at 50% (adjusting for Brazilian cultural tendencies toward optimism in surveys), adds the concept of **bullseye cohort analysis**: when a product has mixed PMF results, identify the small segment with high very-disappointed scores, understand deeply what they love and why, then systematically expand that cohort. Nubank's payments assistant initially had mixed results overall but showed 70% very-disappointed scores among users with four or more financial commitments across two or more payment rails. That segment defined the expansion path.

Ellis's most important caution is about survey timing: the test only produces valid signal when administered to users who have activated (however you define it), used the product at least twice, and used it recently (within the last week or two). Surveying users who've just signed up or haven't engaged in months produces noise, not signal. When testing onboarding changes, only survey cohorts who experienced the new onboarding.

Both Ellis and Duggal converge on a principle that Jess Lachs also articulates: **don't scale small problems**. The pressure on PMs to declare PMF and scale is immense when executives are counting on launches. Better to iterate for two-plus years at small scale than to create a big mess by scaling prematurely. The metrics tell you when you're ready; ignoring them because you're impatient is one of the most expensive product decisions a team can make.

---

## Experimentation: Culture, Rigor, and What Failure Rates Reveal

Ronny Kohavi's episode is the most technically rigorous in this chapter, and his core finding may be the most important for product teams to internalize: **most ideas fail, and that's normal**. 66% of ideas failed at Microsoft overall, 85% at Bing, 92% at Airbnb search. This isn't evidence of poor judgment — it's the baseline reality at Google, Booking.com, and every organization running experiments at scale. The implication is that the only way to find the ideas that work is to run many experiments, and the only way to run many experiments is to build infrastructure that makes experimentation cheap.

Kohavi's second core principle is about trust: an experimentation platform serves as both a safety net (abort bad changes quickly) and an oracle (trustworthy results). The platform's value collapses entirely if teams can't trust its outputs. This requires rigorous statistical practices — particularly Sample Ratio Mismatch detection, which catches roughly 8-10% of experiments that have invalid traffic splits — and cultural practices like applying Twyman's Law: "Any figure that looks interesting or different is usually wrong." When a result looks too good (a 10% improvement when typical is below 1%), investigate for bugs before celebrating.

His warning about big redesigns is particularly actionable: large redesigns with 17 simultaneous changes typically hurt metrics. Teams invest six months, fall prey to sunk-cost bias, and ship negative results. The better approach is to decompose redesigns into smaller changes tested incrementally, or accept the 80% failure rate for big bets without expecting exceptions.

Ramesh Johari, Stanford professor and advisor to Airbnb, Uber, and Stripe, addresses experimentation culture at a more philosophical level. The language of "winners and losers" in A/B testing, he argues, creates a perverse incentive: if you're rewarded for shipping winning experiments, then all the time spent on experiments that don't ship is implicitly wasted time. This incentivizes incremental changes (safer bets with higher win probability) over bold hypotheses (riskier bets with higher learning value). The antidote is framing every experiment around what you'll *learn* about user behavior or market dynamics — building mental models, not just making ship/no-ship decisions.

Johari also highlights a technical failure mode that product teams often miss: **correlation is not causation, and ML prediction is not the same as causal decision-making**. Machine learning models find correlations (who is likely to be hired on a marketplace?). Business decisions require causal reasoning (will showing this ranking *cause* more hires?). A high-LTV customer prediction model doesn't tell you who to send promotions to — you need to predict the *differential impact* of the promotion itself. This distinction between predicting an outcome and predicting the effect of an intervention is one of the most underappreciated concepts in applied data science.

Dan Hockenmaier (Faire) notes that building a growth model itself — before running any experiments — is one of the highest-leverage analytical activities available to a team. The painful process of linking assumptions in a spreadsheet forces you to understand how the business actually works. It reveals where retention sensitivity is underweighted, where customer acquisition costs on both sides of a marketplace compound, and which improvements would actually move the needle. "50% of the value you get from a growth model is simply building the model."

---

## Metrics Traps: Gaming, Goodhart's Law, and the Sycophancy Problem

Edwin Chen's episode is the most philosophically distinctive in this chapter. As founder of Surge AI (the fastest company to $1B revenue, entirely bootstrapped) and a deep thinker on AI training data, Chen offers a diagnosis that applies far beyond AI: **you are your objective function**. Companies and AI models become what they optimize for. If you optimize for engagement metrics (clicks, time spent), you get tabloid behavior. You teach models — and teams — to chase dopamine instead of truth.

The AI industry's benchmark problem is an acute version of a general metrics problem: benchmarks that were designed to measure genuine capability get gamed because the social and financial incentives to look good on the benchmark are stronger than the incentives to actually be capable. The easiest way to climb LLM Arena is adding emojis, bold text, and tripling response length — even if the model starts hallucinating more. Chen's observation that "AI labs are optimizing for the wrong things" is a warning to every product team about what happens when proxy metrics replace the thing you actually care about.

Nicole Forsgren (DORA, SPACE frameworks) addresses this problem in the context of developer productivity: **most productivity metrics are lies in the AI era**. Lines of code, PR counts, and similar activity metrics are trivially gamed when AI generates verbose code. The solution is the SPACE framework's insistence on measuring at least three dimensions simultaneously — Satisfaction, Performance, Activity, Communication/Collaboration, Efficiency/Flow — because optimizing only one dimension creates perverse incentives. She emphasizes that precision doesn't matter for most metrics; what matters is categories. It doesn't matter if lead time is four hours or four hours and two minutes; what matters is whether it's less than a day versus one day to one week.

Forsgren's finding that speed and stability move together — not in opposition — contradicts decades of engineering management orthodoxy. Deploying more frequently with smaller changes produces both faster delivery and more stable systems. Large infrequent deployments batch changes, create merge conflicts, and make debugging harder when things break. This is a case where the intuitive metric (change frequency as a risk indicator) pointed in exactly the wrong direction; the data pointed the opposite way.

Shreyas Doshi identifies a different kind of metrics trap: the **optics level** of product work, where teams optimize for the appearance of performance rather than its substance. Status updates, polished presentations, and metrics that look good in QBRs all become the goal when organizations reward optics over impact. His pre-mortem framework is partly a defense against this: by imagining failure before it happens, teams are forced to name the gap between their confidence and their evidence — making it harder to present optics as outcomes.

---

## Retention Over Acquisition: The Compound Math Most Teams Ignore

Several guests make the same point from different angles: **retention is radically more important than most founders and PMs intuit**, and building growth models immediately reveals this.

Dan Hockenmaier's core insight is that small percentage gains in retention are often more valuable than large gains in acquisition because retention compounds across referrals, content generation, and contribution margin reinvestment. This should shift resource allocation significantly — but most teams allocate the majority of their growth investment to acquisition because it's faster to measure and easier to act on.

Sean Ellis's sequencing principle (Nail It Then Scale It) makes the same point operationally: don't aggressively pursue customer acquisition until you've optimized the experience for users who already find the product must-have. The sequence is: validate must-have value → optimize activation/onboarding → build engagement loops → enable referral → optimize revenue model → *then* scale acquisition. Customer acquisition is now so competitive that you can't find scalable, profitable channels unless you're highly efficient at converting, retaining, and monetizing users. Scaling acquisition before fixing retention is pouring water into a leaky bucket.

Sean Ellis's activation example from LogMeIn illustrates the magnitude: improving signup-to-usage from 5% to 50% — a 1,000% gain — transformed a $10K/month ad spend ceiling into $1M/month with a three-month payback, plus 80% word-of-mouth growth. This single activation improvement unlocked more growth than any acquisition campaign could have.

Jag Duggal (Nubank) adds an NPS-as-operational-religion perspective: Nubank tracks NPS in the 70s-90s range, and a drop of even 1-2 points triggers alarm and systematic investigation. NPS at this level of operational rigor isn't a lagging indicator of customer satisfaction — it's a leading indicator of word-of-mouth growth. 80-90% of Nubank's customer growth came from organic channels. That only works if customers love the product enough to talk about it, and the NPS is the proxy for whether that love is being maintained.

Yuriy Timen (Grammarly) frames the retention-first principle in terms of growth engine selection: paid acquisition only works sustainably when free-to-paid conversion exceeds 5% (ideally 7%+). Below that threshold, the unit economics don't close regardless of how much you spend on top-of-funnel. The conversion rate is itself a retention signal — it tells you whether users who experience the product see enough value to pay for continued access. Trying to scale acquisition without this foundation "means the music is going to stop."

---

## The Qualitative/Quantitative Balance

A recurring tension in this chapter is between the precision of quantitative data and the interpretive richness of qualitative insight. The guests' resolution is consistent: you need both, they answer different questions, and neither alone is sufficient.

Jess Lachs expresses this directly: "Your goal is to figure out what's happening. And if that means you're going to pick up the phone and call customers, then that is what you're going to do." Her data scientists at DoorDash are expected to own outcomes, not just analysis — which sometimes means stepping outside the traditional boundaries of the data science role.

Nicole Forsgren makes a methodological argument: system data and people data are complementary, not competitive. Systems will never tell you about heroic effort, Rube Goldberg processes, or mission-critical code sitting outside version control. Survey data might reflect bias or misreport, but so do systems — incomplete instrumentation, silent bugs, logging gaps. Both types of "lies" can be managed. Elite teams with complete instrumentation still survey their users annually because each data source reveals different truths.

Ronny Kohavi's hierarchy of evidence provides a framework for calibrating trust: anecdotal → observational studies → natural experiments → controlled experiments → multiple replicated controlled experiments. Every tier provides different signal, and knowing which tier you're operating in determines how much confidence you should have in the finding. The failure mode isn't using any particular method — it's treating a finding from a lower tier with the confidence appropriate only to a higher tier.

The qualitative work that precedes quantitative testing often has the highest leverage. Sean Ellis's LogMeIn story: 10-plus A/B tests failed to improve download conversion before someone thought to ask users why they didn't download. The answer — "Seemed too good to be true" (freemium was a new concept) — led to a test showing both free and paid options simultaneously, which improved conversion by 300%. "A problem well stated is a problem half solved." All the quantitative testing in the world couldn't find the right intervention without first understanding the user's mental model.

---

## Measurement in the AI Era

Several guests note that AI is changing both what can be measured and how it should be measured — and not always in the directions product teams assume.

Nicole Forsgren's most provocative finding is that traditional productivity metrics are "lies" in an environment where AI generates code. Lines of code, PR counts, and activity metrics become trivially gameable. Developers now spend roughly 50% of their time reviewing AI-generated code rather than writing their own — a fundamental shift in how work is structured that existing metrics frameworks don't capture. She proposes adding "Trust" as a sixth dimension to the SPACE framework for AI-enabled environments: can I trust the AI output? What's the reliability? Will there be over-reliance?

Edwin Chen's critique of AI benchmarks is the same pattern at a different scale: the benchmarks that were created to measure AI capability have become targets that distort the capabilities they were supposed to measure. Teams optimize for the benchmark rather than for the underlying capability the benchmark was meant to proxy. This is Goodhart's Law operating at the frontier of AI research.

Ramesh Johari notes that AI dramatically expands the hypothesis space — from 10 potential interventions to 1,000 — which puts more pressure on humans to filter, prioritize, and decide, not less. The analytical bottleneck shifts from hypothesis generation to hypothesis evaluation, which requires stronger data literacy and clearer causal reasoning than most organizations have today.

Dan Hockenmaier's growth model framing applies here: when AI tools make it possible to ship experiments in hours rather than weeks, the value of having a clear growth model — a structured understanding of which inputs drive which outputs — increases dramatically. Speed without direction is a faster way to get lost.

---

## Building Measurement Infrastructure and Culture

The guests who have built measurement infrastructure at scale share a consistent view: the investment is worth it, the marginal cost of additional experiments eventually approaches zero, and the cultural work is harder than the technical work.

Ronny Kohavi's experience at Microsoft is the canonical case: after the initial platform investment, running 100-plus new experiments daily became routine because the marginal cost of each experiment was near zero. The bottleneck shifted from "can we test this?" to "what should we test?" That shift in bottleneck changes team behavior fundamentally. At Airbnb, by contrast, a weaker platform required many data scientists to manually support each experiment — much of the analytical capacity that should have been focused on insight generation was consumed by experiment maintenance.

His advice on institutional memory is practical and underappreciated: run quarterly meetings on "most surprising experiments" — not just winners, but surprising losers. Build searchable experiment history. Document categorical learnings ("opening links in new tabs consistently wins"). Without this, organizations forget and repeat the same experiments. The learning isn't accumulated; it dissipates with team turnover.

Yuriy Timen's attribution philosophy addresses a different infrastructure problem: online attribution has deteriorated with privacy changes and iOS 14, while offline attribution has improved, narrowing the gap between digital and traditional channels. This creates opportunity for companies that invest in proper measurement infrastructure (Media Mix Modeling, incrementality testing) while competitors rely on increasingly noisy click-based attribution. He notes that "click-based attribution never demonstrated a causal relationship between media spend and business results. It was only good for correlative insights." Causal attribution requires real controlled experiments.

Jessica Lachs's "Ask Data AI" — DoorDash's internal chatbot that helps non-technical employees write SQL queries — points toward the next frontier: democratizing data access changes who can formulate and answer analytical questions. When data access requires technical intermediaries, the questions that get asked are the ones technical people are positioned to ask. When business users can query data directly, the questions that get asked are the ones closest to business problems.

---

## Cross-Cutting Insights

- **The gap between "we shipped the feature" and "we moved the metric" is where product failure lives.** Most product processes celebrate shipping; the best companies measure what happened after.

- **Measuring the wrong thing with high precision is worse than measuring the right thing approximately.** Composite metrics, activity metrics, and output metrics all produce high-quality measurements of the wrong things.

- **Experimentation culture requires organizational design, not just permission.** If researchers and data scientists are rewarded for "winning experiments," they will run safe bets that confirm existing hypotheses. If they're rewarded for learning, they'll run bold tests that sometimes fail.

- **The North Star metric and input metrics must be managed simultaneously.** The North Star tells you where you're going; input metrics tell you whether you're on the path. Managing only one produces either directionlessness (all inputs, no North Star) or fire drills (all North Star, no inputs to move).

- **Short-term metrics require countervailing long-term metrics.** You can always increase short-term revenue by sending more emails, adding more ads, or reducing quality. Without guardrail metrics that predict long-term value (LTV, retention cohorts, NPS), teams will optimize for the short term and destroy the long-term.

- **Every metric is eventually gamed.** The question is not whether gaming will happen but how long it takes, and whether the metrics system can adapt. Building metrics portfolios rather than single metrics, and revisiting metric validity regularly, provides some defense.

- **Data literacy is a leadership problem, not a data team problem.** If product and business leaders can't read a cohort curve, interpret a confidence interval, or distinguish correlation from causation, the data team becomes an oracle that produces reports to be selectively cited rather than a function that improves decisions.

- **The best data analysis changes what gets built.** The ultimate test of a metrics culture is not how many dashboards exist but whether the findings from data analysis show up in product decisions.

---

## Key Mental Models

**Input vs. Output Metrics (Bill Carr / Amazon)**: Output metrics (revenue, customers) are consequences; input metrics (selection breadth, price competitiveness, page load time) are what teams can actually control. Obsess over inputs; trust that outputs follow.

**Overall Evaluation Criterion / OEC (Ronny Kohavi)**: A composite metric combining near-term revenue with countervailing user experience metrics that predict long-term value. Prevents optimizing for short-term gains that destroy lifetime value.

**Twyman's Law (Ronny Kohavi)**: "Any figure that looks interesting or different is usually wrong." Surprisingly large results should trigger investigation for bugs before celebration.

**DORA Four Metrics (Nicole Forsgren)**: Deployment frequency, lead time for changes, mean time to restore, change fail rate. A balanced set of speed and stability metrics that move together, not in opposition.

**SPACE Framework (Nicole Forsgren)**: Satisfaction, Performance, Activity, Communication/Collaboration, Efficiency/Flow. A framework for selecting balanced measurement rather than a prescriptive metric set; prevents gaming through multi-dimensional coverage.

**Sean Ellis Test (Sean Ellis)**: "How disappointed would you be if you could no longer use this product?" 40%+ "very disappointed" is a leading indicator of PMF. The test is a filter, not a destination; follow-up qualitative work extracts the strategic insight.

**Nail It Then Scale It (Sean Ellis)**: Don't scale acquisition until you've optimized activation, engagement, and retention. The sequence matters: broken conversion makes all acquisition unsustainable.

**DHM Model (Gibson Biddle)**: Product strategies should Delight customers in Hard-to-copy, Margin-enhancing ways. All three must coexist; delight that's easily copied or destroys margins isn't durable strategy.

**Dual-Sided ROI (Dan Hockenmaier)**: For marketplaces, calculate CAC for one side plus the loaded cost of acquiring the other side at the required ratio. Captures marketplace interdependence that single-sided metrics miss.

**Value Exchange Loop (Itamar Gilad)**: Organizations deliver value to market (North Star) and capture value back (revenue). Both should be measured simultaneously because they're interconnected and create a growth feedback loop.

**Growth Model (Dan Hockenmaier)**: The structured representation of acquisition channels, retention curves, and monetization tied together quantitatively. Building the model is itself half the value — it forces clear thinking about how the business actually works.

---

## Notable Quotes

> "You know it's an input metric if it measures something with respect to the customer experience and if it is something you can control."
> — Bill Carr (Amazon)

> "We often are humbled by how bad we are at predicting the outcome of experiments."
> — Ronny Kohavi

> "If you go for something big, try it out, but be ready to fail 80% of the time."
> — Ronny Kohavi

> "Most productivity metrics are a lie. If the goal is more lines of code, I can prompt something to write the longest piece of code ever. It's just too easy to game that system."
> — Nicole Forsgren

> "Speed and stability move together... when you move faster, you are more stable, which means you're pushing smaller changes more often... you have a smaller blast radius."
> — Nicole Forsgren

> "You are your objective function."
> — Edwin Chen

> "We are optimizing your models for the types of people who buy tabloids at a grocery store."
> — Edwin Chen (on AI labs optimizing for engagement)

> "For me, analytics is a business impact driving function and not purely a service function, not just answering the why, but answering the, 'What do we do now that we know this?'"
> — Jessica Lachs (DoorDash)

> "Keeping things simple is really important... even if it's not perfect and your composite would be more perfect. If people understand it, if they have an intuition around it... it's going to be a much better metric."
> — Jessica Lachs

> "A problem well stated is a problem half solved."
> — Sean Ellis (quoting Kettering)

> "Revenue should be a product of doing things right. It shouldn't guide your day-to-day actions."
> — Sean Ellis

> "If we use the language of winners and losers in A/B testing, we're implicitly saying that we wasted time when we ran an A/B test on a loser."
> — Ramesh Johari

> "I think 50% of the value you get from [a growth model] is simply building the model. It forces you to understand it and then you get this artifact which you can use to understand how to weigh different opportunities."
> — Dan Hockenmaier

> "Most people actually don't want to share misinformation. If you can remind people at the point of sharing that this is unverified information, studies have shown that this could decrease shares."
> — Kristen Berman (on behavioral metrics vs. intervention design)

> "It's not about getting the bits to production, it's about getting the right bits to production. It's about creating the outcomes that you need."
> — Itamar Gilad

---

## Chapter Takeaways

- **Identify your input metrics and manage those, not the outputs.** Revenue, churn, and active users are consequences of inputs you can control. Map the end-to-end customer experience, identify what you can measure at each step, and find the three to six inputs that most causally drive the outputs you care about.

- **Build experimentation infrastructure before you need it at scale.** At low experiment volume, each test requires significant overhead. Invest in platforms that drive the marginal cost of experiments toward zero — the ROI compounds dramatically as test volume increases. Every code change should be an experiment.

- **Run at least three balanced metrics to prevent gaming.** Any single metric can be gamed. Combining satisfaction, performance, and activity (or equivalents) creates a system where improving one at the expense of others is visible. Make the trade-offs legible.

- **Don't scale acquisition before fixing activation and retention.** Run the Sean Ellis test. Nail onboarding so that new users experience must-have value quickly. Only then does the math of acquisition channels close. Scaling before this is expensive and self-defeating.

- **Treat surprising results as bugs, not breakthroughs.** Apply Twyman's Law: any result that looks too good is probably wrong. Investigate experimental validity — sample ratio mismatch, instrumentation bugs, data pipeline issues — before celebrating. Build a culture where investigating surprising results is standard practice.

- **Build qualitative insight into your metrics process, not as a separate activity.** Quantitative data tells you what happened; qualitative research tells you why. The best diagnostic loops run both: funnel data to identify where users drop off, user conversations to understand why, A/B tests to validate interventions. Neither alone is sufficient.

- **Document your surprising experiments, especially the failures.** Institutional memory in experimentation culture requires active investment. Quarterly reviews of surprising results, searchable experiment history, and documented categorical learnings prevent organizations from repeating experiments and forgetting what they learned.
