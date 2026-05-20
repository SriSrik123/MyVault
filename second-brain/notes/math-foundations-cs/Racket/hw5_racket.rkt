#lang racket

;The following two lines are required to test the code.
(require rackunit)
(require rackunit/text-ui)

#|
CS 270
Homework 4

Created By Professors Bruce Char, Mark Boady, Jeremy Johnson, Galen Long, and Steve Earth

Complete each of the below functions.

Tests given are not designed to be comprehensive.
They will give you an idea if your code is right, but they do not test all possible cases.
Think about your design. 
The number of tests passed is NOT your final score for the problem.
A grader will review your functions and may add or remove points from the autograder.


Important Rules:
0. Run your code before submitting it.
   If it crashes or goes into an infinite loop,
   A ZERO MAY BE GIVEN FOR THE ASSIGNMENT.

1. You may not use any loop constructs; if used, your answer will get a zero.

2. Unless stated otherwise, all these functions must be implemented recursively.

3. You may not use any Racket commands not discussed in class. If used, your answer may get a zero.
   See Blackboard Learn for a summary of acceptable commands.

4. Do not try to hard code if statements just to pass each test.
   Think about which are special cases and need to be hard coded and which can be handled by recursion.

5. The graders will always obey the input contracts. We will not test inputs that would break the input contract.

6. While you are encouraged to create your own comments, NEVER delete any provided comments.

7. Block comments are only used here and not in the code to help you debug.
   Only line comments will be used below.
|#


;------------ Start of Questions ---------------------

; Question 1
; Srinarayan Srikanth
; Input contract:  No inputs. This function always returns the same thing.
; Output contract: (your-name) is the name of the student who did this assignment.
(define (your-name)
  "Srinarayan Srikanth" ; Put your name as a string like "Ted Bundy"
)

;Test Bed
(display "Question 1 Tests\n")
(define-test-suite test_q1
  (test-equal? "" (string? (your-name) ) #t)
  (test-equal? "" (> (string-length (your-name) ) 0) #t)
)
(define q1_score (- 4 (* 2 (run-tests test_q1 'verbose))))


; Question 2
; Input contract:  n is a non-negative integer
; Output contract: (sumodds n) is the sum of the first n odd numbers.
; Requirements: even if you think you see a simple non-recursive pattern to the answers,
;               you must still implement this recursively.
;               DO NOT try to find a closed form.
; Example: when n=4, the output would be 16 because of 1 + 3 + 5 + 7
(define (sumodds n)
  (if (= n 0)
      0
      (+ (sumodds (- n 1)) (- (* n 2) 1)))
)
  
;Test Bed
(display "Question 2 Tests\n")
(define-test-suite test_q2
  (test-equal? "" (sumodds 1) 1)
  (test-equal? "" (sumodds 2) 4)
  (test-equal? "" (sumodds 3) 9)
  (test-equal? "" (sumodds 4) 16)
  (test-equal? "" (sumodds 5) 25)
  (test-equal? "" (sumodds 6) 36)
  (test-equal? "" (sumodds 7) 49)
  (test-equal? "" (sumodds 8) 64)
  (test-equal? "" (sumodds 9) 81)
  (test-equal? "" (sumodds 10) 100))
(define q2_score (- 10 (run-tests test_q2 'verbose)))


; Question 2
; Input contract:  n is a non-negative integer
; Output contract: (altcubes n) is an alternating adding/subtracting of the first n cubes
; You may use expt to compute exponents (although it is not required)
; Example: when n=5, the output would be 81  because of 1 - 8 + 27 - 64 + 125;
; Hint: How can you decide on +/- using an if?
(define (altcubes n)
  (if (= n 0)
      0
      (+ (altcubes (- n 1))
         (if (= (remainder n 2) 0)
             (- (expt n 3))
             (expt n 3))))

)

;Test Bed
(display "Question 3 Tests\n")
(define-test-suite test_q3
  (test-equal? "" (altcubes 1) 1)
  (test-equal? "" (altcubes 2) -7)
  (test-equal? "" (altcubes 3) 20)
  (test-equal? "" (altcubes 4) -44)
  (test-equal? "" (altcubes 5) 81)
  (test-equal? "" (altcubes 6) -135)
  (test-equal? "" (altcubes 10) -575)
  (test-equal? "" (altcubes 100) -507500)
  (test-equal? "" (altcubes 347) 20981268)
  (test-equal? "" (altcubes 1001) 502253001))
(define q3_score (- 10 (run-tests test_q3 'verbose)))


; Question 3
; Input contract:  n is a positive integer
; Output contract: (logfloor n) is the largest power of 2 which is less than or equal to n
; Example: when n=100, the output would be 6 because 2^6 <= 100 but 2^7 > 100
; Requirement: do NOT use any math operations beyond basic integer arithmetic (e.g. +, - , *, quotient, remainder)
; Hint: (quotient a b) and (/ a b) are slightly different.
(define (logfloor n)
  (if (= n 1)
      0
      (+ 1 (logfloor (quotient n 2))))
      )


;Test Bed
(display "Question 4 Tests\n")
(define-test-suite test_q4
  (test-equal? "" (logfloor 1) 0)
  (test-equal? "" (logfloor 2) 1)
  (test-equal? "" (logfloor 3) 1)
  (test-equal? "" (logfloor 4) 2)
  (test-equal? "" (logfloor 5) 2)
  (test-equal? "" (logfloor 6) 2)
  (test-equal? "" (logfloor 7) 2)
  (test-equal? "" (logfloor 8) 3)
  (test-equal? "" (logfloor 9) 3)
  (test-equal? "" (logfloor 10) 3))
(define q4_score (- 10 (run-tests test_q4 'verbose)))


; Question 5
; Input contract: n is a positive integer, L is a list (possibly empty)
; Output contract: (skip n L) is a list of every nth element of L 
; Example: (skip 3 '(a b c d e f g h)) would be '(a d g)
; Requirements:
;       - Helper functions are allowed as long as recursion is used at least once
;       - DO NOT compute the length (either using built in or hand-made functions)
; Hint: What if (skip n L) *only* skipped once? For example, (skip 3 '(a b c d e f g h)) would be '(a d e f g h).
;       If you can figure out that pattern first it will help with the more general solution.
(define (drop-helper k L)
  (if (null? L)
      null
      (if (= k 0)
          L
          (drop-helper (- k 1) (rest L)))))

(define (skip n L)
  (if (null? L)
      null
      (cons (first L) (skip n (drop-helper (- n 1) (rest L))))))


;Test Bed
(display "Question 5 Tests\n")
(define-test-suite test_q5
  (test-equal? "" (skip 1 '(a b c d e f g h i)) '(a b c d e f g h i))
  (test-equal? "" (skip 2 '(a b c d e f g h i)) '(a c e g i))
  (test-equal? "" (skip 3 '(a b c d e f g h i)) '(a d g))
  (test-equal? "" (skip 4 '(a b c d e f g h i)) '(a e i))
  (test-equal? "" (skip 5 '(a b c d e f g h i)) '(a f))
  (test-equal? "" (skip 6 '(a b c d e f g h i)) '(a g))
  (test-equal? "" (skip 7 '(a b c d e f g h i)) '(a h))
  (test-equal? "" (skip 8 '(a b c d e f g h i)) '(a i))
  (test-equal? "" (skip 9 '(a b c d e f g h i)) '(a))
  (test-equal? "" (skip 10 '(a b c d e f g h i)) '(a)))
(define q5_score (- 10 (run-tests test_q5 'verbose)))


; Question 6
; Input contract: n is a nonnegative integer, L is a list (possibly empty)
; Output contract: (dropLast n L) is the list L with the last n elements removed.
;                 If you try to drop more elements than exist in L, then return null.                 
; Example: (dropLast 3 '(a b c d e f g)) would be '(a b c d) since the last three elements (the e,f,g) were dropped.
; Requirements: 
;       - Helper functions are allowed as long as recursion is used at least once
;       - Do NOT use "let" or "list-ref"
;       - DO NOT compute the length of the whole list (either using built in or hand-made functions)
; Hint: Helper functions are allowed. 

(define (dropLast n L)
  (define (dropper fast slow)
    (if (null? fast)
        null
        (cons (first slow) (dropper (rest fast) (rest slow)))))
  (define (advance lst count)
    (if (or (= count 0) (null? lst)) lst (advance (rest lst) (- count 1))))
  (if (= n 0) L (dropper (advance L n) L)))

;Test Bed
(display "Question 6 Tests\n")
(define-test-suite test_q6
  (test-equal? "" (dropLast 0 '(a b c d e f g h)) '(a b c d e f g h))
  (test-equal? "" (dropLast 1 '(a b c d e f g h)) '(a b c d e f g))
  (test-equal? "" (dropLast 2 '(a b c d e f g h)) '(a b c d e f))
  (test-equal? "" (dropLast 3 '(a b c d e f g h)) '(a b c d e))
  (test-equal? "" (dropLast 4 '(a b c d e f g h)) '(a b c d))
  (test-equal? "" (dropLast 5 '(a b c d e f g h)) '(a b c))
  (test-equal? "" (dropLast 6 '(a b c d e f g h)) '(a b))
  (test-equal? "" (dropLast 7 '(a b c d e f g h)) '(a))
  (test-equal? "" (dropLast 8 '(a b c d e f g h)) null)
  (test-equal? "" (dropLast 9 '(a b c d e f g h)) null))
(define q6_score (- 10 (run-tests test_q6 'verbose)))


; Question 7:
; Descending a Staircase
;
; Imagine you are standing at the top of a staircase and heading to the bottom.
; Your motion options are:
;      - Jump (3 stairs at a time)
;      - Scamper (2 stairs at a time)
;      - Tiptoe (1 stair at a time)
; You would have 4 different methods to descend 3 stairs
; 1. tiptoe, tiptoe, tiptoe
; 2. tiptoe, scamper
; 3. scamper, tiptoe
; 4. jump
; For 5 steps, you have 13 options. (sj, ttj, js, tss, sts, ttts, tjt, sst, ttst, jtt, tstt, stt, ttttt)

; Input contract:  n is a positive integer representing the number of stairs on the staircase
; Output contract: (stepways n) is the number of different ways you could descend to the bottom from the top
; Example: (stepways 5) returns 13
; Hint: The program only needs to give the total count of ways. It should not generate those letters.

(define (stepways n)

  (cond
    [(= n 0) 1]
    [(< n 0) 0]
    [else (+ (stepways (- n 1))
             (stepways (- n 2))
             (stepways (- n 3)))])
)

;Test Bed
(display "Question 7 Tests\n")
(define-test-suite test_q7
  (test-equal? "" (stepways 1) 1)
  (test-equal? "" (stepways 2) 2)
  (test-equal? "" (stepways 4) 7)
  (test-equal? "" (stepways 5) 13)
  (test-equal? "" (stepways 7) 44)
  (test-equal? "" (stepways 10) 274)
  (test-equal? "" (stepways 15) 5768)
  (test-equal? "" (stepways 20) 121415)
  (test-equal? "" (stepways 25) 2555757)
  (test-equal? "" (stepways 30) 53798080))
(define q7_score (- 10 (run-tests test_q7 'verbose)))


; Question 8
; Input contract: n is a positive integer
; Output contract: (sum_digits n) returns the sum of the digits of n.
; For example, when n=3123, the output would be 9 because of 3+1+2+3
; Requirement: Do not convert to lists or strings.
;           Use the basic integer arithmetic functions.
;           (addition, subtraction, multiplication, quotient, remainder)

(define (sumDigits n)

  (if (= n 0)
      0
      (+ (remainder n 10) (sumDigits (quotient n 10))))
)


;Test Bed
(display "Question 8 Tests\n")
(define-test-suite test_q8
  (test-equal? "" (sumDigits 12) 3)
  (test-equal? "" (sumDigits 1) 1)
  (test-equal? "" (sumDigits 999) 27)
  (test-equal? "" (sumDigits 1111) 4)
  (test-equal? "" (sumDigits 22222) 10)
  (test-equal? "" (sumDigits 10000000001) 2)
  (test-equal? "" (sumDigits 395718860534) 59)
  (test-equal? "" (sumDigits 193139816415) 51)
  (test-equal? "" (sumDigits 22424170465) 37)
  (test-equal? "" (sumDigits 800187484459) 58)
  (test-equal? "" (sumDigits 427552056869) 59)
  (test-equal? "" (sumDigits 842622684442) 52)
  (test-equal? "" (sumDigits 412286285840) 50)
  (test-equal? "" (sumDigits 996417214180) 52)
  (test-equal? "" (sumDigits 386408307450) 48)
  (test-equal? "" (sumDigits 694607189265) 63)
)
(define q8_score (- 16 (run-tests test_q8 'verbose)))


; Question 9: 
 
; In this question, you will determine if a number is prime.
; Here is a basic layout for your function.
; 1.) Negative Numbers, 0, and 1 are not primes.
; 2.) To determine if n is prime:
; 2a.) See if n is divisible by i=2
; 2b.) Set i=i+1
; 2c.) If i^2 <=n continue.
; 3.) If no values of i evenly divided n, then it must be prime.
; Note: You can stop when i*i > n.
; Why?
; Take n=19 as an example.
; i=2, 2 does not divide 19 evenly
; i=3, 3 does not divide 19 evenly
; i=4, 4 does not divide 19 evenly
; i=5, we don't need to test this. 5*5=25.
; If 5*x=19, the value of x would have to be smaller then 5.
; We already tested those values!
; No larger numbers can be factors unless one we already test is to.

; Input contract: n is any integer
; Output contract: (prime? n) returns #t if n is prime and #f if it isn't.
; Hint: Use a helper!
(define (prime? n)
 
 (define (prime-helper n i)
    (cond
      [(> (* i i) n) #t]
      [(= (remainder n i) 0) #f]
      [else (prime-helper n (+ i 1))]))
  (if (< n 2)
      #f
      (prime-helper n 2))

 
)


;Here are some tests to see if your function works.
(display "Question 9 Tests\n")
(define-test-suite test_q9
  (test-equal? "" (prime? -1) #f)
  (test-equal? "" (prime? 0) #f)
  (test-equal? "" (prime? 1) #f)
  (test-equal? "" (prime? 2) #t)
  (test-equal? "" (prime? 3) #t)
  (test-equal? "" (prime? 4) #f)
  (test-equal? "" (prime? 5) #t)
  (test-equal? "" (prime? 6) #f)
  (test-equal? "" (prime? 7) #t)
  (test-equal? "" (prime? 8) #f)
  (test-equal? "" (prime? 9) #f)
  (test-equal? "" (prime? 10) #f)
  (test-equal? "" (prime? 11) #t)
  (test-equal? "" (prime? 12) #f)
  (test-equal? "" (prime? 13) #t)
  (test-equal? "" (prime? 14) #f)
  (test-equal? "" (prime? 16) #f)
  (test-equal? "" (prime? 18) #f)
  (test-equal? "" (prime? 20) #f)
  (test-equal? "" (prime? 35) #f))
(define q9_score (- 20 (run-tests test_q9 'verbose)))

;;;;;;;;;;;;;;Test Summary;;;;;;;;;;;;;;;;;;;;;;;
(display "------Test Summary------\n")
(display "Q1 Score: ")(display q1_score)(display "/4\n")
(display "Q2 Score: ")(display q2_score)(display "/10\n")
(display "Q3 Score: ")(display q3_score)(display "/10\n")
(display "Q4 Score: ")(display q4_score)(display "/10\n")
(display "Q5 Score: ")(display q5_score)(display "/10\n")
(display "Q6 Score: ")(display q6_score)(display "/10\n")
(display "Q7 Score: ")(display q7_score)(display "/10\n")
(display "Q8 Score: ")(display q8_score)(display "/10\n")
(display "Q9 Score: ")(display q9_score)(display "/20\n")
(display "Total: ")(display (+ q1_score q2_score q3_score q4_score q5_score q6_score q7_score q8_score q9_score))(newline)
