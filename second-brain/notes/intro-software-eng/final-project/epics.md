# SE-201 Bank System — Epics & User Stories

User stories for all 8 epics in the Bank Software System term project.
Kanban board → [[second-brain/notes/intro-software-eng/final-project/Lab-W3-Kanban|Lab W3 Kanban]]

---

## Epic 1 — Create

> As a bank system, I want to create accounts from a command string so that customers can open checking, savings, or CD accounts with a unique ID and APR.

| Story | Description |
|-------|-------------|
| BANK-001 | Create a checking account with a valid 8-digit ID and APR |
| BANK-002 | Create a savings account with a valid 8-digit ID and APR |
| BANK-003 | Create a CD account with a valid ID, APR, and initial amount |
| BANK-004 | Reject create with an invalid account type |
| BANK-005 | Reject create with a non-8-digit ID or duplicate ID |
| BANK-006 | Reject create with APR outside 0–10 |
| BANK-007 | Reject CD creation with amount outside $1,000–$10,000 |
| BANK-008 | Initialize checking/savings at $0 and accept case-insensitive type |

---

## Epic 2 — Deposit

> As a bank system, I want to deposit money into checking and savings accounts so that customers can add funds up to account-specific limits.

| Story | Description |
|-------|-------------|
| BANK-009 | Deposit into a checking account up to the $1,000 max |
| BANK-010 | Deposit into a savings account up to the $2,500 max |
| BANK-011 | Reject any deposit into a CD account |
| BANK-012 | Reject a deposit that exceeds the account's maximum |
| BANK-013 | Reject a negative deposit amount |
| BANK-014 | Allow a deposit of exactly zero |

---

## Epic 3 — Withdrawal

> As a bank system, I want to process withdrawals with account-specific rules so that customers can take out money within the allowed limits and timing constraints.

| Story | Description |
|-------|-------------|
| BANK-015 | Withdraw from a checking account up to the $400 max |
| BANK-016 | Withdraw from a savings account up to the $1,000 max |
| BANK-017 | Enforce a maximum of 1 savings withdrawal per month |
| BANK-018 | Reject any CD withdrawal before 12 months have passed |
| BANK-019 | Allow only a full-balance withdrawal from a CD after 12 months |
| BANK-020 | Handle overdraft — balance caps at $0, does not go negative |
| BANK-021 | Allow a withdrawal of exactly zero |
| BANK-022 | Reject a negative withdrawal amount |

---

## Epic 4 — Transfer

> As a bank system, I want to transfer money between eligible accounts so that customers can move funds while all applicable deposit and withdrawal rules are enforced.

| Story | Description |
|-------|-------------|
| BANK-023 | Transfer between two checking accounts |
| BANK-024 | Transfer between a checking and savings account (either direction) |
| BANK-025 | Transfer between two savings accounts |
| BANK-026 | Reject any transfer involving a CD account (from or to) |
| BANK-027 | Reject a transfer from an account to itself |
| BANK-028 | Apply deposit and withdrawal rules to each side of a transfer |
| BANK-029 | Only deposit the amount actually withdrawn when source overdraws |

---

## Epic 5 — Pass Time

> As a bank system, I want to advance time in monthly increments so that accounts accrue interest, incur fees, and get closed when appropriate.

| Story | Description |
|-------|-------------|
| BANK-030 | Accept pass time of 1–60 whole months |
| BANK-031 | Reject pass time of 0 or more than 60 |
| BANK-032 | Reject decimal or non-integer pass time values (e.g. 6.0) |
| BANK-033 | Close any account with a $0 balance at the start of each month |
| BANK-034 | Deduct a $25 minimum-balance fee for accounts under $100 each month |
| BANK-035 | Accrue monthly APR for checking and savings accounts |
| BANK-036 | Accrue CD APR four times per month (compounded) |

---

## Epic 6 — Output

> As a bank system, I want to produce a formatted list of account states and transaction histories so that the caller can see the current system state after all commands have been processed.

| Story | Description |
|-------|-------------|
| BANK-037 | Output each open account's state: type, ID, balance, APR |
| BANK-038 | List accounts in the order they were created |
| BANK-039 | Output each account's full transaction history in order |
| BANK-040 | Floor-truncate balance to 2 decimal places |
| BANK-041 | Floor-truncate APR to 2 decimal places with trailing zeros (e.g. 3.00) |
| BANK-042 | Capitalize account type correctly (e.g. Savings, Checking, Cd) |
| BANK-043 | Append all invalid commands at the end of output in order received |

---

## Epic 7 — Validation

> As a bank system, I want to catch and store all malformed or invalid commands so that they can be reported in the output without crashing the system.

| Story | Description |
|-------|-------------|
| BANK-044 | Reject all unrecognized commands and store them for output |
| BANK-045 | Reject any command that has extra arguments |
| BANK-046 | Reject commands with leading or mid-string extra spaces |
| BANK-047 | Reject scientific or exponential notation in any numeric field |

---

## Epic 8 — Master Control

> As a developer, I want a single public-facing method that accepts and returns `List<String>` so that the bank system can be tested and driven entirely through string commands with no I/O side effects.

| Story | Description |
|-------|-------------|
| BANK-048 | Accept a `List<String>` as the sole input to the public method |
| BANK-049 | Return a `List<String>` as the sole output of the public method |
| BANK-050 | No Scanner or System.out anywhere in the codebase |

---

## Related Notes

[[second-brain/notes/intro-software-eng/final-project/Lab-W3-Kanban|Kanban Board]]
[[second-brain/notes/intro-software-eng/final-project/project-spec|Project Spec]]
[[second-brain/notes/intro-software-eng/assignments/index|Assignments & Labs]]
