#lang racket
(require racket/contract)
(require rackunit)
(require rackunit/text-ui)

; This file comes premade with some useful tree functions.
; Recall that we are defining a tree recursively as
; Tree: = null | (int Tree Tree)

; In all these functions, our contracts are that T,L,R are trees and v is an integer. (x represents any object)

; These just alias functions we already have.
(define emptyTree null)  ; this represents option 1 in the definition, the nonrecursive tree case, on the left of the | symbol
(define emptyTree? null?) ; this gives us a predicate to check for our base structure, similar to zero? for integers and null? for list

; This is the constructor for trees.
; A tree has a root, left and right side.
; Input Contract: v is an integer, L and R are trees.
; Ouput Contract: A new tree with v as the root, L as the left side, and R as the right side.
(define (consTree v L R)  (cons v (cons L (cons R null))))

; Input Contract: T is a nonempty Tree
; Output Contract: (left T) is the left branch of T
(define (left T) (first (rest T))) ;  an accessor for subtrees. left is a way to make a tree smaller, similar to pred for pnums and rest for lists.

; Input Contract: T is a nonempty Tree
; Output contract: (right T) is the right branch of T
; Note: we need two distinct functions to get subtrees (left and right) since a tree is constructed out of two independent branches. 
(define (right T) (first (rest (rest T))))

; the tree predicate, exactly matching the definition on line4
; Input Contact: Anything
; Output Contract: True if x is a tree (by our definition)
(define (tree? x) (or (emptyTree? x) (and (list? x) (equal? (length x) 3) (integer? (first x)) (tree? (left x)) (tree? (right x)))))  

; this is a "setter" for trees, and lets us assign a value for the root
; Input Contract: v is an integer and T is a tree
; Output Contact: A new tree with v replacing the old root
(define (setValue v T) (consTree v (left T) (right T)))

; this is the "getter" for trees, and returns the integer value at the root
; Input Contract: T is a tree
; Output Contract: The root value of tree
(define (getValue T) (first T))

(define test1 '(5 (3 (1 () (2 () ())) ()) (7 () (9 () ()))) )
(define test2 '(6 (3 (1 () ()) (4 () ())) (7 () (8 () (9 () ())))) )

; code for Lab can be entered below:

; input contract: T is a binary tree
; output contract: (countvals T) is the amount of values stored in T 
;note: like all counts, this will always be a non-negative integer).
; Requirements: use functions provided in trees.rkt

(define (countvals T) 
    (if (emptyTree? T) 
        0 
     (+ 1 (countvals (left T)) 
        (countvals (right T)))))


(countvals test1)
(countvals test2)

; input contract: T is a binary search tree and v is an integer
; output contract: (search v T) is true if v is a value in T
; and false otherwise
; Requirements: you should never need to search down both branches,
;       since T is a binary search tree, choose the single appropriate path.
(define (search v T) 
    (if (emptyTree? T) 
        
        false 

    (if (equal? v (getValue T)) 
            
            true 

    (if (< v (getValue T)) (search v (left T)) (search v (right T))))))

(search 1 test1) ;#t
(search 7 test1) ;#t
(search 11 test1) ;#f
(search 3 test2) ;#t
(search 7 test2) ;#t
(search 5 test2) ;#f