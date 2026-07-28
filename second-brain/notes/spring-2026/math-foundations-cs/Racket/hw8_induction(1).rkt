#lang racket
(require rackunit)
(require rackunit/text-ui)
#|
CS 270

Professor B. Char, M. Boady,  J. Johnson, S. Earth, and G. Long
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



; IMPORTANT:
; Each of the below questions (except Q1) has two parts.
; First, you will be asked to write a Racket function to solve a problem.
; Secondly, you will be asked to prove by induction that your
; Racket code has some property.

;---------------------------------------------------------------------
;---------------------------------------------------------------------
;---------------------------------------------------------------------
; Question 1
; Put your name here.
; Input contract:  No inputs. This function always returns the same thing.
; Output contract: (your-name) is the name of the student who did this assignment.
(define (your-name)
  "Srinarayan Srikanth" 
)

;Test Bed
(display "Question 1 your-name (2 points)\n")
(define-test-suite test_q1
  (test-equal? "" (string? (your-name) ) #t)
  (test-equal? "" (> (string-length (your-name) ) 0) #t)
)
(define q1_score (- 2 (run-tests test_q1 'verbose)))

;---------------------------------------------------------------------
;---------------------------------------------------------------------
;---------------------------------------------------------------------
;Question 2a (10 points)
; Write a recursive function to compute
; the sum( 6*x^2 , x = 1..n) for a given n
; You must write a recursive function.
; If you use any iterative commands (for/loop/sum/etc you will receive a 0)

; Computes sum( 6*x^2 , x = 1..n)
; Input contract:  n an integer >= 1
; Output contract: an integer, the result of the summation
(define (spec_sum n)
  (if (= n 1)
      6
      (+ (* 6 n n) (spec_sum (- n 1)))))

;Test Bed
(display "Question 2a spec_sum (8 points)\n")
(define-test-suite test_spec_sum
  (check-equal? (spec_sum 1) 6)
  (check-equal? (spec_sum 2) 30)
  (check-equal? (spec_sum 4) 180)
  (check-equal? (spec_sum 5) 330)
  (check-equal? (spec_sum 7) 840)
  (check-equal? (spec_sum 8) 1224)
  (check-equal? (spec_sum 9) 1710)
  (check-equal? (spec_sum 10) 2310)
)
(define q2a_score (- 8 (run-tests test_spec_sum 'verbose)))

;Question 2 (10 points)
;Prove by induction that
;For all integers n >= 1 -> (spec_sum n) = 2n^3+3n^2+n

;You may provide your proof below in the comments
; or submit a PDF to gradescope along with this file
; containing the proof.

; Claim: For all integers n >= 1, (spec_sum n) = 2n^3+3n^2+n
;
; Anchor: n = 1
;
; Inductive Hypothesis:
; For some integer k >= 1: (spec_sum k) = 2k^3+3k^2+k
;
; Base Case
; LHS
; Expression                                                          | Justification
; (spec_sum 1)                                                        | Premise for LHS Base Case
; (if (= 1 1) 6 (+ (* 6 1 1) (spec_sum (- 1 1))))                    | Apply definition of spec_sum
; (if #t 6 (+ (* 6 1 1) (spec_sum 0)))                               | Evaluate =
; 6                                                                   | Evaluate if
;
; RHS
; Expression           | Justification
; 2(1)^3+3(1)^2+1 = 6 | Premise for RHS Base Case
;
; Since LHS = RHS = 6, the Base Case holds.
;
; Leap Case (n = k+1, assume (spec_sum k) = 2k^3+3k^2+k)
; LHS
; Expression                                                          | Justification
; (spec_sum (+ k 1))                                                  | Premise for LHS Leap Case
; (if (= (+ k 1) 1) 6 (+ (* 6 (+ k 1) (+ k 1)) (spec_sum k)))       | Apply definition of spec_sum
; (if #f 6 (+ (* 6 (+ k 1) (+ k 1)) (spec_sum k)))                   | Evaluate = (k >= 1 so k+1 != 1)
; (+ (* 6 (+ k 1) (+ k 1)) (spec_sum k))                             | Evaluate if
; (+ 6(k+1)^2 (spec_sum k))                                          | Evaluate *
; (+ 6(k+1)^2 (2k^3+3k^2+k))                                         | Invoke IH
; 2k^3+9k^2+13k+6                                                     | Expand and simplify
;
; RHS
; Expression                                             | Justification
; 2(k+1)^3+3(k+1)^2+(k+1) = 2k^3+9k^2+13k+6           | Premise for RHS Leap Case
;
; Since LHS = RHS = 2k^3+9k^2+13k+6, the Leap Case holds.
;
; Conclusion: Both base and leap cases have been demonstrated.
; By PMI, for all integers n >= 1, (spec_sum n) = 2n^3+3n^2+n.

;---------------------------------------------------------------------
;---------------------------------------------------------------------
;---------------------------------------------------------------------
;Question 3 (10 points)
; Write a function in Racket (define (veryNested n x) ...)
; that takes two integers, n and x, as input.

; veryNested will return a new list with value x nested
; into 2n parenthesis.

; For example, (veryNested 3 9) will return '((((((9)))))).
; The value 9 has been nested into 2*3=6 parenthesis
; (i.e. six left parentheses, the integer 9, then followed by six right parentheses).

; Your code must be recursive. You may NOT use high order functions (no map, foldr, etc.)
; --- you must implement the recursion yourself.
; No helper functions are allowed.
 

; Create a very nested list
; input-contract: n is a nonnegative integer, and x is a positive integer
; output-contract: (veryNested n x) is an x surrounded by 2*n parentheses 
(define (veryNested n x)
  (if (= n 0)
      x
      (cons (cons (veryNested (- n 1) x) null) null)))

;Test Bed
(display "Question 3a veryNested Tests (10 points)\n")
(define-test-suite test_very_nested
  (check-equal? (veryNested 3 9) '((((((9)))))) )
  (check-equal? (veryNested 5 7) '((((((((((7)))))))))) )
  (check-equal? (veryNested 11 2) '((((((((((((((((((((((2)))))))))))))))))))))) )
  (check-equal? (veryNested 1 1) '((1)) )
  (check-equal? (veryNested 1 3) '((3)) )
  (check-equal? (veryNested 2 4) '((((4)))) )
  (check-equal? (veryNested 4 2) '((((((((2)))))))) )
  (check-equal? (veryNested 5 5) '((((((((((5)))))))))) )
  (check-equal? (veryNested 7 4) '((((((((((((((4)))))))))))))) )
  (check-equal? (veryNested 10 8) '((((((((((((((((((((8)))))))))))))))))))) )
)
(define q3a_score (- 10 (run-tests test_very_nested 'verbose)))

;Question 3b (10 points)
;Prove by induction

;You will use the function depth in this proof.
;You do not need to know it's implementation,
;just the follow properties.

;There is a function (depth X) that counts the levels of nesting in a list.
;The implementation is not relevant.
;You may use the following two lemmas about the depth function.

;Lemma 0: (depth a) = 0 for any integer a
;Lemma 1: (depth (cons L null)) = (+ 1 (depth L)) for any list L

;Prove that (depth (veryNested n x)) = 2*n
;for all non-negative integers n and for all integers x.
;Hint: You may treat x as a constant.

; You may provide your proof below in the comments
; or submit a PDF to gradescope along with this file
; containing the proof.

; Claim: For all non-negative integers n and for all integers x,
;        (depth (veryNested n x)) = 2*n
;
; Anchor: n = 0
;
; Inductive Hypothesis:
; For some integer k >= 0: (depth (veryNested k x)) = 2*k
;
; Base Case
; LHS
; Expression                                                                | Justification
; (depth (veryNested 0 x))                                                  | Premise for LHS Base Case
; (depth (if (= 0 0) x (cons (cons (veryNested (- 0 1) x) null) null)))    | Apply definition of veryNested
; (depth (if #t x ...))                                                     | Evaluate =
; (depth x)                                                                 | Evaluate if
; 0                                                                         | By Lemma 0 (x is an integer)
;
; RHS
; Expression | Justification
; 2*0 = 0    | Premise for RHS Base Case
;
; Since LHS = RHS = 0, the Base Case holds.
;
; Leap Case (n = k+1, assume (depth (veryNested k x)) = 2*k)
; LHS
; Expression                                                                  | Justification
; (depth (veryNested (+ k 1) x))                                              | Premise for LHS Leap Case
; (depth (if (= (+ k 1) 0) x (cons (cons (veryNested k x) null) null)))       | Apply definition of veryNested
; (depth (if #f x (cons (cons (veryNested k x) null) null)))                  | Evaluate = (k+1 != 0)
; (depth (cons (cons (veryNested k x) null) null))                            | Evaluate if
; (+ 1 (depth (cons (veryNested k x) null)))                                  | By Lemma 1
; (+ 1 (+ 1 (depth (veryNested k x))))                                        | By Lemma 1
; (+ 1 (+ 1 (* 2 k)))                                                         | Invoke IH
; 2*(k+1)                                                                      | Arithmetic
;
; RHS
; Expression  | Justification
; 2*(k+1)     | Premise for RHS Leap Case
;
; Since LHS = RHS = 2*(k+1), the Leap Case holds.
;
; Conclusion: Both base and leap cases have been demonstrated.
; By PMI, for all non-negative integers n and for all integers x,
; (depth (veryNested n x)) = 2*n.

;---------------------------------------------------------------------
;---------------------------------------------------------------------
;---------------------------------------------------------------------
; Q4a (10 Points)
; Write a recursive function duplicate that takes every element in a list
; and makes a second copy of the item.
; For example if we started with (1 2 3)
; then the duplicated list would be (1 1 2 2 3 3)

; Duplicates Elements in a list
; Input contract:  X a list
; Output contract: A new list with two copies of even value in X
(define (duplicate X)
  (if (null? X)
      '()
      (cons (car X) (cons (car X) (duplicate (cdr X))))))

(display "Question 4a duplicate Tests (10 points)\n")
(define-test-suite test_duplicate
  (check-equal? (duplicate '()) '())
  (check-equal? (duplicate '(1)) '(1 1))
  (check-equal? (duplicate '(1 2)) '(1 1 2 2))
  (check-equal? (duplicate '(4 6)) '(4 4 6 6))
  (check-equal? (duplicate '((1) (2 3))) '((1) (1) (2 3) (2 3)))
  (check-equal? (duplicate '(4 5 6)) '(4 4 5 5 6 6))
  (check-equal? (duplicate '(7 8 9 10)) '(7 7 8 8 9 9 10 10))
  (check-equal? (duplicate '(1 2 3 4 5)) '(1 1 2 2 3 3 4 4 5 5))
  (check-equal? (duplicate '(9 9 9)) '(9 9 9 9 9 9))
  (check-equal? (duplicate '(1 4 5 6 4 3 4 5))
                '(1 1 4 4 5 5 6 6 4 4 3 3 4 4 5 5))
)
(define q4a_score (- 10 (run-tests test_duplicate 'verbose)))

;4b (10 Points)
; Supposed x is the number of elements in L
; Prove By Induction
; For all lists we have (length (duplicate L)) = 2x

; You may use the following properties of length
; Length Lemma 1: (length '()) = 0 
; Length Lemma 2: If a is an object and B is a list
; (length (cons a B)) = (+ 1 (length B))
; You may Justify lines by saying [By Length Lemma 1]

;You may provide your proof below in the comments
; or submit a PDF to gradescope along with this file
; containing the proof.

; Claim: For all lists L with x elements, (length (duplicate L)) = 2*x
;
; Anchor: L = '() (x = 0)
;
; Inductive Hypothesis:
; For some list B with x elements: (length (duplicate B)) = 2*x
;
; Base Case
; LHS
; Expression                                                                | Justification
; (length (duplicate '()))                                                  | Premise for LHS Base Case
; (length (if (null? '()) '() (cons (car '()) (cons (car '()) (...)))))    | Apply definition of duplicate
; (length (if #t '() ...))                                                 | Evaluate null?
; (length '())                                                              | Evaluate if
; 0                                                                         | By Length Lemma 1
;
; RHS
; Expression | Justification
; 2*0 = 0    | Premise for RHS Base Case
;
; Since LHS = RHS = 0, the Base Case holds.
;
; Leap Case (L = (cons a B), length(B) = x, length(L) = x+1)
; LHS
; Expression                                                                | Justification
; (length (duplicate (cons a B)))                                           | Premise for LHS Leap Case
; (length (if (null? (cons a B)) '()                                        | Apply definition of duplicate
;             (cons (car (cons a B)) (cons (car (cons a B))                 |
;             (duplicate (cdr (cons a B)))))))                              |
; (length (if #f '() (cons a (cons a (duplicate B)))))                     | Evaluate null?, car, cdr
; (length (cons a (cons a (duplicate B))))                                  | Evaluate if
; (+ 1 (length (cons a (duplicate B))))                                     | By Length Lemma 2
; (+ 1 (+ 1 (length (duplicate B))))                                        | By Length Lemma 2
; (+ 1 (+ 1 (* 2 x)))                                                       | Invoke IH
; 2*(x+1)                                                                    | Arithmetic
;
; RHS
; Expression  | Justification
; 2*(x+1)     | Premise for RHS Leap Case
;
; Since LHS = RHS = 2*(x+1), the Leap Case holds.
;
; Conclusion: Both base and leap cases have been demonstrated.
; By POSI, for all lists L with x elements, (length (duplicate L)) = 2*x.

;---------------------------------------------------------------------
;---------------------------------------------------------------------
;---------------------------------------------------------------------
;Question 5a (10pts)
; Write a recursive function (cut_end L) that removes the last element from the list

; Removes the last element in a list
; Input contract:  X non-empty a list
; Output contract: A new list with the last element removed
(define (cut_end L)
  (if (null? (cdr L))
      '()
      (cons (car L) (cut_end (cdr L)))))

(display "Question 5a cut_end Tests (10 points)\n")
(define-test-suite test_cut_end
  (check-equal? (cut_end '(1)) '())
  (check-equal? (cut_end '(1 2)) '(1))
  (check-equal? (cut_end '(3 4 5)) '(3 4))
  (check-equal? (cut_end '( (1) (2) (3) )) '( (1) (2) ))
  (check-equal? (cut_end '((1 2 3 4))) '())
  (check-equal? (cut_end '((1 2) (3 4))) '((1 2)))
  (check-equal? (cut_end '(9 9 8)) '(9 9))
  (check-equal? (cut_end '(AND A B)) '(AND A))
  (check-equal? (cut_end '(NOT X)) '(NOT))
)
(define q5a_score (- 10 (run-tests test_cut_end 'verbose)))

;Question 5b
; Supposed x represents the number of elements in L
; Prove by Induction that
; For all lists with length >= 1 we have (length (cut_end L)) = x-1
; You may use the properties of length from Question 4.

;You may provide your proof below in the comments
; or submit a PDF to gradescope along with this file
; containing the proof.

; Claim: For all lists L with x >= 1 elements, (length (cut_end L)) = x-1
;
; Anchor: L = (cons a null) (x = 1, a single-element list)
;
; Inductive Hypothesis:
; For some list B with x >= 1 elements: (length (cut_end B)) = x-1
;
; Base Case (L = (cons a null), x = 1)
; LHS
; Expression                                                              | Justification
; (length (cut_end (cons a null)))                                        | Premise for LHS Base Case
; (length (if (null? (cdr (cons a null))) '() (cons (car ...) (...))))    | Apply definition of cut_end
; (length (if (null? null) '() ...))                                      | Evaluate cdr
; (length (if #t '() ...))                                                | Evaluate null?
; (length '())                                                             | Evaluate if
; 0                                                                        | By Length Lemma 1
;
; RHS
; Expression | Justification
; 1-1 = 0    | Premise for RHS Base Case
;
; Since LHS = RHS = 0, the Base Case holds.
;
; Leap Case (L = (cons a B), length(B) = x >= 1, length(L) = x+1)
; LHS
; Expression                                                              | Justification
; (length (cut_end (cons a B)))                                           | Premise for LHS Leap Case
; (length (if (null? (cdr (cons a B))) '()                                | Apply definition of cut_end
;             (cons (car (cons a B)) (cut_end (cdr (cons a B))))))        |
; (length (if (null? B) '() (cons a (cut_end B))))                        | Evaluate cdr and car
; (length (if #f '() (cons a (cut_end B))))                               | Evaluate null? (B has x >= 1 elements)
; (length (cons a (cut_end B)))                                            | Evaluate if
; (+ 1 (length (cut_end B)))                                              | By Length Lemma 2
; (+ 1 (x-1))                                                             | Invoke IH
; x                                                                        | Arithmetic
;
; RHS
; Expression    | Justification
; (x+1)-1 = x  | Premise for RHS Leap Case
;
; Since LHS = RHS = x, the Leap Case holds.
;
; Conclusion: Both base and leap cases have been demonstrated.
; By POSI, for all lists L with x >= 1 elements, (length (cut_end L)) = x-1.


;---------------------------------------------------------------------
;---------------------------------------------------------------------
;---------------------------------------------------------------------
; Question 6a (10pts)
; Write a recursive function (add_pairs L)
; that adds pairs of numbers.
; You may assume the length of L will always be even.

; Adds pairs of numbers
; Input contract:  L a list (the list must have even length)
; Output contract: A new list with pairs of elements added together.
(define (add_pairs L)
  (if (null? L)
      '()
      (cons (+ (car L) (cadr L)) (add_pairs (cddr L)))))

(display "Question 6a add_pairs Tests (10 points)\n")
(define-test-suite test_add_pairs
  (check-equal? (add_pairs '()) '())
  (check-equal? (add_pairs '(1 2)) '(3))
  (check-equal? (add_pairs '(1 2 3 4)) '(3 7))
  (check-equal? (add_pairs '(2 2 2 2)) '(4 4))
  (check-equal? (add_pairs '(0 -1 -2 3)) '(-1 1))
  (check-equal? (add_pairs '(1 1 1 1)) '(2 2))
  (check-equal? (add_pairs '(1 2 3 4 5 6 7 8)) '(3 7 11 15))
  (check-equal? (add_pairs '(9 9 9 9 9 9)) '(18 18 18))
  (check-equal? (add_pairs '(7 3 4 6 5 5)) '(10 10 10))
  (check-equal? (add_pairs '(-9 9 -8 8)) '(0 0))
)
(define q6a_score (- 10 (run-tests test_add_pairs 'verbose)))

;Question 6b
; Suppose n represents the number of elements in L
; Prove by induction that
; for all lists of even length it is true that (length (add_pairs L)) = n/2
; You may use the properties of length from previous questions.

;You may provide your proof below in the comments
; or submit a PDF to gradescope along with this file
; containing the proof.

; Claim: For all lists L of even length n, (length (add_pairs L)) = n/2
;
; Anchor: L = '() (n = 0)
;
; Inductive Hypothesis:
; For some even-length list B with n elements: (length (add_pairs B)) = n/2
;
; Base Case
; LHS
; Expression                                                              | Justification
; (length (add_pairs '()))                                                | Premise for LHS Base Case
; (length (if (null? '()) '() (cons (+ (car '()) (cadr '()))             | Apply definition of add_pairs
;             (add_pairs (cddr '())))))                                   |
; (length (if #t '() ...))                                               | Evaluate null?
; (length '())                                                            | Evaluate if
; 0                                                                       | By Length Lemma 1
;
; RHS
; Expression | Justification
; 0/2 = 0    | Premise for RHS Base Case
;
; Since LHS = RHS = 0, the Base Case holds.
;
; Leap Case (L = (cons a (cons b B)), length(B) = n, n even, length(L) = n+2)
; LHS
; Expression                                                              | Justification
; (length (add_pairs (cons a (cons b B))))                                | Premise for LHS Leap Case
; (length (if (null? (cons a (cons b B))) '()                             | Apply definition of add_pairs
;             (cons (+ (car ...) (cadr ...)) (add_pairs (cddr ...)))))    |
; (length (if #f '() (cons (+ a b) (add_pairs B))))                      | Evaluate null?, car, cadr, cddr
; (length (cons (+ a b) (add_pairs B)))                                   | Evaluate if
; (+ 1 (length (add_pairs B)))                                            | By Length Lemma 2
; (+ 1 (n/2))                                                             | Invoke IH
; (n+2)/2                                                                 | Arithmetic
;
; RHS
; Expression  | Justification
; (n+2)/2     | Premise for RHS Leap Case
;
; Since LHS = RHS = (n+2)/2, the Leap Case holds.
;
; Conclusion: Both base and leap cases have been demonstrated.
; By POSI, for all lists L of even length n, (length (add_pairs L)) = n/2.

;---------------------------------------------------------------------
;---------------------------------------------------------------------
;---------------------------------------------------------------------
;;;;;;;;;;;;;;Grade Summary;;;;;;;;;;;;;;;;;;;;;;;
(display "------Test Summary------\n")
(display "Q1 Scored: ")
(display q1_score)
(display "/2\n")
(display "Q2 Scored: ")
(display q2a_score)
(display "/8\n")
(display "Q3 Scored: ")
(display q3a_score)
(display "/10\n")
(display "Q4 Scored: ")
(display q4a_score)
(display "/10\n")
(display "Q5 Scored: ")
(display q5a_score)
(display "/10\n")
(display "Q6 Scored: ")
(display q6a_score)
(display "/10\n")


(define grand_total (+ q1_score q2a_score q3a_score q4a_score q5a_score q6a_score))
(display "\n")
(display "Total: ")
(display grand_total)
(display "/50\n")
(display "\nNOTE: last 50 points are manually graded.\n")