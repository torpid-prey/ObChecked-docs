---
layout: default
title: Target Type — NumericBands
---

## Purpose

The **NumericBands** target type evaluates numeric values that fall within defined ranges.

Each band defines an upper limit and assigns a flag when the value falls within that range.

NumericBands is typically used for values such as:

- part lengths
- bolt lengths
- weight limits

It is designed for **range validation**, not exact value matching.

Numeric bands cannot be entered straight into the Target details. You need to open the Bands collection via the `...` button.

Once defined, they will become visible in the Target properties.

---

## How NumericBands Works

NumericBands compares the numeric value of the target column against a collection of defined bands.

Each band represents a value that the cell must be **less than or equal to**.

Bands are evaluated from **lowest value to highest value**.

The first band whose value is greater than or equal to the cell value determines the result.

If the value exceeds all defined bands, the **Otherwise** flag is applied.

---

## Example Range Evaluation

Example configuration:

```
Okay:
    12000

Warn:
    15000
```

Interpretation:

```
Value ≤ 12000 → Okay
12000 < Value ≤ 15000 → Warn
Value > 15000 → Otherwise
```

This allows audit severity to increase as values exceed acceptable limits.

---

## Defining Minimum Values

NumericBands can also be used to enforce **minimum values** by defining a band with a low threshold.

Example:

```
Error:
    500

Okay:
    15000

Warn:
    18000

Otherwise: Error
```

Interpretation:

```
Value ≤ 500 → Error
500 < Value ≤ 15000 → Okay
15000 < Value ≤ 18000 → Warn
Value > 18000 → Error
```

This configuration allows both minimum and maximum limits to be enforced.

---

## Band Ordering

Bands are evaluated from **lowest value to highest value**.

The system sorts bands automatically to ensure correct evaluation order.

The first group that the cell value fits in determines the flag that it receives.

---

## Otherwise Result

If the value exceeds all defined bands, the **Otherwise** flag is applied.

In most cases this is set to **Error**, ensuring values outside the defined ranges are flagged.

---

## Token Support in Messages

Band values can be referenced in audit messages using tokens.

Available tokens include:

```
{@OKAY}
{@INFO}
{@WARN}
{@ERROR}
```

Example message:

```
Expected length ≤ {@OKAY}
```

When a user selects a flagged cell, the message panel will display the configured band values.

This allows audit messages to dynamically display the expected limits.

---

## Tolerance

NumericBands support numeric tolerance.

Tolerance is derived from the display format defined in the Column Definitions form.

This helps avoid false failures caused by rounding or display precision.

For example, equality does not require the two values to be mathematically identical down to every decimal place. Instead, they are considered equal if the difference falls within tolerance.

This same tolerance system is also used by **NumericCompare**.

---

## Column Limitations

NumericBands evaluates only the value of the **TargetColumn**.

It does not extract numeric values from complex strings.

For example, profile dimensions such as **depth** or **thickness** cannot currently be derived directly from a profile string.

If these values need to be audited, they must be available as a separate column (for example via a ReportProperty).

Profile dimensions can still be used within **Condition nodes**, but NumericBands itself only evaluates the numeric value contained in the target column.

---

## NumericBands vs Exact Values

NumericBands is designed for **ranges of numeric values**, not strict equality checks.

If a cell must equal a specific numeric value, the **StringCases** target type should be used instead.

Example:

Checking whether a class equals `1` should use **StringCases**, not NumericBands.

---

## When to Use NumericBands

NumericBands is best used when values must fall within defined numeric limits.

Typical uses include:

- validating maximum stock lengths
- detecting values below minimum thresholds
- enforcing tolerance limits
- identifying values outside standard ranges

It provides a clear and flexible way to define numeric ranges and apply audit flags based on those limits.
