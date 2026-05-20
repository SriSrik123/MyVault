#lang racket


;Question 1
; Write a recursive Racket function that applies an arbitrary function f to the value n until the result is less that b.

; Define the function (star f n b) to return the number of times the function f
; f needs to be repeatedly applied until the input values is less that b

;input-contract: a function f that takes an integer and decreases its value,
;    n is a non-negative integer, b is the target to get below
;output-contract: an integer, the amount of times the function needs
;    to be applied repeatedly to get a value less than b

(define (star f n b)
    (if (< n b)
        0                                                                                                                                                                      
        (+ 1 (star f (f n) b))))


(star log 100 1) 


; Question 2
; The function (map f I) is built into Racket. It takes two arguments:
; • f a function of a single variable
; • La list of elements in the domain of f
; If L = (x1 x2... xn), the output of the function is the list ((f x1) (f x2)... (f xn)). Map creates a new list
; by applying the function to each value in the list.
; If we want to square numbers we know that is (* * *). The result of (map (Lambda (x) (* * x)) '(1 2 3 4)1 is | (1 A 9 16). It makes a list (12 22 32 42).
; 
;Q2.1
; 8 Points
; Using lambda and map come up with a single line command to change the list "(1 2 3 4) into the list (3 6 9 12)

(map (lambda (x) (* 3 x)) '(1 2 3 4))

; Using lambda and map come up with a single line command to change the list ' 
;(1 2  3 4) into the ; list '(-1 - 2 -3 -4)

(map (lambda (x) (* -1 x)) '(1 2 3 4))
(map -'( 1 2 3 4))

; Using lambda and map come up with a single line command to change the list '(1 2 3 4) into the
; list : (9 8 7 6)

(map (lambda (x) (- 10 x)) '(1 2 3 4))

; Question 3. 
; Racket has two functions to combine the elements of a list. Both have the same three inputs.
; • J a function of two variables
; • init the value to be returned when L = null
; • L a list of elements in the domain of f
; Calling (foldr - 0 '(1 2 3 4)) computes - 2
; This function computes (- 1(-2 (-3 (- 4 0)))).
; Calling (fold1 - O '(1 2 3 4)) computes 2
; This function computes (- 4 (- 3 (- 2 (- 1 0)))) .
; Decide which direction to fold (foldr or fold) and a single arithmetic operation (+, -, * , /) starting at a
; base of either 0 or 1, such that the folding the list (1 2 3 4) would result in the target value.
; Write down the racket expression which accomplishes this.

;3.1 How can you get a result of 24? 

(foldl * 1 '(1 2 3 4))

;3.2 How can you get a result of 3/8?

(foldr / 1 '(1 2 3 4))

;3.3 How can you get a result of 8/3?
(foldl / 1 '(1 2 3 4))

;Question 4
;In this question, you will build a single line command that solves a problem. Each question builds towards the final answer.

;4.1 Write a function (define (neg? x) ...) that returns 1 if the number is negative and 0 otherwise.
(define (neg? x)
    (if (< x 0)
        1
        0))

(neg? 5)  ;Should be 0
(neg? -5) ;Should be 1

;4.2 Write a racket expression that uses map to apply your neg? function to the list '(1 -3 -4 5 9).

(map neg? '(1 -3 -4 5 9))

;4.3
; Write a single line expression to use map, foldr, and lambda to count the number of negative numbers in a list named L.
; Do not explicitly call the neg? function you wrote, instead use lambdas to do everything in a single line command.
; Provide your command below. You may use L = '(1 -3 -4 5 9) for testing but design your code for
; a general list.

(foldr + 0 (map (lambda (x) (if (< x 0) 1 0)) '(1 -3 -4 5 9)))