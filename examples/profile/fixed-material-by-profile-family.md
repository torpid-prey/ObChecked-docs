[Contents](../../README.md) | [Concepts](../../core-concepts/overview.md) | [Configuration](../../configuration/overview.md) | [Main](../../user-interface/main-window.md) | [Audits](../../user-interface/audit-definition-editor.md) | [Examples](../../examples/overview.md) | [Troubleshooting](../../troubleshooting/overview.md)

---

# Fixed Material by Profile Family

## Problem

All members within a recognised profile family must use the same material grade.

A simple example is a UB family where all recognised profiles must use `300PLUS`.

## Strategy

Use the `PROFILE` subject to recognise the profile family, then audit the `MATERIAL` cell using a simple expected-value target.

This is one of the simplest and most useful audit patterns because it shows the standard flow:

- recognise the subject value
- run one target
- compare the target cell against the expected value

## Rule Structure

Subject
: `PROFILE`

Match
: Regex or Like pattern recognising the required family

Target
: `MATERIAL`

Expected Result
: `300PLUS`

## Minimal Tree

    Subject: PROFILE
      Match: UB*
        Target: MATERIAL

## Why This Pattern Is Useful

This pattern is useful whenever a whole profile family shares one required property.

Typical examples include:

- fixed material grade
- fixed paint system
- fixed class value
- fixed prefix

## Example Results

| Profile | Material | Result |
|--|--|--|
| UB310x40 | 300PLUS | Okay |
| UB310x40 | 350 | Error |
| UB460x82 | 300PLUS | Okay |

## Notes

This is a good starting example for new users because it introduces the basic audit flow without conditions or fallback logic.

If the required value later depends on another property, the same pattern can be extended using Conditions.
