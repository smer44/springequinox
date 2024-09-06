# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
init python:
    class CharSozial:
        def __init__(self,str,kno,man,lok):
            self.str = str
            self.kno = kno
            self.man = man
            self.lok = lok
            self.status_effects = set()

        def  __str__(self):
            return f"{self.str} {self.kno} {self.man} {self.lok}"

    class CharBattle:
        def __init__(self,name,str,dex,end,mstr,mdex,mend):
            self.name = name
            self.str = str
            self.dex = dex
            self.end = end
            self.mstr = mstr
            self.mdex = mdex
            self.mend = mend

            self.wrong_desigion = False


            self.updatestats()

            self.healfull()
            self.status_effects = set()

        def updatestats(self):
            self.maxhp = self.str * 5 + self.mstr * 5
            self.maxsta = self.end * 5
            self.maxcsta = self.dex * 5
            self.maxmana = self.mend * 5
            self.maxcmana = self.mdex * 5
            self.defe = self.str //2
            self.mdef = self.mstr//2
            self.cdef = self.defe
            self.cmdef = self.mdef


        def healfull(self):

            self.hp =self.maxhp
            self.sta = self.maxsta
            self.csta = self.maxcsta
            self.mana = self.maxmana
            self.cmana = self.maxcmana

            self.for_healthbar = ["hp","sta","csta","mana","cmana"]



        def defend(self, other):
            if self.sta < 10:
                self.wrong_desigion = True
                return
            self.wrong_desigion = False
            self.sta -= 10
            self.cdef = 2*self.defe

        def gain_pdamage(self,dmg):
            dmg = max(dmg - self.cdef,0)
            self.hp -= dmg
            self.cdef = self.defe










        def  __str__(self):
            return f"{self.str} {self.dex} {self.end} {self.mstr}"

    girl = CharBattle("girl",5,3,2,1,2,1)
    no_action = lambda : None


screen healthbar(mainchar):

    # Top Left: Character Stats
    frame:
        align (0.0, 0.0)
        hbox:
            vbox:
                spacing 25
                xmaximum 350
                text f"Health       : {mainchar.hp}/{mainchar.maxhp}" size 20
                text f"Stamina      : {mainchar.sta}/{mainchar.maxsta}" size 20
                text f"Counter pts  : {mainchar.csta}/{mainchar.maxcsta}" size 20
                text f"Mana         : {mainchar.mana}/{mainchar.maxmana}" size 20
                text f"Counter Mana : {mainchar.cmana}/{mainchar.maxcmana}" size 20
                text f"Defence      : {mainchar.cdef}/{mainchar.defe}" size 20
                text f"Magic defence: {mainchar.cmdef}/{mainchar.mdef}" size 20
            vbox:
                spacing 10
                xmaximum 350
                bar value StaticValue(girl.hp, mainchar.maxhp)
                bar value StaticValue(girl.sta, mainchar.maxsta)
                bar value StaticValue(girl.csta, mainchar.maxcsta)
                bar value StaticValue(girl.mana, mainchar.maxmana)
                bar value StaticValue(girl.cmana, mainchar.maxcmana)
                bar value StaticValue(girl.cdef, mainchar.defe*3)
                bar value StaticValue(girl.cmdef, mainchar.mdef*3)

            # Display status effects
            if mainchar.status_effects:
                vbox:
                    text "Status Effects:" size 18
                    for effect in mainchar.status_effects:
                        text effect size 18 color "#FF0000"
