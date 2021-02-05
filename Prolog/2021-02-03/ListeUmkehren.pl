letztesElement([K1|R1], K1):- R1==[].
letztesElement([K1|R1], E):- E\==K1, letztesElement(R1, E).

