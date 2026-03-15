---
layout: default
title: Target Node
---

## Purpose

A **Target** node defines the property that will be audited when a Match succeeds.

Each Target points to a specific column in the grid and evaluates the value of that cell for the current row.

If the Match above the Target succeeds, the Target performs its audit logic and may assign a flag and message to the cell.

Targets are the nodes where audit rules actually evaluate values and produce results.

---

## Target Execution Flow

When auditing a row, the Target node follows this sequence:

1. The parent **Match** recognises the Subject value.
2. The Target identifies the cell specified by **TargetColumn**.
3. If the Target has **Conditions**, they are evaluated.
4. If the conditions pass, the Target performs its audit logic according to **Type**.
5. The audit result generates a **flag and message**.
6. **ApplyMode** determines whether this result overwrites any existing flag on the cell.

Because multiple audit rules may evaluate the same cell, the final flag depends on the configured ApplyMode.

---

## Target Properties

Targets expose several configuration properties which determine how the audit behaves.

These properties appear in the property grid when editing an audit definition.

### Cell Details

#### TargetColumn

The column whose value will be evaluated by the audit rule.

Each Target audits exactly one column.

#### Type

Determines how the cell value will be evaluated.

The following Target types are supported:

- **[StringCases](target-stringcases.md)** – categorises string values into predefined cases
- **[NumericBands](target-numericbands.md)** – evaluates numeric values against defined bands
- **[StringCompare](target-stringcompare.md)** – compares string values against another column
- **[NumericCompare](target-numericcompare.md)** – compares numeric values against another column
- **[Direct](target-direct.md)** – performs specialised built-in checks

---

## Results

### Otherwise

Defines the flag and message that is applied to the cell if the audit fails. This applies to **all** types.

The default flag for a failed audit is **Error**.

### Pass

Defines the flag and message applied to the cell when the audit is successful.

This property only applies to certain Audit Types:

- StringCompare
- NumericCompare
- Direct

These Target Types determine their own result flags internally and **do not** use the Pass value.

- StringCases
- NumericBands

This is because StringCases and NumericBands allow multiple options to faciliate a range of outcomes, not limited to pass or fail.

Using these options allows some values to receive an `Okay` flag, while others may receive an `Info` or `Warn` flag.

### ApplyMode

Determines how the Target's result interacts with existing flags already assigned to the same cell.

Available modes:

**bySeverity (default)**  
The new flag only replaces the existing flag if it is more severe.

**onFirstMatch**  
The flag is only applied if the cell has not been flagged previously.

**onAnyMatch**  
The new flag always replaces the existing flag regardless of severity.

Because cells may be audited multiple times by different rules, ApplyMode determines how the final result is resolved.

---

## Conditions

Targets may contain a collection of **Condition nodes**.

Conditions determine whether the Target should execute.

If the conditions fail, the Target is skipped and no audit is performed.

The **ConditionsMode** property controls how the conditions are evaluated:

**All**  
All conditions must pass for the Target to run.

**Any**  
At least one condition must pass for the Target to run.

Conditions allow audit rules to depend on the values of other cells within the row.

More detailed information about Conditions is available in the Condition node documentation.

---

## Targeting the Same Cell

Within a single Match branch, the same column generally cannot be targeted more than once.

If multiple Targets attempt to audit the same cell, they will flag a warning and saving audit changes will be blocked.

The only way multiple nodes can target the same cell is when the Targets contain **different Conditions**, allowing separate rules to apply depending on context.

---

## Summary

The Target node performs the actual audit of a cell.

It determines:

- which cell is evaluated
  - and under which conditions
- how the value is tested
  - which values are acceptable
- which flag is applied
  - and if the flag should be applied

Targets therefore represent the core of the auditing process, where recognised objects are evaluated against defined validation rules.
