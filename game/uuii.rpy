# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.


default current_day = "Monday"
default current_date = 1
default current_time = "8:00 AM"


screen main_interface():

    # Top Right: Date, Day, Time
    frame:
        align (0.95, 0.05)
        hbox:
            text "[current_day], Day [current_date] Time: [current_time]" size 20 xalign 1.0
