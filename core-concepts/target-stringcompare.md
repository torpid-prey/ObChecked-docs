---
---

<div class="sticky-nav">
{% include nav.html %}
</div>

# Core Concepts

{% include nav_concepts.html %}

---

# Target Node — Type: StringCompare

{% include nav_concepts_targets.html %}

---

## Purpose

The **StringCompare** target type compares the value of one column against the value of another column.

This allows audit rules to enforce relationships between properties.

Typical uses include:

- ensuring naming conventions match profile identifiers
- verifying assembly prefixes match phase numbers
- validating property relationships between columns
- checking that one property contains information derived from another

StringCompare produces either a **Pass** or **Otherwise** result depending on whether the comparison succeeds.

---

## How StringCompare Works

StringCompare compares the value of the **TargetColumn** against the value of a **ComparisonColumn**.

The comparison is performed using a selected **Operator**.

The comparison value can optionally be extracted from the ComparisonColumn using substring settings.

The evaluation process is:

```
1. Read value from TargetColumn
2. Read value from ComparisonColumn
3. Optionally extract substring from ComparisonColumn
4. Apply the selected Operator
5. Apply Pass or Otherwise flag
```

---

## ComparisonColumn

This property specifies the column whose value will be compared against the target cell.

The ComparisonColumn will be another property/cell within the same row.

Example:

```
TargetColumn: MATERIAL
ComparisonColumn: PROFILE
```

---

## Substring Extraction

The value from the ComparisonColumn can optionally be reduced to a substring before comparison.

Two properties control this behaviour:

```
StartIndex
StringLength
```

### StartIndex

Defines the starting position of the substring.

### StringLength

Defines the number of characters to include in the substring.

If both StartIndex and StringLength are defined, the substring is extracted using both values.

Example:

```
PROFILE: A405-MPG-995
StartIndex: 0
StringLength: 4
Result: A405
```

If StartIndex is set without StringLength, the substring continues to the end of the string.

Example:

```
PROFILE: A405-MPG-995
StartIndex: 5
StringLength: 
Result: MPG-995
```

---

## Operators

StringCompare supports several operators for comparing values.

_Since wildcards cannot be used with comparison values, additional operators (contains, startsWith, endsWith etc.) were added to improve versatility._

### Equals

The target value must exactly match the comparison value.

### NotEquals

The target value must not match the comparison value.

### Contains

The target value must contain the comparison value.

### NotContains

The target value must not contain the comparison value.

### StartsWith

The target value must start with the comparison value.

### EndsWith

The target value must end with the comparison value.

---

## Numeric Extraction Operators

Two specialised operators extract numeric values from the target string.

These operators are designed for situations where numeric identifiers appear within string values.

In both of these cases, the ComparisonColumn or substring must be a numeric value.

---

### LeadingInteger

Extracts the **numeric value at the beginning of the target string** before comparing against the comparison value.

The extracted number is then compared to the comparison value.

Example:

```
Target: 10B
LeadingInteger → 10
```

This allows the full numeric value to be compared rather than simply matching characters.

Example use case:

```
Assembly Prefix: 1B
Assembly Prefix: 10B
Phase: 1
```

Using **StartsWith**:

```
1B → Match
10B → Match
```

Using **LeadingInteger**:

```
1B → Match
10B → No match
```

This ensures that only assemblies with the correct numeric prefix are recognised.

---

### TrailingInteger

Extracts the **numeric value at the end of the target string** before comparing against the comparison value.

Example:

```
Target: B12
TrailingInteger → 12
```

This operator is useful when numeric identifiers appear at the end of a string.

---

## Example

Example rule ensuring that material matches the important part of a profile identifier.

```
TargetColumn: MATERIAL
ComparisonColumn: PROFILE
Operator: StartsWith
StartIndex: 0
StringLength: 4
```

Example values:

```
PROFILE: A405-MPG-995
MATERIAL: A405MP
```

Result:

```
A405MP startsWith A405 → Pass
```

This ensures the material matches the profile series.

---

## Result Flags

StringCompare produces two possible results:

```
Pass
Otherwise
```

If the comparison succeeds, the **Pass** flag is applied.

If the comparison fails, the **Otherwise** flag is applied.

Unlike some other Target types, StringCompare does not support multiple severity levels within the comparison itself.

---

## When to Use StringCompare

StringCompare is best used when one property must match or contain information derived from another property.

Typical uses include:

- enforcing naming conventions
- verifying assembly prefixes
- matching profile identifiers to material names
- validating relationships between properties

It provides a flexible way to ensure consistency between related values within a row.
