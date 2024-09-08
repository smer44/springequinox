# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

#define mc = Character("MC")

image flbg=  "flowers background.jpg"
# The game starts here.

image book = "book.jpg"
image flower = "flower_static.png"

image basement = "basement.jpg"

#image mc = "mc.png"

image palace_hall = "palace_bg.jpg"


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene flbg:
        xsize config.screen_width
        ysize config.screen_height

    show book:
        xalign 0.5
        yalign 0.5

    show flower:
        xalign 0.5
        yalign 0.5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene basement:
        xsize config.screen_width
        ysize config.screen_height
    # These display lines of dialogue.
    "One day you suddenly discovered that there is a portal in another dimention in your basement"
    jump home_actions

transform std_mc:
    zoom .7

label home_actions:
    show expression girl.image at left, std_mc
    show screen healthbar(girl,0,0,350,250,3.5)
    show screen main_interface

    menu:
        "Dungeon lvl 1":
            jump dunglvl1
        "Shop":
            "shop"
        "Damage test":
            $girl.gain_pdamage(10)
        "Defence test":
            $girl.defend(None)
        "Skill points":
            "skill points will be spendable at home"
        "Rest":
            $girl.healfull()
            "after rest, character is fully healed"
        "Test battle":
            $rat.healfull()
            hide expression girl.image
            call fight_start(girl,rat)
        "Test show formation":
            hide expression girl.image
            show screen ff_fight_start(testFormation)
            "[testFormation]"
            hide window
            pause
            hide screen ff_fight_start
            show expression girl.image at left, std_mc





    # This ends the game.

    jump home_actions


label dunglvl1:
    window hide
    call visit_mmap_cell(first_floor)


    jump dunglvl1



label palace_scene_deprecated:

    scene palace_hall:
        xsize config.screen_width
        ysize config.screen_height


    "All the young and capable young ladies of Andala have been told to wait in the main hall, while the male servants of the palace keep track of the logistics of the Knight Maiden Selection Ceremony."

    "A tradition held by generations. The Knight Maiden’s position is so sacred to the Dormeen Dynasty that the entire kingdom is paused and the secret of the chosen one is held only by the princess."

    "Although there is no shortage of rumors that, at least for some of the princesses of the past, the selection was completely random."

    show mc at left


    menu:
        "Surprised":
            $ mainchar.status_effects.add("Surprised")
            mc "... because I am here for a completely different reason"
            mc "I am a..."
            menu :
                "Spy":
                    "I am a agent of other kingdom, sent here to spy in the court"
                    $ mainchar.status_effects.add("Spy")
                    $ mainchar.str +=1
                "Thief":
                    "I wanted to steal something valuable from the treasury"
                    $ mainchar.status_effects.add("Thief")
                    $ mainchar.kno +=1
                "Сame for the company":
                    "I  came just to support a friend, who wants to become the Knight Maiden."
                    $ mainchar.status_effects.add("Slacker")
                    $ mainchar.man +=1
                "Beauty contest":
                    "I just thought there will be beauty contest here!"
                    $ mainchar.status_effects.add("Model")
                    $ mainchar.lok +=1

        "Confident":

            $ mainchar.status_effects.add("Confident")
            mc "With my swordfight skills, nobody here can stand against me!"
            $ mainchar.str +=1

        "Anxious":
            $ mainchar.status_effects.add("Anxious")
            mc "W-What if one of my friends is chosen and I can’t see them anymore!?"
            $ mainchar.man +=1

        "Curious":
            $ mainchar.status_effects.add("Curious")
            mc "I can’t wait to find out who will be the lucky one!"
            $ mainchar.kno +=1

        "Annoyed":
            $ mainchar.status_effects.add("Annoyed")
            mc "Nobody pays attention to my gorgeous look!"
            $ mainchar.lok +=1






    mc "Look like the ceremony is about to start."
    mc "I can barely see anything from here."

    "This is not the first time twins have been born in the Dormeen family, but it will be the first time a joint Knight Maid Selection Ceremony will be held."
    "Maybe to maximize security after the current threats the royal family has received."
