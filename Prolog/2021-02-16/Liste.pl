sucheInListe(E, [E|R]).
sucheInListe(E, [K|R]) :- E\==K, sucheInListe(E, R).


zusammenfuegen(L1, [], L1).
zusammenfuegen(L1, [K2|R2], [K2|E]) :- zusammenfuegen(L1, R2, E).

ohneLetztes([K], []).
ohneLetztes([K|R], [K|R2]) :- ohneLetztes(R,R2).

letztesElement([K], K).
letztesElement([K|R], E) :- R \== [], letztesElement(R,E).

listeUmkehren([K],[K]).
listeUmkehren(L,[K3|R3]):-letztesElement(L,K3),ol(L,L2),listeUmkehren(L2,R3).

teilBisHilf([K|R], K, [K]).
teilBisHilf([K|R], E, [K|N]) :- teilBisHilf(R, E, N).
teilBis(L, E, N) :- sucheInListe(E,L), teilbishilf(L,E,N).
teilBis(L, E, []) :- not(sucheInListe(E,L)).

vonBis(L,E1,E2,L) :- letztesElement(L, E2), listeUmkehren(L, LU), letztesElement(LU, E1).
