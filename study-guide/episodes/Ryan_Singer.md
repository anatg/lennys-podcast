# Ryan Singer — Shape Up: A Different Approach to Building Product

## Guest Profile
- **Name**: Ryan Singer
- **Role/Company**: Former Head of Product Strategy at 37signals (Basecamp), author of *Shape Up*
- **Background**: One of the first few hires at 37signals in 2003, worked there for ~17 years building Basecamp. Developed the Shape Up methodology to formalize how small, fast-moving teams can maintain their velocity as they grow. Now consults with companies struggling to ship predictably. Co-created the "Shaping in Real Life" course to help teams implement Shape Up in real-world contexts beyond Basecamp's unique structure.

## Tags
`Product Strategy` `Execution` `Frameworks` `Startup` `Enterprise` `Org Design` `Engineering` `Design` `Leadership` `Culture` `Process` `Shipping` `Team Dynamics` `Agile Alternatives`

## TL;DR
Ryan Singer explains the Shape Up methodology—an alternative to Scrum/Agile that emphasizes shaping projects *before* building, working backward from fixed time "appetites" (not estimates), and giving small teams clear problems with room for creative implementation. The key innovation: collaborative shaping sessions where product, design, and senior engineering wrestle with ideas together *before* committing resources, surfacing technical risks and trade-offs early to avoid projects that drag indefinitely.

## Core Frameworks & Mental Models

- **Appetites, Not Estimates**: Instead of estimating how long something will take, decide upfront how much time you're willing to spend (the "appetite"), then shape the solution to fit that constraint. Work backward from the business's time budget rather than forward from feature requirements. Maximum useful appetite: six weeks—beyond that, too many unknowns compound.

- **Shaping vs. Building**: Shaping is pre-work done by a small group (senior engineer + product + designer) to define what will be built. It's not PRDs or high-fidelity Figma—it's collaborative whiteboarding to get a concrete idea that's *just detailed enough* to commit to. Output: roughly 10 or fewer "moving pieces" that make the idea concrete and technically feasible. If you can't describe it in <10 components, it's not shaped.

- **Framing Before Shaping**: Before shaping a solution, narrow the problem. "Build a calendar" is too big. "Show empty spaces so users can find free time slots" is frameable. Framing is negotiating down from fuzzy requests (sales/CEO/research) to a specific, valuable problem worth solving in the given appetite.

- **The 9-Box Kickoff Exercise**: After shaping, at project kickoff, the *building team* breaks the shaped idea into nine or fewer major implementation scopes. This tests if the project is truly clear and achievable. Nine boxes × ~4 days each = six-week project. If you can't fit it in nine boxes, scope isn't clear enough or appetite is mismatched.

- **Circuit Breaker Principle (Adapted for Real Life)**: Basecamp's original rule was to cancel projects that didn't ship in the time box. In practice, most teams can't stomach that. The real-world adaptation: if a project isn't on track to finish, pull it *back into shaping mode*—don't keep investing in something you don't understand. Rework the idea with new information before recommitting.

- **Shaping Session Structure**: Three-hour collaborative sessions with senior engineer, product lead, designer. Try multiple approaches to the problem, deliberately attempt to break ideas by surfacing technical or UX weaknesses. Goal: rough sketches (fat marker drawings or breadboarding) showing flows, key elements, and logic—not pixel-perfect Figma. Repeat sessions (~3 total) until you reach clarity on what's buildable in the appetite.

- **The Home Renovation Analogy**: You can have a beautiful rendering of bedroom lamps mounted to the wall, but if you haven't checked whether there's electricity in that wall, cost and time explode. Shaping is "opening up the walls" before committing—engineers must be in the room to identify hidden complexity before the project starts.

- **Time Boxes (Not Necessarily Cycles)**: Teams don't have to run synchronized six-week cycles if they're small or don't have dependencies. The key is *fixed time pushing back on scope*. Could be two weeks, four weeks, six weeks—whatever matches the problem's importance. Six weeks is the *maximum* before unknowns compound too much to see the end.

## Top Insights (Timeless)

1. **Engineering must be in shaping, not just informed after**: The dominant failure mode Ryan sees is product/design shaping in isolation, then discovering major technical blockers mid-build. A senior engineer who "knows where the bodies are buried" must be in the shaping session, opening up the code to check assumptions. Otherwise, beautiful Figma files collide with reality in week four.

2. **Clarity enables autonomy**: Teams can't "vary scope creatively" if they don't understand the idea deeply. Handing a team "build a newsletter builder in six weeks—figure it out!" is cruel. But handing them a well-shaped idea with ~10 concrete moving pieces *empowers* them to solve implementation details and feel engaged, not like ticket-takers.

3. **Startups often don't need Shape Up until they delegate**: Founders working together don't need a formalized process—it's organic. The tipping point comes when founders hire the first PMs/engineers and try to delegate. That's when projects start dragging because the implicit understanding that made the founders fast doesn't transfer. Formalizing shaping helps new hires understand the trade-offs.

4. **Most "feature factories" aren't even efficient factories**: The critique of "feature factories" assumes companies are shipping too much without outcomes. Ryan's experience: most teams struggle to ship *anything* predictably. If you had a real factory that cranked out features reliably, you'd just feed it better inputs (framed problems). The actual problem is projects dragging, not over-shipping.

5. **Detail level is a dial you turn based on team seniority**: Junior engineers benefit from *more* shaping detail (suggested approaches, architectural hints). Senior engineers need less—or should be *in* the shaping. If someone feels micromanaged by shaping detail, bring them into the shaping session next time. Don't universally reduce detail; calibrate to who's building.

6. **The real pain isn't at the end—it's accumulated from the start**: Projects blow up in week six, but the root cause is often at week zero: fuzzy problem definition, no technical review, or scope that was never realistic. The circuit breaker (or pulling back to re-shape) is a symptom. The fix is better shaping upfront and ruthless framing.

7. **Basecamp's advantages are invisible until you leave**: Jason and DHH's companies have: no sales org (no "we need this to close a deal" pressure), designers who code (no design/eng handoff), founders deeply involved in shaping, and 10+ years of slow hiring (organic process spread). Most companies have *none* of these. Shape Up still works, but requires deliberate bridges across org walls that didn't exist at Basecamp.

8. **Shaping is creative problem-solving under constraint**: It's not a planning document exercise. It's live whiteboarding with multiple smart people trying to break each other's ideas until you find the version of the problem + solution that's *both valuable and achievable* in the appetite. That's why it's energizing when done right—it's a puzzle, not bureaucracy.

9. **PMs move upstream in Shape Up**: Instead of chasing engineers mid-sprint to unblock tickets, PMs spend more time in framing (understanding customer jobs, negotiating problem scope) and shaping (collaboratively designing feasible solutions). Building becomes more autonomous. This shift mirrors what AI may force: PMs focusing on *what* to build while implementation becomes more automated.

10. **If you're consistently shipping, leadership leaves you alone**: Companies with quarterly planning often wonder how Shape Up fits. Answer: if your team reliably says "we'll ship X in Y weeks" and *does*, no one cares if your cycles align to quarters. Executives just want to see movement and results, not process compliance. Shape Up's value is *producing that reliability*.

## AI & The Changing PM Role

Ryan draws a parallel between Shape Up and an AI-future PM role: as AI tooling makes *building* faster (potentially instant), the critical questions shift entirely to *what* to build and *whether* what's built is correct. This mirrors Shape Up's emphasis on PMs moving upstream—spending more time framing problems, shaping solutions with technical input, and validating direction rather than managing execution rituals. The "make the thing" part may shrink in time/complexity; the "figure out the right thing" part becomes the entire job. Shape Up already trains that muscle by pulling PMs out of sprint ceremonies and into strategic problem definition and collaborative solutioning with engineering.

## Notable Interview Questions Lenny Asked

- "What would you say is a good first step for a team that's currently just shipping every two weeks and wants to try this?"
- "Say someone's like, 'I don't know any friends that are using this. It's weird, this way of working. It's not a thing I hear about all the time.' What can you say to help them get over that hump?"
- "What are signs that it's time to try something? What sort of pain do you often see?"
- "What's the sweet spot stage for a company to start using Shape Up?"
- "If you were to try this approach and have a shaping session, what's a sign you're heading in a good direction?"
- "Have you also seen this increased interest in Shape Up [recently]?"
- "How long are these [shaping] sessions usually? Who should join?"

## Best Quotes

> "We are not going to start something unless we can see the end from the beginning. We're not going to take a big concept and say, 'What's the estimate?' We're going to work backward and say, what is the maximum time we're willing to spend before we actually finish something?"

> "I often use this analogy of a home renovation: you can have the most beautiful rendering of bedroom lamps coming out from the wall. But if you haven't checked if there's electricity in that wall, it's going to drastically change the cost and the time."

> "You can't put 10 pounds of crap in a five-pound bag." *(quoting Bob Moesta)*

> "If it's shaped well, you can usually describe it in less than 10 moving pieces. If you have 100 things, that doesn't tell me anything. But if it has to be nine or less—do we actually have a picture of what it means to build this that we can hold in our heads?"

> "Product managers and CTOs don't like to go on a public forum and say, 'Our company isn't shipping, our engineering team is stuck, our team is always lost in the weeds.' That's not an easy community topic."

> "The dominant failure case I see again and again is not enough detail. The engineers run back to product and say, 'I'm not getting enough from you.'"

> "If you have a feature factory—meaning you're continually cranking out features—you're probably quite healthy. All you need is to feed a different input to the beginning of the factory. What most teams struggle with is stuff isn't moving, it's dragging, I can't see the end."

> "If you're consistently shipping meaningful things without excuses, leadership will leave you alone. That's what everyone wants to see: movement."

## Interview Prep Takeaways

**How to apply lessons from this episode to your own PM interviews:**

- **Demonstrate cross-functional problem-solving fluency**: Be ready to describe a time you brought engineering into problem definition *early* to surface technical constraints and shape a better solution. Interviewers value PMs who don't throw requirements over the wall. Use Ryan's "shaping session" framing: "We got eng, design, and product in a room with a whiteboard and iterated on three approaches until we found one that was both valuable and technically feasible in our time budget."

- **Talk in terms of appetites and trade-offs, not just estimates**: When discussing project planning, flip the script. Instead of "we estimated three months," try "we decided we were only willing to spend six weeks on this problem, so we had to creatively scope down to the highest-value slice—here's how we framed it." Shows strategic thinking and comfort with constraints.

- **Show you understand the difference between shaping and building**: Describe projects where you worked *upstream* to define a crisp idea before handing it to a team. Contrast that with projects where you were "chasing engineers mid-sprint"—acknowledge the difference in outcomes. Interviewers want PMs who don't just manage tickets but define clear, achievable problems.

- **Use the "nine boxes" or "ten moving pieces" heuristic**: When explaining a project's scope, say something like, "I made sure we could articulate the solution in roughly eight major components: A, B, C... That clarity let the team break it down confidently and ship in four weeks." Demonstrates structured thinking and ability to communicate scope concretely.

- **Acknowledge real-world messiness**: Don't oversell a methodology. Ryan's candor about Basecamp's unique advantages (no sales pressure, designers who code) and his admission that "most teams can't just cancel projects" shows self-awareness. In interviews, acknowledge constraints ("We didn't have the luxury of delaying for perfect shaping, so here's how we adapted...") rather than painting everything as ideal. Authenticity > polish.

- **Highlight when you've "opened up the walls"**: Use Ryan's metaphor. Describe a time you insisted on technical due diligence before greenlighting a project: "We almost committed to this feature based on mockups, but I asked our senior engineer to check the existing codebase first. Turned out it was three separate code paths, not one—totally changed our scoping conversation and saved us weeks of pain."

- **Be ready to explain failure-to-ship stories**: Ryan says teams are reluctant to discuss shipping struggles, but interviewers will probe for failure stories. Have one ready where a project dragged, explain the root cause (fuzzy problem? no eng input? too many unknowns?), and what you'd do differently now. Frame it around shaping/framing gaps, not blaming people.

## Related Themes

- Alternatives to Agile/Scrum for product development
- Cross-functional collaboration (product-engineering-design)
- Managing scope and time constraints without sacrificing quality
- The role of senior engineers in product strategy
- Startup velocity vs. scale challenges
- Framing problems before solving them (Jobs-to-be-Done connection)
- PM skill evolution: from execution to strategy
- Consulting for product/engineering teams stuck in delivery struggles
