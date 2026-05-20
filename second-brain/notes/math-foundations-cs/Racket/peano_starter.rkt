#lang racket
(require rackunit)
(require rackunit/text-ui)

; CS 270: Starter File for Peano Numbers (aka "pnums")

; Here is the base pnum, and the predicate that checks for it

; This is just giving alias names to built in commands
(define pzero null)
(define pzero? null?)

; The successor of any number is the next number.
; Input contract: N is the pnum representation of n
; Output contract: (succ N) is the pnum representation of n+1
(define (succ N) (cons 's N))

; The predecessor of any number is the previous number.
; Input contract: N is the pnum representation of the non-negative integer n
; Output contract: (pred N) is the pnum representation of n-1, or pzero if N=pzero.
(define (pred N) (if (pzero? N) pzero (rest N)))

; To make testing easier, we define 1-10 as pnums.
(define pone (succ pzero))
(define ptwo (succ pone))
(define pthree (succ ptwo))
(define pfour (succ pthree))
(define pfive (succ pfour))
(define psix (succ pfive))
(define pseven (succ psix))
(define peight (succ pseven))
(define pnine (succ peight))
(define pten (succ pnine))

#| Question 2
Implement the following function according the following specifications.
Input contract: A and B are pnums representing the nonnegative integers a,b respectively
Output contract: (subtract A B) is the pnum representing a-b, or pzero if a<b
Hint: when done optimally, a nested if/cond is not needed
|#
;input-contract: A and B are the pnum for the integers a and b.
;output-contract: (subtract A B) is the pnum for a-b

(define (subtract A B)
  (if (pzero? B)
      A
      (subtract (pred A) (pred B))))

;Tests
(define-test-suite test-subtract
  (check-equal? (subtract pone pzero) pone)
  (check-equal? (subtract pone pone) pzero)
  (check-equal? (subtract pthree ptwo) pone)
  (check-equal? (subtract ptwo pthree) pzero)
  (check-equal? (subtract pten pseven) pthree)  )
(define q2 (- 5 (run-tests test-subtract)))
(display "Q2 passed ")
(display q2)
(display "/5 unit tests\n")

#| Question 3
Implement the following function according the following specifications.
Input contract: n is a nonnegative integer
Output contract: (toPeano n) is N, the pnum representing n
|#
(define (toPeano n)
 
  (if (= n 0)
      pzero
      (succ (toPeano (- n 1))))
      
     )

  

;Tests
(define-test-suite test-toPeano
  (check-equal? (toPeano 1) pone)
  (check-equal? (toPeano 2) ptwo)
  (check-equal? (toPeano 5) pfive)
  (check-equal? (toPeano 7) pseven)
  (check-equal? (toPeano 0) pzero)  )
(define q3 (- 5 (run-tests test-toPeano)))
(display "Q3 passed ")
(display q3)
(display "/5 unit tests\n")