import csv                                                          #Allows to get csv files#
file = "CFSpring2018Employers.csv"                                  #Gives the file a value#
f = open(file)                                                      #Basic open and close file reader in python#
reader = csv.reader(f)
f.close

                                                                    #I made a dictionary of the given information from the problem#

company_dict = {"0":"Company", "1":"Booth",
                "2":"Full-Time", "3":"Full-Time Visa Sponsor",
                "4":"Part-Time", "5":"Internship",
                "6":"Freshman", "7":"Sophomore",
                "8":"Junior", "9":"Senior",
                "10":"Post-Bacs", "11":"MS",
                "12":"PhD", "13":"Alumni",
               }
for numbers in company_dict:                                        #Helps organize the dictionary into a neat table#
    print("{}\t{}".format(numbers,company_dict[numbers]))           #I added \t so it adds a space between, you could easily just space as well#

strings = ("AIG","Baylor","CGG","Citi","EcconMobil","Flow-Cal Inc.",
           "Global SHop Solutions","Harris Count CTS","HCSS",
           "Hitachi Consulting", "HP Inc.","INT Inc.","JPMorgan Chase & Co",
           "Leidos","McKesson","MRE Consulting Ltd.","NetIQ","PROS",
           "San Jacinto College","SAS","Smartbridge","Sogeti USA",
            "Southwest Research Institute","The Reynolds and Reynolds Company",
           "UH Enterprise Systems","U.S. Marine Corps","ValuD Consuting LLC","Wipro")
newLines = []
with open("CFSpring2018Employers.csv", "rb") as csvfile:
    try:
        for line in csvfile:
            if any(s in line for s in strings):
                newLines.append(line)
    except:
        pass
theFile = open("CFSpring2018Employers-out.csv","w")
for line in newLines:
    theFile.write(line)
theFile.close()