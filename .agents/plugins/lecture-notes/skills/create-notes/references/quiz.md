---
callout_type: "question"
foldable_callouts: true
---

# Quiz Module Specification

Use this module at the conclusion of major sections or conceptually rich topics to reinforce learning through self-assessment questions that test mechanisms and trade-offs.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:quiz section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
> [!question]- 📝 Self-Assessment Check: <Topic Name>
> 
> **Question 1**: <Conceptual prompt probing operational understanding of a core rule or mechanism.>
> - [ ] A) <Plausible distractor representing common misconception>
> - [ ] B) <Plausible distractor representing superficial reading>
> - [x] C) <Correct option accurately stating the technical invariant>
> - [ ] D) <Plausible distractor failing on an edge condition>
> 
> **Question 2**: <Diagnostic question probing trade-offs, limiting cases, or design friction.>
> 
> > [!tip]- Answer & Explanation
> > - **Question 1 (C)**: <Technical explanation of why C holds and why distractors fail.>
> > - **Question 2**: <Direct explanation resolving the diagnostic question with reference to system invariants.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 1 question | 1 direct multiple-choice or short-answer prompt with folded answer | Accessible, recall | Question and answer folded (`-`) |
| **`2`** | 2 questions | 1 multiple-choice + 1 scenario prompt + folded explanations | Standard analytical | Question and answer folded (`-`) |
| **`3`** | 3 questions | 1 conceptual + 1 edge-case + 1 trade-off scenario prompt + deep explanations | Challenging, diagnostic | Question and answer folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the quiz callout directly below it.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **Fold Answers**: Always fold the answer/explanation sub-callout so the learner can test themselves before seeing the answer.
- **No Trivial Trivia**: Avoid testing arbitrary slide numbers or historical dates; test fundamental mechanisms and trade-offs.
