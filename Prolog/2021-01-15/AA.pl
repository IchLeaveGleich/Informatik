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

vorfahren(KIND, ELTERN) :- kind(KIND, ELTERN).
vorfahren(KIND, ELTERN) :- kind(KIND, GROSSELTERN), vorfahren(GROSSELTERN, ELTERN).
nachfahren(GROSSELTERN, ELTERN) :- vorfahren(ELTERN, GROSSELTERN).
weiblicherVorfahre(WEIBLICHERVORFAHRE, KIND) :- vorfahren(KIND, WEIBLICHERVORFAHRE), weiblich(WEIBLICHERVORFAHRE).
nachkommenVonOnkelTante(NACHWUCHS, KIND) :- kind(KIND, ELTERN), kind(ELTERN, GROSSELTERN), kind(ONKELTANTE, GROSSELTERN), nachfahren(ONKELTANTE, NACHWUCHS), ELTERN\==ONKELTANTE.
