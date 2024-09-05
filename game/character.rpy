# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
init python:
    class Char:
        def __init__(self,str,kno,man,lok):
            self.str = str
            self.kno = kno
            self.man = man
            self.lok = lok
            self.status_effects = set()

        def  __str__(self):
            return f"{self.str} {self.kno} {self.man} {self.lok}"

    mainchar = Char(10,10,10,10)
    mainchar.status_effects.add("Surprised")
