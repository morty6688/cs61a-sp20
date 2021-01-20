; https://github.com/chenyuxiang0425/cs61a_sp20/blob/master/lab11/lab11.scm
; python3 scheme -i lab11.scm
; (speed 0) (dragon 10 10)
(define (flatmap f x)
  (define (helper k f x)
    (cond 
      ((null? x)
       k)
      (else
       (helper (append k (f (car x))) f (cdr x)))))
  (helper nil f x))

(define (expand lst)
  (define (g x)
    (cond 
      ((equal? x 'x) '(x r y f r))
      ((equal? x 'y) '(l f x l y))
      (else          (list x))))
  (flatmap g lst))

(define (interpret instr dist)
  (cond 
    ((null? instr)
     (fd 0))
    ((equal? (car instr) 'f)
     (begin (fd dist) (interpret (cdr instr) dist)))
    ((equal? (car instr) 'l)
     (begin (lt 90) (interpret (cdr instr) dist)))
    ((equal? (car instr) 'r)
     (begin (rt 90) (interpret (cdr instr) dist)))
    (else
     (interpret (cdr instr) dist))))

(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))
