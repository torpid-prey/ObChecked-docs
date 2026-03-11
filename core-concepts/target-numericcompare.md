# Target Type: NumericCompare

## Purpose

The **NumericCompare** target type compares the numeric value of one column against the numeric value of another column.

It is used when two cells in the same row must satisfy a numeric relationship.

Typical examples might include:

- one length being greater than another
- one tolerance value being less than or equal to another
- one numeric property being expected to equal another within rounding tolerance

NumericCompare produces either a **Pass** or **Otherwise** result depending on whether the comparison succeeds.

---

## How NumericCompare Works

NumericCompare compares the value of the **TargetColumn** against the value of a **ComparisonColumn** using a numeric operator.

The evaluation process is:

```text
1. Read numeric value from TargetColumn
2. Read numeric value from ComparisonColumn
3. Determine numeric tolerance
4. Apply the selected operator
5. Apply Pass or Otherwise flag
```

If either cell is empty or cannot be interpreted as numeric, the comparison fails and the **Otherwise** result is applied.

---

## ComparisonColumn

This property specifies the column whose numeric value will be compared against the target cell.

Example:

```text
TargetColumn: LENGTH_NET
ComparisonColumn: LENGTH_GROSS
```

---

## Operators

NumericCompare supports the following operators:

- `==`
- `!=`
- `<`
- `<=`
- `>`
- `>=`

These operators compare the numeric value of the TargetColumn against the numeric value of the ComparisonColumn.

---

## Tolerance

NumericCompare supports numeric tolerance.

Tolerance is derived from the display format defined in the Column Definitions form.

The comparison uses the greater tolerance of:

- the **TargetColumn**
- the **ComparisonColumn**

This helps avoid false failures caused by rounding or display precision.

For example, equality does not require the two values to be mathematically identical down to every decimal place. Instead, they are considered equal if the difference falls within tolerance.

This same tolerance system is also used by **NumericBands**.

---

## Comparison Behaviour

NumericCompare uses tolerance when evaluating operators.

Conceptually, the comparisons behave like this:

```text
==   Pass if the two values are equal within tolerance
!=   Pass if the difference is greater than tolerance
<    Pass if left is less than right beyond tolerance
<=   Pass if left is less than or effectively equal within tolerance
>    Pass if left is greater than right beyond tolerance
>=   Pass if left is greater than or effectively equal within tolerance
```

This makes NumericCompare more practical for model data than strict floating-point comparison.

---

## Result Flags

NumericCompare produces two possible results:

```text
Pass
Otherwise
```

If the comparison succeeds, the **Pass** flag is applied.

If the comparison fails, the **Otherwise** flag is applied.

Unlike **StringCases** or **NumericBands**, NumericCompare does not support multiple severity levels within the comparison itself.

---

## Non-Numeric Values

NumericCompare requires both compared cells to contain numeric values.

If either value is:

- empty
- null
- non-numeric

then the comparison is treated as a failure and the **Otherwise** result is applied.

---

## When to Use NumericCompare

NumericCompare is best used when one numeric property must relate directly to another numeric property.

Typical uses include:

- checking whether one value is greater than another
- checking whether two numeric values are equal within tolerance
- validating numeric relationships between columns

If the audit is checking whether a value falls within a defined range, **NumericBands** is usually a better choice.

If the audit is checking whether a cell value must be equal to a substring of another cell, **StringCompare** with LeadingInteger or TrailingInteger is possibly a better choice.

---

## Notes

NumericCompare is included as a general-purpose comparison type so that numeric cross-column checks are available when needed.

In many audit rule sets it may be used less often than StringCompare, StringCases, or NumericBands, but it remains useful for specialised numeric relationships between properties.
