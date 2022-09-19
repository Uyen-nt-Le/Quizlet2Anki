#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::cout << "Converting Quizlet file to Anki file...\n\n";

    std::ifstream quizletfile ("quizletexport.txt");
    std::ofstream ankifile ("ankiimport.txt");
    std::string quizline = "";
    std::string ankiline = "";
    bool canAdd = false;

    if (quizletfile.is_open()) {
        getline(quizletfile, ankiline);
        while(getline(quizletfile, quizline)) {
            if(canAdd && quizline[0] == '#') {
                ankifile << ankiline;
                ankiline = "";
            }
            if(quizline[0] == '#') {
                quizline.erase(quizline.begin());
                ankiline = ankiline + quizline;
                canAdd = true;
            } else {
                canAdd = false;
                ankiline.erase(ankiline.end()-1);
                ankiline = ankiline + "<br>" + quizline;
            }
        }
        ankifile << ankiline;
    }


    return 0;
}
