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

# CHS Length override rules with *onAnyMatch*

---

## Problem

A CHS member may initially fail the first length table, but still be valid under a second table when the material and size combination allow a longer stock length.

This means a later rule may need to **replace** an earlier error.

## Strategy

Apply the first length rule normally.

If the member is recognised by the secondary table, use a later `LENGTH_NET` target with `onAnyMatch` so it can overwrite the earlier error result.

## Rule Structure

Subject
: `PROFILE`

Match
: Regex (CHS)

Primary Target
: `LENGTH_NET` checked against first table

Override Target
: `LENGTH_NET` checked against second table using `onAnyMatch`

## Minimal Tree

    Subject: PROFILE
      Match: Regex (CHS)
        Target: LENGTH_NET  [first table]
        Target: LENGTH_NET  [second table, onAnyMatch]

## Why `onAnyMatch` Matters

`onAnyMatch` allows a later rule to overwrite an existing result even if the earlier result is more severe.

This is useful when:

- a later rule is intentionally more specific
- an earlier error should be cleared when an exception is recognised
- rule evaluation must support layered override logic

## Example Behaviour

| Profile | Material | Length | First Table | Second Table | Final Result |
|--|--|--:|--|--|--|
| CHS... | 250 | 6400 | Okay | not needed | Okay |
| CHS... | 350 | 7000 | Error | Okay via second table | Okay |
| CHS... | 350 | 8000 | Error | Error | Error |

## Why This Pattern Is Useful

This example gives a real purpose to `onAnyMatch`.

Without it, a later valid rule could not replace the earlier error even when the second table clearly shows that the member is acceptable.

## Notes

This is a good reference whenever a rule set needs:

- a broad first-pass validation
- a more specific later exception
- intentional overwriting of an earlier result
