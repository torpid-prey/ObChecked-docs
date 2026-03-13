# Rule: <Rule Name>

## Problem
Describe the modelling issue this rule detects.

## Strategy
Explain the approach used to detect it.

## Rule Structure

Subject  
<column>

Match  
<Exact / Like / Regex>

Pattern (if regex)

<regex here>

Target  
<column>

Condition  
(optional)

## Rule Diagram

Group
└─ Subject: <column>
   └─ Match: <type>
      └─ Target: <cell>
         └─ Condition: <condition>

## Example Results

| Input | Value | Result |
|--|--|--|
| example | example | OK |

## Explanation

Explain why the rule works.

## Notes

Optional notes or variations.
