# Quizlet2Anki
###### Disclaimer
*This program is written to make Anki **basic** deck cards only.*

*It will convert export files from Quizlet and make it easier to import to Anki.*

*Images not included.*

*Written for a friend not for the public. Use at your own risk.*
## Instructions
Use PyCharm to run this program.

###### Exporting from Quizlet
1. Choose your flashcards on Quizlet.
2. Click on the 3 dots (...) and select **export**.
3. For "Between term and definition", choose custom and type (backtick): **`**
     - Or whichever symbol that most likely won't show up in the flashcards.
4. For "Betwen rows", choose custom and type: **\n#**
5. Copy and paste the text to the **quizletexport.txt** file.

###### PyCharm
6. Open PyCharm and make sure main.py is selected.
7. Click the run button.
8. **ankiimport.txt** will update when program runs successfully.

###### Importing to Anki
9. Open Anki.
10. Select **Import File**.
11. Select **ankiimport.txt**.
12. Import options: 
     - Type = Basic
     - Deck = **Select your deck**
     - Fields separated by: `
     - [x] Allow HTML in fields
13. Click **Import**.
14. Make sure the number of cards uploaded match what you're uploading.
     - Duplicated cards from other decks will upload/update/be ignored depending on the options you choose.
15. Done! :>


###### NOTES
C++ Version included. Compiled with g++ using WSL Ubuntu 20.04.

cpp file not meant for PyCharm.
