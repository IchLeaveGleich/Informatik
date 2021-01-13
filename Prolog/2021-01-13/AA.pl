%NR 1) a) Der Voreil von Regeln liegt darin, dass sie  mit der bereits vorhandenen Wissen die Wissensbasis erweitern. Ein Beispiel waere die Unterteilung von Lebensmittel in den neuen Nutri-Score anhand ihrer Zutaten (viel gehaertete Fettsaeuren -> schlechter Score; hoher Bestandteil an Obst & Gemuese -> guter Score). Die Rekursion koennte in dem Beispiel verwendet werden um bereits bekannte Zutaten die in einem Produkt vorhanden sind einfliessen zu lassen anstatt den Score jedes mal neu errechnen zu muessen. z.B. Knoblauchbrot -> Knoblauch & Brot -> Knoblauch & Wasser + Mehl -> Score Knoblauch: 60 & Score Wasser: 100 + Score Mehl: 5
%NR 1) b) Vorallem die Syntax ist ein wesentlicher Unterschied, ausserdem gibt es nicht wie in der imerpativen Programmierung for while Schleifen und auch keine if Abfrage im typischen Sinn, jedoch kann man Regeln erzeugen welche das Pendant zu einer if Abfragen waaeren.

%NR 2) 

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


onkel(ONKEL, NEFFE) :- kind(NEFFE, ELTERNTEIL), kind(ELTERNTEIL, GROSSELTERNTEIL), kind(ONKEL, GROSSELTERNTEIL), maennlich(ONKEL), ONKEL\==ELTERNTEIL.
