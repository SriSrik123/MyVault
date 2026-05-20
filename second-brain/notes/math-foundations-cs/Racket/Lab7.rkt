#lang racket
;Question 1


(define (rem a b)
   (if (< a b)
      a
   

(rem (- a b) b)))

(rem 1 2)

;Question 2
(define (R n)

  (if (= n 0)
      0
  
  
      (+ (/ 1 (expt 2 n)) (R (- n 1)))))
(R 4)

;Question 3

(define (largestMultiple max mult)
  (if (= (remainder max mult) 0)
      max
      (largestMultiple (- max 1) mult)))

(largestMultiple 4000 11)

;Question 4

(define (logStar n)
  (if (< n 1)
      0
      (+ 1 (logStar (log n)))))

(logStar 100)
