# prishuset
programs to help with administrative work at prishuset

Main file includes a command line interface.

Färdigt
Identifierat alla dolda artikelnummer
Identifierat alla dubbla artikelnummer
Prishöjning förberedd

Kommentarer på höjning:
Dokumentation på föreslagen prishöjning i excelformat
Se att billiga produkter har högre prispåslag, upp till 33% för mycket billiga produkter. Enligt samtal så ska dessa, säg jetonger, endast rundas till 50 öre
Många produkter får en prishöjning på så lite som 10% på grund av nedrundning, men detta är inom marginalerna

Namngivning av artikelnummer i jetshop attribut:
plåtar gav jag grundartikelnummer.storlek.(första 4 tecknen i typsnitt plus hur många linjer) Enligt INTECKNINGBLSILVER.50x20.vane5 för vanessa5l

produkter med eller utan gravyr har jag börjat namnge enligt följande
utan gravyrkostnad pbd109.1.grav0
För produkter där gravyr ingår är suffixet endast .grav

pbd109.1.grav10 innebär standardgravyrkostnad av 10
pbd109.1.grav15 innebär likaså att gravyrkostnaden är 15

för mängdrabatterade produkter så införde jag suffix .tak200 för upp till 200 av produkten.
Vid ingen övre gräns så har jag angett suffix .takmax som t.ex. vid 201 och uppåt osv.

Efter höjning så kan dessa värden fortfarande användas som basvärden vid höjningar, så att priserna blir relativa.
Om alla produkter har den typen av gravyrvärden så kan vi dynamiskt höja gravyrkostnaderna på hela jetshop och även separat från produkterna. I nuläget så kan vi endast höja alla priser samtidigt.

Korrigerat vissa oregelbundna priser, t.ex. black mountain mittenstorlek hade gravyrkostnad 30kr medan närliggande storlekar hade gravyrkostnad 40kr.

4941 artiklar har prisjusterats i dokumentationen

Manuell prisjustering
jetonger 3,50 inte 4,00
PG42208G och PG42206G pris ojusterat


VISMA
+46470 706 200
orgnr prishuset 556514-6056

artiklar lager prisinläsning
se dokumentation

https://www.vismaspcs.se/visma-support/visma-administration-2000/content/online-help/prisinlasning.htm

För Paketlösningar och inläsning i lager, prata med jetshop om integrationen med visma.

Planerat Jobb:

Lösning per kategori
Inklusive Kategori : Alla produkter som tillhör en viss kategori
Exklusive Kategori : Alla produkter som inte tillhör en viss kategori
Inklusive + Exklusive Kategori : Alla produkter som tillhör en viss kategori och inte tillhör en annan kategori

Prisuppdateringshistorik
Ett samlingsdokument där alla produkter som blivit uppdaterade läggs till rad för rad.

Produktkategorier och ID

TO DO
LÖST Programmet ska kunna hantera olika mängd argument i dokumentet. Om det finns dölj artikel eller ej eller ej.
LÖST Produktkategorier eller ej.

LÖST Förmåga att sortera per kategori(Eller annat värde) så att endast vissa produkter uppdateras.
PÅ GÅNG Sortering kan ske inklusive och/eller inklusive

LÖST MEN KRÄVER LITE MANUELL HANTERING En historikfil som går att använda för att ha koll på uppdateringar osv.

LÖST MEN HA LITE KOLL PÅ PAKETPRIS OCH MÄNGDRABATTER OSV Förmåga att uppdatera priser med och utan gravyr separat.

Bättre support i menyn så att det går att se alla val man har gjort och vad som kommer göras

Det som ger är att programmet läser artikelnummer ett efter ett.
Om artikelnumret är detsamma fram till första punkten så identifieras det som ett unikt artikelnummer och ses som grundpriset för produkten.
Sedan går den igenom andra artiklar som har samma artikelnummer men andra suffix efter punkten och justerar priset utan mellanskillnaden.
Om det finns gränsfall där detta skapar problem så kan det behöva justeras manuellt. Till exempel vid produkter med mängdrabatt, då påslaget för större antal inte ändras.
Pbd109 11:-, priset höjs enligt kalkyl
Pbd109.02.attr2 26:-, mellanskillnaden på 15:- plussas på på baspriset som höjts enligt första pbd109

	PTME08901
	PBD106
 	PBDI320601V8BLGE

Har lagt till produktkategori på en del produkter som saknade det som uppenbarligen skulle ha det.
Annars finns en lista på produkter som saknar produktkategori men som kanske ska tas bort från hemsidan.


-- Höjning 1 --
Medaljer, medaljband och medaljetuier

Kategorier:
Medaljband långa & korta
Medaljer
Medaljetuier
Medaljer Neutrala
Medaljer Präglade
Medaljer Specialtillverkade
Medaljaskar & etuier
Rea-medaljer

11% Höjning med rundning enligt ö.k.

OBS att produkter med 100 250 500 osv pack kan ha felaktiga priser enligt nuvarande modell. Höjs manuellt enligt första attributet. Markus har koll.
PG42208G och PG42206G pris ska också ickejusteras.

Importlogg
12:28:52 - Import av data slutförd med fel. Filnamn: Jetshop_Höjning_Medaljer__band_och_etuier_2023-11-18.csv
12:28:52 - Felrapport import: Slut
Fel nummer 5:  - Ett fel har inträffat vid import, försök igen. Om felet kvarstår kontakta support.
Fel nummer 4:  - Artikelnumret är inte unikt på attributet , Artikelnr: PTSME01801
Fel nummer 3:  - Artikelnumret är inte unikt på attributet , Artikelnr: PBD70.27
Fel nummer 2:  - Artikelnumret är inte unikt på attributet , Artikelnr: PBD70.02
Fel nummer 1:  - Artikelnumret är inte unikt på attributet , Artikelnr: PBD70.01
12:28:52 - Felrapport import: Start
12:28:35 - 
Startar import av csvfil: Jetshop_Höjning_Medaljer__band_och_etuier_2023-11-18.csv
12:28:04 - Fil sparad! Filnamn: Jetshop_Höjning_Medaljer__band_och_etuier_2023-11-18.csv


12:51:51 - Import av data slutförd. Filnamn: Medaljband_2023-11-20.csv
12:51:51 - Importerade/uppdaterade 42 produkt(er) och 47 attribut av 89 inläst(a) produkter/attribut från filen med 89 rad(er).
12:51:43 - 
Startar import av csvfil: Medaljband_2023-11-20.csv
12:51:32 - Fil sparad! Filnamn: Medaljband_2023-11-20.csv



Alla medaljband hade inte rätt ändelser så pris för 201+ är oförändrat sedan tidigare. Kommer behöva justeras manuellt artikelnummer och pris.

08:33:40 - Import av data slutförd med fel. Filnamn: Medaljer_2023-11-22.csv
08:33:40 - Felrapport import: Slut
Fel nummer 5:  - Ett fel har inträffat vid import, försök igen. Om felet kvarstår kontakta support.
Fel nummer 4:  - Artikelnumret är inte unikt på attributet , Artikelnr: PTSME01801
Fel nummer 3:  - Artikelnumret är inte unikt på attributet , Artikelnr: PBD70.27
Fel nummer 2:  - Artikelnumret är inte unikt på attributet , Artikelnr: PBD70.02
Fel nummer 1:  - Artikelnumret är inte unikt på attributet , Artikelnr: PBD70.01
08:33:40 - Felrapport import: Start
08:33:33 - 
Startar import av csvfil: Medaljer_2023-11-22.csv
08:33:19 - Fil sparad! Filnamn: Medaljer_2023-11-22.csv

PBB66 hade helt annat artikelnummer från produkten före den och fick justeras manuellt.
PBV2GR medaljband gröns attribut har ett extra P i sig. PBVP2GR. Det gjorde att den inte uppdaterades som den skulle. manuellt justerat pris men ej artikelnummer.
PBV2RAIN har en extra 2:a på slutet i sina artikelattribut. PBV2RAIN2. Samma som ovan.
