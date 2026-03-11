# Firm Folder Setup

ObChecked supports using a **shared firm folder** so configuration files can be maintained centrally and accessed by multiple users.

If Tekla's `XS_FIRM` environment variable is defined and accessible, the **Configure Firm Folder** dialog becomes available in ObChecked.

This allows users to define a shared location inside the firm's Tekla environment where ObChecked configuration files can be stored.

---

## Purpose of the Firm Folder

The firm folder allows teams to maintain **consistent configuration across multiple workstations**.

Typical items stored in the firm folder include:

- Column Definitions
- Audit Rule Definitions
- Shared configuration files

Once configured, updates made to these files can be shared across all users connected to the same firm environment.

---

## Firm Folder Structure

Although the firm folder root is defined by Tekla, it is recommended to create a **dedicated subdirectory for ObChecked**.

Example:
