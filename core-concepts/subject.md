---
---

{% include nav.html %}
{% include nav_concepts.html %}

# Subject Node

## Purpose

A **Subject** defines the property that an audit rule begins with.

The Subject column specifies the name of the property whose value will be examined by the match rules beneath it.

Each **Match** node evaluates the value of this property and attempts to recognise it according to the defined patterns.

---

## How Subject Matching Works

When a row is processed, each Match node beneath the Subject is evaluated.

If **any Match successfully recognises the value**, the Subject cell receives the **OnMatch** flag and message.

If the row completes evaluation without any successful matches, the Subject cell receives the **OnNoMatch** flag and message.

This allows the Subject node to determine whether a value is recognised before further rule logic is applied.

---

## Recognising Valid Values

In many cases, audit rules depend heavily on the value of another property.

The Subject is often used only to determine whether a value is recognised.

Typical examples include:

- **PROFILE**
- **NAME**

For these cases, the Match nodes define the set of acceptable values.

Example configuration:

```
Subject: PROFILE
Matches: list of recognised profile patterns
OnMatch: Okay
OnNoMatch: Unknown
```

If the value is recognised, the cell receives **Okay**.

If the value is not recognised, the cell receives **Unknown**, indicating that no audit rules were applied because the value is not recognised.

---

## Running Rules on Every Row

Some audit rules should apply to every row regardless of the value in the subject property.

In this case, the Subject can be configured with a generic match rule.

Example:

```
Subject: PROFILE
Match pattern: *
PatternKind: Like
```

This match will recognise every value.

When using this pattern, the Subject node is not being used to determine whether values are recognised. Instead, it simply allows audit rules to run for every object.

In these situations it is typically best to set:

```
OnMatch: None
OnNoMatch: None
```

This prevents the Subject node from generating unnecessary flags.

---

## ApplyMode

The **ApplyMode** setting determines how the Subject cell updates its flag if the same cell has already been audited by another rule.

Each cell may be evaluated multiple times during auditing, but it can only store **one flag and one message**.

ApplyMode controls how new results interact with existing flags.

---

### bySeverity (default)

The new flag will only overwrite an existing flag if it is **more severe**.

Example:

```
Existing flag: Error
Current flag: Okay
Result: Error remains
```

This is the default and recommended behaviour in most situations.

---

### onFirstMatch

The cell flag will only be set if the cell has **not already been flagged**.

If a flag is already set, this flag will not overwrite it.

This only relates to flags already applied to the cell. 

IMPORTANT — *It cannot prevent this flag from being overwritten if a latter audit is set to bySeverity or onAnyMatch.*

---

### onAnyMatch

The current flag will **always overwrite** the existing flag, regardless of severity.

Example:

```
Existing flag: Error
Current flag: Okay
Result: Okay
```

This mode is useful when later rules should override earlier ones.

IMPORTANT — *If a flag severity is set to None, it does not set any flag, and will never overwrite an existing flag, even onAnyMatch*

---

## Multiple Audits per Cell

A single cell may be evaluated many times by different audit rules.

However, the grid can only store **one flag and one message per cell**.

Because of this, **bySeverity** is usually the preferred mode. If multiple rules produce different results, the most severe flag is generally the one that requires attention.

---

## Source Information

The filename and source path of an audit rule are determined by the **Group** and **Subject** node.

These values are displayed for information only and do not affect rule behaviour.
