---
---

<div class="sticky-nav">
{% include nav.html %}
</div>

# Examples

{% include nav_examples.html %}

---

# Profile Rule Examples

{% include nav_examples_profiles.html %}

## Length by Profile Depth

---

## Problem

The maximum permitted member length depends on the depth of the profile.

For example, smaller UB sections may only be available in shorter stock lengths than deeper sections.

## Strategy

Use a regex Match on `PROFILE` to extract the profile depth into a numeric match group.

Then audit `LENGTH_NET` with one or more targets whose Conditions use `matchNumber[0]` to decide which limit applies.

## Rule Structure

Subject
: `PROFILE`

Match
: Regex that extracts profile depth, e.g. `UB310*40`

Target
: `LENGTH_NET`

Conditions
: based on `matchNumber[0]`

## Minimal Tree

    Subject: PROFILE
      Match: Regex
        Target: LENGTH_NET <= 15000
          Condition: matchNumber[0] <= 200
        Target: LENGTH_NET <= 18000
          Condition: matchNumber[0] > 200
*Therefore, sections up to incl. 200 deep are available in 15000 lengths. Deeper sections are available in 18000 lengths.*

## Why This Pattern Is Useful

This pattern shows how a profile string can drive a numeric rule without needing a separate dedicated depth column.

It is especially useful when:

- stock length depends on profile size
- a profile code contains the dimensions needed for the rule
- the rule depends on a numeric value extracted by regex

## Example Results

| Profile | Extracted Depth | Length | Result |
|--|--:|--:|--|
| UB200x18 | 200 | 12000 | Okay |
| UB200x18 | 200 | 16000 | Error |
| UB460x82 | 460 | 12000 | Okay |
| UB460x82 | 460 | 16000 | Okay |

## Notes

This is one of the most common “regex + numeric condition” patterns in ObChecked.

If the same depth logic also controls material or prefix rules, the same match can contain additional targets for those cells.
