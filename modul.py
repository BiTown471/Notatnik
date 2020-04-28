############################ KRZYSZTOF NIEZABITOWSKI L3
import datetime

class Note:
    NR=0
    def __init__(self,text,tag,):#kontruktor klasy Note,parametry takst,etykieta
        Note.NR += 1
        self.text = text
        self.tag = tag
        self.data = datetime.date.today()
        self.ID=Note.NR


    def match(self,tmp):##jesli tekst lub etykieta zawiera ciag tmp zwraca True
                        ##przyjmuje jeden parametr tmp
        if tmp in self.text or tmp in self.tag:
            return True
        else:
            return False
        
    





class Notebook:

    def __init__(self):##konstruktor klasy Notebook
        self.notes = []

    def new_note(self,Note):##dodaje nowa notatke do listy, parametr to obiekt Note
        self.notes.append(Note)
        
    def modify_text(self,nr,newText):##modefikuje tekst obiktu,parametry ID,nowy tekst
        self.notes[nr-1].text = newText
        
    def modify_tag(self,nr,newTag):##modefikuje etykiete obiektu,parametry ID,nowytag
        self.notes[nr-1].tag = newTag
        
    def search(self,fraza):#szuka frazy w tekscie lub w etykiecie,parametr fraza
                           #zwraca liste notatek z szukana fraza
        tmp = []
        for i in range(len(self.notes)):
            if self.notes[i].match(fraza):
                tmp.append(self.notes[i])
        return tmp

