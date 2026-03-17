---
---

<div class="sticky-nav">
{% include nav.html %}
</div>

# Rule — Recognised Assembly Names Set Prefix and Class

## Problem
Certain object names represent specific assembly types.

These assemblies should use consistent prefixes and class values.

Without validation, inconsistent naming can occur across the model.

## Strategy
Use the **NAME** column to detect recognised assembly types and validate related assembly properties.

## Rule Structure

Subject:
`NAME`

Match: 
Exact match that returns a recognised assembly part name, BEAM, COLUMN, etc.

Target:
`ASSY_PREFIX`, `CLASS`, using stringCases to define options.

Conditions:
(None)

## Minimal Tree

    Subject: NAME
      Match: BEAM
        Target: ASSY_PREFIX [B]
        Target: CLASS: Okay: [1], Info: [7]

## Example Results
*Results per cell*

| NAME | Assy Prefix | Result |
|--|--|--|
| BEAM | B | Okay |
| BEAM | C | Error |

| NAME | Class | Result |
|--|--|--|
| BEAM | 1 | Okay |
| BEAM | 2 | Error |
| BEAM | 7 | Info |

## Explanation

Assembly naming often defines how objects are organised in drawings and schedules.

Ensuring the correct prefix and classification maintains consistency across the project.

## Notes

Multiple targets can be applied to the same match to validate both prefix and class.

Multiple acceptable options / severities can be provided using stringCases arrays.
