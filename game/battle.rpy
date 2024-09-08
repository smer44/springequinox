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

    show expression  player.image at left, std_mc
    show expression enemy.image at right, std_mc

    show screen enemyhealthbar(enemy)

    label .fight_step_label:

        call fight_step(player, enemy)
        if player.hp <= 0:
            "You lost the fight "
            jump fight_step_end
        elif enemy.hp <= 0:
            jump fight_step_end

    jump .fight_step_label

    label .fight_step_end:

    hide screen enemyhealthbar
    return


#of the rought academy legacy oricinal mechanicks
label fight_step(player, enemy):
    $ enemy.decide(player)
    #hide screen fight_menu
    call screen fight_menu(player,enemy)
    $ renpy.pause(0.1)
    if player.wrong_desigion:
        player.c "i can not do that"
        return

    $ enemy.execute_desigion(player)
    $ renpy.pause(0.1)

    #call fight_loop(player,enemy)
    return
