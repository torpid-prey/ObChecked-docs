# Target Type: Direct

## Purpose

The **Direct** target type performs specialised checks that cannot easily be expressed using the other target types.

Unlike other targets, Direct checks do not rely on comparison rules or case lists.  
Instead, they execute predefined validation logic built directly into ObChecked.

Direct checks exist primarily to support validation scenarios that involve:

- model configuration
- derived values
- complex relationships between settings

Currently three Direct checks are available.

---

## Available Direct Checks

### CellValueEmpty

Checks whether the value in the target column is empty.

If the cell contains no value, the comparison succeeds and the **Pass** flag is applied.

If the cell contains any value, the **Otherwise** flag is applied.

This check is typically used when a property **should** be empty.

*e.g. `PHASE.OTHERS` is used to display associated phases that differ to the phase of the part. This value should be empty. If it contains phases, it means child objects (cuts/welds) or father components are in a different phase to the part itself, and should be corrected.*

---

### CellValueNotEmpty

Checks whether the value in the target column contains any value.

If the cell contains a value, the comparison succeeds and the **Pass** flag is applied.

If the cell is empty, the **Otherwise** flag is applied.

This check is typically used when a property **should not** be empty.

---

### RotationByProjectNorth

This check validates that part rotation settings are correct relative to the model's **Project North** orientation.

Tekla uses several independent settings that together determine how assembly marks and parts are oriented relative to the drawing view. These include:

- the **Project North** angle
- the advanced option **XS_ORIENTATION_MARK_DIRECTION**
- the **part rotation** values applied to columns or droppers

Because these settings interact with each other, it is possible for models to display assembly marks incorrectly even when individual settings appear valid.

The **RotationByProjectNorth** check evaluates these settings together and determines whether the resulting part rotation is consistent with the current Project North orientation.

If the orientation combination is valid, the **Pass** flag is applied.

If the configuration does not match the expected rotation rules for the current Project North direction, the **Otherwise** flag is applied.

This rule helps ensure that assembly marks appear in the expected position relative to the structure.

---

## Result Flags

Direct checks produce two possible outcomes:

```
Pass
Otherwise
```

If the validation succeeds, the **Pass** flag is applied.

If the validation fails, the **Otherwise** flag is applied.

---

## When to Use Direct

Direct checks are intended for specialised validation logic that cannot easily be expressed using the other target types.

Typical uses include:

- checking whether required values are present
- validating model configuration settings
- enforcing complex rules tied to model orientation

As additional specialised checks are developed, they may be added to the Direct target type.
