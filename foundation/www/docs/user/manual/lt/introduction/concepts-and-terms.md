<!-- add-breadcrumbs -->
# Sąvokos ir spibrėžimai

Prieš pradėdami diegti ERPNext, galite susipažinti su naudojama terminologija ir kai kuriomis pagrindinėmis ERPNext sąvokomis.

* * *

### Pagrindinės sąvokos

#### Įmonė

Organizacija, kuriai yra naudojama ERPNext sistema. Įdiegus ERPNext sistem1, ją galima naudoti ir kelioms įmonėms valdyti, kurių kiekviena yra atskiras
juridinis asmuo. Kiekvienos Įmonės apskaita bus atskira, bet jos gali
dalinkis įrašais apie klientus, tiekėjus ir prekes.

> Nustatymai > Įmonė

#### Klientas

Klientas gali būti asmuo ar organizacija. Galite sukurti kelis kontaktus ir adresus kiekvienam klientui.

> Pardavimai > Klientas

#### Tiekėjas

Prekių ar paslaugų tiekėjas. Jūsų telefono kompanija yra
Tiekėjas jums yra žaliavų tiekėjas. Vėlgi, tiekėjas gali būti
fizinis ar juridinis asmuo su keleta kontaktų ir adresų.

> Pirkimai > Tiekėjas

#### Produktas

Produktas, dalinis gaminys ar paslauga, kuri yra arba nupirkta, parduodama ar pagaminta ir yra unikaliai identifikuojama.

> Ištekliai > Produktas

#### Paskyra

Paskyra yra finansinių ir verslo sandorių apjungimas. Pavyzdžiui, "Kelionės išlaidos" yra paskyra "Klientas Zoė", "Tiekėjas Mae" yra paskyros. ERPNext Klientams ir Tiekėjams paskyras sukuria automatiškai.

> Paskyros > Paskyrų diagrama

#### Adresas

Adresas nurodo kliento ar tiekėjo vietos informaciją. Tai gali būti skirtingų vietų, tokių kaip pagrindinė buveinė, gamykla, sandėlys, parduotuvė ir kt.

> Pardavimai > Adresas

#### Kontaktas

Atskiri Kontaktai priklauso arba Klientui arba Tiekėjui arba niekam nepriklausomas. Kontaktas turi vardą ir kontaktinę informaciją, pvz. el. pašto adresą ir telefono numerį.

> Pardavimai > Kontaktai

#### Bendravimas

Sąrašas viso bendravimo su Kontaktu arba Galimu klientu. Visi el. laiškai, išsiųsti iš sistemos pridedama prie komunikacijos sąrašo.

> Palaikymas > Bendravimas

#### Kainoraštis

Kainoraštyje galima saugoti skirtingų tarifų planus. Tai vardas jūs pateikiate tam tikro sąrašo saugomų elementų kainų rinkinį.

> Pardavimai > Kainoraštis


> Pirkimai > Kainoraštis

* * *

### Apskaita

#### Fiskaliniai metai

Finansiniai metai arba apskaitos metai. Galite dirbti kelis kartus
Fiskaliniai metai tuo pačiu metu. Kiekvienas fiskalinių metų pradžios data ir pabaiga data ir sandoriai gali būti užregistruoti tik šiuo laikotarpiu. Kai jūs "uždarykite" a fiskaliniai metai, tai likučiai pervedami kaip "atidarymo" likučiai kitam fiskaliniai metai.

> Nustatymai > Įmonė > Fiskaliniai metai

#### Mokesčių centras

Mokesčių centras yra kaip sąskaita, tačiau vienintelis skirtumas yra tas, kad jisstruktūra atstovauja jūsų verslui labiau nei sąskaitos.
Pavyzdžiui, savo sąskaitų lentelėje galite atskirti savo išlaidas pagal jo rūšį
(t. y. kelionės, rinkodara ir kt.). Savo kortelių kainų centruose galite atskirti pagal produktų grupes ar verslo grupes (pvz., pardavimai internetu, mažmeninė prekyba ir kt.).

> Sąskaitos > sąnaudų centrų schema

#### žurnalo įrašas

Dokumentas, kuriame yra General Ledger (GL) įrašai ir Debeto ir
Šių įrašų kreditai yra tokie patys. ERPNext galite atnaujinti mokėjimus,
Grąžina ir tt, naudojant žurnalo įrašus.

> Sąskaitos > Žurnalo įrašas

#### Pardavimo sąskaita faktūra

Sąskaitą, siunčiamą Klientams pristatant daiktus (prekes ar paslaugas).

> Sąskaitos > Pardavimo sąskaitą faktūrą

#### Pirkimo sąskaita faktūra

Tiekėjo siunčiama sąskaita už daiktų (prekių ar paslaugų) pristatymą.

> Sąskaitos > Pirkimo sąskaita faktūra

#### Valiuta

ERPNext leidžia jums užsisakyti sandorius keliais valiutomis. Yra tik vienas
nors jūsų sąskaitų knygelė yra viena valiuta. Skelbdami savo sąskaitas faktūras
mokėjimai skirtingomis valiutomis, suma konvertuojama į numatytąsias
valiuta pagal nurodytą perskaičiavimo kursą.

> Nustatymai > Valiuta

* * *

### Pardavimas

#### Klientų grupė

Klientų grupavimas, dažniausiai pagal rinkos segmentą.

> Pardavimai > sąranka > klientų grupė

#### Vadovauti

Asmuo, kuris galėtų būti būsimas verslo šaltinis. Švinas gali generuoti
Galimybės. (nuo: "gali sukelti pardavimą").

> CRM> "Lead"

#### Galimybė

Galimas pardavimas. (nuo: "galimybė verslui").

> CRM> galimybė

#### Citata

Kliento prašymas sumokėti prekę ar paslaugą.

> Pardavimai > Citata

#### Pardavimo užsakymas

Pastaba, patvirtinanti prekių pristatymo sąlygas ir kainą (prekė arba prekė)
paslauga). Pristatymai, darbo užsakymai ir sąskaitos faktūros
remiantis pardavimo orderiais.

> Pardavimai > Pardavimų užsakymas

#### Teritorija

Geografinės vietovės klasifikacija pardavimų valdymui. Galite nustatyti tikslus
Teritorijoms ir kiekvienas pardavimas yra susijęs su teritorija.

> Pardavimai > Nustatymai > teritorija

#### Pardavimų partneris

Trečiosios šalies platintojas / prekybininkas / filialas / komisijos atstovas, kuris parduoda
kompanijos produktai paprastai yra komisiniai.

> Pardavimai > Nustatymai > pardavimo partneris

#### Pardavėjas

Kažkas, kuris stengiasi Klientui ir uždaro sandorius. Galite nustatyti tikslus
Parduodami asmenys ir pažymėkite juos sandoriuose.

> Pardavimai > Nustatymai > pardavimo atstovas

* * *

### Pirkimas

#### Pirkimo užsąkymas

Tiekėjui sudaryta sutartis nurodyti nurodytus elementus pristatyti nurodytomis sąlygomis kaina, kiekis, datos ir kitos sąlygos.

> Pirkimai > Pirkimo užsakymas

#### Medžiagos užklausa

Prašymas, kurį pateikia sistemos vartotojas arba automatiškai sugeneruotas pagal ERPNext dėl perrinkimo lygio arba numatomo kiekio gamybiniame plane, norint įsigyti rinkinį elementų.

> Pirkimai > Medžiagos užklausa

* * *

### Ištekliai (Inventory)

#### Sandėlis

Loginis sandėlis, kurio atsargos įrašomos.

> Ištekliai > Sandėlis

#### Sandėlyje įrašas

Medžiaga perduodama iš sandėlio, į sandėlį arba iš vieno sandėlio į
kitas.

> Ištekliai > Ištekliai Entry

#### Pristatymo pastaba

Elementų sąrašas su siuntos kiekiu. Pristatymo pastaba sumažins
daiktų sandėlis sandėlyje, iš kurios siunčiate. Pristatymo pastaba yra
dažniausiai pateikiamas prieš pardavimo užsakymą.

> Ištekliai > Pristatymo pastaba

#### Pirkimo kvitas

Pastaba, patvirtinanti, kad tiekėjas gavo tam tikrą elementų rinkinį,
greičiausiai prieš pirkimo užsakymą.

> Ištekliai > pirkimo kvitas

#### Serijos numeris

Unikalus numeris tam tikram vienetui.

> Ištekliai > Serijos numeris

#### Partija

Numeris, suteiktas konkretaus Prekės vienetų grupei, kurią galima įsigyti
arba gaminami grupėje.

> Ištekliai > partija

#### Sandėlio vadovo įrašas

Vieningą stalą visam materialiam judėjimui iš vieno sandėlio į kitą. Tai
yra lentelė, kuri yra atnaujinama, kai pateikiamas atsargų įrašas, pristatymo pastaba, pirkimas
Kvitas ir pardavimo sąskaita (POS).

#### Ištekliai Matching

Atnaujinkite keletą elementų iš skaičiuoklės (CSV) failo.

> Ištekliai > Ištekliai reconciliation

#### Kokybės tikrinimas

Pastaba, paruošta įrašyti tam tikrus Parametro parametrus gavimo metu
iš tiekėjo ar pristatymo klientui.

> Ištekliai > Kokybės tikrinimas

#### Prekių grupė

Pozicijos klasifikacija.

> Ištekliai > Nustatymai > Item Group

* * *

### Žmogiškųjų išteklių valdymas

#### Darbuotojas

Įrašo apie asmenį, dabr arba praeityje, įdarbinantą
įmonėje.

> Žmogiškieji ištekliai > Darbuotojai

#### Palikti paraišką

Patvirtinto arba atmesto prašymo atvykti įrašas.

> Žmogiškieji ištekliai > Palikite paraišką

#### Palikite tipą

Atostogų rūšis (pvz., Ligos palikimas, gimdymo atostogos ir kt.).

> Žmogiškieji ištekliai > Atostogos ir dalyvavimas> Atostogų tipas

#### Darbo užmokesčio įrašas

Įrankis, kuris padeda kurti darbuotojams kelis atlyginimus.

> Žmogiškieji ištekliai > Darbo užmokesčio įrašas

#### Algos lapelis

Darbuotojui skirtos mėnesinės algos įrašas.

> Žmogiškieji ištekliai > Atlyginimai

#### Darbo užmokesčio struktūra

Šablonas, identifikuojantis visus darbuotojo algos (uždarbio) komponentus,
mokesčių ir kitų socialinio draudimo atskaitymų.

> Žmogiškieji ištekliai > Darbo užmokestis ir darbo užmokestis> Darbo užmokesčio struktūra

#### Įvertinimas

Darbuotojo veiklos rezultatai per nustatytą laikotarpį, remiantis
tam tikri parametrai.

> Žmogiškieji ištekliai > Vertinimas

#### Vertinimo šablonas

Šablonas, kuriame įrašomi skirtingi Darbuotojų našumo ir parametrų parametrai
jų svarba tam tikram vaidmeniui.

> Žmogiškieji ištekliai > Darbuotojų Nustatymai > Vertinimo šablonas

#### Lankomumas

Įrašas, nurodantis darbuotojo buvimą ar nebuvimą konkrečioje dieną.

> Žmogiškieji ištekliai > Lankomumas

* * *

### Gamyba

#### Medžiagų sąvadas (BOM)

Operacijų ir elementų sąrašas su jų kiekiais, kurių reikia
pateikite kitą punktą. Medžiagų sąvadas (BOM) naudojamas planuojant pirkimus ir
atlikite produkto sąnaudas.

> Gamyba > BOM

#### Workstation

Vieta, kur vyksta BOM operacija. Naudinga apskaičiuoti
tiesioginės produkto kainos.

> Gamyba > darbo stotis

#### Darbų užsakymas

Dokumentas, signalizuojantis konkretaus gaminio gamybą (gamybą) su
nurodyti kiekiai.

> Gamyba > Darbo tvarka

#### Gamybos planavimo įrankis

Automatizuoto darbo užsakymų ir pirkimų prašymų kūrimo įrankis
apie atidarytus pardavimo užsakymus per tam tikrą laikotarpį.

> Gamyba > Gamybos planavimo įrankis

* * *

### Interneto svetainė

#### Dienoraščio įrašas

Pateikiamas trumpas straipsnis, sukurtas svetainės "Dienoraščio" skyriuje
iš ERPNext svetainės modulio. Dienoraštis yra trumpa "žiniatinklio žurnalo" forma.

> Svetainė > Dienoraščio įrašas

#### Tinklo puslapis

Tinklalapis su unikaliu URL (žiniatinklio adresu) iš svetainės, sukurtos iš
ERPNext.

> Svetainė > Tinklalapis

* * *

### Nustatymai / pritaikymas

#### Pasirinktinis laukas

Vartotojo apibrėžtas laukas formoje / lentelėje.

> Nustatymai > Pritaikyti ERPNext > Pasirinktinis laukas

#### Global Defaults

Tai skyrius, kuriame jūs nustatote numatytuosius įvairių parametrų parametrus
sistema.

> Nustatymai > duomenys> globalūs numatymai

#### Spausdinti antraštę

Pavadinimas, kurį galima nustatyti tik spausdinimui. Pavyzdžiui, jūs
norite išspausdinti pasiūlymą su antrašte "Pasiūlymas" arba "Pro forma sąskaita faktūra".

> Nustatymai > Brendis ir spausdinimas > Spausdinimo antraštės

#### Sąlygos ir sąlygos

Jūsų sutarties sąlygų tekstas.

> Pardavimai > Nustatymai > Sąlygos

#### Matavimo vienetas (MV)

Kaip kiekį išmatuojamas elementui. Pvz., "Kg", "No", "Paketas", "Paketas" ir tt.

> Ištekliai > Nustatymai > MV

{next}
