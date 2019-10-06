import json
from pprint import pprint

noneGradeIndex = 6

# Function that parses and stores the kanjis found in the kanji database
def parseKanjiDatabase():
    # Open the file and get the contents
    with open('full_kanji_db.json') as json_data:
        kanjiList = json.load(json_data)
    # List to store the simplified version of the Kanjis
    simplifiedKanjiList = [[], [], [], [], [], [], []]
    # Loop though the kanjis result and save each file into a separate JSON file
    if kanjiList is not None:
        for index, kanji in enumerate(kanjiList):
            kanjiCharacter = kanji['kanji']['character']
            print('Parsing through the Kanji: ' + kanjiCharacter + ' - Index: ' + str(index))
            # Creating a simplifiedKanji object to store the most important elements of the Kanji
            simplifiedKanji = {}
            simplifiedKanji['character'] = kanjiCharacter
            simplifiedKanji['meaning'] = kanji['kanji']['meaning']['english']
            simplifiedKanji['onyomi-romaji'] = kanji['kanji']['onyomi']['romaji']
            simplifiedKanji['onyomi-katakana'] = kanji['kanji']['onyomi']['katakana']
            simplifiedKanji['kunyomi-romaji'] = kanji['kanji']['kunyomi']['romaji']
            simplifiedKanji['kunyomi-hiragana'] = kanji['kanji']['kunyomi']['hiragana']
            simplifiedKanji['grade'] = str(kanji['references']['grade'])
            simplifiedKanji['index'] = str(index)

            if simplifiedKanji['grade'] == "None":
                simplifiedKanjiList[noneGradeIndex].append(simplifiedKanji)
            else:
                simplifiedKanjiList[int(simplifiedKanji['grade'])-1].append(simplifiedKanji)

            # Write the Kanji information in the proper path
            print('./Level' + str(simplifiedKanji['grade']) + '/KanjiInfo')
            writeToJSONFile('Level' + str(simplifiedKanji['grade']), str(index), kanji)
    print(simplifiedKanjiList)
    for index, kanjiList in enumerate(simplifiedKanjiList):
        # Write the Simplified Kanji List into a single file
        writeToJSONFile('./', "simplifiedKanjiList" + str(index), kanjiList)


# Function to save the kanji data to the proper path and filename
def writeToJSONFile(path, fileName, data):
    filePathNameExt = './' + path + '/' + fileName + '.json'
    print(filePathNameExt)
    with open(filePathNameExt, 'w') as fp:
        json.dump(data, fp)
        print("JSON file: " + filePathNameExt + " saved")

parseKanjiDatabase()
