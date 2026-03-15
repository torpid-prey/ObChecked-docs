[Contents](../../README.md) | [Concepts](../../core-concepts/overview.md) | [Configuration](../../configuration/overview.md) | [Main](../../user-interface/main-window.md) | [Audits](../../user-interface/audit-definition-editor.md) | [Examples](../../examples/overview.md) | [Troubleshooting](../../troubleshooting/overview.md)

---

# Grating Material Substring Match

## Problem

Some complex profile names cannot be validated using a simple wildcard pattern.

For example, a grating profile such as `A325-MPG-993` may need to be checked against a material value where only part of the profile string is significant.

## Strategy

Use a normal profile match to recognise the grating family, then audit `MATERIAL` with `StringCompare`.

The comparison uses a substring from a cell rather than a full-cell comparison.

This is useful when the important identifier is embedded inside a larger string.

## Rule Structure

Subject
: `PROFILE`

Match
: Recognises the grating profile family

Target 
: `MATERIAL` *(cell to receive audit result)*

Target Type
: `StringCompare`

Comparison Column
: `PROFILE`
: `startIndex = 0`
: `stringLength = 4`

## Minimal Tree

    Subject: PROFILE
      Match: <grating pattern>
        Target: MATERIAL

## Example Logic

Material *(Target)* value:

    A325-MP*

Profile *(Comparison)* value:

    A325-MPG-993

Relevant substring from Profile:

    StartIndex = 0
    StringLength = 4
    Result = A325

Comparison:

    MATERIAL startsWith PROFILE substring

## Example Results

| Profile | Material | Substring Used | Result |
|--|--|--|--|
| A325-MPG-993 | A325MP* | A325 | Okay |
| A325-MPG-993 | A253MP* | A325 | Error |

## Why This Pattern Is Useful

This example demonstrates why `StringCompare` exists.

A standard Like or wildcard pattern is not always enough when:

- only part of a value is significant
- two cells must be checked against each other
- the relationship between cells is more important than an exact literal value

## Notes

This pattern is a good reference whenever a rule needs:

- substring extraction
- cross-column comparison
- validation of encoded identifiers
