# Day 25: Git Version Control – Theory and Practical Notes

## 1. Git's Internal Model and Architecture
* **Staging Area (Index):** The preparation zone where changes are selected and held before being recorded in a commit.
* **Commit:** A precise snapshot and permanent record of your project's state at that exact moment. Each commit references the preceding one, chaining the history and recording who changed what and when.
* **Branch:** A lightweight, movable pointer referencing a specific commit. It creates a parallel line of development without altering the main codebase.
* **HEAD:** The primary pointer indicating the current state of your working directory, specifically the active branch or commit.

## 2. Practical Command Notes and Acquired Commands
* **Branching and Merging:**
  * `git checkout -b <branch_name>` — Create a new branch and switch to it immediately.
  * `git merge <branch_name>` — Merge changes from another branch into the current branch.
* **History Reorganization (Rebase):**
  * `git rebase <branch>` — Replay commits from one branch onto another.
  * `git rebase -i HEAD~N` — Reorder and modify commits interactively.
* **Selection and Reversion Operations:**
  * `git cherry-pick <commit>` — Copy a specific commit from any branch into your current workflow.
  * `git restore --staged <file>` — Unstage a file from the index.
  * `git commit --amend` — Modify or update the last commit.