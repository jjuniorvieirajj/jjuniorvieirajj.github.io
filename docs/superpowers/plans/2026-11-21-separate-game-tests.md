# Separate Game Tests Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a separate standard-library unittest file covering every Rock Paper Scissors winner matchup.

**Architecture:** Keep `game.py` unchanged and add `test_game.py` beside it. Test `determine_winner` directly with table-driven tie, user-win, and computer-win cases.

**Tech Stack:** Python 3, unittest

## Global Constraints

- Test only the core winner rules.
- Do not add dependencies or project configuration.
- Keep input prompts, random choice generation, replay behavior, and console output outside the test scope.

---

### Task 1: Create the Rock Paper Scissors winner tests

**Files:**
- Create: `test_game.py`
- Verify: `game.py`
- Spec: `docs/superpowers/specs/2026-11-21-separate-game-tests-design.md`

**Interfaces:**
- Consumes: `game.determine_winner(user_choice, computer_choice)`
- Produces: unittest cases covering ties, user wins, and computer wins

- [ ] **Step 1: Create `test_game.py` with a table-driven unittest**

```python
import unittest

from game import determine_winner


class DetermineWinnerTest(unittest.TestCase):
    def test_equal_choices_are_ties(self):
        cases = ("rock", "paper", "scissors")

        for choice in cases:
            with self.subTest(choice=choice):
                self.assertEqual(determine_winner(choice, choice), "It's a tie!")

    def test_user_winning_matchups(self):
        cases = (
            ("rock", "scissors"),
            ("paper", "rock"),
            ("scissors", "paper"),
        )

        for user_choice, computer_choice in cases:
            with self.subTest(
                user_choice=user_choice,
                computer_choice=computer_choice,
            ):
                self.assertEqual(
                    determine_winner(user_choice, computer_choice),
                    "You win!",
                )

    def test_computer_winning_matchups(self):
        cases = (
            ("scissors", "rock"),
            ("rock", "paper"),
            ("paper", "scissors"),
        )

        for user_choice, computer_choice in cases:
            with self.subTest(
                user_choice=user_choice,
                computer_choice=computer_choice,
            ):
                self.assertEqual(
                    determine_winner(user_choice, computer_choice),
                    "Computer wins!",
                )


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests**

Run:

```sh
python3 -m unittest test_game.py
```

Expected: `Ran 3 tests` with `OK`.

- [ ] **Step 3: Inspect the final diff**

Run:

```sh
git --no-pager diff --stat
git --no-pager diff -- test_game.py
```

Expected: only `test_game.py` contains the new test implementation.

- [ ] **Step 4: Commit the test file**

Run:

```sh
git add test_game.py
git diff --cached --check
git commit -m "test: add rock paper scissors winner tests

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```
