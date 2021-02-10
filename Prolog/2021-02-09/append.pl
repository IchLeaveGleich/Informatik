append([], L, [L]).
append([K|R], L, [K|N]) :- appendListe(R, L, N).
