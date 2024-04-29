# kb 4 28 2024
# program to ingest steam .acf files
import os
class Acf:

    def __init__(self):
        self.acfList = []

    def openConfig(configPath):
        return

    def detectPackages(self, wordList, inBannedList):
        #to do: filter out PROTON packages and any in banList from the acfList
        return True


    def getAcfList(self, steamAppsPath, banList):
        # steamAppsPath
        # banList = list of packages referenced in acf files that definetely aren't games.
        #           some of these break steam when launched.

        #get list of Acfs from steam folder
        appList = os.listdir(steamAppsPath)

        # iterate over these, filter out any non-acf files and steam utilities, like proton.

        acfList = [] #init empty list for confirmed acfs

        for filename in appList:
             passPackageFlag = True
             if (filename.endswith('.acf')):
                #this is an acf file, keep processing:
                #todo: open file and detect any reference to any on banList
                acfPath = steamAppsPath + '/' + filename
                try:
                    file = open(acfPath, "r")
                except:
                    print ("ACF File read error! Could not read .acf file: ") + acfPath
                    return None

                #read lines as list
                acfLinesList = file.readlines()


                #look at each line
                for line in acfLinesList:
                    wordList = line.split() #tokenize to list
                    wordListFil = [] # init filtered list
                    for word in wordList:
                        if (word != "{") and (word != "}"):

                            wordFil = word.replace("\'","").replace("\"","") #strip quotes
                            wordListFil.append(wordFil)

                            #debug wordlist uncomment below
                            #print(wordListFil)

                            if passPackageFlag and self.detectPackages(wordListFil, banList):
                                #this adds the filename which has the id in the name
                                acfList.append(filename)
                                # only append acf once
                                passPackageFlag = False

        msg = (acfList, wordListFil)
        return msg

acf = Acf()
output = acf.getAcfList("~/.steam/steam/steamapps", [])[0]
print(output)
