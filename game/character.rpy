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
        def __init__(self,name,image,str,dex,end,mstr,mdex,mend):
            self.name = name
            self.c = Character(name)
            self.image = image
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
            self.maxhp = self.str * 2 + self.mstr * 2
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
            attack_power = self.str
            if not self.check_min_stat(self.sta,attack_power):
                return False
            self.sta -= attack_power
            self.reset_def()
            other.gain_pdamage(attack_power)
            return True

        def maattack(self,other):
            spellpower = (self.mstr * 3) // 2
            if not self.check_min_stat(self.mana,spellpower):
                return False
            self.mana -=spellpower
            self.reset_def()
            other.gain_mdamage(spellpower)
            return True

        def defend(self, other):
            added_defence = self.str//2
            if not self.check_min_stat(self.sta,added_defence):
                return False
            self.sta -= added_defence
            self.cdef = self.defe + added_defence
            return True


        def rest(self,other):
            if not self.check_nomax():
                return False
            self.sta = min(self.sta + self.end, self.maxsta)
            self.mana = min(self.mana + self.mend, self.maxmana)


        def gain_pdamage(self,dmg):
            dmg = max(dmg - self.cdef,0)
            self.hp -= dmg
            self.reset_def()

        def gain_mdamage(self,dmg):
            dmg = max(dmg - self.cmdef,0)
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
            return f"CharBattle({self.name},{self.str},{self.dex},{self.end},{self.mstr})"

        def  __repr__(self):
            return str(self)



    class CharBattleAI(CharBattle):
        #decide is called before
        def decide(self,other):
            if self.cdef <= self.defe:
                if self.sta >= self.str:
                    self.desigion  = "Defend"
                else:
                    self.desigion  = "Rest"
            else:
                if self.mana >= (self.mstr * 3 // 2):
                    self.desigion  = "Cast"
                elif self.sta >= self.str//2:
                    self.desigion  = "Attack"
                else:
                    self.desigion  = "Rest"

        def execute_desigion(self,other):
            if self.desigion  == "Defend":
                self.defend(other)
            elif self.desigion  == "Attack":
                self.attack(other)
            elif self.desigion  == "Cast":
                self.maattack(other)
            elif self.desigion  == "Rest":
                self.rest(other)



    girl_image = Image("warrior_girl.png")
    girl = CharBattle("Adventurer",girl_image,5,3,2,1,2,1)
    no_action = lambda : None

    rat_image = Image("rat.png")
    rat = CharBattleAI("Ratman",rat_image,5,3,2,1,2,1)


screen healthbar(mainchar,xa,ya,xmax,ymax,spacing_koef):
    $test_sz = ymax//8
    $bar_sz = ymax//8
    # Top Left: Character Stats
    frame:
        align (xa, ya)
        hbox:
            vbox:

                xmaximum xmax
                spacing test_sz/spacing_koef

                text f"Health       : {mainchar.hp}/{mainchar.maxhp}" size test_sz
                text f"Stamina      : {mainchar.sta}/{mainchar.maxsta}" size test_sz
                text f"Counter pts  : {mainchar.csta}/{mainchar.maxcsta}" size test_sz
                text f"Mana         : {mainchar.mana}/{mainchar.maxmana}" size test_sz
                text f"Counter Mana : {mainchar.cmana}/{mainchar.maxcmana}" size test_sz
                text f"Defence      : {mainchar.cdef}/{mainchar.defe}" size test_sz
                text f"Magic defence: {mainchar.cmdef}/{mainchar.mdef}" size test_sz
            vbox:


                spacing bar_sz/2
                xmaximum xmax

                bar value StaticValue(mainchar.hp, mainchar.maxhp) ysize bar_sz
                bar value StaticValue(mainchar.sta, mainchar.maxsta) ysize bar_sz
                bar value StaticValue(mainchar.csta, mainchar.maxcsta) ysize bar_sz
                bar value StaticValue(mainchar.mana, mainchar.maxmana) ysize bar_sz
                bar value StaticValue(mainchar.cmana, mainchar.maxcmana) ysize bar_sz
                bar value StaticValue(mainchar.cdef, mainchar.defe*3) ysize bar_sz
                bar value StaticValue(mainchar.cmdef, mainchar.mdef*3) ysize bar_sz

            # Display status effects
            if mainchar.status_effects:
                vbox:
                    text "Status Effects:" size 18
                    for effect in mainchar.status_effects:
                        text effect size 18 color "#FF0000"


screen enemyhealthbar(c):

    # Top Left: Character Stats
    frame:
        align (1.0, 0.0)
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
                text f"Desigion     : {c.desigion}" size 20
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
            if c.status_effects:
                vbox:
                    text "Status Effects:" size 18
                    for effect in c.status_effects:
                        text effect size 18 color "#FF0000"
