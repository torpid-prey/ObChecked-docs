---
layout: default
title: Name Rule Examples
---

The **NAME** column is one of the most commonly used subject columns when auditing model data.

Unlike the **PROFILE** subject, which usually extracts technical properties from the section name, the **NAME** subject is primarily used to classify parts based on their intended modelling role.

These rules typically define:

- which object names are recognised
- how certain names affect assembly behaviour
- when certain parts must not be used as main parts
- when additional checks should apply to specific object types

Because the name of a part often reflects its modelling purpose, these rules allow audit behaviour to adapt based on the type of object being modelled.

For example:

- assemblies such as **Beam**, **Column**, or **Loose Cleat** may define expected assembly prefixes or class values
- welded secondary parts such as **Plate** or **Channel** should not be the main part of an assembly
- vertical members such as **Column**, **Stub Column**, or **Dropper** may require additional orientation checks

The examples below demonstrate several common rule patterns using the **NAME** subject.

These patterns can be used to design additional rules for other modelling conventions.

---

## Example Rules

- [Recognised assembly names set prefix and class](recognised-assembly-name-sets-prefix-and-class.md)
- [Welded part names should not be main parts](welded-part-name-should-not-be-main-part.md)
- [Name determines valid profile](name-determines-valid-profile.md)
- [Vertical part names require correct rotation](vertical-part-name-requires-correct-rotation.md)

---

## System File Reference

The rules used in these examples are based on the system audit file:

[Parts_NAME.aud](../system-files/Parts_NAME.aud)

This file contains the complete set of name-based audit rules installed with ObChecked.

---

## Related Documentation

- Core Concepts → [Subject Node](../../core-concepts/subject.md)
- Core Concepts → [Match Node](../../core-concepts/match.md)
- Core Concepts → [Target Node](../../core-concepts/target.md)
- Core Concepts → [Condition Node](../../core-concepts/condition.md)
- User Interface → [Audit Definition Editor](../../user-interface/audit-definition-editor.md)
