# Austin Hay — Head of Marketing Technology (Ramp)

## Guest Profile
- **Name**: Austin Hay
- **Role/Company**: Head of Marketing Technology at Ramp; formerly VP of Business Operations at Runway; VP of Growth at mParticle; 4th employee at Branch Metrics (unicorn); consultant to Airbnb, Notion, Robinhood, Postmates, Walmart, Mars; Reforge instructor on MarTech
- **Background**: One of the deepest operators in Marketing Technology — the cross-functional discipline at the intersection of product, growth, engineering, and marketing. Has built and advised MarTech stacks at companies from seed to public. Particularly strong on attribution, CDPs, data infrastructure, and the philosophical frameworks for thinking about tool decisions.

## Tags
`Growth` `MarTech` `Attribution` `Tools` `Data Infrastructure` `B2B` `B2C` `PLG` `Frameworks` `Hiring`

## TL;DR
Austin is the canonical voice on Marketing Technology as a discipline — when to hire a MarTech person, what they do, how the stack has evolved, and the principled frameworks for making tool decisions. His "Build and Buy" (not build vs. buy), PPS (Problem → People → System), and "Thinking Gray" frameworks are applicable far beyond MarTech. The Golden Stack section is the most actionable tool recommendation in the catalog for growth teams.

## Core Frameworks & Mental Models

- **What is MarTech**: Marketing Technology is a product management role whose specific focus is the system — the collection of first-party and third-party platforms that power growth and marketing. Not just "buying SaaS tools" — at scale it includes building first-party systems on top of third-party tools, managing data architecture, handling contracts/procurement, and designing systems 1-2 years into the future. Sits at the crossroads of product, growth, engineering, and marketing. At small companies (< 30 people), it's everyone. At 100-150 people, it needs to be someone's job.

- **When to Hire a MarTech Person**: Signs you need one:
  - Tools are accumulating and nobody knows how they connect
  - One "systems person" has been there two years and is overwhelmed
  - You can't make changes without fear of breaking things
  - Data schemas are unknown — nobody can tell you what user attributes you're collecting
  - Email marketing tool is holding your growth team hostage
  - You're looking at a migration that requires coordination across engineering, marketing, and data
  Critical mass: ~100-150 employees. Before that, it's usually one person moonlighting. After that, a village approach creates liability (permissioning, contract, security risks).

- **Where MarTech Lives in the Org**:
  - **B2C**: Under growth/CMO org. MarTech's job is to serve the growth team. Single centralized function working with a CDP-first architecture.
  - **B2B (sales-driven)**: Under rev ops / business technology. Salesforce is the center of gravity.
  - **B2B2C (PLG + enterprise)**: Most complex. Two CRMs may exist (HubSpot for top-of-funnel, Salesforce for sales). No universal answer. At Ramp: started centralized (rev ops), decentralized (CMO org), then recentralized (rev ops) based on whose problems were actually being solved.
  No universal answer — the org placement should follow the key stakeholder being served and the technical leader available.

- **Build and Buy (Not Build vs. Buy)**: The false dichotomy that creates organizational conflict: should we build this ourselves or buy a third-party tool? The real framework: buy the 90% of the solution from a third party to get there fast, then build the differentiating 10% on top. Benefits: (1) faster to initial capability, (2) vendor becomes committed to your success when you're a major customer, (3) preserves engineering resources for proprietary differentiation. Example: AB testing tool — buying a platform (split.io, Optimizely) + building custom integrations on top far beats either pure build or pure buy.

- **PPS Framework (Problem → People → System)**: When a systems challenge arises, the instinct is to jump straight to the system (tool/solution). The right sequence:
  1. **Problem**: What specifically is the issue? What is the person trying to accomplish?
  2. **People**: Who is involved? Who has authority? Who needs to be aligned or trained?
  3. **System**: Only now design the technical solution.
  Most companies get in trouble by skipping to System immediately. The PPS sequence prevents over-engineering, gets organizational alignment, and produces solutions that actually stick.

- **Tools Are Meant to Solve Problems**: Core philosophy underlying all tool decisions. Tools have no intrinsic value — only instrumental value relative to problems. Corollaries: (1) you don't have to buy a tool to solve a problem, (2) you don't have to use the same tool you used before, (3) problems are not always the same so tools shouldn't always be the same. The best MarTech people are tool-agnostic; the worst are tool-biased.

- **Thinking Gray (Steven B. Sample, "Contrarian's Guide to Leadership")**: Don't make a decision until you have to. The tendency to decide quickly (on systems, on people, on problems) is the most common decision quality failure. Thinking gray means staying in an ambiguous state as long as possible — avoiding premature black/white judgment. Applies to: tool decisions (don't rush to consolidate or replace), people evaluation (don't judge someone after one meeting), prioritization (is this actually urgent or does someone just want a decision?). Patience is the underrated decision-making skill.

- **Attribution System Design (Build for MTA from Day One)**:
  The evolution most companies make: first touch → last touch → 50/50 split → multi-touch attribution (MTA). The mistake: they don't set up the infrastructure for MTA until they decide they need it, then have to wait months to collect the data. The right approach: design for MTA from the start, even if you're only using first-touch today.
  
  What to collect:
  - Full referring URL + all UTM parameters (utm_campaign, utm_medium, utm_source, utm_content)
  - Store as **both first** and **last** versions on the user object
  - Fire as an attribute on every page view event
  - Capture ad network IDs (Google Click ID/GCLID, Facebook FBPID/FBP, TikTok ID, Microsoft ID)
  
  Result: warehouse team can coalesce first UTM (all the way back to acquisition), all middle-journey UTMs, and last UTM — the foundation for any attribution model.

- **Probabilistic Attribution (Post-ATT World)**: 2010-2020 were the golden years of deterministic matching — IDFA gave exact one-to-one attribution for mobile apps. iOS 14.5 ATT (2021) ended this. Now: at most 10-15% of users opt into IDFA tracking. The result: ad networks have to run probabilistic models. Skill marketers and MarTech people need to develop: making spend decisions with probabilistic data (model 30% of population, extrapolate to 100%). Parallel browser problem: browsers are stripping URL parameters, making more traffic appear organic. Third-party cookie deprecation: anonymous users stay anonymous until login.

- **MMM vs. MTA**: Media Mix Modeling (MMM) is a statistical approach to attributing marketing spend across channels using historical data and regression. Multi-touch Attribution (MTA) is a user-level approach that tracks the customer journey across touchpoints. Most businesses aren't actually ready for MMM — they need better MTA and probabilistic modeling first. MMM is relevant when: you have significant TV/offline spend, you've maxed out deterministic attribution capability, and your data science team has the skills to build/maintain the model.

- **B2C MarTech Stack Evolution**:
  - **Then (2016-2020)**: CDP (Segment) → connected to all third-party tools (email, analytics, ad networks). The "one SDK to rule them all" promise.
  - **Now (2021+)**: Two paths:
    1. **CDP-centric** (if engineering-light or speed matters): Same pattern, better tools
    2. **Warehouse-centric** (if engineering culture + data team): All data into Snowflake → Reverse ETL (Hightouch, Census) to push data back to tools. More complex but more powerful and customizable.
  - The key choice: Amplitude/Segment CDP OR Snowflake + Hightouch. The criterion: do you have the data team and engineering culture to maintain a warehouse-centric architecture?

- **"Golden Stack" Recommendations**:
  - **B2C**: Amplitude (CDP + product analytics) + Customer.io or Braze (email) + Snowflake (warehouse) + Hightouch (reverse ETL) + AppsFlyer (mobile attribution)
  - **B2B**: Similar, but: Salesforce as CRM center of gravity, Branch for web attribution (better than AppsFlyer for web-first), HubSpot for mid-funnel (with Salesforce for bottom-funnel)

- **Hiring for MarTech**:
  - **Look for**: Intellectual curiosity (#1) + basic engineering scrappiness (can read API docs, knows JS/Python, can make an API call) + cross-functional quarterback skills (manages up, lateral, and down)
  - **Interview question #1**: "How did you prepare for this interview?" — reveals how the person thinks, plans, and takes things seriously
  - **Interview question #2**: "You start Monday; by Friday write up everything we should change in our systems. What do you do?" — reveals tool bias vs. problem-first thinking; the right answer includes asking questions about what problems you're trying to solve
  - **False flag to ignore**: Resume gaps (often enriching experiences); school pedigree
  - **Red flag when joining a company**: If a director-level candidate can't get access to basic financial information, the culture doesn't have appropriate trust

## Top Insights (Timeless)

1. **Build and buy beats build vs. buy.** The dichotomy is false. Buying 90% + building 10% on top gives you speed, vendor commitment, and differentiation simultaneously.

2. **Set up attribution infrastructure for MTA from day one, even if you're using first-touch today.** The cost of retroactively collecting the data is enormous. Collecting UTM first/last on user objects from the start is cheap. You'll thank yourself in 18 months.

3. **Problems are not always the same, so tools shouldn't always be the same.** The biggest hiring red flag in MarTech: someone who recommends the same tools they've always used regardless of the problem.

4. **The company will outlast you.** Every system decision should be made with "what happens if I don't change anything for a year?" thinking. Build for the future state at minimum viable engineering cost.

5. **Thinking gray saves you from bad quick decisions.** On systems, on people, on priorities — the decision you make in 5 minutes when you feel pressure is usually worse than the one you make in 5 days when you've had space.

6. **Cookie blockers and ATT are permanent.** The golden age of deterministic one-to-one attribution is over. Probabilistic matching is a foundational skill for the next decade of growth work.

7. **Appreciation for what's beneath the surface of the people you work with makes you a better leader.** Understanding the hardships people carry outside of work changes how you lead, prioritize, and create psychological safety.

## AI & The Changing PM Role

- AI is creating new tools in the MarTech category at an extraordinary pace — Austin mentions 70,000 enterprise AI tools launched in one year (from Asha Sharma's episode context)
- The "tools are meant to solve problems" principle is increasingly important as AI tool proliferation makes tool bias even more costly
- Attribution and measurement are becoming more probabilistic, not less — the skills needed (statistical modeling, experimental design, probabilistic reasoning) are adjacent to AI/ML skills
- Threads (Meta) and Reddit advertising maturity were the channels Austin was most watching at the time of recording

## Notable Questions Lenny Asked
- "What exactly is MarTech and what does someone in MarTech do?"
- "What's the difference between a growth PM and a MarTech person?"
- "When should you hire a dedicated MarTech person?"
- "Walk me through the tech stack for B2C and B2B companies."
- "What has changed with iOS 14 ATT and how do you adapt?"
- "What are some frameworks you find especially useful in your work or life?"
- "What is your Golden Stack recommendation?"

## Best Quotes
> "Tools are just meant to solve problems. Not the other way around. You don't buy a tool and then find the problem it solves."

> "Build and buy, not build versus buy. Buy 90% of the solution from a third party to get there fast, then build the differentiating 10% on top."

> "Most people skip straight to the system. The PPS framework says: first understand the problem, then understand the people, then design the system."

> "Thinking gray — don't make a decision until you have to. I have very little patience, and that's why I have to remind myself of this constantly."

> "Set up your attribution infrastructure for MTA from day one. Collect UTM first and last on both user objects and events. The cost of retroactively collecting it is enormous."

> "Probabilistic attribution is the skill marketers and MarTech people need to develop. The golden years of deterministic matching are over."

> "From 2010 to 2020, we had the golden years of deterministic matching. You could run an ad and know with precision who installed the app. You can't do that anymore."

## Interview Prep Takeaways
- **"How do you approach build vs. buy decisions?"**: Build and buy, not build vs. buy. Buy the 90% that's commodity, build the 10% that's differentiating. Model the total cost including engineering time and future scale.
- **"How do you set up attribution measurement?"**: Design for MTA from day one even if you start with first/last touch. Collect referring URL + UTMs + ad network parameters as first and last on both user objects and events. Don't wait until you need MTA.
- **"How do you handle the iOS 14 / cookie deprecation world?"**: Accept probabilistic attribution. Build probabilistic models from the 30% you can identify and extrapolate. Use geo-based holdout tests as an experimental alternative. Be skeptical of organic attribution at face value.
- **"How do you structure your MarTech team?"**: It depends on B2C vs B2B, and centralized vs. decentralized. B2C: usually under CMO/growth. B2B: usually under rev ops. B2B2C: no right answer, follow the stakeholder. Critical mass is ~100-150 employees.
- **"What do you look for when hiring?"**: Intellectual curiosity, engineering scrappiness, cross-functional quarterback. Use "how did you prepare?" and "audit our systems by Friday" interview questions. Avoid tool-biased candidates.

## Related Themes
- "marketing technology martech stack B2C B2B"
- "attribution MTA UTM first last touch infrastructure"
- "build and buy not build vs buy framework"
- "PPS problem people system framework"
- "probabilistic attribution iOS 14 ATT post-cookie"
