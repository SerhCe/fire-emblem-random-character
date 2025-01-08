threehousescharlist = [
    ["Byleth (M)", "m"],
    ["Byleth (F)", "f"],
    ["Edelgard", "f"],
    ["Dimitri", "m"],
    ["Claude", "m"],
    ["Hubert", "m"],
    ["Ferdinand", "m"],
    ["Linhardt", "m"],
    ["Caspar", "m"],
    ["Dedue", "m"],
    ["Felix", "m"],
    ["Ashe", "m"],
    ["Sylvain", "m"],
    ["Lorenz", "m"],
    ["Raphael", "m"],
    ["Ignatz", "m"],
    ["Bernadetta", "f"],
    ["Dorothea", "f"],
    ["Petra", "f"],
    ["Mercedes", "f"],
    ["Annette", "f"],
    ["Ingrid", "f"],
    ["Lysithea", "f"],
    ["Marianne", "f"],
    ["Hilda", "f"],
    ["Leonie", "f"],
    ["Seteth", "m"],
    ["Hanneman", "m"],
    ["Gilbert", "m"],
    ["Alois", "m"],
    ["Cyril", "m"],
    ["Flayn", "f"],
    ["Manuela", "f"],
    ["Catherine", "f"],
    ["Shamir", "f"],
    ["Anna", "f"],
    ["Jeritza", "m"],
    ["Aelfric", "m"],
    ["Yuri", "m"],
    ["Balthus", "m"],
    ["Constance", "f"],
    ["Hapi", "f"],
    ["Sothis", "f"],
    ["Jeralt", "m"],
    ["Gatekeeper", "m"],
    ["Abysskeeper", "m"],
    ["Monica", "f"],
    ["Fleche", "f"],
    ["Arundel", "m"],
    ["Randolph", "m"],
    ["Metodey", "m"],
    ["Lonato", "m"],
    ["Miklan", "m"],
    ["Rodrigue", "m"],
    ["Acheron", "m"],
    ["Judith", "f"],
    ["Nader", "m"],
    ["Rhea", "f"],
    ["Flame Emperor", "m"],
    ["Kostas", "m"],
    ["Death Knight", "nb"],
    ["Thales", "m"],
    ["Solon", "m"],
    ["Kronya", "f"],
    ["Cornelia", "f"],
    ["Seiros", "f"],
    ["The Immaculate One", "nb"],
    ["Nemesis", "m"],
    ["Lambert", "m"],
    ["Sitri", "f"]
]


engagecharlist = [
    ["Alear (M)", "m"],
    ["Alear (F)", "f"],
    ["Vander", "m"],
    ["Clanne", "m"],
    ["Framme", "f"],
    ["Alfred", "m"],
    ["Boucheron", "m"],
    ["Louis", "m"],
    ["Jean", "m"],
    ["Céline", "f"],
    ["Etie", "f"],
    ["Chloé", "f"],
    ["Diamant", "m"],
    ["Alcryst", "m"],
    ["Amber", "m"],
    ["Jade", "f"],
    ["Citrinne", "f"],
    ["Lapis", "f"],
    ["Yunaka", "f"],
    ["Saphir", "f"],
    ["Zelkov", "m"],    
    ["Kagetsu", "m"],    
    ["Rosado", "m"],    
    ["Lindon", "m"],    
    ["Ivy", "f"],    
    ["Hortensia", "f"],    
    ["Goldmary", "f"],    
    ["Anna", "f"],    
    ["Fogado", "m"],    
    ["Merrin", "f"],    
    ["Timerra", "f"],    
    ["Panette", "f"],    
    ["Bunet", "m"],    
    ["Pandreo", "m"],    
    ["Seadall", "m"],    
    ["Mauvier", "m"],    
    ["Nel", "f"],    
    ["Rafal", "m"],    
    ["Zelestia", "f"],    
    ["Gregory", "m"],    
    ["Madeline", "f"],    
    ["Sommie", "nb"],
    ["Lumera", "f"],
    ["Ève", "f"],
    ["Morion", "m"],
    ["Seforia", "f"],
    ["Hyacinth", "m"],
    ["Zephia", "f"],
    ["Griss", "m"],
    ["Veyle", "f"],
    ["Sombron", "m"]
]

id = 861
outputstring = ""
for i in engagecharlist:
    id+=1
    if i[1] == "m":
        outputstring += str(id) 
        outputstring += "," 
        outputstring += i[0] 
        outputstring += "," 
        outputstring += "17,Engage,1,0\n" 
    if i[1] == "f":
        outputstring += str(id) 
        outputstring += "," 
        outputstring += i[0] 
        outputstring += "," 
        outputstring += "17,Engage,0,1\n" 
    if i[1] == "nb":
        outputstring += str(id) 
        outputstring += "," 
        outputstring += i[0] 
        outputstring += "," 
        outputstring += "17,Engage,1,1\n" 

print (outputstring)