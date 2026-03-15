# Target Type — Direct

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

### Example: PHASE.OTHERS

In some cases a column may intentionally be empty under normal conditions.

For example, the `PHASE.OTHERS` property reports phase numbers that differ from the main part.  
This may include:

- phases of cuts or welds applied to the part
- phases of parent components
- phases of assembly main parts

Under normal circumstances, these values should match the part phase and the `PHASE.OTHERS` field should therefore remain empty.

If a value appears in `PHASE.OTHERS`, it indicates that conflicting phases exist within the assembly and may require correction.

An audit rule can therefore be configured to ensure this column remains empty:

```
TargetColumn: PHASE.OTHERS
Type: Direct
DirectID: CellValueEmpty
Pass: Okay
Otherwise: Error
```

This will flag any part where conflicting phase information is detected.

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
