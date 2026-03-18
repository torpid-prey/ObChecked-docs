---
---

<div class="sticky-nav">
{% include nav.html %}
</div>

# Examples

{% include nav_examples.html %}

---

# Common Rule Examples

{% include nav_examples_common.html %}

# Warning Field Should Normally Be Empty

---

## Problem

In this system, the `fabricator` field is used to mark special warnings such as parts on hold.

> Any part property can be used here, but examples here use `fabricator`. 

Under normal conditions this field should remain empty. Model objects with queries support comments to be added for future reference.

When combined with model view representation settings, parts with these notes can be highlighted in pink to be immediately identifiable.

Combining multiple UDAs can allow numerous notes to be added to each part, and therefore, ObChecked can display these same notes.

## Strategy

Check whether the `fabricator` column contains a value.

If a value exists, the rule flags the row and displays the message stored in a hidden column.

## Rule Structure

Subject:
`PHASE.OTHERS`

Match:
Wildcard `*`

Target:
`fabricator`

Conditions:
(None)

## Minimal Tree

    Subject: PHASE.OTHERS
      Match: *
        Target: fabricator [Direct: CellValueEmpty], 
        - Otherwise message: Part noted {fabricator}, {USER_FIELD_1}

## Example Results

| fabricator | User Field 1 | Result | Message |
|--|--|--|--|
| HOLD | Check baseplate on site | Error | Part noted HOLD, Check baseplate on site |
| (empty) | (empty) | Okay | (empty) |

## Explanation

This rule checks whether the warning field contains a value.

If a warning is present, the audit message displays the associated message stored in `USER_FIELD_1`.

## Notes

Hidden columns can be referenced in audit messages even when they are not visible in the main table.

Although this check has nothing to do with `PHASE.OTHERS`, it is safe to use any column for any target that needs to run on all rows, as long as `OnMatch` and `OnNoMatch` are both set to `None` in the Match node.
