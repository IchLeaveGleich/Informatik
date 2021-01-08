% Fakten
vorspeise(kalt,oliven).
vorspeise(kalt,tzatziki).
vorspeise(kalt,peperoni).
vorspeise(warm,feta).
vorspeise(warm,pita).
fleisch(bifteki).
fleisch(gyros).
fleisch(souvlaki).
salat(thunfischsalat).
salat(bauernsalat).
gemuese(gemueseteller).
gemuese(spetsofai).
dessert(baklava).
dessert(chalvas).

hauptgericht(F,S,G) :- fleisch(F), salat(S), gemuese(G).
menue(V,F,S,G,D) :- vorspeise(V), hauptgericht(F, S, G), dessert(D).
