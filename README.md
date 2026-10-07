# Calculator Test

This repository is a controlled target repository for testing software-engineering agents.

## Available Operations

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`
- `percentage(value, percent)`
- `power(base, exponent)`

## Known Issues

1. `divide()` does not safely handle division by zero.
2. `percentage()` calculates percentages incorrectly.
3. `power()` returns the wrong value when exponent is zero.

## Suggested PatchPilot Test Requests

### Test 1 — Easy

Fix divide() so division by zero raises:

ValueError("Cannot divide by zero")

while preserving all existing calculator behavior.

Add focused tests for the new behavior.

### Test 2 — Medium

Fix percentage() so percentage(200, 10) returns 20 while preserving all other calculator operations.

Add tests covering zero percent, 100 percent, decimal percentages and negative values.

### Test 3 — Medium

Fix power() so exponent 0 follows normal mathematical behavior and returns 1.

Preserve normal positive-exponent behavior.

### Test 4 — Multi-Bug Challenge

Fix all three documented calculator bugs while preserving all existing functionality.

Add focused tests for each corrected behavior.
