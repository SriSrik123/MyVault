#lang racket

;Question 1.1 Create '(1 2 3)
(cons 1(cons 2(cons 3 null)))

;Question 1.2 Create '((1) (2))
(cons (cons 1 null) (cons (cons 2 null) null))

;Question 1.3 Create '(((1)))
(cons (cons (cons 1 null) null) null)

;Question 1.4 Create '(() ())
(cons null (cons null null))

;Question 1.5 Create '((1 2) (3))
(cons (cons 1 (cons 2 null)) (cons (cons 3 null) null))

;Question 1.6 Create '(((())))

(cons (cons (cons null null) null) null)

;Q2 Define a recursive racket function (seq n) that returns a list of integers from n down to 0.  If the input is negative, return the null list. This is useful because the last number you want to work on is 0, all negative numbers returning the empty list is a simple starting point. Your solution must use recursion.
;For example: 

;(seq -1) ;Returns '()
;(seq 0) ;Returns '(0)
;(seq 1) ;Returns '(1 0)
;(seq 2) ;Returns '(2 1 0)
;(seq 3) ;Returns '(3 2 1 0)
;(seq 4) ;Returns '(4 3 2 1 0)
;Question 2.1

;Input: n - an integer
;Output: a list of integers from n down to 0, or the null list if n is negative

;2.2 actual function
(define (seq n)
  (if (< n 0)
      null
      (cons n (seq (- n 1)))))

(seq 4)

; Define a recursive racket function (mult5 n k) that returns a list of n integers that are multiples of 5 starting with k
;Your solution must use recursion.

; You may assume that k will always be a multiple of 5.

; For example: 

; (mult5 0 10) ;Returns '()
; (mult5 1 10) ;Returns '(10)
; (mult5 2 10) ;Returns '(10 15)
; (mult5 3 10) ;Returns '(10 15 20)
; (mult5 4 10) ;Returns '(10 15 20 25)
; (mult5 5 10) ;Returns '(10 15 20 25 30)
; (mult5 6 90) ;Returns '(90 95 100 105 110 115)
; (mult5 7 25) ;Returns '(25 30 35 40 45 50 55)
; (mult5 8 5) ;Returns '(5 10 15 20 25 30 35 40)
; Question 3.1

;Input: n - an integer, k - an integer (multiple of 5)
;Output: a list of n integers that are multiples of 5 starting with k

;3.2 actual function
(define (mult5 n k)
  (if (<= n 0)
      null
      (cons k (mult5 (- n 1) (+ k 5)))))

(mult5 5 10)


; Define a recursive racket function (largest L) finds the largest number in an unsorted list L.  Your solution must use recursion.

; You may assume that  L will be null or only contain positive integers.

; For example: 

; (largest null) ;Returns 0
; (largest '(1 2)) ;Returns 2
; (largest '(2 1)) ;Returns 2
; (largest '(1 9 2 8 3 7 4 6 5)) ;Returns 9
; (largest '(1 2 3 4 5 6 7 8 9)) ;Returns 9
; (largest '(9 8 7 6 5 4 3 2 1)) ;Returns  9
; (largest '(10 20 100 50 92 72 99)) ;Returns 100

;Question 4.1
;Input: L - a list of positive integers (or null)
;Output: the largest number in the list, or 0 if the list is null

;4.2 actual function
(define (largest L)
  (if (null? L)
      0
      (if (null? (rest L))
          (first L)
          (if (> (first L) (largest (rest L)))
              (first L)
              (largest (rest L))))))

(largest '(1 67 2 8 3 7 4 6 5))

