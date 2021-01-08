maennlich(cronus).
maennlich(zeus).
maennlich(poseidon).
maennlich(hades).
maennlich(ares).
maennlich(hephaistos).
maennlich(percy).
maennlich(tyson).
maennlich(nico).
maennlich(malcolm).
maennlich(frank).
maennlich(jake).
maennlich(leo).
maennlich(charles).
maennlich(harley).
maennlich(chris).

weiblich(rhea).
weiblich(hera).
weiblich(demeter).
weiblich(athena).
weiblich(hazel).
weiblich(bianca).
weiblich(miranda).
weiblich(katie).
weiblich(annabeth).
weiblich(clarissa).
weiblich(thalia).

kind(hera,cronus).
kind(hera,rhea).
kind(zeus,cronus).
kind(zeus,rhea).
kind(poseidon,cronus).
kind(poseidon,rhea).
kind(hades,cronus).
kind(hades,rhea).
kind(demeter,cronus).
kind(demeter,rhea).
kind(athena,zeus).
kind(athena,hera).
kind(ares,zeus).
kind(ares,hera).
kind(hephaistos,zeus).
kind(hephaistos,hera).
kind(percy,poseidon).
kind(tyson,poseidon).
kind(nico,hades).
kind(hazel,hades).
kind(bianca,hades).
kind(miranda,demeter).
kind(katie,demeter).
kind(annabeth,athena).
kind(malcolm,athena).
kind(clarissa,ares).
kind(frank,ares).
kind(jake,hephaistos).
kind(leo,hephaistos).
kind(charles,hephaistos).
kind(harley,hephaistos).
kind(chris,hephaistos).
kind(thalia,zeus).

%Regeln
mutter(MUTTER,KIND) :- kind(KIND,MUTTER), weiblich(MUTTER).
enkel(ENKEL,OPA) :- kind(KIND,OPA), kind(ENKEL,KIND).
vater(VATER,X):- maennlich(VATER), kind(X,VATER).
bruder(BRUDER, X) :- maennlich(BRUDER), elternteil(ELTERNTEIL, BRUDER),elternteil(ELTERNTEIL, X), BRUDER \== X.
elternteil(ELTERNTEIL,X):- mutter(ELTERNTEIL, X); vater(ELTERNTEIL,X).
sohn(SOHN,X):-  kind(SOHN, X), maennlich(SOHN).
oma(OMA,X):- mutter(OMA, Y), kind(X,Y).
vorfahren(K,VORFAHR):- kind(K,VORFAHR).
vorfahren(K,VORFAHR):- kind(K, VORFAHR), vorfahren(ELTERN,VORFAHR).
nachfahren(E,NACHFAHR):- vorfahren(NACHFAHR, E).
