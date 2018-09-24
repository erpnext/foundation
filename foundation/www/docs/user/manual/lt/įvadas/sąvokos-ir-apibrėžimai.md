<!-- add-breadcrumbs -->
# Sąvokos ir apibrėžimai

Prieš pradėdami diegti ERPNext, galite susipažinti su naudojama terminologija ir kai kuriomis pagrindinėmis ERPNext sąvokomis.

* * *

### Pagrindinės sąvokos

#### Įmonė

Įmonė, kuriai yra skirta įdiegta ERPNext sistema. Įdiegus ERPNext sistemą, ją galima naudoti ir kelioms įmonėms valdyti, kurių kiekviena yra atskiras juridinis asmuo. Kiekviena Įmonės turės atskirą apskaitą, bet įmonės gali dalintis įrašais apie klientus, tiekėjus ir prekes.

> Nustatymai > Įmonė

#### Klientas

Klientas gali būti asmuo arba organizacija. Galite sukurti kelis kontaktus ir adresus kiekvienam klientui.

> Pardavimai > Klientas

#### Tiekėjas

Prekių ar paslaugų tiekėjas. Pvz. jūsų telefono kompanija yra jūsų Tiekėjas. Tiekėjas gali būti fizinis ar juridinis asmuo ir turėti keletą Kontaktų ir Adresų.

> Pirkimai > Tiekėjas

#### Daiktas

Daiktas - dalinis gaminys ar paslauga, kuri yra arba perkama, parduodama ar gaminama ir yra unikaliai identifikuojama.

> Ištekliai > Daiktas

#### Sąskaita

Sąskaita yra finansinių ir verslo sandorių apjungimas. Pavyzdžiui, "Kelionės išlaidos" yra sąskaita "Klientas Jolanta", "Tiekėjas Gediminas" yra sąskaitos. ERPNext Klientams ir Tiekėjams sąskaitas sukuria automatiškai.

> Sąskaitos > Sąskaitų lentelė

#### Adresas

Adresas nurodo kliento ar tiekėjo vietos informaciją. Tai gali būti skirtingos vietos, tokios kaip pagrindinis biuras, gamykla, sandėlys, parduotuvė ir kt.

> Pardavimai > Adresas

#### Kontaktas

Kontaktas gali būti nepriklausomas arba priklausyti Klientui arba Tiekėjui. Kontaktas turi vardą ir kontaktinę informaciją, pvz. el. pašto adresą ir telefono numerį.

> Pardavimai > Kontaktas

#### Komunikacija

Sąrašas viso bendravimo su Kontaktu arba Potencialiu klientu. Visi elektroniniai laiškai, išsiųsti iš sistemos, pridedami prie komunikacijos sąrašo.

> Palaikymas > Komunikacija

#### Kainoraštis

Kainoraštyje galima saugoti skirtingų tarifų planus, kainas. Tai jūsų suteiktas pavadinimas tam tikrų Daiktų kainų sąrašui.

> Pardavimai > Kainoraštis

> Pirkimai > Kainoraštis

* * *

### Apskaita

#### Finansiniai metai

Finansiniai metai arba apskaitos metai. J8s galite operuoti keliais Finansianiais metais tuo pa2iu metu. Kiekvieni finansiniai metai turi pradžios ir pabaigos datą, visi įmonės veiksmai gali būti užregistruoti tik šiuo laikotarpiu. Kai jūs "uždarote" finansinius metus, tai likučiai perkeliami kaip "atidarymo" likučiai kitiems finansiniams metams.

> Nustatymai > Įmonė > Finansiniai metai

#### Sąnaudų centras

Sąnaudų centras yra kaip Sąskaita, tačiau skirtumas yra tas, kad jis skirtas labiau būtent jūsų verslui nei Sąskaitos. Pavyzdžiui, savo Sąskaitų lentelėje galite atskirti savo išlaidas pagal jų rūšį (t.y. kelionės, rinkodara ir kt.). Savo Sąnaudų centrų lentelėje galite jas atskirti pagal daiktų grupes ar verslo grupes (pvz., pardavimai internetu, mažmeninė prekyba ir kt.).

> Sąskaitos > Sąnaudų centrų lentelė

#### Žurnalo įrašas

Dokumentas, kuriame yra Didžiosios knygos (DK) įrašai, suma Debetų ir Kreditų iš šių yrašų yra sutampa. Per ERPNext Žurnalo įrašus galite atnaujinti Mokėjimus, Grąžą ir t.t.

> Sąskaitos > Žurnalo įrašas

#### Pardavimo sąskaita-faktūra

Sąskaita-faktūra siunčiama Klientams tiekiant Daiktus (prekes ar paslaugas).

> Sąskaitos > Pardavimo sąskaitą-faktūrą

#### Pirkimo sąskaita-faktūra

Tiekėjo siunčiama sąskaita-faktūra už Daiktų (prekių ar paslaugų) pristatymą.

> Sąskaitos > Pirkimo sąskaita-faktūra

#### Valiuta

ERPNext leidžia jums atlikti sandorius keliomis valiutomis nepaisant to, kad jūsų Sąskaitų lentelei yra prisikirta tik viena valiuta. Skelbdami mokėjimus pagal sąskaitas-faktūras skirtingomis valiutomis, suma konvertuojama į numatytąsias valiuta pagal nurodytą perskaičiavimo kursą.

> Nustatymai > Valiuta

* * *

### Pardavimas

#### Klientų grupė

Klientų grupavimas, dažniausiai pagal rinkos segmentą.

> Pardavimai > Nustatymai > Klientų grupė

#### Potencialus klientas

Asmuo, kuris galėtų tapti klientu. Potencialus klientas gali tapti Pardavimo galimybe.

> CRM > Potencialus klientas

#### Pardavimo galimybe

Galimas pardavimas.

> CRM > Pardavimo galimybe

#### Apmokęstinimo pasiūlymas

Apmokęstinimo pasiūlymas pagal Kliento prašymą apmokęstinti prekę ar paslaugą.

> Pardavimai > Apmokęstinimo pasiūlymas

#### Pardavimo patvirtinimas

Daiktų (prekių arba paslaugų) pristatymo sąlygų ir kainos patvirtinimas. Pristatymai, darbo užsakymai ir sąskaitos-faktūros atliekami remiantis Pardavimo užsakymais.

> Pardavimai > Pardavimo patvirtinimas

#### Teritorija

Geografinės vietovės skirstymas pardavimų valdymui. Galite nustatyti tikslias Teritorijas ir kiekvieną pardavimą susieti su šia Teritorija.

> Pardavimai > Nustatymai > Teritorija

#### Pardavimo partneris

Trečiosios šalies platintojas / prekybininkas / filialas / tarpininkas (komisionierius), kuris parduoda kompanijos Daiktus, dažniausiai už komisinius.

> Pardavimai > Nustatymai > Pardavimo partneris

#### Pardavėjas

Asmuo, kuris teikia pasiūlymus Klientui ir uždaro sandorius. Galite nustatyti tikslus
Pardavėjui ir žymėti juos sandoriuose.

> Pardavimai > Nustatymai > Pardavėjas

* * *

### Pirkimas

#### Pirkimo užsąkymas

Tiekėjui sudaryta sutartis, kuri nurodo tiekti nurodytus Daiktus nurodytomis sąlygomis (kaina, kiekis, datos ir t.t.)

> Pirkimai > Pirkimo užsakymas

#### Medžiagų užklausa

Prašymas, kurį pateikia sistemos vartotojas arba automatiškai sugeneruotas ERPNext pagal pakartotinių užsakymų lygį arba numatomo kiekio Gamybos plane tam, kad įsigyti reikiamų Daiktų.

> Pirkimai > Medžiagų užklausa

* * *

### Ištekliai

#### Sandėlis

Teorinio sandėlio likutis.

> Ištekliai > Sandėlis

#### Išteklių įrašas

Medžiaga perduodama iš vieno Sandėlio į kitą.

> Ištekliai > Išteklių įrašas

#### Pristatymo pranešimas

Daiktų sąrašas su siuntos kiekiu. Pristatymo pranešimas sumažins Produkų skaičių sandėlyje, iš kurio atliekamas tiekimas. Pristatymo pranešimas yra dažniausiai pateikiamas prieš Pardavimo užsakymą.

> Ištekliai > Pristatymo pranešimas

#### Pirkimo kvitas

Įrašas, patvirtinantis, kad tiekėjas gavo tam tikrą Daiktų rinkinį, dažniausiai, pagal Pirkimo užsakymą.

> Ištekliai > Pirkimo kvitas

#### Serijos numeris

Unikalus numeris tam tikram Daiktui.

> Ištekliai > Serijos numeris

#### Partija

Numeris, suteiktas konkretaus Daikto vienetų partijai, kurią galima įsigyti arba gaminti grupėje.

> Ištekliai > Partija

#### Sandėlio apskaitos knygos įrašas

Bendra lentelė visam išteklių judėjimui iš vieno Sandėlio į kitą. Tai yra lentelė, kuri yra atnaujinama, kai pateikiamas Išteklių įrašas, Tiekimo įrašas, Pirkimo kvitas ir Pardavimo užsakymas.

#### Inventorizacija

Atnaujinkite kelis įrašus lentelinės skaičiuoklės (CSV) byloje vienu metu.

> Ištekliai > Inventorizacija

#### Kokybės kontrolė

Įrašas skirtas išsaugoti Daikto parametrus Gavimo iš Tiekėjo metu arba Pristatymo Klientui metu.

> Ištekliai > Kokybės kontrolė

#### Daiktų grupė

Daiktų klasifikavimas.

> Ištekliai > Nustatymai > Daiktų grupė

* * *

### Žmogiškųjų išteklių valdymas

#### Darbuotojas

Įrašas apie šiuo metu arba anskčiau įmonėje įdarbinantą asmenį.

> Žmogiškieji ištekliai > Darbuotojas

#### Atostogų prašymas

Patvirtintų arba atmestų atostogų prašymų sąrašas.

> Žmogiškieji ištekliai > Atostogų prašymas

#### Atostogų rūšis

Atostogų rūšis (pvz., Dėl ligos, gimdymo atostogos ir kt.).

> Žmogiškieji ištekliai > Atostogos ir lankomumas > Atostogų rūšis

#### Atlyginimo įrašas

Įrankis, kuris padeda formuoti įvairius darbuotojų atlyginimo lapelius.

> Žmogiškieji ištekliai > Atlyginimo įrašas

#### Atlyginimo lapelis

Darbuotojui skirtos mėnesinės algos įrašas.

> Žmogiškieji ištekliai > Atlyginimo lapelis

#### Darbo užmokesčio struktūra

Šablonas, nustatantis visus darbuotojo atlyignimo komponentus, mokesčius ir kitus, kaip pvz.  papildomą sveikatos draudimą.

> Žmogiškieji ištekliai > Darbo užmokestis > Darbo užmokesčio struktūra

#### Vertinimas

Darbuotojo veiklos rezultatų vertinimas per nustatytą laikotarpį, remiantis tam tikrais parametrais.

> Žmogiškieji ištekliai > Vertinimas

#### Vertinimo šablonas

Šablonas, kuriame įrašomi skirtingi Darbuotojų našumo parametrai ir jų snoris tam tikram pareigai.

> Žmogiškieji ištekliai > Darbuotojo nustatymai > Vertinimo šablonas

#### Lankomumas

Įrašas, nurodantis darbuotojo buvimą ar nebuvimą konkrečią dieną.

> Žmogiškieji ištekliai > Lankomumas

* * *

### Gamyba

#### Komplektavimo specifikacija

Operacijų ir Daiktų sąrašas su jų kiekiais, kurių reikia kuriant kitą Daiktą. Komplektavimo specifikacija naudojama planuojant pirkimus ir vertinti gaminamo Daikto sąnaudas.

> Gamyba > Komplektavimo specifikacija

#### Darbo stotis

Vieta, kur vykdoma gamyba pagal Komplektavimo specifikacija. Padeda apskaičiuoti tiesioginęs Daikto sąnaudas.

> Gamyba > Darbo stotis

#### Darbo užsakymas

Dokumentas, signalizuojantis konkretaus gaminio gamybos paleidimą pagal nurodytą kiekį.

> Gamyba > Darbo užsakymas

#### Gamybos planavimo įrankis

Automatizuoto įrankis sukūriantis Darbų užsakymą ir Pirkimų prašymus pagal Aktyvius pardavimo užsakymus per tam tikrą laikotarpį.

> Gamyba > Gamybos planavimo įrankis

* * *

### Svetainė

#### Tinklaraščio įrašas

Pateikiamas trumpas straipsnis, sukurtas ERPNext svetainės "Tiklaraščio" modulio skyriuje. Dienoraštis yra trumpa "interneto žurnalo" forma.

> Svetainė > Tinklaraščio įrašas

#### Tinklapis

Tinklalapis su unikaliu URL (interneto adresu), sukurtos ERPNext.

> Svetainė > Tinklalapis

* * *

### Nustatymai / pakeitimai

#### Pasirinktinis laukas

Vartotojo apibrėžtas laukas formoje / lentelėje.

> Nustatymai > Keisti ERPNext > Pasirinktinis laukas

#### Globalios numatytos reikšmės

Skyrius, kuriame jūs nustatote numatytuosius įvairių parametrų reikšmes sistemoje.

> Nustatymai > Duomenys > Globalios numatytos reikšmės

#### Spausdinama antraštė

Antraštė, kurią galima nustatyti tik spausdinimui. Pavyzdžiui, jūs norite atspausdinti pasiūlymą su antrašte "Pasiūlymas" arba "Sąskaita-faktūra".

> Nustatymai > Ženklai ir spausdinimas > Spausdinama antraštė

#### Sąlygos

Jūsų sutarties sąlygų tekstas.

> Pardavimai > Nustatymai > Sąlygos

#### Matavimo vienetas

Kokiais vienetais matuojamas Daiktas. Pvz., "Kg", "No", "Paketas" ir tt.

> Ištekliai > Nustatymai > Matavimo vienetas

{next}
