---
---

<div class="sticky-nav">
{% include nav.html %}
</div>

# Rule — Assembly Prefix Must Start With Phase Number

## Problem

In some workflows, the assembly prefix should begin with the current phase number.

This helps keep assembly marks grouped logically by phase and reduces the chance of numbering conflicts between otherwise similar assemblies in different phases.

A simple `startsWith` comparison is not sufficient here.

For example:

- `ASSY_PREFIX = 1B` and `PHASE.NUMBER = 1` is correct
- `ASSY_PREFIX = 10B` and `PHASE.NUMBER = 1` is **not** correct

If `startsWith` were used, both of these would pass because both strings begin with `1`.

## Strategy

Use a `stringCompare` target on `ASSY_PREFIX` with the operator `leadingInteger`.

This operator extracts the full leading integer from the **Target** cell before comparing it with the **ComparisonColumn**.

This means:

- `1B` returns leading integer `1`
- `10B` returns leading integer `10`
- `144B` returns leading integer `144`

The extracted numeric value is then compared against `PHASE.NUMBER`.

## Rule Structure

Subject:
`PHASE.OTHERS`

Match:
Wildcard `*`, `DisplayName: (Run on all rows)`

Target:
`ASSY_PREFIX` [leadingInteger = PHASE.NUMBER]

Conditions:
(Optional, depending on whether certain rows should be excluded)

## Minimal Tree

    Subject: PHASE.OTHERS
      Match: *
        Target: ASSY_PREFIX (stringCompare leadingInteger PHASE.NUMBER)

## Example Results

| ASSY_PREFIX | PHASE.NUMBER | Result |
|--|--|--|
| 1B | 1 | Okay |
| 10B | 10 | Okay |
| 10B | 1 | Error |
| 2045B | 2045 | Okay |
| 2045B | 245 | Error |

## Explanation

This rule uses the `leadingInteger` operator rather than `startsWith`.

That distinction is important:

- `startsWith` compares the start of the string literally
- `leadingInteger` extracts the full numeric value at the start of the target cell

This makes it suitable for assembly prefixes where the phase number may contain one digit or many digits.

The `stringCompare` target type is required because `ASSY_PREFIX` is a **string** column.

Although the comparison behaves numerically, the source cell itself is still a string value.

## Notes

This pattern also illustrates the difference between:

- `startsWith` and `leadingInteger`
- `endsWith` and `trailingInteger`

`leadingInteger` and `trailingInteger` are only drawn from the **Target** value, not the comparison value.

The **ComparisonColumn** must still return a comparable numeric value.

In this example, `PHASE.NUMBER` already contains only a number, so no substring extraction is required.

If the comparison value comes from a string such as `1ABC` or `12ABC`, the `StartIndex` and `StringLength` options may be needed to return only the numeric portion.

At present, `StartIndex` and `StringLength` are fixed values, so they are not suitable when the numeric portion of the comparison value has variable length.

This limitation only affects the **ComparisonColumn**.

The **Target** value can contain any number of digits at the start, and `leadingInteger` and `trailingInteger` will still extract the correct full integer value.