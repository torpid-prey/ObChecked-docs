---
---

<div class="sticky-nav">
{% include nav.html %}
</div>

# Examples

{% include nav_examples.html %}

---

# Rule — Vertical Part Name Requires Correct Rotation

## Problem
Certain part names represent vertical members such as columns or droppers.

These parts must maintain the correct orientation relative to project north.

Incorrect rotation may cause drawing symbols to appear in the wrong location.

## Strategy
Use the **NAME** column to identify vertical members and apply a **Direct** rotation check.

## Rule Structure

Subject:
`NAME`

Match:
Exact match that returns a recognised vertical part, COLUMN, DROPPER, etc.

Target:
Direct: `RotationByProjectNorth`

Conditions:
(None)

## Minimal Tree

    Subject: NAME
      Match: COLUMN
        Target: ROTATION (Top, Front, Back, Below, depending on Project North Rotation)

## Example Results

| NAME | ROTATION | Result |
|--|--|--|
| COLUMN | FRONT | Okay |
| DROPPER | BACK | Error |
| COLUMN | TOP | Okay |
| COLUMN | BELOW | Error |

## Explanation

Tekla uses several settings to determine assembly mark direction.

If vertical members are rotated incorrectly relative to project north, drawing output becomes inconsistent.

This rule ensures that these elements maintain the correct orientation.

## Notes

This rule uses the **[Direct](../../core-concepts/target-direct.md)** audit type rather than a value comparison.

Also note that `XS_ORIENTATION_MARK_DIRECTION` must be correctly configured also. 
