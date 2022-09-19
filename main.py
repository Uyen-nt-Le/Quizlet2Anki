# This program converts quizlet exports to a format suitable for Anki's basic card format.

# Instructions are on Github readMe file

def quizlet2anki():
    quizletfile = open('quizletexport.txt', 'r', encoding='utf-8')
    ankifile = open('ankiimport.txt', 'w', encoding='utf-8')
    ankiline = ""
    canAdd = False

    quizletlines = quizletfile.readlines()
    ankifile.write(quizletlines[0])
    quizletlines = quizletlines[1:]

    for quizletline in quizletlines:
        if canAdd and quizletline[0] == '#':
            ankifile.write(ankiline)
            ankiline = ""
        if quizletline[0] == '#':
            quizletline = quizletline[1:]
            ankiline = ankiline + quizletline
            canAdd = True
        else:
            canAdd = False
            ankiline = ankiline[:-1]
            ankiline = ankiline + "<br>" + quizletline
    ankifile.write(ankiline)


if __name__ == '__main__':
    print("Converting quizlet to anki...")
    quizlet2anki()
    print("...DONE!")

