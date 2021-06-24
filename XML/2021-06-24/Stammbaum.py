from xml.dom.minidom import *
from datetime import datetime

xmlQuelltext = """
<Stammbaum>
<Person Vorname="Joseph Wilhelm" Name="Peter" Geschlecht="m" Geboren="1926-12-02" Gestorben="1998-03" Geburtsort="Erfweiler" Sterbeort="Dahn" Index="1">
<Person Vorname="Franz Josef" Name="Peter" Geschlecht="m" Geboren="1900-01-06" Gestorben="1968" Geburtsort="Busenberg" Sterbeort="Busenberg" Index="2">
<Person Vorname="Franz Josef" Name="Peter" Geschlecht="m" Geboren="1877-05-17" Gestorben="?" Geburtsort="Busenberg" Sterbeort="Busenberg" Index="4">
<Person Vorname="Valentin" Name="Peter" Geschlecht="m" Geboren="1823-07-13" Gestorben="1898-01-22" Geburtsort="Busenberg" Sterbeort="Busenberg" Index="8">
<Person Vorname="Georg Lorenz" Name="Peter" Geschlecht="m" Geboren="1791-08-15" Gestorben="1869-10-16" Geburtsort="Busenberg" Sterbeort="Busenberg" Index="16"> </Person>
<Person Vorname="Katharina" Name="Sauer" Geschlecht="w" Geboren="1791" Gestorben="1832-11-13" Geburtsort="Busenberg" Sterbeort="Busenberg" Index="17"> </Person>
</Person>
<Person Vorname="Elisabetha" Name="Weis" Geschlecht="w" Geboren="1844-12-29" Gestorben="?" Geburtsort="Busenberg" Sterbeort="?" Index="9">
<Person Vorname="Johannes Adam" Name="Weis" Geschlecht="m" Geboren="1809-07-13" Gestorben="1885-02-01" Geburtsort="Busenberg" Sterbeort="Busenberg" Index="18"> </Person>
<Person Vorname="Jakobina" Name="Keller" Geschlecht="w" Geboren="1820-02-08" Gestorben="1874-11-15" Geburtsort="Busenberg" Sterbeort="Busenberg" Index="19"> </Person>
</Person>
</Person>
<Person Vorname="Karolina" Name="Burkhart" Geschlecht="w" Geboren="1873-04-09" Gestorben="?" Geburtsort="Bruchweiler-BÃ¤renbach" Sterbeort="?" Index="5">
<Person Vorname="Johannes Georg" Name="Burkhart" Geschlecht="m" Geboren="1835-10-16" Gestorben="v1899" Geburtsort="Bruchweiler-BÃ¤renbach" Sterbeort="Bruchweiler-BÃ¤renbach" Index="10">
<Person Vorname="Markus" Name="Burkhart" Geschlecht="m" Geboren="~1809" Gestorben="1859-12-04" Geburtsort="Bruchweiler-BÃ¤renbach" Sterbeort="Bruchweiler-BÃ¤renbach" Index="20"> </Person>
<Person Vorname="Elisabetha" Name="Lieber" Geschlecht="w" Geboren="1814-11-15" Gestorben="1875-11-23" Geburtsort="Bruchweiler-BÃ¤renbach" Sterbeort="Bruchweiler-BÃ¤renbach" Index="21"> </Person>
</Person>
<Person Vorname="Anna Maria" Name="Zwick" Geschlecht="w" Geboren="1839-09-05" Gestorben="v1899" Geburtsort="Bruchweiler-BÃ¤renbach" Sterbeort="?" Index="11"> </Person>
</Person>
</Person>
<Person Vorname="Magdalena" Name="Burkhard" Geschlecht="w" Geboren="1902-02-13" Gestorben="1963-11" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="3">
<Person Vorname="Georg" Name="Burkhard" Geschlecht="m" Geboren="1854-11-15" Gestorben="1937-01-01" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="6">
<Person Vorname="Franz Joseph" Name="Burkhard" Geschlecht="m" Geboren="1825-10-04" Gestorben="1892-07-24" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="12">
<Person Vorname="Lorenz" Name="Burkhart" Geschlecht="m" Geboren="1783-06-22" Gestorben="1850-07-21" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="24"> </Person>
<Person Vorname="Maria Magdalena" Name="Kuntz" Geschlecht="w" Geboren="1784-10-15" Gestorben="1847-07-26" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="25"> </Person>
</Person>
<Person Vorname="Barbara" Name="Bassimir" Geschlecht="w" Geboren="1830-11-18" Gestorben="1876-12-11" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="13">
<Person Vorname="Georg Michael" Name="Bassimir" Geschlecht="m" Geboren="1806-05-20" Gestorben="1870-01-27" Geburtsort="Annweiler am Trifels" Sterbeort="Erfweiler" Index="26"> </Person>
<Person Vorname="Katharina" Name="Keller" Geschlecht="w" Geboren="1807-08-11" Gestorben="1864-12-14" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="27"> </Person>
</Person>
</Person>
<Person Vorname="Maria Anna Katharina" Name="Fries" Geschlecht="w" Geboren="1873-04-24" Gestorben="1911-04-23" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="7">
<Person Vorname="Adam" Name="Fries" Geschlecht="m" Geboren="1830-09-07" Gestorben="1919-11-04" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="14">
<Person Vorname="Georg Adam" Name="Fries" Geschlecht="m" Geboren="1797-12-01" Gestorben="1875-10-15" Geburtsort="Busenberg" Sterbeort="Erfweiler" Index="28"> </Person>
<Person Vorname="Appollonia" Name="Hentzel" Geschlecht="w" Geboren="1798-07-08" Gestorben="1857-11-20" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="29"> </Person>
</Person>
<Person Vorname="Katharina" Name="Erhard" Geschlecht="w" Geboren="1840-02-20" Gestorben="1903-05-23" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="15">
<Person Vorname="Johannes Adam" Name="Erhard" Geschlecht="m" Geboren="1808-08-05" Gestorben="1879-01-01" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="30"> </Person>
<Person Vorname="Margaretha" Name="Erhard" Geschlecht="w" Geboren="1810-07-09" Gestorben="1885-01-09" Geburtsort="Erfweiler" Sterbeort="Erfweiler" Index="31"> </Person>
</Person>
</Person>
</Person>
</Person>
</Stammbaum>"""

def printByIndex(doc, inputIndex):
    ausgabe = []
    dokument = parseString(doc)
    allePersonen = dokument.getElementsByTagName("Person")
    for person in allePersonen:
        index = person.getAttribute("Index")
        if int(index) == inputIndex:
            ausgabe.append(person.getAttribute("Vorname"))
            ausgabe.append(person.getAttribute("Name"))
            ausgabe.append(person.getAttribute("Geschlecht"))
            ausgabe.append(person.getAttribute("Geboren"))
            ausgabe.append(person.getAttribute("Gestorben"))
            ausgabe.append(person.getAttribute("Geburtsort"))
            ausgabe.append(person.getAttribute("Sterbeort"))
            ausgabe.append(person.getAttribute("Index"))
    return ausgabe


def printByName(doc, inputName):
    ausgabe = []
    dokument = parseString(doc)
    allePersonen = dokument.getElementsByTagName("Person")
    for person in allePersonen:
        name = person.getAttribute("Name")
        if str(name) == inputName:
            ausgabe.append(person.getAttribute("Vorname"))
            ausgabe.append(person.getAttribute("Name"))
            ausgabe.append(person.getAttribute("Geschlecht"))
            ausgabe.append(person.getAttribute("Geboren"))
            ausgabe.append(person.getAttribute("Gestorben"))
            ausgabe.append(person.getAttribute("Geburtsort"))
            ausgabe.append(person.getAttribute("Sterbeort"))
            ausgabe.append(person.getAttribute("Index"))
    return ausgabe

def durschnittsalterPersonenNachGeschlechter(doc):
    dokument = parseString(doc)
    allePersonen = dokument.getElementsByTagName("Person")
    for person in allePersonen:
        geschlecht = person.getAttribute("Geschlecht")
        geboren = person.getAttribute("Geboren")
        gestorben = person.getAttribute("Gestorben")
        gestorbenStriped = datetime.strptime(gestorben, "%Y-%m-%d")
        geborenStriped = datetime.strptime(geboren, "%Y-%m-%d")
        print(gestorbenStriped)
    
    
printByIndex(xmlQuelltext,5)
printByName(xmlQuelltext, "Peter")
durschnittsalterPersonenNachGeschlechter(xmlQuelltext)
