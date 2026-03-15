[Contents](../README.md) | [Concepts](../core-concepts/overview.md) | [Configuration](../configuration/overview.md) | [Main](../user-interface/main-window.md) | [Audits](../user-interface/audit-definition-editor.md) | [Examples](../examples/overview.md) | [Troubleshooting](../troubleshooting/overview.md)

---

# Target Type — StringCases

## Purpose

The **StringCases** target type categorises string values into predefined groups.

Each group represents a collection of recognised values and assigns a flag when a match is found.

This allows audit rules to classify string values and assign different severities depending on the recognised value.

StringCases is commonly used for validating properties such as:

- material grades
- assembly prefixes
- naming conventions
- paint systems
- classification codes

---

## How StringCases Works

When a Target uses the **StringCases** type, the value in the target column is compared against a collection of defined cases.

Each case group contains an array of patterns and is associated with a flag.

The case groups are evaluated in the following order:

```
Okay → Info → Warn → Error
```

If the value matches a pattern within one of the case groups, that group’s flag is applied to the cell.

If no patterns recognise the value, the **Otherwise** flag is applied.

---

## Case Groups

StringCases contains four case groups:

- **Okay** _— receives blue text, no cell colour_
- **Info** _— receives blue cell colour_
- **Warn** _— receives yellow cell colour_
- **Error** _— receives red cell colour_

Each group contains an array of patterns representing recognised values.

Example:

```
Okay:
    S355
    S460

Warn:
    S235
```

If the cell value matches any pattern within a group, that group’s flag is applied.

Each group may contain multiple values.

---

## Otherwise Result

If the value does not match any of the defined patterns, the **Otherwise** flag is applied.

In most cases, Otherwise is left as **Error**, which allows any unrecognised values to be automatically flagged.

Because of this behaviour, it is usually unnecessary to populate the **Error** case group unless specialised behaviour is required.

Example:

```
Okay:
    S355
    S460

Warn:
    S235

Otherwise: Error
```

Any value other than the recognised ones will be flagged as **Error**.

---

## Pattern Matching

StringCases supports two pattern matching modes, controlled by the **MatchKind** property.

### Exact

The value must match the pattern exactly.

Example:

```
Pattern: S355
Value: S355
Result: Match
```

```
Pattern: S355
Value: S355JR
Result: No match
```

Exact matching is useful when values must match specific identifiers.

---

### Like

The **Like** mode allows wildcard matching using `*`.

Wildcards are supported only at the **start and/or end** of the pattern.

Example:

```
Pattern: S355*
```

This will match values such as:

```
S355
S355JR
S355J2
```

Wildcards are not supported in the middle of the pattern.

---

## Case Arrays

Each severity group supports an **array of values**.

This allows a single case group to recognise multiple valid options.

Example:

```
Okay:
    S355
    S355JR
    S355J2
```

Each value in the array is treated as a valid recognised option.

---

## Using Tokens in Messages

Values listed within the case groups can be referenced in audit messages using tokens.

For example:

```
{@OKAY}
```

This token will display the values defined in the **Okay** case group.

Example message:

```
Expected material: {@OKAY}
```

When a user clicks on a flagged cell, the message panel will display the list of expected values.

The same token system applies to other groups:

```
{@INFO}
{@WARN}
{@ERROR}
```

This allows messages to dynamically display recognised values without repeating them manually.

---

## Duplicate Values

Values should not appear in multiple case groups.

If the same value appears in multiple groups, the behaviour becomes ambiguous and difficult to interpret.

If a value requires different outcomes under different conditions, this should be implemented using:

- multiple **Target** nodes
- **Condition** nodes to determine which rule applies

---

## Example

Example audit rule validating steel grades:

```
TargetColumn: MATERIAL
Type: StringCases

Okay:
    S355
    S460

Warn:
    S235

Otherwise: Error
```

Possible results:

```
Value: S355 → Okay
Value: S235 → Warn
Value: S690 → Error (Otherwise)
```

---

## When to Use StringCases

StringCases is best used when values fall into clearly defined categories.

Typical use cases include:

- validating acceptable material grades
- enforcing allowed prefixes
- classifying naming conventions
- identifying deprecated values

It provides a flexible way to map recognised values directly to audit severities.
