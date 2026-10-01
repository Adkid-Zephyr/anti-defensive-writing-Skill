---
name: anti-defensive-writing-en
description: >
  Academic-paper defensive-writing review and revision using the Press-Release
  Principle. Use for writing or revising papers (including abstracts, introductions,
  and conclusions), cutting length, organizing experiments, and defensive-writing
  checks in rebuttals or reviewer responses. When users mention AI-flavored academic
  writing, an insecure tone, or defensive writing, check for self-undermining and
  work-report narration.
---

# The Press-Release Principle (Paper as Press Conference)

## One-line principle

A paper is a press conference, not a project summary, a lab log, or a self-audit.
Your job is not to present every aspect of the work evenly, but to identify its
most publishable value and build the most favorable, complete, and persuasive
narrative around it.

## Task scope

- **Local polishing or revision:** identify each issue and show a fix. Preserve the
  author's wording habits and paragraph structure; make only the necessary minimal
  edits, without rewriting whole paragraphs, and leave problem-free parts untouched.
  If evidence cannot support the original narrative, narrow the affected claims and
  recommend restructuring; do not reorganize the entire paper without authorization.
- **Whole-paper writing or restructuring:** when the user requests building or
  changing the overall narrative, reselect the main line and reorder material based
  on evidence. Use the restructuring rule in Section 1 when evidence is insufficient;
  wording cannot close an evidence gap.
- **Review or reviewer responses:** check defensive writing within the requested
  scope. Answer existing questions directly with evidence; reducing self-undermining
  is not a reason to evade them. This skill is neither a complete rebuttal method
  nor a general-purpose guide to removing AI-sounding prose.

## 1. Narrative rules

1. **Organize the paper around genuine strengths.** Look for what is genuinely ahead,
   unique, or irreplaceable: a new capability, a new problem, a new mechanism, a new
   perspective, broader applicability, lower cost, higher efficiency, better
   scalability, or a more meaningful trade-off. Content that forms no advantage
   does not carry the core contribution; retain necessary facts under Section 5.
2. **Organize by the argument chain.** Present the final standing logic rather than
   the research timeline: why the problem matters → why
   existing methods fall short → what this paper provides → how the evidence
   supports it.
3. **Choose a meaningful value dimension.** If a metric is not a strength, choose
   a task definition, evaluation dimension, application scenario, constraint, or
   comparison frame that better reflects the work's genuine value. Name the
   meaningful comparison in which this paper excels. Support the new frame with
   evidence; changing the main line does not hide necessary results of the original
   comparison.
4. **State the advantage explicitly.** Do not expect reviewers to discover the
   contribution from a table. Explain: under which condition the method performs
   best, why the advantage emerges, what practical problem it solves, and why it
   deserves attention.
5. **Limit the comparison scope.** Do not chase "wins on every dataset and metric."
   Make only claims your evidence firmly supports. Persuasion comes from tight
   claim-evidence alignment, not from the number of comparisons.
6. **Restructure the story when evidence is insufficient.** When existing results
   cannot support the original narrative, use the strongest evidence to redefine
   the problem, reorder contributions, reselect the headline result, and redesign
   the title, abstract, introduction, and experiment structure. Task scope determines
   whether to execute whole-paper restructuring; in local revision, recommend
   changes that exceed that scope.

## 2. Language rules (against self-undermining)

- Express results through evidence-bounded neutral facts, applicable scope, and
  genuine trade-offs. Retain information needed to understand and test claims;
  remove unnecessary self-negation without altering results. Use Section 5 as the
  single decision order for unfavorable material.
- Identify self-undermining by meaning, not word matching. "Unfortunately", "merely",
  "only achieves", "still lags far behind", and "limited improvement" are recognition
  examples, not banned strings: "requires only one forward pass" can state a strength,
  and "performance drops" can state a necessary experimental fact.
- Example: "Our method improves accuracy on two in-domain datasets; cross-domain
  generalization has not been evaluated." This states a demonstrated strength while
  retaining the unevaluated boundary.
- Results that form no advantage need not be forced into contribution takeaways.
  Retain necessary result summaries, but bound judgments by the evidence rather than
  turning a local observation into a verdict on the whole method.

## 3. Experiment rules

Experiments are tools of argument, not a warehouse of results. Every experiment
must carry at least one of the following explicit duties:

- prove the core method works;
- prove the advantage comes from the key mechanism;
- prove the method matters in the target scenario;
- rule out the most plausible alternative explanations;
- define applicable boundaries or present key counterevidence.

An experiment that does not strengthen the main line, distracts, or invites
irrelevant disputes: choose applicable actions under Section 5.
Experiments that establish claim boundaries or rule out alternative explanations
still carry an argumentative duty; unfavorable results alone do not justify removal.

## 4. Structure rules

**Abstract and introduction = the opening of the press conference.** Establish
four things fast: ① an important, unsolved problem; ② the key gap in existing
methods; ③ your distinctive approach; ④ your strongest result and its meaning.
Establish the problem and contribution before expanding implementation details,
background, and necessary boundaries. Qualifiers affecting opening claims belong
alongside those claims.

**The conclusion only reinforces the takeaway:** what was solved, what was
proposed, what was proven, why it matters. Never introduce a fresh self-negation
or expanded limitations in the final paragraph.

## 5. Authoritative decision order for unfavorable material

First mark information that must be retained or answered: facts, applicable
boundaries, and key counterevidence needed to understand or test the core claim,
and matters the user or reviewer explicitly asks to address. Deletion priority
does not apply to them. Moving them must preserve visibility and their connection
to the claims they qualify. Choose applicable actions in this seven-level priority
order, rather than forcing every action:

1. Delete content irrelevant to the core claim with no retention obligation;
2. Narrow the claim to avoid a pointless head-on comparison;
3. Switch to an evidence-supported evaluation dimension that better reflects value;
4. When supported by evidence, explain the result as a goal difference or trade-off;
5. Reorganize experiments so genuine strengths become the visual and narrative center;
6. Redefine the paper's story within the authorized scope, or recommend restructuring;
7. State necessary material plainly and neutrally, specifying conditions and scope.

The seventh level is a fallback for necessary disclosure, not permission to hide
facts; required information stays throughout. A narrative change must not alter
results, conceal key counterevidence, or present unevaluated matters as established.
Without evidence for a trade-off, narrow the claim or state the evidence boundary
rather than inventing an explanation.

## 6. Pre-submission checklist (never hand the reviewer a knife)

- Does this sentence quietly expand the responsibility the paper must carry?
- Does each new question serve the core argument, necessary boundaries, or an explicit
  obligation to respond?
- Does it describe a local phenomenon as a universal flaw?
- Does it use a negative judgment broader than the evidence?
- Is any passage unfolding as "what we did" process narration?
- Is a non-winning metric set as the main battlefield?
- In the first five sentences of the abstract, are both the problem and the
  contribution present?
- Does the conclusion smuggle in a sudden self-negation?

## Completion criteria

Check every section, paragraph, table, and sentence within the requested scope
against the applicable rules. Each identified issue is revised, given a proposed
fix, or accompanied by a reason for retaining it. Before delivery, confirm:

- Claims, comparison frames, and trade-off explanations are supported by evidence;
  necessary facts, counterevidence, and applicable boundaries remain visible.
- Edits stay within the authorized scope. Local revision identifies each issue's
  location and fix, leaving problem-free parts unchanged.
- Each experiment within the requested scope has an explicit argumentative duty.
  Structural checks cover only paper parts within the requested scope, including
  any abstract, introduction, or conclusion the request includes, under applicable rules.

For review tasks, report each issue and fix. For writing or whole-paper restructuring,
deliver the text without requiring a separate full checklist. Explicitly flag issues
that exceed the scope or remain unresolved for lack of evidence; stronger wording
is not a substitute for resolving them.
