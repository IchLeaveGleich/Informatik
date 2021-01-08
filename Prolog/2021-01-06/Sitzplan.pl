% Autor:            KB.
% Datum: 18.05.2018

%% Fakten

% Zeilen:
% sitznachbar(links,rechts)

sitznachbar(percy,annabeth).
sitznachbar(annabeth,thalia).
sitznachbar(thalia,frank).
sitznachbar(hazel,miranda).
sitznachbar(miranda,malcolm).
sitznachbar(malcolm,harley).
sitznachbar(jake,bianca).
sitznachbar(bianca,katie).
sitznachbar(katie,clarissa).
sitznachbar(leo,charles).
sitznachbar(charles,nico).
sitznachbar(nico,chris).

% Spalten:
% hinter(hintermann, vorderfrau)

hinter(jake,leo).
hinter(hazel,jake).
hinter(percy,hazel).
hinter(bianca,charles).
hinter(miranda,bianca).
hinter(annabeth,miranda).
hinter(katie,nico).
hinter(malcolm,katie).
hinter(thalia,malcolm).
hinter(clarissa,chris).
hinter(harley,clarissa).
hinter(frank,harley).

% Reihen:

reihe(percy,vier).
reihe(annabeth,vier).
reihe(thalia,vier).
reihe(frank,vier).
reihe(hazel,drei).
reihe(miranda,drei).
reihe(malcolm,drei).
reihe(harley,drei).
reihe(jake,zwei).
reihe(bianca,zwei).
reihe(katie,zwei).
reihe(clarissa,zwei).
reihe(leo,eins).
reihe(charles,eins).
reihe(nico,eins).
reihe(chris,eins).


%Regeln:
nachbar(X,Y):- sitznachbar(X,Y); sitznachbar(Y,X).
selbe_Reihe(X,Y):- reihe(X,Z), reihe(Y,Z), Y\==X.
schraeg_dahinter(X,Y):- nachbar(X,N), hinter(Y,N).
alleHinter(X,Y):- hinter(Y,X).
alleHinter(X,Y):- hinter(Z,X), alleHinter(Z,Y).
