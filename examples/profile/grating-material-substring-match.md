# Grating Material Substring Match

## Problem

Some complex profile names cannot be validated using a simple wildcard pattern.

For example, a grating profile such as `A325-MPG-993` may need to be checked against a material value where only part of the profile string is significant.

## Strategy

Use a normal profile match to recognise the grating family, then audit `MATERIAL` with `StringCompare`.

The comparison uses a substring from one column rather than a full-cell comparison.

This is useful when the important identifier is embedded inside a larger string.

## Rule Structure

Subject
: `PROFILE`

Match
: Recognises the grating profile family

Target
: `MATERIAL`

Target Type
: `StringCompare`

Comparison
: compare `MATERIAL` against a substring of `PROFILE`

## Minimal Tree

    Subject: PROFILE
      Match: <grating pattern>
        Target: MATERIAL

## Example Logic

Profile value:

    A325-MPG-993

Relevant substring from profile:

    StartIndex = 0
    StringLength = 4
    Result = A325

Material value:

    A325-MP*

Comparison:

    MATERIAL startsWith PROFILE substring

## Example Results

| Profile | Material | Substring Used | Result |
|--|--|--|--|
| A325-MPG-993 | A325-MP | A325 | Okay |
| A325-MPG-993 | A405-MP | A325 | Error |

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
