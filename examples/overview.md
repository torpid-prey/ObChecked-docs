# Examples Overview

The examples section demonstrates how the audit system can be used to detect modelling issues and enforce modelling conventions.

Each example explains the **problem**, the **strategy used to detect it**, and the **rule structure** required to implement it.

The examples are organised by the **subject column** used in the audit rules.

---

# Example Groups

## Profile Rules

Profile rules analyse the **PROFILE** column.

These rules typically validate:

- available material grades
- maximum lengths
- profile-specific requirements
- profile formatting

Profile rules are often the most complex because information must be extracted from profile strings using **regular expressions**.

Examples are based on the system audit file:

`Parts_PROFILE.aud`

See:

- [Profile Rule Examples](profile/overview.md)

---

## Name Rules

Name rules analyse the **NAME** column.

These rules classify objects based on their modelling purpose and ensure that the correct modelling conventions are followed.

Examples include:

- recognised assembly names
- welded parts that should not be main parts
- names that require specific profiles
- vertical members that require correct rotation

Examples are based on the system audit file:

`Parts_NAME.aud`

See:

- [Name Rule Examples](name/overview.md)

---

## Common Rules *(Coming Soon)*

Common rules apply to **all objects**, regardless of their profile or name.

These rules use a wildcard subject column and are useful for detecting global modelling issues such as:

- inconsistent phases
- incorrect finishes
- objects marked as on hold
- other project-wide conditions

See:

- [Common Rule Examples](common/overview.md)

---

# System Audit Files

The following audit files are installed with ObChecked and form the basis for the example rules.

| File | Purpose |
|--|--|
| [`Parts_PROFILE.aud`](system-files/Parts_PROFILE.aud) | Profile-specific audit rules |
| [`Parts_NAME.aud`](system-files/Parts_NAME.aud) | Object name classification rules |
| [`Parts_PHASE_OTHERS.aud`](system-files/Parts_PHASE_OTHERS.aud) | Global checks applied to all objects |

These and other example files can be found here:

`examples/system-files/`

They are included so users can review the full audit definitions used by the example rules.

---

# How to Use These Examples

The examples are intended as **design patterns** rather than strict templates.

When creating new audit rules:

1. Identify the **column that best represents the problem**
2. Choose the appropriate **match method** (Exact, Like, Regex)
3. Define the **target column or property**
4. Add **conditions if the rule depends on other values**

By following the same patterns used in these examples, users can create custom audit rules tailored to their modelling standards.
