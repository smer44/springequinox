# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.


default current_day = "Monday"
default current_date = 1
default current_time = "8:00 AM"


screen main_interface():

    # Top Left: Character Stats
    frame:
        align (0.05, 0.05)
        hbox:
            text "Strength: [mainchar.str]" size 20
            text "Knowledge: [mainchar.kno]" size 20
            text "Look: [mainchar.lok]" size 20
            text "Manners: [mainchar.man]" size 20
            # Display status effects
            if mainchar.status_effects:
                vbox:
                    text "Status Effects:" size 18
                    for effect in mainchar.status_effects:
                        text effect size 18 color "#FF0000"

    # Top Right: Date, Day, Time
    frame:
        align (0.95, 0.05)
        hbox:
            text "[current_day], Day [current_date] Time: [current_time]" size 20 xalign 1.0
