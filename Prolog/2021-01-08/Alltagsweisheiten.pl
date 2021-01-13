%Prädikate
platz(a,1).
platz(a,2).
platz(b,4).
platz(c,7).
platz(c,5).
platz(c,6).
platz(c,3).

auf(1, a).
auf(2, 1).
auf(4, b).
auf(7, c).
auf(5, 7).
auf(6, 5).
auf(3, 6).

%Regeln
ueber(OBEN,UNTEN):- auf(OBEN,UNTEN).
ueber(OBEN,UNTEN):- auf(UB,UNTEN), ueber(OBEN,UB).
