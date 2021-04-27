% Fakten zu Städten an Flüssen

staedte_am_fluss(mosel, [metz, konz, trier, bernkastel, cochem, koblenz]).
staedte_am_fluss(saar, [saarbruecken, saarburg, konz]).
staedte_am_fluss(rhein, [basel, mannheim, mainz, koblenz, koeln, duesseldorf]).
staedte_am_fluss(donau, [ulm, ingolstadt, regensburg, wien, budapest]).
staedte_am_fluss(main, [schweinfurt, wuerzburg, offenbach, frankfurt, mainz]).


element(E, [K|R]) :- E = K.
element(E, [K|R]) :- E \== K, element(E, R).
zusammenfuegen([], L, L).
zusammenfuegen([K|R], L, [K|RL]) :- zusammenfuegen(R, L, RL).
letztes_element([E], E).
letztes_element([K|R], E) :- letztes_element(R, E).
mit_letztem_element([], E, [E]).
mit_letztem_element([K|R], E, [K|L]) :- mit_letztem_element(R, E, L).
umkehren([], []).
umkehren([K|R], L) :- umkehren(R, U), mit_letztem_element(U, K, L).
vorletztes_element([E1, E2], E1).
vorletztes_element([K1,K2|R], E) :- vorletztes_element([K2|R], E).
zweites_element([E1, E2|R], E2).

teilliste_bis_element([], Element, []).
teilliste_bis_element([K|R], Element, [Element]) :-
  K = Element.
teilliste_bis_element([K|R], Element, [K|Teilliste]) :-
  K \== Element,
  element(Element, R),
  teilliste_bis_element(R, Element, Teilliste).
teilliste_bis_element([K|R], Element, []) :-
  K \== Element,
  not(element(Element, R)).

teilliste_von_element_bis_element(L, Anfang, Ende, []) :- not(element(Anfang, L)).
teilliste_von_element_bis_element(L, Anfang, Ende, []) :- element(Anfang, L), not(element(Ende, L)).
teilliste_von_element_bis_element([K|R], Anfang, Ende, [K|Teilliste])  :-
  element(Anfang, [K|R]), element(Ende, [K|R]),
  K = Anfang,
  element(Ende, R),
  teilliste_bis_element(R, Ende, Teilliste).
teilliste_von_element_bis_element([K|R], Anfang, Ende, [K])  :-
  element(Anfang, [K|R]), element(Ende, [K|R]),
  K = Anfang,
  not(element(Ende, R)).
teilliste_von_element_bis_element([K|R], Anfang, Ende, Teilliste)  :-
  element(Anfang, [K|R]), element(Ende, [K|R]),
  K \== Anfang,
  element(Anfang, R),
  teilliste_von_element_bis_element(R, Anfang, Ende, Teilliste).

% Flussfahrt
muendet_in(Fluss1, Fluss2, Stadt) :-
  staedte_am_fluss(Fluss1, ListeStaedteFluss1),
  staedte_am_fluss(Fluss2, ListeStaedteFluss2),
  letztes_element(ListeStaedteFluss1, Stadt),
  element(Stadt, ListeStaedteFluss2),
  Fluss1 \== Fluss2.

liegen_am_selben_fluss(StadtA, StadtB) :-
  staedte_am_fluss(Fluss, ListeStaedteFluss),
  element(StadtA, ListeStaedteFluss),
  element(StadtB, ListeStaedteFluss).

liegen_am_selben_fluss_flussabwaerts(StadtA, StadtB) :-
  staedte_am_fluss(Fluss, ListeStaedteFluss),
  element(StadtA, ListeStaedteFluss),
  element(StadtB, ListeStaedteFluss),
  StadtA \== StadtB,
  teilliste_von_element_bis_element(ListeStaedteFluss, StadtA, StadtB, Liste),
  Liste \== [].

liegen_flussabwaerts(StadtA, StadtB) :-
  liegen_am_selben_fluss_flussabwaerts(StadtA, StadtB).

liegen_flussabwaerts(StadtA, StadtB) :-
  liegt_am_fluss(StadtA, Fluss1),
  muendet_in(Fluss1, Fluss2, StadtC),
  liegen_am_selben_fluss_flussabwaerts(StadtA, StadtC),
  liegen_flussabwaerts(StadtC, StadtB).

liegen_flussaufwaerts(StadtA, StadtB) :-
  liegen_flussabwaerts(StadtB, StadtA).

liegen_flussabwaerts_flussaufwaerts(StadtA, StadtB, StadtC) :-
  not(liegen_flussabwaerts(StadtA, StadtB)),
  not(liegen_flussaufwaerts(StadtA, StadtB)),
  liegen_flussabwaerts(StadtA, StadtC),
  liegen_flussaufwaerts(StadtC, StadtB).

liegen_am_fluss(StadtA, StadtB, Fluss) :-
  staedte_am_fluss(Fluss, ListeStaedteFluss),
  element(StadtA, ListeStaedteFluss),
  element(StadtB, ListeStaedteFluss).

liegt_am_fluss(Stadt, Fluss) :-
  staedte_am_fluss(Fluss, ListeStaedteFluss),
  element(Stadt, ListeStaedteFluss).

fahrt_abwaerts_ueber_denselben_fluss(StadtA, StadtB, ListeStaedteAB) :-
  liegen_am_fluss(StadtA, StadtB, Fluss),
  staedte_am_fluss(Fluss, ListeStaedteFluss),
  teilliste_von_element_bis_element(ListeStaedteFluss, StadtA, StadtB, ListeStaedteAB).
alleStaedteAmFlussVonStadt(STADT, ABSTADTABWAERTS) :- staedte_am_fluss(FLUSS, STADTLISTEFLUSS),
element(STADT, STADTLISTEFLUSS),
letztes_element(STADTLISTEFLUSS, LETZTESTADT),
LETZTESTADT \== STADT,
teilliste_von_element_bis_element(STADTLISTEFLUSS, STADT, LETZTESTADT, ABSTADTABWAERTS),
not(alleStaedteAmFlussVonStadt(LETZTESTADT, STADTLISTE2)).

alleStaedteAmFlussVonStadt(STADT, STADTLISTE) :- staedte_am_fluss(FLUSS, STADTLISTEFLUSS),
element(STADT, STADTLISTEFLUSS),
letztes_element(STADTLISTEFLUSS, LETZTESTADT),
LETZTESTADT \== STADT,
teilliste_von_element_bis_element(STADTLISTEFLUSS, STADT, LETZTESTADT, ABSTADTABWAERTS),
ohne_letztes_element(ABSTADTABWAERTS, ABSTADTABWAERTS2),
alleStaedteAmFlussVonStadt(LETZTESTADT, STADTLISTE2),
zusammenfuegen(ABSTADTABWAERTS2, STADTLISTE2, STADTLISTE).

ohne_letztes_element([K], []).
ohne_letztes_element([K|R], [K|R2]) :- ohne_letztes_element(R, R2).

fahrt_abwaerts(STADT, STADT2, F) :- alleStaedteAmFlussVonStadt(STADT, STADTLISTE),teilliste_von_element_bis_element(STADTLISTE, STADT, STADT2, F).

fahrt_aufwaerts(STADT, STADT2, L) :- fahrt_abwaerts(STADT2, STADT, F), umkehren(F, L). 

fahrt(S1,S2,L) :- liegen_flussabwaerts(S1,S2), fahrt_abwaerts(S1,S2,L).
fahrt(S1,S2,L) :- liegen_flussaufwaerts(S1,S2), fahrt_aufwaerts(S1,S2,L).
fahrt(S1,S2,L) :- liegen_flussabwaerts_flussaufwaerts(S1,S2,SE),
fahrt_abwaerts(S1,SE,E1),
fahrt_aufwaerts(SE,S2,E2),
zusammenfuegen(E1,E2,L),

nurPositiv([K|R]) :- 0 < K, R==[].
nurPositiv([K|R]) :- 0 < K, nurPositiv(R).

allePostiven([],[]).
allePostiven([K|R],[K|R2]):- K>0,allePostiven(R,R2).
allePostiven([K|R],R2):- K=<0,allePostiven(R,R2).

alleNegativen([],[]).
alleNegativen([K|R],[K|R2]):- K<0,alleNegativen(R,R2).
alleNegativen([K|R],R2):- K>=0,alleNegativen(R,R2).

alleErgebnisse(L,P,N) :- allePostiven(L,P), alleNegativen(L,N).
