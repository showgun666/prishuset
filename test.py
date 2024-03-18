import pytest
import helpers as h
import jetshop as j

def test_roundNearest():
    a = h.roundNearest(123.449) # 123
    b = h.roundNearest(123.453) # 124
    c = h.roundNearest(123.523) # 124
    d = h.roundNearest(123.193) # 123
    e = h.roundNearest(126.123) # 126
    f = h.roundNearest(126.123) # 126

    x = h.roundNearest(126.1) # 126
    y = h.roundNearest(126.5) # 126
    z = h.roundNearest(126.8) # 126

    a1 = h.roundNearest(126.0) # 126
    a2 = h.roundNearest(126) # 126

    ab = h.roundNearest(0.00) # 0

    assert a == 123 and b == 124 and c == 124 and d == 123 and e == 126 and x == 126 and y == 127 and z == 127 and a1 == 126 and a2 == 126 and ab == 0

def test_rounding():
    a = h.rounding(14, "nearest", 1) # 14
    b = h.rounding(14.1, "nearest", 1) # 14
    c = h.rounding(14.6, "nearest", 1) # 15

    ab = h.rounding(144, "nearest", 5) # 145
    ac = h.rounding(144.1, "nearest", 5) # 145
    ad = h.rounding(144.1, "down", 5) # 140
    ae = h.rounding(144.1, "up", 5) # 145
    af = h.rounding(8, "nearest", 5) # 10
    ah = h.rounding(142.6, "nearest", 5) # 145
    ai = h.rounding(144.1, "nearest", 50) # 150

    ba = h.rounding(999.7, "nearest", 5) # 1000
    bb = h.rounding(993, "nearest", 5) # 995
    bc = h.rounding(1004, "nearest", 10) # 1000
    bd = h.rounding(1005, "nearest", 10) # 1010
    be = h.rounding(1439.754, "nearest", 10) # 1440
    bf = h.rounding(123456789, "nearest", 10) # 123456790

    abb = h.rounding(0.00, "up", 1) # 0
    abc = h.rounding(0.00, "down", 1) # 0

    assert abc == 0 and abb == 0 and a == 14 and b == 14 and c == 15 and ab == 145 and ac == 145 and ad == 140 and ae == 145 and af == 10 and ah == 145 and ai == 150 and ba == 1000 and bb == 995 and bc == 1000 and bd == 1010 and be == 1440 and bf == 123456790

def test_pricing():
    a = j.pricing(10.4, 1.11)[0] # 15
    b = j.pricing(5, 1.11)[0] # 7
    c = j.pricing(1, 1.11)[0] # 2
    d = j.pricing(136.88, 1.11)[0] # 190
    e = j.pricing(190, 1.11)[0] # 190
    
    aa = j.pricing(255.55, 1.11)[0] # 355
    ab = j.pricing(574.4, 1.11)[0] # 795
    ac = j.pricing(999, 1.11)[0] # 1390
    ad = j.pricing(555.555, 1.11)[0] # 770
    ae = j.pricing(444.444, 1.11)[0] # 615

    bb = j.pricing(0.00, 1.11)[0] # 0

    assert bb == 0 and a == 15 and b == 7 and c == 2 and d == 190 and e == 265 and aa == 355 and ab == 795 and ac == 1390 and ad == 770 and ae == 615

def test_extractCatIDs():
    headers = ["Artikelnummer", "Produktnamn", "KategoriID", "MetaKeywords"]
    dataColumn1 = ["00000200", "Silverfärgad laserskylt som måttbeställes", "293", ""]
    dataColumn2 = ["530", "Pokal St Annes Claret", "227", "253", ""]
    dataColumn3 = ["ACV1-1", "", "", ""]
    dataColumn4 = ["PBD112B01.strk1", "Medalj Löpning 50mm", "187", "211", "245", ""]
    dataColumn5 = ['WINDSURFSILVER.attr1', '', '', '']

    test1 = j.extractCategoryIDs(headers, dataColumn1)
    test2 = j.extractCategoryIDs(headers, dataColumn2)
    test3 = j.extractCategoryIDs(headers, dataColumn3)
    test4 = j.extractCategoryIDs(headers, dataColumn4)
    test5 = j.extractCategoryIDs(headers, dataColumn5)

    assert test1[0] == ["293"] and test2[0] == ["227", "253"] and test3[0] == [""] and test4[0] == ["187", "211", "245"] and test5[0] == [""]

def test_categoryStringToIDs():
    categories1 = ["Friidrott, Löpning"]
    categories2 = ["Friidrott, Löpning", "Övrigt", "Medaljer Präglade"]

    test1 = j.categoryStringToIDs(categories1)
    test2 = j.categoryStringToIDs(categories2)

    assert test1 == ["187"] and test2 == ["187", "211", "245"]


### NEED TO ADD BETTER TESTS
