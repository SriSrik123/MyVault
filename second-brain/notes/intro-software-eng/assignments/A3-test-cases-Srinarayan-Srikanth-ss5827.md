
## Valid Test Cases

| Test Name                       | Test String                                                        | Test Conditions    | Expected Result |
| ------------------------------- | ------------------------------------------------------------------ | ------------------ | --------------- |
| Valid checking account          | `Create checking 12345678 0.6`                                     | Empty bank         | Valid           |
| Valid savings account           | `Create savings 12345678 0.6`                                      | Empty bank         | Valid           |
| Valid CD account                | `Create cd 12345678 1.2 2000`                                      | Empty bank         | Valid           |
| Case insensitive — all caps     | `CREATE CHECKING 12345678 0.6`                                     | Empty bank         | Valid           |
| Case insensitive — mixed case   | `cReAtE sAvInGs 12345678 0.6`                                      | Empty bank         | Valid           |
| APR of zero (minimum boundary)  | `Create checking 12345678 0`                                       | Empty bank         | Valid           |
| APR of 10 (maximum boundary)    | `Create savings 12345678 10`                                       | Empty bank         | Valid           |
| APR with decimal                | `Create checking 12345678 0.01`                                    | Empty bank         | Valid           |
| APR as whole number             | `Create checking 12345678 3`                                       | Empty bank         | Valid           |
| CD with minimum amount ($1000)  | `Create cd 12345678 1.2 1000`                                      | Empty bank         | Valid           |
| CD with maximum amount ($10000) | `Create cd 12345678 1.2 10000`                                     | Empty bank         | Valid           |
| CD with decimal amount          | `Create cd 12345678 1.2 1500.50`                                   | Empty bank         | Valid           |
| Trailing space on command       | `Create checking 12345678 0.6 `                                    | Empty bank         | Valid           |
| ID with leading zeros           | `Create checking 00000001 0.6`                                     | Empty bank         | Valid           |
| Two unique accounts, same type  | `Create checking 12345678 0.6` then `Create checking 87654321 1.0` | After first create | Valid           |

---

## Invalid — Account Type

| Test Name | Test String | Test Conditions | Expected Result |
|-----------|-------------|-----------------|-----------------|
| Unrecognized account type | `Create foobar 12345678 0.6` | Empty bank | Invalid |
| Misspelled type | `Create chekcing 12345678 0.6` | Empty bank | Invalid |
| Numeric type | `Create 123 12345678 0.6` | Empty bank | Invalid |
| Missing type entirely | `Create 12345678 0.6` | Empty bank | Invalid |
| Empty string | `` | Empty bank | Invalid |
| Only the word create | `Create` | Empty bank | Invalid |

---

## Invalid — ID

| Test Name | Test String | Test Conditions | Expected Result |
|-----------|-------------|-----------------|-----------------|
| ID too short — 7 digits | `Create checking 1234567 0.6` | Empty bank | Invalid |
| ID too long — 9 digits | `Create checking 123456789 0.6` | Empty bank | Invalid |
| ID contains letters | `Create checking abcdefgh 0.6` | Empty bank | Invalid |
| ID is alphanumeric | `Create checking 1234567a 0.6` | Empty bank | Invalid |
| Duplicate ID — same type | `Create checking 12345678 0.6` | Account 12345678 already exists | Invalid |
| Duplicate ID — different type | `Create savings 12345678 1.0` | Checking 12345678 already exists | Invalid |
| ID is zero | `Create checking 00000000 0.6` | Empty bank | Invalid |
| Missing ID | `Create checking 0.6` | Empty bank | Invalid |

---

## Invalid — APR

| Test Name | Test String | Test Conditions | Expected Result |
|-----------|-------------|-----------------|-----------------|
| APR just above maximum (10.01) | `Create checking 12345678 10.01` | Empty bank | Invalid |
| APR well above maximum | `Create checking 12345678 11` | Empty bank | Invalid |
| APR negative (–0.1) | `Create checking 12345678 -0.1` | Empty bank | Invalid |
| APR negative whole number | `Create checking 12345678 -1` | Empty bank | Invalid |
| APR as a string | `Create checking 12345678 abc` | Empty bank | Invalid |
| APR in scientific notation | `Create checking 12345678 1e2` | Empty bank | Invalid |
| Missing APR | `Create checking 12345678` | Empty bank | Invalid |

---

## Invalid — CD Amount

| Test Name | Test String | Test Conditions | Expected Result |
|-----------|-------------|-----------------|-----------------|
| CD amount just below minimum ($999.99) | `Create cd 12345678 1.2 999.99` | Empty bank | Invalid |
| CD amount well below minimum | `Create cd 12345678 1.2 500` | Empty bank | Invalid |
| CD amount just above maximum ($10000.01) | `Create cd 12345678 1.2 10000.01` | Empty bank | Invalid |
| CD amount well above maximum | `Create cd 12345678 1.2 50000` | Empty bank | Invalid |
| CD amount of zero | `Create cd 12345678 1.2 0` | Empty bank | Invalid |
| CD amount negative | `Create cd 12345678 1.2 -500` | Empty bank | Invalid |
| CD missing amount entirely | `Create cd 12345678 1.2` | Empty bank | Invalid |

---

## Invalid — Command Structure

| Test Name | Test String | Test Conditions | Expected Result |
|-----------|-------------|-----------------|-----------------|
| Extra argument on checking | `Create checking 12345678 0.6 extra` | Empty bank | Invalid |
| Extra argument on savings | `Create savings 12345678 0.6 999` | Empty bank | Invalid |
| Extra argument on CD | `Create cd 12345678 1.2 2000 extra` | Empty bank | Invalid |
| Leading space | ` Create checking 12345678 0.6` | Empty bank | Invalid |
| Extra space between words | `Create  checking 12345678 0.6` | Empty bank | Invalid |
| Checking supplied with CD-style amount | `Create checking 12345678 0.6 1000` | Empty bank | Invalid |

---

## Summary

| Category | Valid | Invalid |
|----------|-------|---------|
| Account type | 5 | 6 |
| ID | 4 | 8 |
| APR | 5 | 7 |
| CD amount | 3 | 7 |
| Command structure | 3 | 6 |
| **Total** | **15** | **34** |
