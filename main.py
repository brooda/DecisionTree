from Tree import *
from Fuzziness import *

gepard = TreeNode("Gepard", Fuzziness.LEAF)
lew = TreeNode("Lew", Fuzziness.LEAF)
tygrysBengalski = TreeNode("TygrysBengalski", Fuzziness.LEAF)
kotPerski = TreeNode("KotPerski", Fuzziness.LEAF)
kotSyjamski = TreeNode("KotSyjamski", Fuzziness.LEAF)
dachowiec = TreeNode("Dachowiec", Fuzziness.LEAF)
rys = TreeNode("Ryś", Fuzziness.LEAF)
kangur = TreeNode("Kangur", Fuzziness.LEAF)
czlowiek = TreeNode("Człowiek", Fuzziness.LEAF)
szympans = TreeNode("Szympans", Fuzziness.LEAF)
swinia = TreeNode("Świnia", Fuzziness.LEAF)
kon = TreeNode("Koń", Fuzziness.LEAF)
slon = TreeNode("Słoń", Fuzziness.LEAF)
jelen = TreeNode("Jeleń", Fuzziness.LEAF)
sokol = TreeNode("Sokół", Fuzziness.LEAF)
orzel = TreeNode("Orzeł", Fuzziness.LEAF)
wrobel = TreeNode("Wróbel", Fuzziness.LEAF)
pingwinRownikowy = TreeNode("PingwinRownikowy", Fuzziness.LEAF)
pingwinCesarski = TreeNode("PingwinCesarski", Fuzziness.LEAF)
strus = TreeNode("Struś", Fuzziness.LEAF)
kura = TreeNode("Kura", Fuzziness.LEAF)
kiwi = TreeNode("Kiwi", Fuzziness.LEAF)
karp = TreeNode("Karp", Fuzziness.LEAF)
pstrag = TreeNode("Pstrag", Fuzziness.LEAF)
losos = TreeNode("Łosos", Fuzziness.LEAF)
mintaj = TreeNode("Mintaj", Fuzziness.LEAF)
rozdymka = TreeNode("Rozdymka", Fuzziness.LEAF)
zlotaRybka = TreeNode("ZlotaRybka", Fuzziness.LEAF)
zolw = TreeNode("Zolw", Fuzziness.LEAF)
kameleon = TreeNode("Kameleon", Fuzziness.LEAF)
waz = TreeNode("Waz", Fuzziness.LEAF)
pterozaur = TreeNode("Pterozaur", Fuzziness.LEAF)
triceratops = TreeNode("Triceratops", Fuzziness.LEAF)
salamandraPlamista = TreeNode("SalamandraPlamista", Fuzziness.LEAF)
zaba = TreeNode("Zaba", Fuzziness.LEAF)
biedronka = TreeNode("Biedronka", Fuzziness.LEAF)


ZmieniacKolor = TreeNode("Czy potrafi zmieniać kolor?", Fuzziness.NO)
ZmieniacKolor.insertLeft(kameleon)
ZmieniacKolor.insertRight(waz)

#FUZZY
BujneFutro = TreeNode("Czy ma bujne futro?", Fuzziness.LINEAR)
BujneFutro.insertLeft(kotPerski)
BujneFutro.insertRight(kotSyjamski)

#FUZZY
SkladaneDuzeJaja = TreeNode("Czy składane jaj są dużę?", Fuzziness.LINEAR)
SkladaneDuzeJaja.insertLeft(strus)
SkladaneDuzeJaja.insertRight(kura)

#FUZZY
Wigilia = TreeNode("Czy jest tradycyjną rybą jedzoną na Wigilię?", Fuzziness.LINEAR)
Wigilia.insertLeft(karp)
Wigilia.insertRight(pstrag)

#FUZZY
Droga = TreeNode("Czy ta ryba jest droga?", Fuzziness.LINEAR)
Droga.insertLeft(losos)
Droga.insertRight(mintaj)

#FUZZY
ZyjeDlugo = TreeNode("Czy żyje długo?", Fuzziness.LINEAR)
ZyjeDlugo.insertLeft(zolw)
ZyjeDlugo.insertRight(ZmieniacKolor)

CzyLatal = TreeNode("Czy latał?", Fuzziness.NO)
CzyLatal.insertLeft(pterozaur)
CzyLatal.insertRight(triceratops)

Ogon = TreeNode("Czy ma ogon?", Fuzziness.NO)
Ogon.insertLeft(salamandraPlamista)
Ogon.insertRight(zaba)

#FUZZY
BardzoSzybki = TreeNode("Czy jest bardzo szybki?", Fuzziness.LINEAR)
BardzoSzybki.insertLeft(gepard)
BardzoSzybki.insertRight(lew)

#FUZZY
UtrzymanieKoszutje = TreeNode("Czy utrzymanie dużo kosztuje?", Fuzziness.LINEAR)
UtrzymanieKoszutje.insertLeft(BujneFutro)
UtrzymanieKoszutje.insertRight(dachowiec)

#FUZZY
Programuje = TreeNode("Czy umie programować?", Fuzziness.LINEAR)
Programuje.insertLeft(czlowiek)
Programuje.insertRight(szympans)

Raciszki = TreeNode("Czy ma raciczki?", Fuzziness.NO)
Raciszki.insertLeft(swinia)
Raciszki.insertRight(kon)

Afryka = TreeNode("Czy mieszka w afryce?", Fuzziness.NO)
Afryka.insertLeft(slon)
Afryka.insertRight(jelen)

#FUZZY
Wzrok = TreeNode("Czy ma bardzo dobry wzrok?", Fuzziness.LINEAR)
Wzrok.insertLeft(sokol)
Wzrok.insertRight(orzel)

PolkulaPolnoca = TreeNode("Czy żyje na półkuli północnej?",Fuzziness.NO)
PolkulaPolnoca.insertLeft(pingwinRownikowy)
PolkulaPolnoca.insertRight(pingwinCesarski)

#FUZZY
JajaWKuchni = TreeNode("Czy składane jaja wykorzystywane są przez człowieka w kuchni?", Fuzziness.LINEAR)
JajaWKuchni.insertLeft(SkladaneDuzeJaja)
JajaWKuchni.insertRight(kiwi)

Slodkowodna = TreeNode("Czy jest rybą słodkowodną?", Fuzziness.NO)
Slodkowodna.insertLeft(Wigilia)
Slodkowodna.insertRight(Droga)

Kolce = TreeNode("Czy ma kolce?", Fuzziness.NO)
Kolce.insertLeft(rozdymka)
Kolce.insertRight(zlotaRybka)

ZyjeObecnie = TreeNode("Czy żyje obecnie?", Fuzziness.NO)
ZyjeObecnie.insertLeft(ZyjeDlugo)
ZyjeObecnie.insertRight(CzyLatal)

Plaz = TreeNode("Czy jest płazem?", Fuzziness.NO)
Plaz.insertLeft(Ogon)
Plaz.insertRight(biedronka)

Sawanna = TreeNode("Czy żyje na sawannie?", Fuzziness.NO)
Sawanna.insertLeft(BardzoSzybki)
Sawanna.insertRight(tygrysBengalski)

Dom = TreeNode("Czy żyje w domu u człowieka?", Fuzziness.NO)
Dom.insertLeft(UtrzymanieKoszutje)
Dom.insertRight(rys)

Worek = TreeNode("Czy ma worek na brzuchu?", Fuzziness.NO)
Worek.insertLeft(kangur)
Worek.insertRight(Programuje)

Gospodarskie = TreeNode("Czy jest zwierzęciem gospodarskim?", Fuzziness.NO)
Gospodarskie.insertLeft(Raciszki)
Gospodarskie.insertRight(Afryka)

#FUZZY
Duze = TreeNode("Czy jest duże?", Fuzziness.LINEAR)
Duze.insertLeft(Wzrok)
Duze.insertRight(wrobel)

ZimnyKlimat = TreeNode("Czy żyje w zimnym klimacie?", Fuzziness.NO)
ZimnyKlimat.insertLeft(PolkulaPolnoca)
ZimnyKlimat.insertRight(JajaWKuchni)

#FUZZY
UzywanaWKuchni = TreeNode("Czy jest używana w kuchni", Fuzziness.LINEAR)
UzywanaWKuchni.insertLeft(Slodkowodna)
UzywanaWKuchni.insertRight(Kolce)

Gad = TreeNode("Czy jest gadem?", Fuzziness.NO)
Gad.insertLeft(ZyjeObecnie)
Gad.insertRight(Plaz)

#FUZZY
DuzyKot = TreeNode("Czy jest dużym kotem?", Fuzziness.LINEAR)
DuzyKot.insertLeft(Sawanna)
DuzyKot.insertRight(Dom)

DwieKonczyny =TreeNode("Czy stoi na dwoch konczynach", Fuzziness.NO)
DwieKonczyny.insertLeft(Worek)
DwieKonczyny.insertRight(Gospodarskie)

Lata = TreeNode("Czy lata?", Fuzziness.NO)
Lata.insertLeft(Duze)
Lata.insertRight(ZimnyKlimat)

Ryba = TreeNode("Czy jest rybą?", Fuzziness.NO)
Ryba.insertLeft(UzywanaWKuchni)
Ryba.insertRight(Gad)

Kot = TreeNode("Czy jest kotem?", Fuzziness.NO)
Kot.insertLeft(DuzyKot)
Kot.insertRight(DwieKonczyny)

Ptak = TreeNode("Czy jest ptakiem?", Fuzziness.NO)
Ptak.insertLeft(Lata)
Ptak.insertRight(Ryba)

Ssak = TreeNode("Czy jest ssakiem?", Fuzziness.NO)
Ssak.insertLeft(Kot)
Ssak.insertRight(Ptak)