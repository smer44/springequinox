# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.



screen fight_menu(player, enemy):
    frame:
        xalign 0.5 yalign 0.9
        vbox:
            textbutton "Attack" action Call("battle_action_label", player.attack, enemy)#Function(react, player, rat) #Jump("attack",player,rat)
            textbutton "Defend" action Call("battle_action_label", player.defend, enemy)
            textbutton "Rest" action Call("battle_action_label", player.rest, enemy)
            #textbutton "Run" action Jump("run")


#of the rought academy legacy oricinal mechanicks
label battle_action_label(player_battle_action,enemy):
    $ player_battle_action(enemy)
    return


label fight_start(player,enemy):

    $ player_image = player.image
    $ enemy_image = enemy.image

    show expression  player.image at left
    show expression enemy.image at right

    show screen enemyhealthbar(enemy)

    call fight_loop(player, enemy)
    hide screen enemyhealthbar
    return


#of the rought academy legacy oricinal mechanicks
label fight_loop(player, enemy):
    $ enemy.decide(player)
    #hide screen fight_menu
    call screen fight_menu(player,enemy)
    $ renpy.pause(0.1)
    if player.wrong_desigion:
        player.c "i can not do that"
        call fight_loop(player,enemy)

    $ enemy.execute_desigion(player)
    $ renpy.pause(0.1)
    if player.hp <= 0:

        "You lost the fight "
        return
    elif enemy.hp <= 0:
        return
    call fight_loop(player,enemy)
    return
