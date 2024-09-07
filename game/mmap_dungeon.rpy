# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

init python:

    class MMapFloor:
        def __init__(self,name,image_dict,text):
            self.name = name
            self.image_dict = image_dict
            self.load(text)
            self.csize = 40
            self.x = 0
            self.y = 0

        def load(self,text):
            mmap = []
            width = None
            for raw_line in text.strip().splitlines():
                line = raw_line.strip()
                if line:
                    if width:
                        assert width == len(line)
                    else:
                        width = len(line)
                    mmap.append(line)

            self.width = width
            self.height = len(mmap)
            self.mmap = mmap

        def current_char(self):
            return self.mmap[self.y][self.x]

        def can_left(self):
            return self.x > 0

        def can_right(self):
            return self.x < self.width-1

        def can_up(self):
            return self.y < self.height-1

        def can_down(self):
            return self.y > 0

        def go_left(self):
            if self.x > 0:
                self.x -=1
                return True
            return False

        def go_right(self):
            if self.x < self.width-1:
                self.x +=1
                return True
            return False


        def go_up(self):
            if self.y < self.height-1:
                self.y +=1
                return True
            return False

        def go_down(self):
            if self.y > 0 :
                self.y -=1
                return True
            return False


    text_map = """
    ++++++
    ++00++
    X+0+++
    XX++##
    XXX++#
    X00+++
    """

    mmgrass = Image("mmap/grass.png")

    grassstone = Image("mmap/grassstone.png")

    grasstree = Image("mmap/grasstree.png")

    water = Image("mmap/water.png")

    charmm = Image("mmap/char.png")

    image_mapping = {"0": grassstone, "X": grasstree, "#": water, "+" : mmgrass}

    first_floor = MMapFloor("dungeon level 1",image_mapping,  text_map)

    #-- Background --

    grass_bg = Image("bg/grass.jpg")

    grassrock_bg = Image("bg/grassrock.jpg")

    grasstree_bg = Image("bg/grasstree.jpg")

    water_bg = Image("bg/water.jpg")


    bg_mapping = {"0": grassrock_bg, "X": grasstree_bg, "#": water_bg, "+" : grass_bg}

    #-- Arrows --

    arrow_down = Image("gui/arrow_down.png")

    arrow_up = Image("gui/arrow_up.png")

    arrow_left = Image("gui/arrow_left.png")

    arrow_right = Image("gui/arrow_right.png")







screen minimap_floor(mmap):
    grid mmap.width mmap.height:
        xalign 1.0
        yalign 0.2
        for y in range(mmap.height):
            $row = mmap.mmap[y]
            for x in range(mmap.width):
                if x == mmap.x and y == mmap.y:
                    add charmm size (mmap.csize,mmap.csize)
                else:
                    add  mmap.image_dict[row[x]] size (mmap.csize,mmap.csize)



label visit_mmap_cell(mmap):
    hide screen minimap_floor
    show screen minimap_floor(first_floor)
    scene expression bg_mapping[mmap.current_char()]:
        xsize config.screen_width
        ysize config.screen_height
    show mc at left
    window show
    "[mmap.name] : [mmap.x], [mmap.y] "
    window hide
    call screen navigation_buttons(first_floor)
    return


label go_down(mmap):
    if mmap.go_down():
        call visit_mmap_cell(mmap)
    return

label go_up(mmap):
    if mmap.go_up():
        call visit_mmap_cell(mmap)
    return


label go_left(mmap):
    if mmap.go_left():
        call visit_mmap_cell(mmap)
    return


label go_right(mmap):
    if mmap.go_right():
        call visit_mmap_cell(mmap)
    return


screen navigation_buttons(mmap):
    #up and down swapped because map is drawn from up to down
    if mmap.can_up():
        imagebutton idle arrow_down:
            xalign 0.58
            yalign 1.0
            action Call("go_up", mmap)
    if mmap.can_down():
        imagebutton idle arrow_up:
            xalign 0.58
            yalign 0.7
            action Call("go_down", mmap)
    if mmap.can_left():
        imagebutton idle arrow_left:
            xalign 0.5
            yalign 0.87
            action Call("go_left", mmap)
    if mmap.can_right():
        imagebutton idle arrow_right:
            xalign 0.65
            yalign 0.87
            action Call("go_right", mmap)
