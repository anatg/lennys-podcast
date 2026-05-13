# Ryan J. Salva — VP of Product at GitHub, Incubating GitHub Copilot

## Guest Profile
- **Name**: Ryan J. Salva
- **Role/Company**: VP of Product at GitHub (owned by Microsoft)
- **Background**: Philosophy and English degree (philosophy of aesthetics and 20th century critical theory). Non-traditional path to product management. ~20 years in software development and product management across startups and 10 years at Microsoft before joining GitHub 3 years ago. Previously led product for Microsoft's One Engineering System and Azure DevOps before transitioning to GitHub to work on developer tools closer to the open source community.

## Tags
`AI/ML` `Product Strategy` `Enterprise` `R&D` `Innovation` `Developer Tools` `Execution` `Org Design` `Ethics` `Leadership` `Platform` `Vision`

## TL;DR
Ryan Salva shares how GitHub incubated and launched Copilot—an AI-powered code autocomplete tool—from a fortunate accident (OpenAI cloning GitHub repos) to a product writing 40% of Python developers' code in just 18 months. He reveals the three-horizon framework GitHub uses to balance moonshots with operational products, the critical transition process from R&D to productization, and the unique ethical and legal challenges of bringing AI tools to market.

## Core Frameworks & Mental Models

- **Three Horizons Framework for Portfolio Management**: Allocate team capacity across time horizons: ~5-10% on experimental/research projects (horizon 3, ~5 years out), ~25-30% on operations/maintaining in-market products (horizon 1, next year), and ~60% on incremental improvements to existing products (horizon 2, next 3 years). Think of horizons more as measures of ambiguity and confidence than calendar dates.

- **R&D to Product Transition Process**: (1) Ring-fence an R&D team (GitHub Next) to work on horizon 2-3 moonshots without operational constraints. (2) When customer signal reaches medium confidence that solution solves a real problem in a novel way, begin market testing with prototypes. (3) Move researchers temporarily into a new EPD (Engineering/Product/Design) squad to seed knowledge transfer. (4) Only return researchers to R&D after replacement team members have picked up necessary skills and feel ownership over the roadmap. Transition is based on capability replacement, not calendar dates.

- **AI as Pair Programmer Framing**: Frame AI tools like Copilot as a "pair programmer" sitting beside you—this helps define appropriate behavior boundaries. Just as you wouldn't want a human pair programmer spouting offensive content or distracting you, the AI should help you stay in flow and focus on creative work rather than rote tasks.

- **Response Latency Sweet Spot**: For AI-assisted coding tools, ~200 milliseconds is the optimal response time to avoid breaking developer flow. This became a key parameter to optimize in the model.

## Top Insights (Timeless)

1. **Fortune favors the prepared**: GitHub Copilot started from an accident (OpenAI aggressively cloning repos nearly caused a service incident), but GitHub had already created the Arctic Code Vault snapshot of public code. The team turned a potential crisis into opportunity by packaging that data for OpenAI to experiment with large language models on code.

2. **Invest in moonshots without expectations**: The first step to successful R&D is hiring smart people and giving them space to create without expecting money-makers or operational requirements (security, privacy, uptime, accessibility) upfront. Don't outsource innovation exclusively to R&D—product teams must own innovation as they take over ideas.

3. **Knowledge transfer requires people, not just documentation**: When transitioning from R&D to product, bring researchers along to seed the new product team. Create insulation around them by hiring operational engineers so researchers can eventually return to R&D work. The handoff cannot be calendar-based—it must be based on the new team achieving continuity of expertise.

4. **Engineering fundamentals are the contracts differentiating R&D from product**: Moving from experiment to operational product requires cultural change management. Researchers won't have all the right skillsets for maintaining services at scale, so balance researchers (who bring vision) with engineers comfortable maintaining production systems.

5. **AI product management requires unprecedented community dialogue**: Scaling Copilot required scaling the product team more than the engineering team. Society is still figuring out AI ethics, legality, and expectations. Product managers must lead guided conversations with skeptical communities about training data, security, responsible use, and augmentation vs. replacement.

## AI & The Changing PM Role

- **AI will infuse the entire development stack**: Beyond code completion, AI will optimize build queues, auto-generate commit messages and PR summaries, and remove drudgery so developers focus on design patterns and outcomes rather than syntax memorization.

- **AI as abstraction layer and democratizer**: AI tools like Copilot provide a layer of abstraction that invites more people to become developers while helping experienced developers focus on larger problems and creativity rather than rote work.

- **PM as AI ethics navigator**: Product managers must navigate unprecedented ethical and legal challenges: Who's at fault when AI produces offensive content? How do you edit language without becoming censors? When is training on public code acceptable? PMs need deep engagement with legal, privacy, security, and especially user communities to build trust.

- **Supply chain constraints for AI products**: AI products face unique scaling challenges including GPU scarcity and global supply chain disruptions. These become product constraints PMs must navigate.

- **AI requires continuous skepticism**: Healthy skepticism is necessary for any AI product. PMs must make clear AI augments rather than replaces humans, preserve existing quality measures (static analysis, unit tests), and ensure thinking humans remain in the loop for all decisions.

## Notable Interview Questions Lenny Asked

- "What made you decide to take this leap [from Microsoft to GitHub]?"
- "Can you talk about just the original seed of this idea—who did it come from, who had the original vision, how did this idea emerge and build momentum where you put resources into it?"
- "Was there kind of a point at which it was clear to you or leadership in general like, we should double down on this thing and go big?"
- "Is there anything you've learned about how to do this, where you invest in these big moonshots within a larger company?"
- "How do you work through these challenges [ethical/legal]? Is it discussions with you and the legal team?"
- "Where do you see this all going for developers?"
- "What would you say has been the biggest challenge either technologically or even operationally just kind of scaling it to a real product that people are paying for?"

## Best Quotes

> "Developers for the last 20 years or more have had essentially simple, intelligent autocomplete... Copilot is essentially that magnified by many lines of code."

> "The labor of remembering what's the order of parameters that need to come into a particular API... that's just labor. It's not creating. It's just typing."

> "The first step is to invest in it. The first step is really hire really smart people, attract smart people, and give them the opportunity to be creative. Don't expect anything out of them that is going to turn into a money maker."

> "Making sure that you've got continuity of expertise and sets and domain familiarity before you move over... The criteria for moving researchers back into their R&D team... can't be based on a calendar."

> "We do not want Copilot to replace any other part of the stack... We want you to keep all of those same systems in place to make sure that humans who are leveraging tools like Copilot continue to produce that good quality code."

> "What I hope for our industry five, 10 years from now, is that not only will we be inviting more developers or more people to become developers... but that also the really experienced developers are focusing on much larger problems and focusing on outcomes and creativity."

## Interview Prep Takeaways

- **Tell transition stories with specifics**: When discussing career moves, connect them to impact and mission ("where the community is creating... where I could have a larger impact"). Show you research where innovation energy flows, not just title progression.

- **Frame bold bets with structured thinking**: Use frameworks like three horizons to show you balance moonshots with incremental wins. Demonstrate portfolio thinking: percentages of capacity allocation show strategic maturity beyond individual product execution.

- **Demonstrate cross-functional orchestration**: For AI/complex products, emphasize working with legal, privacy, security, research teams, and especially customers. Show you can navigate ambiguity across unprecedented challenges, not just ship features.

- **Highlight knowledge transfer and team building**: When scaling products, discuss how you built teams around innovations, transitioned expertise, and managed cultural change. Show you think about people sustainability, not just product launches.

- **Use concrete metrics and examples**: "40% of Python code," "200 milliseconds response time," "tens of thousands to hundreds of thousands in technical preview." Specificity demonstrates deep product knowledge and analytical rigor.

## Related Themes

- Building R&D organizations within larger companies
- AI product ethics and responsible AI development
- Developer tools and productivity innovation
- Transitioning from prototype to scaled product
- Cross-functional leadership in ambiguous domains
- Community-driven product development
- Non-traditional backgrounds in product management
- Portfolio management and resource allocation strategies
