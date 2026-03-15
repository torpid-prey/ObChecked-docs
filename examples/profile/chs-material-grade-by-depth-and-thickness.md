[Contents](../../README.md) | [Concepts](../../core-concepts/overview.md) | [Configuration](../../configuration/overview.md) | [Main](../../user-interface/main-window.md) | [Audits](../../user-interface/audit-definition-editor.md) | [Examples](../../examples/overview.md) | [Troubleshooting](../../troubleshooting/overview.md)

---

# CHS Material Grade by Depth and Thickness

## Problem

CHS sections do not use a single material rule.

The permitted grade depends on **both** the depth and wall thickness extracted from the profile.

Some sizes are available only in `250`, some only in `350`, and some are available in both. Where both are available, `250` may be preferred while `350` is still acceptable.

## Strategy

Use one CHS regex Match to extract the key profile values, then apply many `MATERIAL` Targets with Conditions based on both depth and thickness.

This approach avoids duplicating the same regex logic repeatedly.

## Rule Structure

Subject
: `PROFILE`

Match
: Regex extracting CHS depth and thickness

Target
: `MATERIAL`

Conditions
: use depth and thickness match groups together

## Minimal Tree

    Subject: PROFILE
      Match: Regex (CHS)
        Target: MATERIAL
          Condition: depth = X and thickness within range A
        Target: MATERIAL
          Condition: depth = X and thickness within range B
        Target: MATERIAL
          Condition: depth = Y and thickness within range C

## Why This Pattern Is Useful

This is the clearest example of Conditions being used to build a decision table.

The regex provides the raw inputs.
The Conditions interpret those inputs.
The Targets define the valid material outcome.

## Example Results

| Profile | Depth | Thickness | Material | Result |
|--|--:|--:|--|--|
| CHS139.7*4.0 | 139.7 | 4.0 | 350 | Okay |
| CHS139.7*4.0 | 139.7 | 4.0 | 250 | Error |
| CHS139.7*5.0 | 139.7 | 5.0 | 250 | Okay |
| CHS139.7*5.0 | 139.7 | 5.0 | 350 | Info |

## Why `Info` Can Be Useful Here

Where both grades are available, a result of `Info` can be used to show that an alternate acceptable grade exists while still indicating that another option is preferred.

This is a good example of using severity levels for **guidance**, not just pass/fail control.

## Notes

This rule set is intentionally more complex than most profile examples.

It is a good reference whenever a rule depends on:

- more than one extracted regex value
- many conditional targets on the same cell
- preferred vs alternate acceptable values
