---
---

<div class="sticky-nav">
{% include nav.html %}
</div>

# Examples

{% include nav_examples.html %}

---

# Name Rule Examples

{% include nav_examples_names.html %}

---

# Rule — Name Determines Valid Profile

## Problem
Certain object names imply that only specific profile types should be used.

For example, a part named **CHEQUER PLATE** should use a floor plate profile.

If a different profile is used, the name and section are inconsistent.

## Strategy
Use the **NAME** subject to detect the part type, then validate the **PROFILE** column using a wildcard match.

## Rule Structure

Subject:  
`NAME`

Match:  
Exact match that returns a recognised name, e.g. `CHEQUER PLATE`

Target:  
`PROFILE`

Conditions:  
(None)

## Minimal Tree

    Subject: NAME
      Match: CHEQUER PLATE
        Target: PROFILE [like FLRPL*]

## Example Results

| Name | Profile | Result |
|--|--|--|
| CHEQUER PLATE | FLRPL6 | Okay |
| CHEQUER PLATE | PLATE10 | Error |
| PLATE | FLRPL6 | N/A |

## Explanation

This rule ensures that the name of the object corresponds to the correct profile family.

Using the wrong profile type indicates incorrect modelling or naming.

Using `ApplyMode = bySeverity` ensures even if `PROFILE` is given an Okay flag by another audit rule, an incorrect profile for a specific `NAME` can still be flagged as Error.

## Notes

Using the `StringCases` `MatchKind` `Like` we can support wildcards in string case arrays.
