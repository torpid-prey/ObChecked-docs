# Rule: <Rule Name>

## Problem
Describe the modelling issue this rule detects.

## Strategy
Explain the approach used to detect it.

## Rule Structure

Subject:
`COLUMN NAME`

Match:
Describe the match and provide examples, e.g. `PLATE`

Target:
`CELL NAME` [example value]

Conditions:
(optional, but describe the condition if present) 

## Minimal Tree

    Subject: COLUMN NAME
      Match: PATTERN
        Target: CELL [Value]
           Condition: LeftValue = RightValue
           
## Example Results

| Subject Value | Cell Value | Result |
|--|--|--|
| example | example | Okay |
| example | example | Warn |
| example | example | Error |


## Explanation

Explain why the rule works.

## Notes

Optional notes or variations.
