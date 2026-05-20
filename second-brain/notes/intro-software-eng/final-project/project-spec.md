# SE-201 Final Project — Bank Software System

**Due:** Sat Jun 6, 5:00 AM · **Zero extensions — lose all 20%**
**Language:** Java 17 · **Submission:** Blackboard zip
**Code location:** [[second-brain/notes/intro-software-eng/Coding/BankSystem|BankSystem (code)]]

> ⚠️ Do not start coding until instructed. Assignments build toward this in a specific order.

---

## Overview

Build a bank software system driven entirely by command strings. No Scanner, no System.out.

```java
public List<String> execute(List<String> input) { ... }
```

Input: a list of command strings. Output: a list of result strings.

---

## Account Types

| Type | Initial Balance | APR Accrual | Deposit Max | Withdrawal Max |
|------|----------------|-------------|-------------|----------------|
| Checking | $0 | Monthly | $1000 | $400/command |
| Savings | $0 | Monthly | $2500 | $1000/command, 1x/month |
| CD | $1000–$10000 | 4× per month | ❌ | Full balance only, after 12 months |

---

## Commands

### Create
```
create <type> <id> <apr>          // checking or savings
create cd <id> <apr> <amount>     // CD only
```
- `type`: checking / savings / cd (case insensitive)
- `id`: unique 8-digit number
- `apr`: 0–10 (percentage, e.g. 0.6)
- CD `amount`: $1000–$10000

### Deposit
```
deposit <id> <amount>
```
- Checking max: $1000 · Savings max: $2500 · CD: invalid
- Amount ≥ 0

### Withdraw
```
withdraw <id> <amount>
```
- Checking max: $400 · Savings max: $1000 (1x/month) · CD: full balance after 12 months
- Overdraft → balance goes to $0 (valid)

### Transfer
```
transfer <from-id> <to-id> <amount>
```
- Checking ↔ Checking, Checking ↔ Savings, Savings ↔ Savings only (no CD)
- Applies deposit and withdrawal rules of respective account types
- Only transfers the amount actually withdrawn

### Pass Time
```
pass <months>    // 1–60 integer only
```
For each month, in order:
1. Close any account with $0 balance
2. Deduct $25 from any account with balance < $100
3. Accrue APR (checking/savings: monthly formula; CD: 4× per month)

---

## APR Formula

**Checking / Savings (monthly):**
```
monthly_rate = (apr / 100) / 12
new_balance  = balance + (balance × monthly_rate)
```

**CD (4× per month):**
```
for i in range(4):
    monthly_rate = (apr / 100) / 12
    balance = balance + (balance × monthly_rate)
```

---

## Output Format

For each **open** account (in creation order):
```
<Type> <id> <balance> <apr>
<transaction 1>
<transaction 2>
...
```
- Type: capitalized first letter, rest lowercase (e.g. `Savings`, `Cd`)
- Balance & APR: floor-truncated to 2 decimal places (`DecimalFormat("0.00")` + `FLOOR`)
- Transaction history: all commands that touched the account (except pass time), in order; output exactly as received

After all accounts:
```
<invalid command 1>
<invalid command 2>
...
```
Invalid commands: output exactly as received, in order received.

---

## Example

Input:
```
Create savings 12345678 0.6
Deposit 12345678 700
Deposit 12345678 5000
creAte cHecKing 98765432 0.01
Deposit 98765432 300
Transfer 98765432 12345678 300
Pass 1
Create cd 23456789 1.2 2000
```

Output:
```
Savings 12345678 1000.50 0.60
Deposit 12345678 700
Transfer 98765432 12345678 300
Cd 23456789 2000.00 1.20
Deposit 12345678 5000
```
*(Checking account closed — balance went to $0 after transfer + pass time)*

---

## Validation Rules Summary

- All commands case insensitive
- Extra spaces at start or middle → invalid
- Extra arguments on any command → invalid
- Scientific/exponential notation → invalid
- Non-integer pass time (e.g. `pass 6.0`) → invalid
- Invalid commands stored and output at the end, in order

---

## Related Notes

[[second-brain/notes/intro-software-eng/final-project/Lab-W3-Kanban|Lab W3 — Kanban Board]]
[[second-brain/notes/intro-software-eng/Coding/Se201-Projects|SE-201 Code Projects]]
[[second-brain/notes/intro-software-eng/assignments/index|Assignments & Labs]]
[[semester-spring-2026]]
