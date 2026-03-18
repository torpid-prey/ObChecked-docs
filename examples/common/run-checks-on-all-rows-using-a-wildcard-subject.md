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

# Run checks on all rows using a wildcard Subject

---

## Problem

Some audit rules should apply to every row in the table rather than being limited to specific profiles or names.

Examples include phase validation, finish checks, and project-wide warnings.

## Strategy

Use a subject column with a wildcard match so the rule branch runs on every row.

This allows the subject node to act as a global entry point for common audit checks.

> It is important for common Subject nodes (that match all values) to have OnMatch and OnNoMatch both set to None so the subject match result doesn't impede individual Target audit flags.

## Rule Structure

Subject:
`PHASE.OTHERS`, `OnMatch: None`, `OnNoMatch: None`

Match:
Wildcard match `*`, `DisplayName: (Run on all rows)`

Target:
Various common columns depending on the rule.

Conditions:
Optional.

## Minimal Tree

    Subject: PHASE.OTHERS
      Match: *
        Target: Various common checks

## Example Results

| Subject Value | Cell Value | Result |
|--|--|--|
| Any value | Any Value | N/A |

## Explanation

The wildcard match allows the rule branch to run on every row in the dataset.

This makes it possible to perform global validation checks that are not tied to any specific object classification.

## Notes

Wildcard subjects are commonly used for project-wide validation rules.
