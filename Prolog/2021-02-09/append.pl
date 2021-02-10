appendd([], E, [E]).
appendd([K|R], E, [K|N]) :- append(R, E, N).
