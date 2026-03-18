---
---

<div class="sticky-nav">
{% include nav.html %}
</div>

# Examples

{% include nav_examples.html %}

---

# Common Rule Examples

{% include nav_examples_common.html %}

# UserPhase must match PhaseNumber

---

## Problem

The UDA `USER_PHASE` property may be used to match the actual `PHASE.NUMBER`.

> This is a technique which allows Part Mark numbering to differ by phase, since Tekla numbering settings now only supports Assembly Marks to differ by phase.

If these values differ, the model may try to re-use drawings that have already been used, e.g. a new plate might get the same number as a plate in another phase that has already been fabricated. In some workflows, this is extremely problematic.

## Strategy

Compare the value in `USER_PHASE` with `PHASE.NUMBER`.

Exclude objects with materials such as `DUMMY` or `GROUT`, since these objects are not relevant to this check.

## Rule Structure

Subject:
`PHASE.OTHERS`

Match:
Wildcard `*`

Target:
`USER_PHASE (equals PHASE.NUMBER)`

Conditions:
`MATERIAL` is not `DUMMY` or `GROUT`.

## Minimal Tree

    Subject: PHASE.OTHERS
      Match: *
        Target: USER_PHASE (stringCompare equals PHASE.NUMBER)
           Condition: MATERIAL notEquals {DUMMY, GROUT}

## Example Results

| Phase Number | User Phase | Material | Result |
|--|--|--|--|
| 100 | 100 | 300PLUS | Okay |
| 200 | (empty) | 350 | Error |
| 1 |  (empty) | DUMMY | Skipped |

## Explanation

This rule compares the displayed user phase against the actual phase number.

The condition prevents the rule from running on objects that are not relevant to phase auditing.

## Notes

Conditions are often used in common rules to exclude irrelevant object types.
