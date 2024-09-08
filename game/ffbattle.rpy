# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

transform ffbattle_char_size:
    zoom .5


init python:

    class FFBattleFormation:

        def __init__(self,width,height):
            self.width = width
            self.height = height
            self.heroes = [[None for _ in range(self.width)] for _ in range(self.height)]

        def add(self,hero,x,y):
            assert x < self.width
            assert y < self.height
            self.heroes[y][x] = hero

        def __str__(self):
            return str(self.heroes)


    testFormation = FFBattleFormation(3,2)
    testFormation.add(girl,1,0)

    mage_image = Image("white_mage_girl.png")
    mage = CharBattle("Mage",mage_image,5,3,2,1,2,1)

    ass_image = Image("assassin.png")
    assasin = CharBattle("Assasin",ass_image,5,3,2,1,2,1)


    testFormation.add(mage,0,1)
    testFormation.add(assasin,2,1)


screen ff_fight_start(players_formation):

    for y in range(players_formation.height):

        $xpos = int(config.screen_width*0.3- y*config.screen_width*0.15)
        for x in range(players_formation.width):
            $hero = players_formation.heroes[y][x]
            if hero is not None:
                $ypos = int(config.screen_height*0.6 - x*config.screen_height*0.15)
                $yshift = int(x*config.screen_height*0.1)
                add hero.image pos (xpos+yshift, ypos) zoom 0.4
