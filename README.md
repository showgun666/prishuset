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
Programmet ska kunna hantera olika mängd argument i dokumentet. Om det finns dölj artikel eller ej eller ej.
Produktkategorier eller ej.

Förmåga att sortera per kategori(Eller annat värde) så att endast vissa produkter uppdateras.
Sortering kan ske inklusive och/eller inklusive

En historikfil som går att använda för att ha koll på uppdateringar osv.

Förmåga att uppdatera priser med och utan gravyr separat.

Bättre support i menyn så att det går att se alla val man har gjort och vad som kommer göras