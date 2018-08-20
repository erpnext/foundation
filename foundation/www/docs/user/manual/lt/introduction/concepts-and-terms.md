<!-- add-breadcrumbs -->
# Sąvokos ir apibrėžimai

Prieš pradėdami diegti ERPNext, galite susipažinti su naudojama terminologija ir kai kuriomis pagrindinėmis ERPNext sąvokomis.

* * *

### Pagrindinės sąvokos

#### Įmonė

Organizacija, kuriai yra skirta 5diegta ERPNext sistema. Įdiegus ERPNext sistemą, ją galima naudoti ir kelioms įmonėms valdyti, kurių kiekviena yra atskiras juridinis asmuo. Kiekvienos Įmonės apskaita bus atskira, bet jos gali dalintis įrašais apie klientus, tiekėjus ir prekes.

> Nustatymai > Įmonė

#### Klientas

Klientas gali būti asmuo arba organizacija. Galite sukurti kelis kontaktus ir adresus kiekvienam klientui.

> Pardavimai > Klientas

#### Tiekėjas

Prekių ar paslaugų tiekėjas. Pvz. jūsų telefono kompanija yra jūsų Tiekėjas. Vėlgi, tiekėjas gali būti fizinis ar juridinis asmuo turintis keletą kontaktų ir adresų.

> Pirkimai > Tiekėjas

#### Produktas

Produktas, dalinis gaminys ar paslauga, kuri yra arba perkama, parduodama ar gaminama ir yra unikaliai identifikuojama.

> Ištekliai > Produktas

#### Sąskaita

Sąskaita yra finansinių ir verslo sandorių apjungimas. Pavyzdžiui, "Kelionės išlaidos" yra sąskaita "Klientas Zoė", "Tiekėjas Mae" yra sąskaitos. ERPNext Klientams ir Tiekėjams sąskaitas sukuria automatiškai.

> Sąskaitos > Sąskaitų lentelė

#### Adresas

Adresas nurodo kliento ar tiekėjo vietos informaciją. Tai gali būti skirtingos vietos, tokios kaip pagrindinė biuras, gamykla, sandėlys, parduotuvė ir kt.

> Pardavimai > Adresas

#### Kontaktas

Kontaktai priklauso arba Klientui arba Tiekėjui arba niekam nepriklausomas. Kontaktas turi vardą ir kontaktinę informaciją, pvz. el. pašto adresą ir telefono numerį.

> Pardavimai > Kontaktai

#### Komunikacija

Sąrašas viso bendravimo su Kontaktu arba Potencialiu klientu. Visi elektroniniai laiškai, išsiųsti iš sistemos, pridedami prie komunikacijos sąrašo.

> Palaikymas > Komunikacija

#### Kainoraštis

Kainoraštyje galima saugoti skirtingų tarifų planus, kainas. Tai jūsų suteiktas pavadinimas tam tikrų produktų kainų sąrašui.

> Pardavimai > Kainoraštis

> Pirkimai > Kainoraštis

* * *

### Apskaita

#### Finansiniai metai

Finansiniai metai arba apskaitos metai. J8s galite operuoti keliais Finansianiais metais tuo pa2iu metu. Kiekvieni finansiniai metai turi pradžios ir pabaigos datą, visi įmonės veiksmai gali būti užregistruoti tik šiuo laikotarpiu. Kai jūs "uždarote" finansinius metus, tai likučiai perkeliami kaip "atidarymo" likučiai kitiems finansiniams metams.

> Nustatymai > Įmonė > Finansiniai metai

#### Sąnaudų centras

Sąnaudų centras yra kaip Sąskaita, tačiau skirtumas yra tas, kad jis skirtas labiau būtent jūsų verslui nei Sąskaitos. Pavyzdžiui, savo Sąskaitų lentelėje galite atskirti savo išlaidas pagal jų rūšį (t.y. kelionės, rinkodara ir kt.). Savo Sąnaudų centrų lentelėje galite jas atskirti pagal produktų grupes ar verslo grupes (pvz., pardavimai internetu, mažmeninė prekyba ir kt.).

> Sąskaitos > Sąnaudų centrų lentelė

#### Žurnalo įrašas

Dokumentas, kuriame yra Didžiosios knygos (DK) įrašai, suma Debetų ir Kreditų iš šių yrašų yra sutampa. Per ERPNext Žurnalo įrašus galite atnaujinti Mokėjimus, Grąžą ir t.t.

> Sąskaitos > Žurnalo įrašas

#### Pardavimo sąskaita-faktūra

Sąskaita-faktūra siunčiama Klientams tiekiant Produktus (prekes ar paslaugas).

> Sąskaitos > Pardavimo sąskaitą-faktūrą

#### Pirkimo sąskaita-faktūra

Tiekėjo siunčiama sąskaita-faktūra už Produktų (prekių ar paslaugų) pristatymą.

> Sąskaitos > Pirkimo sąskaita-faktūra

#### Valiuta

ERPNext leidžia jums atlikti sandorius keliomis valiutomis nepaisant to, kad jūsų Sąskaitų lentelei yra prisikirta tik viena valiuta. Skelbdami mokėjimus pagal sąskaitas-faktūras skirtingomis valiutomis, suma konvertuojama į numatytąsias valiuta pagal nurodytą perskaičiavimo kursą.

> Nustatymai > Valiuta

* * *

### Pardavimas

#### Klientų grupė

Klientų grupavimas, dažniausiai pagal rinkos segmentą.

> Pardavimai > sąranka > klientų grupė

#### Potencialus klientas

Asmuo, kuris galėtų tapti klientu. Potencialus klientas gali tapti Pardavimo galimybe..

> CRM > Potencialus klientas

#### Pardavimo galimybe

Galimas pardavimas.

> CRM > Pardavimo galimybe

#### Pardavimo pasiūlymas

Kliento prašymas apmokęstinti prekę ar paslaugą.

> Pardavimai > Pardavimo pasiūlymas

#### Pardavimo užsakymas

Produktų (prekių arba paslaugų) pristatymo sąlygų ir kainos patvirtinimas. Pristatymai, darbo užsakymai ir sąskaitos-faktūros atliekami remiantis Pardavimo užsakymais.

> Pardavimai > Pardavimų užsakymas

#### Teritorija

Geografinės vietovės klasifikacija pardavimų valdymui. Galite nustatyti tikslus Teritorijoms ir kiekvienas pardavimas yra susijęs su Teritorija.

> Pardavimai > Nustatymai > Teritorija

#### Pardavimo partneris

Trečiosios šalies platintojas / prekybininkas / filialas / tarpininkas (komisionierius), kuris parduoda kompanijos produktus dažniausiai už komisinius.

> Pardavimai > Nustatymai > Pardavimo partneris

#### Pardavėjas

Asmuo, kuris teikia pasiūlymus Klientui ir uždaro sandorius. Galite nustatyti tikslus
Pardavėjui ir žymėti juos sandoriuose.

> Pardavimai > Nustatymai > pardavimo atstovas

* * *

### Pirkimas

#### Pirkimo užsąkymas

Tiekėjui sudaryta sutartis, kuri nurodo tiekti nurodytus Produktus nurodytomis sąlygomis (kaina, kiekis, datos ir t.t.)

> Pirkimai > Pirkimo užsakymas

#### Medžiagų užklausa

Prašymas, kurį pateikia sistemos vartotojas arba automatiškai sugeneruotas ERPNext pagal pakartotinių užsakymų lygį arba numatomo kiekio Gamybos plane tam, kad įsigyti reikiamų Produktų.

> Pirkimai > Medžiagos užklausa

* * *

### Ištekliai

#### Sandėlis

Teorinio sandėlio likutis.

> Ištekliai > Sandėlis

#### Išteklių įrašas

Medžiaga perduodama iš vieno Sandėlio į kitą.

> Ištekliai > Išteklių įrašas

#### Tiekimo įrašas

Produktų sąrašas su siuntos kiekiu. Tiekimo įrašas sumažins Produkų skaičių sandėlyje, iš kurio atliekamas tiekimas. Tiekimo įrašas yra dažniausiai pateikiamas prieš Pardavimo užsakymą.

> Ištekliai > Tiekimo įrašas

#### Pirkimo kvitas

Įrašas, patvirtinantis, kad tiekėjas gavo tam tikrą Produktų rinkinį, dažniausiai, pagal Pirkimo užsakymą.

> Ištekliai > Pirkimo kvitas

#### Serijos numeris

Unikalus numeris tam tikram Produktui.

> Ištekliai > Serijos numeris

#### Partija

Numeris, suteiktas konkretaus Produkto vienetų partijai, kurią galima įsigyti arba gaminti grupėje.

> Ištekliai > Partija

#### Sandėlio apskaitos knygos įrašas

Bendra lentelė visam išteklių judėjimui iš vieno Sandėlio į kitą. Tai yra lentelė, kuri yra atnaujinama, kai pateikiamas Išteklių įrašas, Tiekimo įrašas, Pirkimo kvitas ir Pardavimo užsakymas.

#### Inventorizacija

Atnaujinkite kelis įrašus lentelinės skaičiuoklės (CSV) byloje vienu metu.

> Ištekliai > Inventorizacija






#### Kokybės tikrinimas

Pastaba, paruošta įrašyti tam tikrus Parametro parametrus gavimo metu iš tiekėjo ar pristatymo klientui.

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
