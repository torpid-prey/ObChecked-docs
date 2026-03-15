[Contents](../../README.md) | [Concepts](../../core-concepts/overview.md) | [Configuration](../../configuration/overview.md) | [Main](../../user-interface/main-window.md) | [Audits](../../user-interface/audit-definition-editor.md) | [Examples](../../examples/overview.md) | [Troubleshooting](../../troubleshooting/overview.md)

---

# CHS Fallback Material Rules with `onFirstMatch`

## Problem

The CHS availability tables overlap awkwardly.

A first set of rules covers the main table, but some additional `350` cases also need to be recognised from a secondary list.

Trying to merge both tables into one clean rule set can become difficult and error-prone.

## Strategy

Use the main CHS material targets first, then add fallback `MATERIAL` targets configured with `onFirstMatch`.

This allows the fallback checks to apply **only if no earlier target has already set a result** for the same cell.

## Rule Structure

Subject
: `PROFILE`

Match
: Regex (CHS)

Primary Targets
: main table of material rules

Fallback Targets
: secondary `350` rules using `onFirstMatch`

## Minimal Tree

    Subject: PROFILE
      Match: Regex (CHS)
        Target: MATERIAL  [main table]
        Target: MATERIAL  [main table]
        Target: MATERIAL  [fallback, onFirstMatch]
        Target: MATERIAL  [fallback, onFirstMatch]

## Why `onFirstMatch` Matters

`onFirstMatch` prevents the fallback rule from overwriting an earlier result.

That makes it ideal for cases where:

- a later rule is only a backup
- the first matching results are limited via conditions
    - i.e. not necessarily applied to every row
- overlapping lists would otherwise create unnecessary conflicts

## Example Behaviour

| Profile | Material | Main Table Result | Fallback Result | Final Result |
|--|--|--|--|--|
| CHS... found in main table | 250 | Okay | skipped | Okay |
| CHS... not in main table | 350 | no result | Okay | Okay |
| CHS... found in main table | 250 | Error | skipped | Error |
| CHS... not in main table | 350 | no result | Info | Info |

## Notes

This is a good reference for any rule set where:

- one table handles the main logic
- another table fills in exceptions
- later rules should only apply if nothing else has already matched
