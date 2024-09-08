# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
#loads and uses character creator from
#https://tainara-p.itch.io/female-character-sprite-creator/download/eyJpZCI6MjE1NjIyNywiZXhwaXJlcyI6MTcyNTc3MTg4N30%3d.CFaBS0GUcRQg0lQmVNYch2Sno3Y%3d


init python:
    class VariableImage:
        def __init__(self,name):
            self.name = name
            self.state = 0
            self.image_variants = []
            self.visible = True

        def next(self):
            self.state = (self.state + 1 ) % len(self.image_variants)

        def image(self):
            return self.image_variants[self.state]

        def add(self,image):
            self.image_variants.append(image)


    class CompoundImage:
        def __init__(self):
            self.image_parts = dict()
            self.order = ["Hair", "Body", "Head", "Iris"]

        def toggle(self,vimage):
            if vimage.name in self.image_parts:
                del self.image_parts[vimage.name]
            else:
                self.image_parts[vimage.name] = vimage
        def set(self,vimage):
            self.image_parts[vimage.name] = vimage


    import os
    class FileManager:
        def __init__(self,cimage):
            self.creator_root = "Female Character Sprite Creator"
            self.img_root =  f"{config.basedir}/game/images/Female Character Sprite Creator"
            #self.img_root_replaced = f"{config.basedir}".replace("\\\\", "/").replace("\\", "/")
            self.open_dict = dict()
            self.cimage = cimage

        def list(self, ref = ""):
            ref = self.img_root + "/" + ref
            return [ (os.path.isfile(ref + "/" + item), str(item)) for item in os.listdir(ref)]

        def toggle(self,level,name):
            self.open_dict[(level,name)] = not self.isopen(level,name)


        def isopen(self,level,name):
            return self.open_dict.get((level,name),False)

        def is_file_ref(self,level, ref):
            if level <= 1:
                return False
            folder_content = self.list(ref)
            ln = len(folder_content)
            return ln == 0 or (ln == 1 and folder_content[0] == "Shadow")

        def set_to_char(self,ref,name):
            path = self.creator_root + "/" + ref + "/" + name
            img = Image(path)
            vimg = VariableImage(ref)
            vimg.add(img)
            self.cimage.set(vimg)



        def close(self,level, name):
            del self.open_dict[(level,name)]



    comp_char = CompoundImage()
    sel_sel = FileManager(comp_char)

screen file_tree(file_manager):
    side "c b r":
        xalign 0.3
        yalign 0.5
        #area (int(config.screen_width*0.3), int(config.screen_height*0.3), int(config.screen_width*0.7), int(config.screen_height*0.7),)
        xsize config.screen_width//3
        ysize config.screen_height//3
        viewport id "vp":
            draggable True
            vbox:
                for isfile, item in file_manager.list():
                    textbutton "[item]":
                        action Function(file_manager.toggle, 0,item)
                    if file_manager.isopen(0,item):
                        for isfile2, item2 in file_manager.list(item):
                            textbutton "    [item2]":
                                action Function(file_manager.toggle, 1,item2)
                            if file_manager.isopen(1,item2):
                                for isfile3, item3 in file_manager.list(item + "/" + item2):
                                    if isfile3:
                                        textbutton "      ->[item3]":
                                            action Function(file_manager.set_to_char, item + "/" + item2, item3)
                                    else:
                                        textbutton "        [item3]":
                                            action Function(file_manager.toggle, 2,item3)
                                        if file_manager.isopen(2,item3):
                                            for isfile, item4 in file_manager.list(item + "/" + item2 + "/" + item3):
                                                if isfile:
                                                    textbutton "          ->[item4]":
                                                        action Function(file_manager.set_to_char, item + "/" + item2+ "/"+item3, item4)
                                                else:
                                                    textbutton "          ##[item4]"




        vbox:
            bar value XScrollValue("vp")
            textbutton "Return":
                action Call("stub")
        vbar value YScrollValue("vp")

label stub:
    return

screen show_compound(cimage,xa,ya,xs,ys):
    for name, vimage in cimage.image_parts.items():
        add vimage.image():
            xalign xa
            yalign ya
            xsize xs
            ysize ys
