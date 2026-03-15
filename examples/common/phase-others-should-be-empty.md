[Contents](../../README.md) | [Concepts](../../core-concepts/overview.md) | [Configuration](../../configuration/overview.md) | [Main Window](../../user-interface/main-window.md) | [Audits](../../user-interface/audits-window.md) | [Examples](../../examples/overview.md) | [Troubleshooting](../../troubleshooting/overview.md)

---

# Rule — Phase Others Should Be Empty

## Problem

The `PHASE.OTHERS` property indicates that associated objects have conflicting phase values.

This can occur when child objects, father components, or assembly main parts have conflicting phases.

## Strategy

Check whether the `PHASE.OTHERS` cell contains a value.

If the cell is not empty, flag the row and guide the user to correct the phase assignments.

## Rule Structure

Subject:
`PHASE.OTHERS`

Match:
Wildcard `*`

Target:
`PHASE.OTHERS`

Conditions:
(None)

## Minimal Tree

    Subject: PHASE.OTHERS
      Match: *
        Target: PHASE.OTHERS [Direct: CellValueEmpty]

## Example Results

| PHASE.OTHERS | Result |
|--|--|
| (empty) | Okay | 
| PHASE2^ | Error | 

## Explanation

If `PHASE.OTHERS` contains a value, it means associated objects have different phases.

This rule ensures that the model remains consistent by detecting those conflicts.

## Notes

The audit message can provide guidance on how to identify the conflicting objects.
