"""
Module for functions relating to jetshop
"""


# creates the dictionary objects and appends them to the list jetSL after splitting it at the ";"
# file == the file to be read and it is a jetshop file.
# Checks that the file is in correct format
# returns list of libraries with contents from txt file
def read(file, boolean=False):
    with open(file) as jetshop:
        currentline = 0
        errors = 0
        jetSL = []

        for line in jetshop:
            try:
                artn, prodna, prisex, dold = line.split(";")
                jetSL.append({
                    "Artikelnummer" : artn.strip(),
                    "Produktnamn" : prodna.strip(),
                    "Pris exkl. moms" : prisex.strip(),
                    "Dölj produkt" : dold.strip(),
                })
            except:
                print("Failed to read Row " + str(currentline))
                print("Expected 4 values with 3 instances of ';'")
                print("Content: " + line)
                errors += 1
            currentline += 1
        
        if currentline >= 1:
            print("Errors found in file: " + str(errors))
        elif boolean:
            print("No errors found in file.")
    return jetSL


# Goes through key artikelnummer in jetSL, adds unique values to uArtik and duplicate values to dArtik, men bara om artikeln inte är dold.
# Prints length of visible Duplicated Article
# Prints length of visible Unique Article
# Prints length of hidden Article
# Returns list of hidden articles, list of unique articles, list of duplicated articles
def duplicates(jetSL, boolean=False):
    doldArtik = []
    uArtik = []
    dArtik = []

    for i in range(len(jetSL)):
        #Skip the first row because it doesn't contain anything but headers, included for readability
        if i == 0:
            continue

        # Go through each line, if it has a value in key "Dölj produkt", save that value in memdold. if it doesn't, set the value in that key to whatever is in memdold.
        # I have no idea what this is or what it is supposed to do.
        try:
            memdold = int(jetSL[i]["Dölj produkt"])
        except:
            jetSL[i]["Dölj produkt"] = memdold

        # Go through each artikelnummer value, if it's Dölj Produkt value is 1 then stove it away in doldArtik. We don't want to see it.
        # If the artikelnummer value is not in the list of unique artikelnummer values, put it in there.
        # If the artikelnummer value is in unique artikelnummer value, we check if it is in the duplicate values. if not, we put it in there.
        # This way we know what values have duplicates and need manual fixing
        if jetSL[i]["Dölj produkt"] == "1":
            doldArtik.append(jetSL[i]["Artikelnummer"])
        elif jetSL[i]["Artikelnummer"] not in uArtik:
            uArtik.append(jetSL[i]["Artikelnummer"])
        elif jetSL[i]["Artikelnummer"] not in dArtik:
            dArtik.append(jetSL[i]["Artikelnummer"])

    # När den går igenom varje rad så kommer den ihåg det senaste värdet för "Dölj produkt"
    # Om den kommer till en rad som inte har ett värde i "Dölj produkt" så anger den värdet av det senaste "Dölj produkt" som den kommer ihåg.

    # prints the length of dArtik so that I can see how many unique duplicates there are.
    if boolean:
        print(f"length of synliga dupliceradeArtiklar: {len(dArtik)}\nlength of synliga unikaArtiklar: {len(uArtik)}\nlength of dolda artiklar: {len(doldArtik)}")
    return doldArtik, uArtik, dArtik



###WRITES A TXT FILE WITH THE OUTPUT ARTICLE IDs###
# this is used for manually fixing the faulty artikelnummer in the website
def write(doldArtik, uArtik, dArtik, argument):
    if argument == "double":
        doubles = 0
        with open("dubblaArtiklar.txt", "w") as txt:
            for i in uArtik:
                arg1 = ""
                arg2 = ""
                if i in dArtik:
                    arg1 = "DOUBLE"
                    doubles += 1
                """
                Leftover from using this in tandem with visma to check for name mismatches
                if i in mismatch:
                    arg2 = "MISMATCH"
                """
                if arg1 or arg2:
                    txt.write(f"{i} --{arg1}{arg2}--\n")
        print(str(doubles) + " Duplicate articles are found in dubblaArtiklar.txt")

    if argument == "hidden":
        with open("doldaArtiklar.txt", "w") as txt:
            for i in doldArtik:
                txt.write(f"{i}\n")
        print(str(len(doldArtik)) + " Hidden articles are found in doldaArtiklar.txt")
