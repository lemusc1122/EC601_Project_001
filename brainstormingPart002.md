# 2026-09-14  Notes for part 2:

## Proposal before executing part II:<br>
Can algorithms be applied to quantum circuits (qc) to reduce noise? can any pi-pulsing patterns used in optical clock systems (NIST) 
be utilized in a qc environment? If algorithms can be applied (Qiskit), which are the best? Does efficiency depend on qc?

## $${\\color{green}Next\ Steps\ -\ Validate\ Before\ Build}$$
1. Rewrite your proposal as 3–5 assumptions.  Someone has this problem · we can build it with data we can access · it beats what the user does today.

2. Rank them: most fatal × most uncertain first.  Not the one you already know how to test — the one that kills the project if wrong.

3. Run the cheapest test that could prove you wrong.  Talk to 3 real users → mock it on paper → baseline on real data → only then build. If your first test is writing code, you skipped a cheaper one.

4. Write your kill criterion before testing.  “We pivot if…” — decided now, while you’re still honest.

5. Bring to next class:  mission sentence · named user · top-5 stories with acceptance criteria · assumption table with test results — in your GitHub repo.

## $${\\color{green}5\ W's\ and\ How}$$
### What?  What are you building — one sentence, no jargon. 
Testing
### Who?  Who uses it, and who else is affected?  
testing 2
### Why?  What breaks if it doesn’t exist?  
testing 3
### When?  When is it used — and when is it needed by? 
testing 4
### Where?  In what setting or workflow does it live?  
testing 5
### How?  How, at the architecture-sketch level? 
testing 6
## $${\\color{green}Mission\ Statement }$$
i.e. For [target user] who [has this need], the [project] is a [category] that [key benefit]. Unlike [what they do today], it [key difference].
## $${\\color{green}User\ and\ Subproduct }$$
who the user and what is the subproduct for semester
## $${\\color{green}User\ Stories\ (Unit\ of\ work) }$$
i.e. As a [specific user], I want [capability], so that [outcome I care about].
## $${\\color{green}INVEST\ -\ 6\ Checks,\ 6\ Failure\ Modes }$$
I — Independent:  No waiting on another story, so you can build in risk order.  ✗ “Show feedback trends” before feedback collection exists.

N — Negotiable:  A promise to talk, not a frozen spec — the how is decided when you build it.  ✗ “Rank with cosine similarity over abstracts” — that’s implementation, not need.

V — Valuable:  A vertical slice a user would notice — the check engineers break most.  ✗ “Set up the database” — no user wakes up wanting a database.

E — Estimable:  The team can size it. If not: too vague, or hides an unknown → run a spike (1-day time-boxed experiment; the deliverable is knowledge).  ✗ “Filter by relevance” before anyone tested if relevance is detectable.

S — Small:  Fits in one sprint. Too big = an epic → split it (next slide).  ✗ Demo is “we’re 40% done.”

T — Testable:  Done vs not-done is checkable by someone other than the author.  ✓ “8/10 picks judged relevant by a labmate in ≤10s.”
