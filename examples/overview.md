---
---

<div class="sticky-nav">
{% include nav.html %}
</div>

# Examples

{% include nav_examples.html %}

---

The examples section demonstrates how the audit system can be used to detect modelling issues and enforce modelling conventions.

Each example explains the **problem**, the **strategy used to detect it**, and the **rule structure** required to implement it.

The examples are organised by the **subject column** used in the audit rules and are briefly outlined.

- [Rule Design Patterns](#rule-design-patterns)
- [Profile Rule Examples](#profile-rules)
- [Name Rule Examples](#name-rules)
- [Common Rule Examples](#common-rules)

---

## Example Structure

Each example follows a consistent structure to make rules easy to understand and compare:

- **Scenario** – what is being checked  
- **Rule Definition** – how the rule is configured  
- **Expected Behaviour** – what should pass or fail  
- **Notes** – any important details or variations  

This structure allows examples to be reused and adapted across different rule types.

---

# Rule Design Patterns

These offer ways to think about designing your own custom rules rather than relying on examples alone.

 - Recognition Pattern
 - Validation Pattern
 - Extraction Pattern (Regex)
 - Conditional Validation Pattern
 - Fallback Match Patterns
 - Global Match Pattern
 - Direct Property Pattern
 - Severity Override Pattern

The below examples groups are great for understanding the default set of audit files and the logic behind each node.

But to understand the rule pattern behind each example will help you create rules that don't fit a current example.

See:
- [Rule Design Patterns](rule-design-patterns.md)

[Top](#examples)

---

# Profile Rules

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

[Top](#examples)

---

# Name Rules

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

[Top](#examples)

---

# Common Rules

Common rules apply to **all objects**, regardless of their profile or name.

These rules use a wildcard subject column and are useful for detecting global modelling issues such as:

- inconsistent phases
- incorrect finishes
- objects marked as on hold
- other project-wide conditions

See:

- [Common Rule Examples](common/overview.md)

[Top](#examples)

---

# System Audit Files

The following audit files plus many others are installed with ObChecked and form the basis for the example rules.

| File | Purpose |
|--|--|
| [`Parts_PROFILE.aud`](system-files/Parts_PROFILE.aud) | Profile-specific audit rules |
| [`Parts_NAME.aud`](system-files/Parts_NAME.aud) | Object name classification rules |
| [`Parts_PHASE_OTHERS.aud`](system-files/Parts_PHASE_OTHERS.aud) | Global checks applied to all objects |

They are included so users can review the full audit definitions used by the example rules.

[Top](#examples)

---

# How to Use These Examples

The examples are intended as **design patterns** rather than strict templates.

When creating new audit rules:

1. Identify the **column that best represents the problem**
2. Choose the appropriate **match method** (Exact, Like, Regex)
3. Define the **target column or property**
4. Add **conditions if the rule depends on other values**

By following the same patterns used in these examples, users can create custom audit rules tailored to their modelling standards.
