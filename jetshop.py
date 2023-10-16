"""
Module for functions relating to jetshop
"""
import helpers as h
import math

# creates the dictionary objects and appends them to the list jetSL after splitting it at the ";"
# file == the file to be read and it is a jetshop file.
# Checks that the file is in correct format
# Corrects comma separated floats into point separated floats
# returns list of libraries with contents from txt file
def read(file, message=False):
    with open(file) as jetshop:
        row = 0
        errors = 0
        jetSL = []
        headers = []

        for line in jetshop:
            rowAttributes = []

            # Establish headers
            if row < 1 :
                try:
                    for line in jetshop:
                        headers = line.split(";")
                        for title in headers:
                            jetSL[row] {
                                title : title,
                            }
                except:
                    print("Could not split headers from file in first row.\n")
            else:
                try:
                    for i in range(len(rowAttributes)):
                        rowAttributes = line.split(";")
                        for title in headers:
                            jetSL[row] {
                                title : rowAttributes[i],
                            }
                except:
                    print("Failed to read Row " + str(row))
                    print("Expected 4 values with 3 instances of ';'")
                    print("Content: " + line)
                    errors += 1
            row += 1
        
        if errors >= 1:
            print("Errors found in file: " + str(errors))
        elif message:
            print("No errors found in file.")
    return jetSL


# Goes through key artikelnummer in jetSL, adds unique values to uArtik and duplicate values to dArtik, men bara om artikeln inte är dold.
# Prints length of visible Duplicated Article
# Prints length of visible Unique Article
# Prints length of hidden Article
# Returns list of hidden articles, list of unique articles, list of duplicated articles
def duplicates(jetSL, message=False):
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
    if message:
        print(f"length of synliga dupliceradeArtiklar: {len(dArtik)}\nlength of synliga unikaArtiklar: {len(uArtik)}\nlength of dolda artiklar: {len(doldArtik)}")
    return doldArtik, uArtik, dArtik



###WRITES A TXT FILE WITH THE OUTPUT ARTICLE IDs###
# this is used for manually fixing the faulty artikelnummer in the website
# Uses argument "double" and "hidden" to determine which files should be written
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
                # Leftover from using this in tandem with visma to check for name mismatches
                if i in mismatch:
                    arg2 = "MISMATCH"
                """
                if arg1 or arg2:
                    # txt.write(f"{i} --{arg1}{arg2}--\n")
                    txt.write(f"{i}\n")
        print(str(doubles) + " Duplicate articles are found in dubblaArtiklar.txt")

    if argument == "hidden":
        with open("doldaArtiklar.txt", "w") as txt:
            for i in doldArtik:
                txt.write(f"{i}\n")
        print(str(len(doldArtik)) + " Hidden articles are found in doldaArtiklar.txt")

# Procenthöjning av produkter enligt boss
# float or int currentPrice
# float percentage, percentage to increase price as 1.10 for 10% increase
# return list new price of product in ink moms and new price in ex moms format
def pricing(currentPrice, percentage):
    tax = 1.25
    increasedPrice = currentPrice * percentage * tax
    # Prices up to this amount
    range1 = 199
    range1round = 1
    range1rounddir = "up"
    # Prices up to this amount
    range2 = 999
    range2round = 5
    range2rounddir = "nearest"
    # Then the rest of the prices
    range3round = 10
    range3rounddir = "nearest"

    if increasedPrice <= range1:
        newPrice = h.rounding(increasedPrice, range1rounddir, range1round)
    elif increasedPrice <= range2:
        newPrice = h.rounding(increasedPrice, range2rounddir, range2round)
    else:
        newPrice = h.rounding(increasedPrice, range3rounddir, range3round)

    return [newPrice, newPrice / tax]

def newPrices(articleList, percentage):
    masterString = ""
    try:
        percentage = float(percentage)
    except:
        print("invalid percentage value. Make sure you have a valid percentage")
        return
    
    for i in range(len(articleList)):
        for key, value in articleList[i].items():
            if key == "Pris exkl. moms" and value != key:
                masterString += str(pricing(float(value), percentage)[1]).replace(".", ",") + ";"
            else:
                masterString += value + ";"
        masterString = masterString[:-1] + "\n"
    
    with open("OUTPUT_RENAME_ME.txt", "w") as output:
        output.write(masterString)

# oldfile string for name of .txt file with pre-change prices
# newfile string for name of .txt file with post-change prices
# 
def logResults(oldFile, newFile, percentage):
    masterString = ""
    listDic = []
    perc = float(percentage)

    with open(oldFile, "r") as old, open(newFile, "r") as new, open("dokumentation.txt", "w") as documentation:
        # Add values of old file to list of dictionaries
        for line in old:
            artn, prodna, prisex, dold = line.split(";")
            listDic.append({
                "Artikelnummer" : artn.strip(),
                "Produktnamn" : prodna.strip(),
                "Före Pris exkl. moms" : prisex.strip(),
            })

        # Add values of new file to list of dictionaries
        row = 0
        for line in new:
            # Skipping headers
            if row == 0:
                listDic[row]["Efter Pris exkl. moms"] = "Efter Pris exkl. moms"
                listDic[row]["Prisskillnad kronor"] = "Prisskillnad kronor"
                listDic[row]["Prisskillnad procent"] = "Prisskillnad procent"
                row += 1
                continue

            artn, prodna, prisex, dold = line.split(";")
            priceDiff = float(prisex.replace(",", ".")) - float(listDic[row]["Före Pris exkl. moms"].replace(",", "."))
            if float(listDic[row]["Före Pris exkl. moms"].replace(",", ".")) > 0:
                priceDiffPercent = float(prisex.replace(",", ".")) / float(listDic[row]["Före Pris exkl. moms"].replace(",", "."))
            else:
                priceDiffPercent = 0

            listDic[row]["Efter Pris exkl. moms"] = prisex.strip()
            listDic[row]["Prisskillnad kronor"] = str(priceDiff).replace(".", ",")
            listDic[row]["Prisskillnad procent"] = str(priceDiffPercent).replace(".", ",")
            row += 1

        # Summarize the results in dokumentation.txt file
        for i in range(len(listDic)):
            for key, value in listDic[i].items():
                masterString += str(value) + ";"
            masterString = masterString[:-1] + "\n"
        documentation.write(masterString)
