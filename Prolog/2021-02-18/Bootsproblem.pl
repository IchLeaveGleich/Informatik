% Fakten zu Städten an Flüssen

staedte_am_fluss(mosel, [metz, konz, trier, bernkastel, cochem, koblenz]).
staedte_am_fluss(saar, ['Saarbrücken', saarburg, konz]).
staedte_am_fluss(rhein, [basel, mannheim, mainz, koblenz, 'Köln', 'Düsseldorf']).
staedte_am_fluss(donau, [ulm, ingolstadt, regensburg, wien, budapest]).
staedte_am_fluss(main, [schweinfurt, 'Würzburg', offenbach, frankfurt, mainz]).

% Listenverarbeitung

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
teilliste_bis_element([K|R], Element, [Element]) :-K = Element.
teilliste_bis_element([K|R], Element, [K|Teilliste]) :-K \== Element,element(Element, R),teilliste_bis_element(R, Element, Teilliste).
teilliste_bis_element([K|R], Element, []) :-K \== Element,not(element(Element, R)).

teilliste_von_element_bis_element(L, Anfang, Ende, []) :- not(element(Anfang, L)).
teilliste_von_element_bis_element(L, Anfang, Ende, []) :- element(Anfang, L), not(element(Ende, L)).
teilliste_von_element_bis_element([K|R], Anfang, Ende, [K|Teilliste])  :- element(Anfang, [K|R]), element(Ende, [K|R]),K = Anfang,element(Ende, R),teilliste_bis_element(R, Ende, Teilliste).
teilliste_von_element_bis_element([K|R], Anfang, Ende, [K])  :- element(Anfang, [K|R]), element(Ende, [K|R]),K = Anfang,not(element(Ende, R)).
teilliste_von_element_bis_element([K|R], Anfang, Ende, Teilliste)  :- element(Anfang, [K|R]), element(Ende, [K|R]),K \== Anfang,element(Anfang, R),teilliste_von_element_bis_element(R, Anfang, Ende, Teilliste).

%Regeln

liegen_am_selben_fluss_flussabwaerts(S1, S2) :- S1\==S2, staedte_am_fluss(F, LS), element(S1, LS), teilliste_von_element_bis_element(LS, S1, S2, N), N\==[].


%$liegen_flussabwaerts(S1, S2) :- S1\==S2, staedte_am_fluss(F, SL1), element(S1, SL1), T1\==T2, umkehren(SL1, UkSL), SL1\==SL2, teilliste_bis_element(UkSL, S1, TNSL), umkehren(TNSL, T1), letztes_element(T1, LES1), staedte_am_fluss(F2, SL2), element(LES1, SL2), letztes_element(SL2, LES2), LES1\==LES2, teilliste_von_element_bis_element(SL2, LES1, LES2, T11), zusammenfuegen(T1, T2, AT), ohne_erstes(T11, T2), element(S2, AT).
liegen_flussabwaerts(S1, S2) :-liegen_am_selben_fluss_flussabwaerts(S1, S2).
liegen_flussabwaerts(S1, S2) :- not(liegen_am_selben_fluss_flussabwaerts(S1, S2)), staedte_am_fluss(F, SL1), letztes_element(SL1, LS), liegen_flussabwaerts(LS, S2).

liegen_flussauswaerts(S1, S2) :-liegen_am_selben_fluss_flussabwaerts(S2, S1).
liegen_flussaufwaerts(S1, S2) :- not(liegen_am_selben_fluss_flussabwaerts(S2, S1)), staedte_am_fluss(F, SL1), letztes_element(SL1, LS), liegen_flussabwaerts(LS, S1).

