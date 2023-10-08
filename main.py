import re
import jetshop as js

def pricing(jetshoplist, pricelist):
    # check if the article in jetshop exists in visma
    # check if the article in jetshop exists in the pricelist
    # check if the article in jetshop has a lower price than the price in pricelist
    #return price
    ...

def sameprice(jetshoplist, vismalist):
    # check if the article in jetshoplist exists in vismalist
    # check if the price is the same, lower or higher in jetshoplist compared to vismalist
    # if the price is the same, do nothing
    # if the price is lower in jetshoplist compared to vismalist, then ping that
    # if the price is higher in jetshoplist compared to vismalist, then ping that
    # actually, return a list of values,
    # [0] = true or false for same price or not,
    # [1] = true or false for if the price is higher or not and
    # [2] returns the price in jetshop and
    # [3] returns the price in visma
    ...

def commands():
    # a command machine that handles input and calls different functions depending on input
    ...

def main():
    #Visma list prepped
    vismaL = []
    #list to hold mismatches where the article number in jetshop doesn't exist in the article number list for visma
    mismatch = []
    #list to hold old jetshop
    oldJetSL = []

    # File to read
    jetshopfile = "./jetshop/jetshop.txt"

    while True:
        print("1) Read jetshop.txt and print errors")
        print("2) Check jetshop.txt for duplicate artikelnummer")
        print("3) Write files for hidden articles and duplicate articles")
        print("q) Quit program")

        choice = input("-->")

        if choice == "q":
            print("Exiting with default answer")
            break

        if choice == "1":
            # List of libraries from jetshop.txt to jetSL
            js.read(jetshopfile)

        if choice == "2":
            # Read file and check for duplicates
            js.duplicates(js.read(jetshopfile))

        if choice == "3":
            # Write
            jetshoplistlib = js.read(jetshopfile)

            js.write(js.duplicates(jetshoplistlib))
        
        input("Press enter to continue...")

"""
    # Creates the visma stuff
    with open("prislistavisma1.txt") as visma:
        for line in visma :
            vart, vprice = line.split(",")
            # Takes off the unwanted A at the beginning of almost every value in vismaL[i]["Artikelnummer"]
            if treff := re.search("^A", vart):
                vart = vart[1:]
            vismaL.append({
                "Artikelnummer" : vart.strip(),
                "Pris exkl. moms" : vprice.strip(),
            })
"""
    # Jag vill jämföra artikelnummer i visma med artikelnummer bland de unika artikelnumren i jetshop. Om ett artikelnummer i jetshop INTE finns i visma, så måste den korrigeras
    # Sedan vill jag jämföra priserna i visma med priserna i jetshop. Jag vill ha priset på allt som inte är exakt samma. Kan börja med allt som är billigare i visma än i jetshop.

    # Här ska vi kontrollera att allt som finns i uArtik också finns i visma. Om en artikel finns i uArtik men inte i visma så lägger vi till den i listan


    # Här skapas alltså en till lista med allt, men egentligen så vill jag ha en samlad lista. Den kanske vi kan få när vi skriver ut allt.


### Måste skära bort första A-et från artikelnumret på alla visma artikelnummer.

"""    for n in range(len(uArtik)):
        match = False
        for i in range(len(vismaL)):
            if uArtik[n] == vismaL[i]["Artikelnummer"]:
                match = True
        if not match:
            #Here we do not add mismatches if they are formatted in the way we want them to be.
            if attr := re.search("\.attr\d+$",uArtik[n]):
                continue
            if attr := re.search("\.strk\d+$",uArtik[n]):
                continue

            #Here we are just checking for bad suffixes
            #Here we are looking for articles that end in G\n*$
            if attr := re.search("[G]\d*$", uArtik[n]):
                mismatch.append(uArtik[n])
                continue
            #Here we are looking for articles that end in _\n+$
            if attr := re.search("_\d+$", uArtik[n]):
                mismatch.append(uArtik[n])
                continue
            #append the mismatch to the mismatch list
            #mismatch.append(uArtik[n])
"""
    # WHAT DO NU, ok så ::
    # VAD BEHÖVER JAG???
    # 1. vilka produkter som är dubletter i jetshop
    # 2. vilka produkter som finns i jetshop men inte finns i visma

    # HUR VILL JAG ATT DET SKA SE UT??? Allt ska vara i en fil.
    # om artikeln är unik och matchar visma så behöver den inte synas
    # om artikeln inte är unik ELLER inte matchar visma så måste den synas och säga vad det är för fel på den
    # Art.nr --MISMATCH--
    # Art.nr --DOUBLE--
    # Art.nr --MISMATCHDOUBLE--

    # Jag har då två listor, en lista med alla unika artikelnummer som inte finns i visma
    # samt en lista med alla duplicerade artikelnummer

    # Om jag itererar över alla unika artikelnummer i jetshop, alltså ALLA artikelnummer.
    # Med det så går jag igenom allt i mismatch listan och allt i dup listan, om det är en träff på antingen eller så printar vi, annars gör vi ingenting.

    # Senare kan jag lösa om priset i visma stämmer eller inte, nu jobbar vi i enbart jetshop

"""
So I kind of wanted to figure out what articles have been deleted, but I don't think that that will work because I've changed the names of pretty much
every article in the whole system. so I think I will leave this unfinished strip of code out.
    try:
        with open("oldjetshop.txt") as oldjetshop:
            for line in oldjetshop :
                artn, prodna, prisex, dold = line.split(";")
                oldJetSL.append({
                    "Artikelnummer" : artn.strip(),
                    "Produktnamn" : prodna.strip(),
                    "Pris exkl. moms" : prisex.strip(),
                    "Dölj produkt" : dold.strip(),
                })

        for i in range(len(oldJetSL)) :
            for j in range(len(jetSL)) :
                if oldJetSL[i]["Artikelnummer"] not in jetSL[j]["Artikelnummer"] :


    except:
        print("oldjetshop.txt file not found.")"""

    ### NU har vi en fil som ger en lista på alla felaktigt duplicerade artikelnummer på produkter som är synliga.


    #Kolla om dolda produkter måste korrigeras. Om inte så behöver programmet kolla om en produkt är dold eller inte för att sedan korrigera den.
    # Sedan så måste vi kontrollera att alla produkter som INTE ska vara dolda är synliga i butiken när redigeringar görs SAMT när integreringen görs.

    #VAD VI HAR JUST NU: Vi har en lista på alla duplicerade artikelnummer i hela jetshop. 1658 produkter. yikes.

    #DOLDA artiklar har värdet 1 i key "Dölj produkt"

    #VAD SKA GÖRAS?
    # För att kunna uppdatera artiklar med attribut så måste alla attributs artikelnummer vara unika

    # Vi måste kunna jämföra artikellistan i jetshop med den i visma.
    # Om en artikel i jetshop inte finns i visma så ska den lägga till den jetshopartikeln i en lista så att jag kan manuellt lägga till produkten i visma

    # Kontrollera att för varje artikelnummer så ska priset i visma == priset i jetshop, om inte så ska priset i visma = priset i jetshop

    # "Produkt som finns I Visma men ej i Jetshop, passivmarkera du, så att de som är aktiva i Visma också finns som aktiva i Jetshop."-Tom
    # Alltså, om en artikel ELLER ett paket i visma inte är aktiv i jetshop så ska den inaktiveras.
    # "Jag går senare igenom de passivmärkta och öppnar eventuella artiklar som ska in i Jetshop men saknas där nu."-Tom
    # Alltså, Tom kommer att gå igenom visma och öppna artiklar som stängts av misstag pga att de ej är aktiva i Jetshop.


    # NÄR VI skapar en CSV fil så måste den vara UTF-8 kodad. Se https://merchantportal.norce.io/artikel/exportera-produkter/ för information om hur export import fungerar.

if __name__ == "__main__":
    main()