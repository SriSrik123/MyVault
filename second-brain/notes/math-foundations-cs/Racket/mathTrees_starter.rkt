#lang racket
(require racket/contract)
(require rackunit)
(require rackunit/text-ui)
(define ns (make-base-namespace))

; This file comes premade with some useful mathTree functions.
; Recall that we are defining a mathTree recursively as
; mathTree: = term | (op mathTree mathTree)
; term : = integer | variable
; op : = * | + | -

; Requirements: Do NOT use list functions (first/rest/cons/null?) on mathtrees! Only use the following tree methods on trees.

; here are the intermediate predicates which precisely mimic their definitions on lines 10&11
(define (term? x) (or (integer? x) (symbol? x)))
(define (op? x) (or (equal? x '*) (equal? x '+) (equal? x '-)))


; this is the constructor for trees.
; similar to succ for pnums, and how cons take an object and a list and makes a bigger list with that object as the new first member,
; this function takes and integer and two trees and puts them together to make a bigger tree with the integer at the root and the two given trees are the branches
(define (consTree op L R)  (cons op (cons L (cons R null))))

; Input Contract: T is a nonempty Tree
; Output Contract: (left T) is the left branch of T
(define (left T) (first (rest T))) ;  an accessor for subtrees. left is a way to make a tree smaller, similar to pred for pnums and rest for lists.

; Input Contract: T is a nonempty Tree
; Output contract: (right T) is the right branch of T
; Note: we need two distinct functions to get subtrees (left and right) since a tree is constructed out of two independent branches. 
(define (right T)
  (first (rest (rest T)))) 

; the MathTree predicate, exactly matching the definition on line5
(define (mathTree? x)
  (or
   (term? x)
   (and (list? x) (equal? (length x) 3) (op? (first x)) (mathTree? (left x)) (mathTree? (right x)))
  )
)  

; this is a "setter" for mathTrees, and lets us assign a value for the root
(define (setOp op T) (consTree op (left T) (right T)))

; this is the "getter" for mathTrees, and returns the root value
(define (getRoot T) (if (term? T) T (first T))) 


; QUESTION 2: countOp
; Input-contract: exp is a mathtree
; Output-contract: (countOp exp) is the number of operators in exp
 
(define (countOp exp)
 
 (if (term? exp)
      0
      (+ 1 (countOp (left exp)) (countOp (right exp))))


)

(display "checking countOp method\n")
(define-test-suite op-test
  (check-equal? (countOp 'x) 0)
  (check-equal? (countOp '(+ x 7)) 1)
  (check-equal? (countOp '(- x y)) 1)
  (check-equal? (countOp '(+ (* 2 x)(- y 2))) 3)
  (check-equal? (countOp 7) 0)
  (check-equal? (countOp '(+ x (- y (* 2 (+ z x))))) 4))
(define op-pass (- 6 (run-tests op-test)))

; QUESTION 3: countOp
; Input-contract: exp is a mathtree
; Output-contract: (countTerms exp) is the number of terms in exp
 
(define (countTerms exp)

(if (term? exp)
      1
      (+ (countTerms (left exp)) (countTerms (right exp)))
      
      ))


(display "checking countTerms method\n")
(define-test-suite term-test
  (check-equal? (countTerms 'x) 1)
  (check-equal? (countTerms '(+ x 7)) 2)
  (check-equal? (countTerms '(- x y)) 2)
  (check-equal? (countTerms '(+ (* 2 x)(- y 2))) 4)
  (check-equal? (countTerms 7) 1)
  (check-equal? (countTerms '(+ x (- y (* 2 (+ z x))))) 5))
(define term-pass (- 6 (run-tests term-test)))

; QUESTION 4: setVar
; Input-contract: exp is a mathtree, var is a variable, val is an integer
; Output-contract: (setVar exp var val) is the mathtree identical to exp, but with var replaced by val
 
(define (setVar exp var val)

(if (term? exp)
    (if (equal? exp var) val exp)
    (consTree (getRoot exp) (setVar (left exp) var val) (setVar (right exp) var val))
    ))

(display "checking setVar method\n")
(define-test-suite setVar-test
  (check-equal? (setVar 'x 'x 2) 2)
  (check-equal? (setVar 7 'x 2) 7)
  (check-equal? (setVar '(+ 9 7) 'x 9) '(+ 9 7))
  (check-equal? (setVar '(- x y) 'y 3) '(- x 3))
  (check-equal? (setVar '(+ (* 2 x)(- y 2)) 'y 9) '(+ (* 2 x)(- 9 2)))
  (check-equal? (setVar '(+ x (- y (* 2 (+ z x)))) 'x 12) '(+ 12 (- y (* 2 (+ z 12)))))
  (check-equal? (eval (setVar '(+ 9 7) 'x 9) ns) 16))
(define setVar-pass (- 7 (run-tests setVar-test)))
(display "countOp method passed: ")(display op-pass)(display "/6\n")
(display "countTerm method passed: ")(display term-pass)(display "/6\n")
(display "setVar method passed: ")(display setVar-pass)(display "/7\n")