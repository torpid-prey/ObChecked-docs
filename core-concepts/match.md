---
---

{% include nav.html %}

<!-- [Contents](../README.md) | [Concepts](../core-concepts/overview.md) | [Configuration](../configuration/overview.md) | [Main](../user-interface/main-window.md) | [Audits](../user-interface/audit-definition-editor.md) | [Examples](../examples/overview.md) | [Troubleshooting](../troubleshooting/overview.md) -->

---

# Match Node

## Purpose

A **Match** node determines whether a rule applies to the current row.

Each Match evaluates the value of the **Subject property** and attempts to recognise it according to a defined pattern.

If a Match successfully recognises the value, the rule branch beneath it becomes active and the associated **Target nodes** are executed.

If the Match does not recognise the value, the Targets beneath it are skipped.

Match nodes therefore control **which rule branch applies to the current object**.

---

## Pattern Types

Match nodes support several pattern types that control how values are recognised.

---

### Exact

The **Exact** pattern kind requires the subject value to match the pattern exactly, and wildcards are not supported.

Exact pattern kind is the fastest match type. It is useful for names or values that have no variation.

Example:

```
Pattern: BEAM
PatternKind: Exact
```

Only values that exactly match the pattern will be recognised.

---

### Like

The **Like** pattern kind supports simple wildcard (\*) matching.

Wildcards can be used at the **start or end of the pattern, or both**. The can also be used in isolation, used for matching every row irrespective of value.

Like pattern kind is useful for simple profile matching.

Example:

```
Pattern: UB*
PatternKind: Like
```

This will match values such as:

- UB310*40
- UB200*18

Wildcard characters are not supported in the middle of the pattern, e.g. UB*18

---

### Regex

The **Regex** pattern allows full regular expression matching.

This provides the most powerful and flexible form of pattern recognition.

Regex patterns can match complex formats such as:

- profile naming structures
- dimensional formats
- structured identifiers

Example:

```
Pattern: ^CHS\d+\.?\d+\*\d+\.?\d+$
PatternKind: Regex
```

This example recognises circular hollow section profiles such as:

- CHS165.1*3.5
- CHS88.9*3.2

---

## Regex Match Groups

Regex patterns can also produce **match groups**, which capture parts of the recognised value.

These captured values are stored in arrays and made available to **Condition nodes**.

Match group results are filtered into one of two lists:

- **matchString**
- **matchNumber**

Numbers extracted from a match are stored as numeric values so they support comparisons using numeric operators.

Example regex:

```
^(CHS)(\d+\.?\d+)\*(\d+\.?\d+)$
```

From a value such as:

```
CHS139.7*5.4
```

The match groups would contain:

```
matchString[0] = CHS

matchNumber[0] = 139.7
matchNumber[1] = 5.4
```

This allows multiple **Target** nodes to target the same cell (e.g. MATERIAL, LENGTH_NET) but with differing criteria which is dependent on depth and/or thickness of the profile.

A useful regex building tool is available at [regex101.com](https://regex101.com/)

---

## Display Name

The Match *DisplayName* is an optional field so node text displays something more user-friendly than the pattern string.

If DisplayName text is empty, a node will display the Pattern text. In the case of regex patterns, this is not always ideal.

You can enter text into the DisplayName and it will update the text in the node without affecting the match pattern.

---

## Match Order

Each Match node is evaluated in order from top to bottom. Once a Match is found, it returns the OnMatch result to the cell and skips all other Matches for that Subject.

Most nodes (except Subject nodes) can be re-orded by drag and drop. This makes it possible to ensure the order is correct.

This allows fallback Match nodes, so if no match is found in a Subject, a wildcard `*` match can be added last, which will only run if no other matches were found in that Subject.

---

## Target Execution

Each Match node contains a collection of **Target nodes**.

Each Target therein defines one property/cell that will be audited if the Match is successful.

When a Match recognises the Subject value:

- the Subject cell receives the `OnMatch` flag and message (if not None)
- all Targets beneath the Match are executed
- each Target evaluates its corresponding cell in that row

If the Match does not recognise the value:

- the Targets beneath that Match are skipped

If none of the Matches are recognised:

- the Subject cell receives the `OnNoMatch` flag and message (if not None)

This allows different rule branches to apply depending on the recognised value.

---

## Summary

A Match node determines whether a rule branch should apply to the current object.

It evaluates the Subject value using pattern matching and activates the Targets beneath it when recognition succeeds.

Match nodes do not generate audit results themselves, but they control which validation rules are executed.
