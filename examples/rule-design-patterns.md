[Contents](../README.md) | [Concepts](../core-concepts/overview.md) | [Configuration](../configuration/overview.md) | [Main Window](../user-interface/main-window.md) | [Audits](../user-interface/audits-window.md) | [Examples](../examples/overview.md) | [Troubleshooting](../troubleshooting/overview.md)

---

# Rule Design Patterns

The examples in this documentation demonstrate how audit rules can be structured to detect modelling issues.  
While each example focuses on a specific scenario, most rules follow a small number of **design patterns**.

Understanding these patterns makes it much easier to design new audit rules.

Instead of thinking about the exact syntax of a rule, it is usually more helpful to think about **which pattern the rule belongs to**.

---

# 1. Recognition Pattern

## Purpose

Identify what type of object the rule applies to.

Recognition happens in the **Subject** node, often using columns such as:

- `PROFILE`
- `NAME`

## Minimal Tree

    Subject: PROFILE
      Match: UB*
      Match: UC*
      Match: PFC*
      etc...

## Explanation

Each match under the subject represents one variation of the subject column.

> Think: Which cell determines if this object is recognised, and what values can they be?

Once an object has been recognised, targets can then check whether other properties are internally consistent.

---

# 2. Validation Pattern

## Purpose

Check whether one property contains the expected value.

This is the most common audit rule pattern.

## Example

Verify that a recognised profile uses the correct material.

## Minimal Tree

    Subject: PROFILE
      Match: UB*
        Target: MATERIAL [300PLUS]
      Match: UC*
        Target: MATERIAL [300PLUS]
      Match: PFC*
        Target: MATERIAL [300PLUS]
      
## Explanation

Once the Subject is recognised, the rule simply verifies that the Target cell contains the correct value.

> Think: For this `PROFILE`, what `MATERIAL`(s) are acceptable?

It is always the Target cell that receives the audit result flag and message.

---

# 3. Extraction Pattern (Regex)

## Purpose

Extract values from a string so they can be used in conditions using regex capture groups.

This pattern is commonly used with **PROFILE** rules.

For example, a profile such as:

    UB310*40

may contain useful information, in this case, depth (mm) and weight (kg/metre).

A regular expression can extract these values and make them available as numeric variables.

## Example

    Regex: UB(\d+)\*(\d+)

Which produces values such as:

- `matchNumber[0]` → 310
- `matchNumber[1]` → 40

## Minimal Tree

    Subject: PROFILE
      Match: DisplayName: UB310*40, Pattern: UB(\d+)\*(\d+)

## Explanation

Extracted values from the Subject can then be used to allow multiple conditional targets.

> Think: Does this profile value contain information that can impact audit criteria?

---

# 4. Conditional Validation Pattern

## Purpose

Apply validation rules only when certain conditions are met.

Conditions allow rules to adapt to different situations without creating completely separate rule branches.

Conditions compare values of other cells **or** regex return groups against one or more predefined values.

If a conditional check fails, the audit rule is skipped.

## Example

A maximum length limit may depend on the depth of the profile.

## Minimal Tree

    Subject: PROFILE
      Match: DisplayName: UB310*40, Pattern: UB(\d+)\*(\d+)
        Target: LENGTH_NET [<= 15000]
           Condition: matchNumber[0] <= 200
        Target: LENGTH_NET [<= 18000]
           Condition: matchNumber[0] > 200

## Explanation

The condition allows a different `LENGTH_NET` value to be applied, depending on the depth of the profile.

> Think: Does this rule only apply to this profile under certain circumstances?

Multiple Targets can be assigned to the same cell, only if they have different conditions.

---

# 5. Fallback Match Patterns

## Purpose

Some validations need to apply across all rows, not just on recognised values.

*Always set Subject `OnMatch` and `OnNoMatch` to `None` when using global/fallback match patterns.*

This pattern allows more specific matches to run first, followed by a broader fallback / catch-all for everything else.

Since Match patterns exit the Subject as soon as a match is found, a wildcard fallback will **only** run if not matched previously.

## Example

Material rules may be structured like this:

    G450
    A325
    *

## Minimal Tree

    Subject: MATERIAL
      Match: G450
        Target: FINISH [A]
      Match: A325
        Target: FINISH [B]
      Match: *
        Target: FINISH [C]

## Explanation

This check may be used to evaluate part `FINISH`, when it is the `MATERIAL` that helps determine which `FINISH` is acceptable.

> Think: **All rows** should have `FINISH = C`, except for `A325` and `G450`.

The wildcard match `*` acts as a fallback and handles all remaining objects that were not recognised earlier.

---

# 6. Global Match Pattern

## Purpose

Run audit checks on every row in the dataset.

*Always set Subject `OnMatch` and `OnNoMatch` to `None` when using global/fallback match patterns.*

This pattern is used for project-wide validation such as:

- phase consistency
- hold warnings

## Minimal Tree

    Subject: PHASE.OTHERS
      Match: *

## Explanation

The wildcard match causes the rule branch to run for every object.

> Think: What should be consistent across every row?

Targets inside the branch then perform the actual checks.

---

# 7. Direct Property Pattern

## Purpose

Validate simple properties without comparing against another value.

Direct targets are useful when checking whether a value is present or empty.

## Example

Verify that a column contains no additional phases.

## Minimal Tree

    Subject: PHASE.OTHERS
      Match: *
        Target: PHASE.OTHERS [CellValueEmpty]

## Explanation

Direct checks like `CellValueEmpty` or `CellValueNotEmpty` are often used in global rules because they are simple and fast to evaluate.

> Think: Are there any cells that simply must contain or not contain some value?

Other specific Direct checks include [RotationByProjectNorth](../core-concepts/target-direct.md#rotationbyprojectnorth)

---

# 8. Severity Override Pattern

## Purpose

Allow later rules to modify or override earlier results.

This pattern is useful when multiple rule sources can influence the same property.

For example, a profile might appear in multiple material availability tables.

## Minimal Tree

    Subject: PROFILE
      Match: DisplayName: CHS168.3*6.4, Pattern: ^(CHS)(\d+\.?\d+)\*(\d+\.?\d+)$
        Target: LENGTH_NET [ value <= 6500 ]
        Target: LENGTH_NET [ value <= 12000, ApplyMode = OnAnyMatch ]
          ConditionL: MATERIAL [ 350 ]
          ConditionL: MatchNumber[0] == 168.3
          ConditionL: MatchNumber[1] == [ 4.8, 6.4, 7.1, 11 ]
        

## Explanation

Using different apply modes allows the final result to reflect the most appropriate rule.

The `CHS168.3*6.4` with `LENGTH_NET > 6500` and `MATERIAL = 350` is matched by the first target and given `error` flag, as per the first table

The same part is then also matched by the second, more specific target (derived from a second table) and the previous `error` flag is overturned and set to `okay`.

> First Think: Which table defines the more restrictive target?

*e.g. `6500` is the more restrictive length compared to `12000`*

> Then Think: Which values can safely override a result from the first table, and under which conditions?

*e.g. only specific depths, thicknesses, and materials are available in the longer sizes*

This pattern is particularly useful when working with multiple specification tables with overlap.

---

# Why These Patterns Matter

Without understanding these patterns, creating audit rules can seem complicated.

Once the patterns are recognised, most rules become combinations of a few simple ideas:

1. Recognise the object
2. Extract any required values
3. Validate the relevant properties
4. Apply conditions if necessary
5. Use fallback matches when needed

By combining these patterns, complex rule systems can be built from relatively simple components.
