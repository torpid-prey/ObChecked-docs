# Configuration Overview

Before auditing rules can be applied, ObChecked must know **where configuration files are stored** and **how column data should be interpreted**. Configuration determines how the application reads object properties, where shared definitions are stored, and how rules can be applied consistently across users and projects.

ObChecked separates configuration into several layers so that rules and settings can be shared across teams while still allowing project-specific overrides when required.

![Main Menu](../screenshots/main-context-menu.png)

*Access all properties via the main menu*

---

## Configuration Layers

ObChecked can read configuration from three different locations:

1. **Application Root**  
2. **Firm Folder**  
3. **Model Folder**

These locations form a hierarchy. More specific locations override broader ones.

---

### Application Root

The application root is the default configuration location bundled with ObChecked.  
If no firm or model configuration is present, ObChecked will fall back to this location.

This layer is typically used for:

- personal defaults
- baseline column definitions
- development or testing setups

---

### Firm Folder

The firm folder allows configuration to be **shared across multiple users** within an organisation.

When defined, ObChecked can read configuration from a shared network location resolved from Tekla’s firm environment. This allows teams to maintain consistent column definitions and audit rule sets.

Typical uses include:

- shared audit rule libraries
- standardised column definitions
- office-wide validation rules

The firm folder must be configured before it can be used. Once configured, definitions can be promoted to this location so they are available to all connected users.

---

### Model Folder

The model folder allows configuration to be **overridden for a specific project**.

This layer is useful when a particular model requires different rules or columns that should not affect other projects or office standards.

Examples include:

- project-specific audit rules
- special naming conventions
- temporary validation checks

When configuration exists in the model folder, it overrides both firm and root configuration.

---

## Configuration Types

Several parts of ObChecked rely on configuration files. These include:

- **Column Definitions** – defines how object properties are read and interpreted  
- **Audit Definitions** – rule sets used to validate objects  

These configuration files can exist in any of the three configuration layers.

---

## Why Configuration Matters

Many auditing features rely on properly defined column data. Column definitions determine:

- which Tekla properties are available in the grid
- the datatype used when evaluating values
- how numeric values are formatted and compared
- which columns can be referenced by audit rules

Because of this, column definitions are typically the **first step when setting up ObChecked**.

---

## Recommended Setup Order

When configuring ObChecked for a new environment, the following order is recommended:

1. Define the **Firm Folder** location  
2. Configure **Column Definitions**  
3. Define or import **Audit Rules**  

Following this order ensures that shared configuration is established before rules and columns are created.

---

## Next Steps

- [Firm Folder Setup](firm-folder.md)  
- [File Locations and Overrides](file-locations.md)  
- [Column Definitions](column-definitions.md)
