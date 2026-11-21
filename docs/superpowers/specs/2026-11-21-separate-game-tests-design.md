# Separate Game Tests Design

## Scope

Create a separate `test_game.py` file for testing the Rock Paper Scissors winner rules.

The tests will cover:

- Equal choices return a tie.
- Rock beats scissors.
- Paper beats rock.
- Scissors beat paper.
- The losing counterpart of each winning matchup returns a computer win.

The test file is limited to `determine_winner`; input prompts, random choice generation, replay behavior, and console output remain outside this scope.

## Approach

Use Python's built-in `unittest` framework so no dependency or project configuration changes are required.

Place `test_game.py` beside `game.py` at the repository root. Import `determine_winner` from `game` and use `subTest` for the matchup table:

- Tie: one case for each of the three choices.
- User wins: rock/scissors, paper/rock, and scissors/paper.
- Computer wins: scissors/rock, rock/paper, and paper/scissors.

This table-driven structure verifies every matchup without duplicating assertion logic.

## Verification

Run:

```sh
python3 -m unittest test_game.py
```
