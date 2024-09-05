# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define mc = Character("MC")

image flbg=  "flowers background.jpg"
# The game starts here.

image book = "book.jpg"
image flower = "flower_static.png"

image mc = "mc.png"

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



    # These display lines of dialogue.

    "When a princess awakes on the first spring of her second decade on this Earth,"

    "she must pray to the Gods that her heart and mind are one."

    "For in that marvelous day, she must summon all the maidens in the kingdom"

    "and, from among them, select one to be her loyal companion."

    "To become her Knight Maiden."

    # This ends the game.

    jump palace_scene


label palace_scene:

    scene palace_hall:
        xsize config.screen_width
        ysize config.screen_height


    "All the young and capable young ladies of Andala have been told to wait in the main hall, while the male servants of the palace keep track of the logistics of the Knight Maiden Selection Ceremony."

    "A tradition held by generations. The Knight Maiden’s position is so sacred to the Dormeen Dynasty that the entire kingdom is paused and the secret of the chosen one is held only by the princess."

    "Although there is no shortage of rumors that, at least for some of the princesses of the past, the selection was completely random."

    show mc at left
    show screen main_interface

    menu:
        "Annoyed":
            $ mainchar.status_effects.remove("Surprised")
            $ mainchar.status_effects.add("Annoyed")
            mc "... because I am here for a completely different reason"
            mc "I am a..."
            menu :
                "Spy":
                    "I am a agent of other kingdom, sent here to spy in the court"
                    $ mainchar.str +=1
                "Thief":
                    "I wanted to steal something valuable from the treasury"
                    $ mainchar.kno +=1
                "Сame for the company":
                    "I just came to support a friend, who wants to become the Knight Maiden."
                    $ mainchar.man +=1
                "Beauty contest":
                    "I justthought there will be beauty contest here!"
                    $ mainchar.lok +=1

        "Confident":
            $ mainchar.status_effects.remove("Surprised")
            $ mainchar.status_effects.add("Confident")
            mc "With my swordfight skills, nobody here can stand against me!"
            $ mainchar.str +=1

        "Anxious":
            $ mainchar.status_effects.remove("Surprised")
            $ mainchar.status_effects.add("Anxious")
            mc "W-What if one of my friends is chosen and I can’t see them anymore!?"
            $ mainchar.man +=1


        "Curious":
            $ mainchar.status_effects.remove("Surprised")
            $ mainchar.status_effects.add("Curious")
            mc "I can’t wait to find out who will be the lucky one!"
            $ mainchar.kno +=1

    "The ceremony is about to start"
