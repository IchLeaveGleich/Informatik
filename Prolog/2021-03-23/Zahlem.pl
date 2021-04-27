quadratzahl(Z) :- Z \== 0, X is sqrt(Z), Y is round(X), Q is Y^2, Q == Z.

exp(B, N, ZAHL) :- ZAHL is **(B, N).

