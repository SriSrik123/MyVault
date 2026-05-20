---

kanban-plugin: board

---

## 🎯 To Do

- [ ] [BANK-003] Create a CD account with a valid ID, APR, and initial amount #create
- [ ] [BANK-006] Reject create with APR outside the range of 0–10 #create
- [ ] [BANK-007] Reject CD creation with an amount outside $1,000–$10,000 #create
- [ ] [BANK-009] Deposit into a checking account up to the $1,000 max #deposit
- [ ] [BANK-010] Deposit into a savings account up to the $2,500 max #deposit
- [ ] [BANK-011] Reject any deposit into a CD account #deposit
- [ ] [BANK-012] Reject a deposit that exceeds the account's maximum #deposit
- [ ] [BANK-014] Allow a deposit of exactly zero #deposit
- [ ] [BANK-015] Withdraw from a checking account up to the $400 max #withdrawal
- [ ] [BANK-016] Withdraw from a savings account up to the $1,000 max #withdrawal
- [ ] [BANK-017] Enforce a maximum of 1 savings withdrawal per month #withdrawal
- [ ] [BANK-018] Reject any CD withdrawal before 12 months have passed #withdrawal
- [ ] [BANK-019] Allow only a full-balance withdrawal from a CD after 12 months #withdrawal
- [ ] [BANK-020] Handle overdraft — balance caps at $0, does not go negative #withdrawal
- [ ] [BANK-021] Allow a withdrawal of exactly zero #withdrawal
- [ ] [BANK-022] Reject a negative withdrawal amount #withdrawal
- [ ] [BANK-023] Transfer between two checking accounts #transfer
- [ ] [BANK-024] Transfer between a checking and a savings account (either direction) #transfer
- [ ] [BANK-025] Transfer between two savings accounts #transfer
- [ ] [BANK-026] Reject any transfer that involves a CD account (from or to) #transfer
- [ ] [BANK-027] Reject a transfer from an account to itself #transfer
- [ ] [BANK-028] Apply deposit and withdrawal rules to each side of a transfer #transfer
- [ ] [BANK-029] Only deposit the amount actually withdrawn when source overdraws #transfer
- [ ] [BANK-030] Accept pass time of 1–60 whole months #pass-time
- [ ] [BANK-031] Reject pass time of 0 or more than 60 #pass-time
- [ ] [BANK-032] Reject decimal or non-integer pass time values (e.g. 6.0) #pass-time
- [ ] [BANK-033] Close any account with a $0 balance at the start of each month #pass-time
- [ ] [BANK-034] Deduct a $25 minimum-balance fee for accounts under $100 each month #pass-time
- [ ] [BANK-035] Accrue monthly APR for checking and savings accounts #pass-time
- [ ] [BANK-036] Accrue CD APR four times per month (compounded) #pass-time
- [ ] [BANK-037] Output each open account's state: type, ID, balance, APR #output
- [ ] [BANK-038] List accounts in the order they were created #output
- [ ] [BANK-039] Output each account's full transaction history in order #output
- [ ] [BANK-040] Floor-truncate balance to 2 decimal places #output
- [ ] [BANK-041] Floor-truncate APR to 2 decimal places with trailing zeros (e.g. 3.00) #output
- [ ] [BANK-042] Capitalize account type correctly (e.g. Savings, Checking, Cd) #output
- [ ] [BANK-043] Append all invalid commands at the end of output in order received #output
- [ ] [BANK-045] Reject any command that has extra arguments #validation
- [ ] [BANK-046] Reject commands with leading or mid-string extra spaces #validation
- [ ] [BANK-047] Reject scientific or exponential notation in any numeric field #validation


## 🔧 In Progress



## ✅ Done

- [x] [BANK-001] Create a checking account with a valid 8-digit ID and APR #create
- [x] [BANK-002] Create a savings account with a valid 8-digit ID and APR #create
- [x] [BANK-004] Reject create with an invalid account type (not checking/savings/cd) #create
- [x] [BANK-005] Reject create with a non-8-digit ID or a duplicate ID #create
- [x] [BANK-008] Initialize checking/savings with $0 and accept case-insensitive type names #create
- [x] [BANK-013] Reject a negative deposit amount #deposit
- [x] [BANK-044] Reject all unrecognized commands and store them for output #validation
- [x] [BANK-048] Accept a `List<String>` as the sole input to the public method #master-control
- [x] [BANK-049] Return a `List<String>` as the sole output of the public method #master-control
- [x] [BANK-050] No Scanner or System.out anywhere in the codebase #master-control





%% kanban:settings
```
{"kanban-plugin":"board"}
```
%%