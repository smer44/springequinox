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


        def attack(self,other):
            if not self.check_min_stat(self.sta,10):
                return False
            self.sta -= 10
            self.reset_def()
            other.gain_pdamage(self.str)
            return True

        def maattack(self,other):
            if not self.check_min_stat(self.mana,15):
                return False
            self.mana -=15
            self.reset_def()
            other.gain_mdamage(self.mstr)
            return True

        def defend(self, other):
            if not self.check_min_stat(self.sta,10):
                return False
            self.sta -= 10
            self.cdef = 2*self.defe
            return True


        def rest(self,other):
            if not self.check_nomax():
                return False
            self.sta += self.end
            self.mana += self.mend


        def gain_pdamage(self,dmg):
            dmg = max(dmg - self.cdef,0)
            self.hp -= dmg
            self.reset_def()

        def reset_def(self):
            self.cdef = self.defe
            self.cmdef = self.mdef


        def check_min_stat(self,stat,value):
            if stat < value:
                self.wrong_desigion = True
                return False
            else:
                self.wrong_desigion = False
                #self.reset_def()
                return True


        def check_nomax(self):
            if self.mana == self.maxmana and self.sta == self.maxsta:
                self.wrong_desigion = True
                return False
            else:
                self.wrong_desigion = False
                return True


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


screen enemyhealthbar(c):

    # Top Left: Character Stats
    frame:
        align (0.0, 0.0)
        hbox:
            vbox:
                spacing 25
                xmaximum 350
                text f"Health       : {c.hp}/{c.maxhp}" size 20
                text f"Stamina      : {c.sta}/{c.maxsta}" size 20
                text f"Counter pts  : {c.csta}/{c.maxcsta}" size 20
                text f"Mana         : {c.mana}/{c.maxmana}" size 20
                text f"Counter Mana : {c.cmana}/{c.maxcmana}" size 20
                text f"Defence      : {c.cdef}/{c.defe}" size 20
                text f"Magic defence: {c.cmdef}/{c.mdef}" size 20
            vbox:
                spacing 10
                xmaximum 350
                bar value StaticValue(c.hp, c.maxhp)
                bar value StaticValue(c.sta, c.maxsta)
                bar value StaticValue(c.csta, c.maxcsta)
                bar value StaticValue(c.mana, c.maxmana)
                bar value StaticValue(c.cmana, c.maxcmana)
                bar value StaticValue(c.cdef, c.defe*3)
                bar value StaticValue(c.cmdef, c.mdef*3)

            # Display status effects
            if mainchar.status_effects:
                vbox:
                    text "Status Effects:" size 18
                    for effect in mainchar.status_effects:
                        text effect size 18 color "#FF0000"
