---
---

<div class="sticky-nav">
{% include nav.html %}
</div>

# Examples

{% include nav_examples.html %}

---

# Rule — Welded Part Name Should Not Be Main Part

## Problem
Some object names represent secondary components that should not be used as the main part of an assembly.

Examples include plates, channels, and other welded attachments.

If one of these objects becomes the main part, it usually indicates incorrect modelling.

## Strategy
Use the **NAME** column as the subject and detect specific part names.

If the name matches one of these secondary components, the audit checks the **MAIN_PART** property and ensures it is set to **False**.

## Rule Structure

Subject:  
`NAME`

Match:  
Exact match that returns a recognised part-only name, `PLATE`, `ANGLE`, etc.

Target:  
`MAIN_PART`

Conditions:
(None)

## Minimal Tree

    Subject: NAME
      Match: PLATE
        Target: MAIN_PART [False]


## Example Results

| Name | Main Part | Result |
|--|--|--|
| PLATE | False | Okay |
| PLATE | True | Error |

## Explanation

Secondary parts such as plates are normally welded or attached to a primary structural member.

If one of these parts becomes the main part of an assembly, it usually means the assembly was created incorrectly.

This rule prevents those modelling mistakes.
