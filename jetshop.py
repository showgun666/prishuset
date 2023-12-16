"""
Module for functions relating to jetshop
"""
import helpers as h
import math
import produktkategorier as pk

# creates the dictionary objects and appends them to the list jetSL after splitting it at the ";"
# file == the file to be read and it is a jetshop file.
# Checks that the file is in correct format
# Corrects comma separated floats into point separated floats
# returns list of libraries with contents from txt file
def read(file, exclude=[], exclusive=[], message=False):
    with open(file) as jetshop:
        # Row being read in the document
        row = 0
        # Errors found during reading of the file. For debugging.
        errors = 0
        # A list of dictionaries containing the product information where every index is one product
        jetSL = [{}]
        # Every header in the document
        headers = getHeaders(file)
        # Check for kategoryID
        kategoriID = False
        for index, value in enumerate(headers):
            if value == "KategoriID":
                kategoriID = True
                kategoriPosition = value 

        if kategoriID and exclude or exclusive:
            # Start Reading the file line by line
            for line in jetshop:
                # Add a dictionary item into jetSL
                jetSL.append({})

                exclusiveIDs = categoryStringToIDs(exclusive)
                excludeIDs = categoryStringToIDs(exclude)

                # For every line we save all the row attributes in this file. Same order as headers.
                categories, rowAttributes = extractCategoryIDs(headers, line.split(";"))
                # For every value in exclude check if there is a match, if there is a match, then move on
                for category in categories:
                    if category in excludeIDs: # If category is to be excluded, then break and move on to next line
                        break
                    elif category in exclusiveIDs and len(exclusiveIDs) > 0: # If categories are exclusive, then only select exclusive lines
                        try:
                            # For every index in headers
                            for index, _ in enumerate(headers):
                                # We insert a value into jetSL list on the row index with every value for the headers, also replace commas with dots.
                                jetSL[row][headers[index]] = rowAttributes[index].replace(',', '.')
                        except:
                            print("Failed to read category exclusive Row " + str(row))
                            print("Content: " + line)
                            errors += 1
                    elif len(exclusiveIDs) == 0:
                        try:
                            # For every index in headers
                            for index, _ in enumerate(headers):
                                # We insert a value into jetSL list on the row index with every value for the headers, also replace commas with dots.
                                jetSL[row][headers[index]] = rowAttributes[index].replace(',', '.')
                        except:
                            print("Failed to read category exclusive Row " + str(row))
                            print("Content: " + line)
                            errors += 1
                row += 1
        elif kategoriID and not exclusive:
            for line in jetshop:
                jetSL.append({})
                categories, rowAttributes = extractCategoryIDs(headers, line.split(";"))
                try:
                    # For every index in headers
                    for index, _ in enumerate(headers):
                        # We insert a value into jetSL list on the row index with every value for the headers, also replace commas with dots.
                        jetSL[row][headers[index]] = rowAttributes[index].replace(',', '.')
                except:
                    print("Failed to read category Row " + str(row))
                    print("Content: " + line)
                    errors += 1
                row += 1
        else:
            # Start Reading the file line by line
            for line in jetshop:
                # Add a dictionary item into jetSL
                jetSL.append({})
                # For every line we save all the row attributes in this file. Same order as headers.
                rowAttributes = line.split(";")
                try:
                    # For every index in headers
                    for index, _ in enumerate(headers):
                        # We insert a value into jetSL list on the row index with every value for the headers, also replace commas with dots.
                        jetSL[row][headers[index]] = rowAttributes[index].replace(',', '.')
                except:
                    print("Failed to read Row " + str(row))
                    print("Content: " + line)
                    errors += 1
                row += 1

        if errors >= 1:
            print("Errors found in file: " + str(errors))
        elif message:
            print("No errors found in file.")
    # Remove empty dictionaries.
    i = len(jetSL) - 1
    while i > -1:
        if not bool(jetSL[i]):
            jetSL.pop(i)
        i -= 1
    return jetSL


# Goes through key artikelnummer in jetSL, adds unique values to uArtik and duplicate values to dArtik, men bara om artikeln inte är dold.
# Prints length of visible Duplicated Article
# Prints length of visible Unique Article
# Prints length of hidden Article
# Returns list of hidden articles, list of unique articles, list of duplicated articles
def duplicates(jetSL, exclude=[], exclusive=[], message=False):
    doldArtik = []
    uArtik = []
    dArtik = []

    for i in range(len(jetSL)):
        #Skip the first row because it doesn't contain anything but headers, included for readability
        if i == 0:
            continue

        # Go through each line, if it has a value in key "Dölj produkt", save that value in memdold. if it doesn't, set the value in that key to 0.
        # I have no idea what this is or what it is supposed to do.
        try:
            memdold = int(jetSL[i]["Dölj produkt"])
        except:
            jetSL[i]["Dölj produkt"] = 0

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
def write(doldArtik, uArtik, dArtik, argument, exclude=[], exclusive=[]):
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

    if percentage == 0:
        return [currentPrice * tax, currentPrice]

    return [newPrice, newPrice / tax]

def newPrices(articleList, percentage):
    masterString = ""
    try:
        percentage = float(percentage)
    except:
        print("invalid percentage value. Make sure you have a valid percentage")
        return
    for key in articleList[0].keys(): # Headers
        masterString += key + ";"
    masterString = masterString[:-1]

    try:
        for i in range(len(articleList)):
            if i == 0:
                continue
            for key, value in articleList[i].items():
                if key == "Pris exkl. moms" and value != key:
                    masterString += str(pricing(float(value), percentage)[1]).replace(".", ",") + ";"
                else:
                    masterString += value + ";"
            masterString = masterString[:-1]
    except:
        print("Error! Could not check key 'Pris exkl. moms' during pricing.\nExiting.")
        exit()
    with open("OUTPUT_RENAME_ME.txt", "w") as output:
        output.write(masterString)

# listdic list of dictionaries from pre .txt file with pre-change prices
# listdic list of dictionaries from post .txt file with post-change prices
# 
def logResults(listdic, newlistdic, percentage, exclude=[], exclusive=[]):
    masterString = ""
    listDic = []
    perc = float(percentage)

    # Add values of listdic to list of dictionaries
    for i in listdic:
        listDic.append({
            "Artikelnummer" : i["Artikelnummer"].strip(),
            "Produktnamn" : i["Produktnamn"].strip(),
            "Före Pris exkl. moms" : i["Pris exkl. moms"].strip(),
        })

    with open("dokumentation.txt", "w") as documentation:
        # Add values of new file to list of dictionaries
        row = 0
        for i in newlistdic:
            # Skipping headers
            if row == 0:
                listDic[row]["Efter Pris exkl. moms"] = "Efter Pris exkl. moms"
                listDic[row]["Prisskillnad kronor"] = "Prisskillnad kronor"
                listDic[row]["Prisskillnad procent"] = "Prisskillnad procent"
                row += 1
                continue
            prisex = i["Pris exkl. moms"].strip()
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

# file argument is txt file
# Returns list of categories in file
def getHeaders(file):
    with open(file, "r") as jetshop:
        # Every header in the document
        headers = []
        # Row being read in the document
        row = 0

        # Establish headers
        for line in jetshop:
            # Add a dictionary item into categories
            if row == 0:
                try:
                    headers = line.split(";")
                except:
                    print("Could not split headers from file in first row.\n")
            else:
                return headers
            row +=1

# returns selected categories
def selectCategories(productCategories):
    categories = []
    for key in productCategories:
        categories.append(key)

    selected = []

    while True:
        index = 0
        for i in categories:
            if i in selected:
                print(str(index) + ". " + str(i) + " SELECTED")
            else:
                print(str(index) + ". " + str(i))
            index += 1

        selection = input("Select a category by typing related number and pressing enter. \nWhen done, input 'done'\n")
        if selection == "done":
            print("Categories selected:")
            for i in selected:
                print(i)
            return selected
        else:
            selection = int(selection)

        if isinstance(selection, str):
            selection = int(selection)

        if categories[selection] in selected:
            print("Removing " + categories[selection] + " from list.\n")
            selected.remove(categories[selection])
        else:
            print("Adding " + categories[selection] + " to list.\n")
            selected.append(categories[selection])
        print(selected)

#   categoryIDs list of IDs
#   returns list of categories as strings
def categoryIDsToString(categoryIDs):
    categoryStrings = []

    for key, value in pk.produktkategorier:
        if value in categoryIDs:
            categoryStrings.append(key)

    return categoryStrings

# headers, list of header names as strings
# dataColumn == list of data per column relative to headers
# Returns list of only Category IDs as strings
# Returns popped list of data columns
def extractCategoryIDs(headers, dataColumn):
    popDataColumn = dataColumn
    for pos, value in enumerate(headers):
        if value == "KategoriID":
            katPos = pos
            break

    catIDs = []
    # If there are more indexes in headers than in the data column, then we have multiple category IDs
    while len(headers) < len(popDataColumn):
        catIDs.append(popDataColumn[katPos].replace('"', '')) # Add category IDs to the new list
        popDataColumn.pop(katPos) # Remove index in kategory ID position
    if len(headers) == len(popDataColumn): # If length is equal then there is either 1 category or 0 categories left
        catIDs.append(popDataColumn[katPos].replace('"', '')) # Add whatever value we have to new IDs
        IDstring = "\""
        for value in catIDs:
            IDstring += value + ";"
        if not catIDs:
            IDstring += "\""
        IDstring = IDstring[:-1] + "\""

        if "KategoriID" in IDstring:
            IDstring = IDstring.replace('"', '')

        popDataColumn[katPos] = IDstring
    return catIDs, popDataColumn

# Writes headers to output file
def initiateOutputFile(headers):
    with open("OUTPUT_RENAME_ME.txt", "w") as txt:
        masterString = ""
        for line in headers:
            masterString += line + ";"
        masterString = masterString[:-1]
        txt.write(masterString)

# Takes list of categories as string names
# Returns list of categories as string IDs
def categoryStringToIDs(categories):
    categoryIDs = []
    if categories and categories[0] == "KategoriID": # För första raden.
        return categories
    for category in categories:
        for key in pk.produktkategorier.keys():
            if category == key:
                categoryIDs.append(pk.produktkategorier[key])
    return categoryIDs

def priceUpdateOnlyBase(articleList, percentage, exclude, exclusive):
    masterString = ""
    masterProduct = ["string1", -1.0, False, False] # position 0 is article number, position 1 is price as a float, position 2 is a boolean representing exclusion, position 3 is a boolean representing exclusivity.
    currentProduct = [["string2", "string3"], -2.0, False, False] # position 0 Contains list of article number split by ".", position 1 is price as a float, position 2 is a boolean representing exclusion, position 3 is a boolean representing exclusivity.
    kategoriID = False
    excludedIDs = categoryStringToIDs(exclude)
    exclusiveIDs = categoryStringToIDs(exclusive)
    for index, value in enumerate(articleList[0]):
        if value == "KategoriID":
            kategoriID = True
            kategoriPosition = index 
    try:
        percentage = float(percentage)
    except:
        print("invalid percentage value. Make sure you have a valid percentage")
        return
    for key in articleList[0].keys(): # Headers
        masterString += key + ";"
    masterString = masterString[:-1]

    if kategoriID and excludedIDs or exclusiveIDs:
        # Skip all exclude articles
        # Include all exclusive articles if length is not 0

        for d in articleList:
            categories = d["KategoriID"].replace('"', '').split(";")
            currentProduct[0] = d["Artikelnummer"].split(".")

            # Set up a master article
            # If to exclude, then flag [2] True
            # If to exclusively include, then flag [3] True
            # Always flag [0] with article number if there is no match
            # Only flag [1] if there is no match and it is to be included
            masterLen = len(masterProduct[0])
            currentLen = len(currentProduct[0][0])
            shorterAttributeName = False
            if currentLen >= masterLen and currentProduct[0][0][:masterLen] in masterProduct[0]:
                shorterAttributeName = True

            if currentProduct[0][0] not in masterProduct[0] and not shorterAttributeName: # If the split article number is not in masterProduct article number then make new master product. We are on a new article.
                if excludedIDs:
                    for category in categories:
                        if category in excludedIDs:
                            masterProduct[2] = True
                            masterProduct[0] = currentProduct[0][0]
                            break
                        else:
                            masterProduct[2] = False
                if masterProduct[2]:
                    break

                if exclusiveIDs:
                    for category in categories:
                        if category in exclusiveIDs or category == "" and currentProduct[0][0][:-2] in masterProduct[0][:-2]:
                            masterProduct[3] = True
                            masterProduct[0] = currentProduct[0][0]
                            masterProduct[1] = float(d["Pris exkl. moms"]) # Price exkl. moms
                            break
                        else:
                            masterProduct[3] = False

                else:
                    masterProduct[3] = True
                    masterProduct[0] = currentProduct[0][0]
                    masterProduct[1] = float(d["Pris exkl. moms"]) # Price exkl. moms
            if masterProduct[3] and not masterProduct[2]:
                for key, value in d.items():
                    if key == "Pris exkl. moms" and value != key:
                        currentProduct[1] = float(d["Pris exkl. moms"]) # Price exkl. moms
                        priceDiff = currentProduct[1] - masterProduct[1]
                        floatPriceString = str(pricing(masterProduct[1], percentage)[1] + priceDiff) # Change price by pricing
                        floatPriceStringList = floatPriceString.split(".")

                        if len(floatPriceStringList[1]) > 3: # If the rounding becomes weird, we round and fix it
                            floatingPointInteger = round(int(floatPriceStringList[1]), -2)
                        else:
                            floatingPointInteger = int(floatPriceStringList[1])

                        priceString = floatPriceStringList[0] + "." + str(floatingPointInteger)
                        masterString += str(priceString).replace(".", ",") + ";" # Price of master product used for pricing.
                    else:
                        masterString += value + ";"
                masterString = masterString[:-1]
    with open("OUTPUT_RENAME_ME.txt", "w") as output:
        output.write(masterString)

# jetshoplist, list of dictionaries from jetshop data
# writes a list of all products that don't have a category
# returns void
def writeProductsWithoutCategories(jetshoplist):
    with open("ingaKategorier", "w") as file:
        for line in jetshoplist:
            if line["KategoriID"] == '""':
                file.write(line["Artikelnummer"] + " : " + line["KategoriID"] + "\n")

# Takes two files, the new log and an old log history file
# Writes all the new unique articles into the newArticles.txt file
# Writes all the unique articles from both files into the newHistoryLog.txt file
# NewArticles.txt file is to see what new articles need to be changed or added.
# newHistoryLog.txt file is to both have a history of all the changes as well as to be able to make sure we don't update the same product twice.
def historyLogNoDuplicates(newLog, oldLog):
    with open(newLog, 'r') as new, open(oldLog, 'r') as old, open('newArticles.txt', 'w') as newArticles, open('newHistoryLog.txt', 'w') as historyLog:
        oldList = []
        oldListArticles = []
        newList = []
        for line in old:
            oldList.append(line)
            oldListArticles.append(line.split(";")[0])
        for line in new:
            newList.append(line)

        input("HAVE YOU BACKED UP THE PREVIOUS LOG FILES???\n SPECIFICALLY newArticles.txt AND newHistoryLog.txt \nPRESS ENTER TO CONTINUE OR CTRL-D TO ABORT")
        for i in newList:
            if i.split(";")[0] not in oldListArticles:
                newArticles.write(i)
                oldList.append(i)
        for i in oldList:
            historyLog.write(i)
