(defrule agregar-facts
=>
(open "data.txt" mydata)
(while (neq (bind ?persona (readline mydata)) EOF)
	(bind ?fact(str-cat "(Persona " ?persona ")"))
	(assert-string ?fact))
(close))