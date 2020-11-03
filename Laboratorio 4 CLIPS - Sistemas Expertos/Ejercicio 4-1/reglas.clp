(defglobal ?*numero* = (random 0 100))
(defrule lee
?h<-(lee)
=>
(retract ?h)
(printout t "Escribe un numero: ")
(assert (numero (read))))

(defrule bajo
?h<-(numero ?n&:(< ?n ?*numero*))
=>
(retract ?h)
(printout t ?n " es bajo" crlf)
(assert (lee)))

(defrule alto
?h<-(numero ?n&:(> ?n ?*numero*))
=>
(retract ?h)
(printout t ?n " es alto" crlf)
(assert (lee)))

(defrule exacto
?h<-(numero ?n&:(= ?n ?*numero*))
=>
(retract ?h)
(printout t ?n " es exacto" crlf))