# Length by Profile Depth

## Problem

The maximum permitted member length depends on the depth of the profile.

For example, larger UB sections may only be available in shorter stock lengths than smaller sections.

## Strategy

Use a regex Match on `PROFILE` to extract the profile depth into a numeric match group.

Then audit `LENGTH_NET` with one or more targets whose Conditions use `matchNumber[0]` to decide which limit applies.

## Rule Structure

Subject
: `PROFILE`

Match
: Regex that extracts profile depth

Target
: `LENGTH_NET`

Conditions
: based on `matchNumber[0]`

## Minimal Tree

    Subject: PROFILE
      Match: Regex
        Target: LENGTH_NET
          Condition: matchNumber[0] <= <depth range>
        Target: LENGTH_NET
          Condition: matchNumber[0] > <depth range>

## Why This Pattern Is Useful

This pattern shows how a profile string can drive a numeric rule without needing a separate dedicated depth column.

It is especially useful when:

- stock length depends on profile size
- a profile code contains the dimensions needed for the rule
- the rule depends on a numeric value extracted by regex

## Example Results

| Profile | Extracted Depth | Length | Result |
|--|--:|--:|--|
| UB310x40 | 310 | 12000 | Okay |
| UB310x40 | 310 | 13500 | Error |
| UB460x82 | 460 | 9000 | Okay |

## Notes

This is one of the most common “regex + numeric condition” patterns in ObChecked.

If the same depth logic also controls material or prefix rules, the same match can contain additional targets for those cells.
