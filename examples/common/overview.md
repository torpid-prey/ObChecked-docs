---
---

{% include nav.html %}

# Common Rule Examples

The **Common** examples demonstrate audit rules that apply broadly across the model rather than being tied to a single profile family or object name.

These rules are usually built from subject columns that either:

- apply to all rows using a wildcard match
- classify rows into broad material or project-wide categories
- enforce general modelling standards that should remain consistent across many object types

Unlike the **PROFILE** and **NAME** examples, common rules are not primarily concerned with identifying what an object is.  
Instead, they are used to check whether model-wide properties are consistent and valid.

These rules typically define:

- whether additional associated phases are present
- whether user phase matches the phase number
- whether warning or hold fields are empty
- whether finishes are valid for steel, grating, or special materials
- whether hidden columns should be used to provide helpful messages

Because these checks are applied broadly, they are useful for detecting project-wide issues that may otherwise be missed.

> It is important for common Subject nodes (that match all values) to have `OnMatch` and `OnNoMatch` both set to `None` so the subject match result doesn't impede individual Target audit flags.

For example:

- `PHASE.OTHERS` can be used to run checks on every row
- `MATERIAL` can classify rows into steelwork, grating, dummy, or grout categories
- hidden columns such as `USER_FIELD_1` can be used to show extra detail in audit messages without displaying the column in the main grid

The examples below demonstrate several common rule patterns that can be reused for global checks.

These patterns can be used to design additional rules that do not depend on a specific profile or name.

---

## Example Rules

- [Run checks on all rows using a wildcard subject](run-checks-on-all-rows-using-a-wildcard-subject.md)
- [PhaseOthers should be empty](phase-others-should-be-empty.md)
- [UserPhase must match PhaseNumber](user-phase-must-match-phase-number.md)
- [On Hold warning field should normally be empty](fabricator-warning-field.md)
- [Material determines valid Finish](material-determines-valid-finish.md)
- [AssemblyPrefix must start with PhaseNumber](assy-prefix-must-start-with-phase-number.md)

---

## System File References

The rules used in these examples are based on the system audit files:

- [Parts_PHASE_OTHERS.aud](../system-files/Parts_PHASE_OTHERS.aud)
- [Parts_MATERIAL.aud](../system-files/Parts_MATERIAL.aud)

These files contain the complete set of common audit rules installed with ObChecked.

---

## Related Documentation

- Core Concepts → [Subject Node](../../core-concepts/subject.md)
- Core Concepts → [Match Node](../../core-concepts/match.md)
- Core Concepts → [Target Node](../../core-concepts/target.md)
- Core Concepts → [Condition Node](../../core-concepts/condition.md)
- User Interface → [Audit Definition Editor](../../user-interface/audit-definition-editor.md)
