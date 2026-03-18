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

## Prefix by Radius

---

## Problem

The required part prefix depends on whether the part is curved.

A radius-based rule is useful when curved members must use a different mark or prefix than straight members.

## Strategy

Recognise the profile normally, then audit the prefix cell using multiple targets aimed at the same column.

This is only valid because the targets use **different Conditions**.

One target handles straight parts.
Another target handles curved parts.

## Rule Structure

Subject
: `PROFILE`

Match
: Recognises the relevant profile family

Targets
: `PART_PREFIX`

Conditions
: based on `RADIUS`

## Minimal Tree

    Subject: PROFILE
      Match: <profile family>
        Target: PART_PREFIX = [M]
          Condition: RADIUS = 0
        Target: PART_PREFIX = [U]
          Condition: RADIUS != 0

## Why This Pattern Is Useful

This pattern shows an important design rule in ObChecked:

The same cell should not normally be targeted twice within one match branch, **unless the targets are separated by different Conditions**.

That allows equivalent checks to apply in different situations without creating separate subject branches.

We use `!=` (not equal) rather than `>` (greater than) because some radius values are negative in Tekla.

## Example Results

| Profile | Radius | Part Prefix | Result |
|--|--|--|--|
| UB310x40 | 0 | M | Okay |
| UB310x40 | 0 | U | Error |
| UB310x40 | 2500 | U | Okay |
| UB310x40 | 2500 | M | Error |

## Notes

This pattern is often easier to maintain than duplicating entire profile rule sets.

It also demonstrates why Conditions exist beneath Targets rather than forcing every variation into separate Match branches.
