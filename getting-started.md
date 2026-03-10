# Getting Started with ObChecked

## Purpose

This guide explains the simplest workflow for running an audit in **ObChecked**.

The goal is to understand the basic structure of an audit and how rules are evaluated.

ObChecked audits are built using a hierarchy of rule definitions that progressively narrow down what is being checked.

```
Group → Subject → Match → Target → Condition
```

Each level refines the scope of the rule until a specific property value is evaluated.

---

# Step 1 — Select Objects from Tekla

ObChecked evaluates the objects currently selected in the Tekla model.

Typical selections include:

- Parts  
- Bolts  
- Components  

If **components** are selected, ObChecked automatically expands them and includes their child parts and bolts.

This ensures that no relevant objects are missed during validation.

---

# Step 2 — Load an Audit Definition

Audit behaviour is controlled by **audit definitions**.

These definitions contain the rule hierarchy that determines what properties are checked and how values are validated.

An audit definition may include rules such as:

- Allowed materials for specific profiles  
- Maximum part lengths based on stock availability  
- Required prefixes for assemblies  
- Required User Defined Attribute (UDA) values  

Different audit files may exist for different company standards or project requirements.

---

# Step 3 — Run the Audit

Once objects are selected and an audit definition is loaded, ObChecked evaluates each object against the defined rules.

For each object:

1. The relevant **Subjects** are identified  
2. Matching rules are applied  
3. Target properties are evaluated  
4. Conditions determine whether values are valid  

Any rule violations are flagged in the grid.

---

# Step 4 — Review the Results

Audit results appear in the **ObChecked grid**.

Each row represents an object, and each column represents a property being evaluated.

Cells are flagged using severity levels:

- **Okay** – value satisfies the rule  
- **Info** – informational message  
- **Warn** – potential issue detected  
- **Error** – rule violation  
- **Unknown** – rule could not be evaluated  

This allows users to quickly identify which objects require attention.

---

# Step 5 — Inspect Messages

Selecting a flagged cell displays additional information in the **message panel**.

Messages explain:

- Which rule was evaluated  
- What value was expected  
- What value was detected  

Messages may also include **tokens** that reference:

- Column names: use token {COLUMN_NAME}
  - right click in property view for column name lists
- Expected values: use token {@OKAY}
  - '@' distinguishes it from column names.
  - It should work for any flag specified by the audit: @OKAY, @INFO, @WARN, @ERROR.

This helps users understand exactly why a value failed validation.

---

# Example Workflow

A typical ObChecked workflow might look like this:

1. Select a group of beams in the Tekla model  
2. Click Fetch to import object data and display results
3. Review flagged results (use filters to focus on severe warnings)
4. Use buttons on the top-right to select objects in the Tekla model
    - option to zoom to objects
    - option to include child objects (cuts/welds etc)
    - option to include father component (to select comppnent object as well as parts)
    - select objects given selected option toggles
5. Objects can be updated in Tekla as required
6. Use ObChecked to reselect those objects in the model again
7. Click Fetch to re-import objects and update grid with updated values

---

# What to Learn Next

To create more advanced audits, the following concepts are important:

- Audit hierarchy (Group → Subject → Match → Target → Condition)  
- Grid column configuration  
- Flag severity levels  
- Message tokens  
- Audit examples  

These topics are explained in the next sections of the documentation.
