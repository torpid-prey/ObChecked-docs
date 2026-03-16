---
---

{% include nav.html %}

<!-- [Contents](../../README.md) | [Concepts](../../core-concepts/overview.md) | [Configuration](../../configuration/overview.md) | [Main](../../user-interface/main-window.md) | [Audits](../../user-interface/audit-definition-editor.md) | [Examples](../../examples/overview.md) | [Troubleshooting](../../troubleshooting/overview.md) -->

---

# Rule — Material Determines Valid Finish

## Problem

Different objects may require a part finish, but the list of acceptable finishes may depend on the type of material.

If the finish does not match the provided collection, the model may contain incorrect fabrication instructions.

## Strategy

Use the `MATERIAL` column to classify rows and apply finish validation rules.

Specific materials are matched first, followed by a wildcard fallback for general steelwork.

## Rule Structure

Subject:
`MATERIAL`

Match:
Exact: 
`G450`, or wildcard fallback `*`

Target:
`FINISH`

Conditions:
`MAIN_PART`, `ASSEMBLY.HIERARCY_LEVEL`

## Minimal Tree

    Subject: MATERIAL
      Match: G450
        Target: FINISH [GALVANISED]
      Match: *
        Target: FINISH [NO PAINT, PRIMER, HD GALV ]
          Conditions: MAIN_PART {like True}, ASSEMBLY.HIERARCHY_LEVEL == 0


## Example Results

| Material | Finish | Main Part | Hierarchy Level | Result |
|--|--|--|--|--|
| G450 | GALVANISED | True | 0 | Okay |
| G450 | NO PAINT | False | 0 | Error |
| 300PLUS | PRIMER | True | 0 | Okay |
| 350 | NO PAINT | True | 0 | Okay |
| 350 | NO PAINT | False | 0 | Skipped |
| 250 | PRIMER | True | 1 | Skipped |
| 300PLUS | GREEN | True | 0 | Error |

## Explanation

This rule set uses layered matches.

Specific material types are matched first. `G450` only allows one finish. Once this match is successful, other matches do not run for this part.

A final wildcard match handles all remaining steelwork and validates finish aginst an array of acceptable finish values.

The target in the wildcard match has multiple conditions, so in some cases the result is skipped because the audit conditions did not pass.

## Notes

Match nodes are order-specific, and only one successful match node is evaluated **per subject**.

Wildcard `*` match results will not override an existing match result *if it is within the same subject*.
