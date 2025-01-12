import bpy
import random 
import os
import sys
import aud

    #### Dictionary ####

items = {
    "sword": {
        "id": 1,
        "name":"sword",
        "type": "weapon",
        "icon": "sword_icon"
    },
    "shield": {
        "id": 2,
        "name":"shield",
        "type": "armor",
    },
    "bow": {
        "id": 3,
        "name":"bow",
        "type": "weapon",
        "icon": "icon/bow.png",
    },
    "ring": {
        "id": 4,
        "name":"ring",
        "type": "accessory",
        "icon": "icon/bow.png"
    },
    "parchment": {
        "id": 5,
        "name":"parchment",
        "type": "artifact",
        "icon": "icon/bow.png",
    },
    "dagger": {
        "id": 6,
        "name":"dagger",
        "type": "weapon",
        "icon": "icon/bow.png"
    },
    "helmet": {
        "id": 7,
        "name":"helmet",
        "type": "armor",
        "icon": "icon/bow.png"
    },
    "potion": {
        "id": 8,
        "name":"potion",
        "type": "accessory",
        "icon": "icon/bow.png"
    }
}

    #### VARIABLES #####

#import items
#from data import items 

#base_dir = os.path.dirname('main')
base_dir = os.path.dirname(bpy.data.filepath) #Path for everything

#INVENTORY
inventory = [None] * 10
custom_icons = None
dice = (1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
launch = None

#SOUND
device = aud.Device()
sound_path = os.path.join(base_dir, "sound", "dice-142528.mp3")
dice_sound = aud.Sound(sound_path) # change for variable

# ICONS
cutoms_icon = None
icon_dir = base_dir, "icon"

bow_icon  = (icon_dir, 'bow.png')
dagger_icon  = (icon_dir, 'dagger.png')
parchment_icon = (icon_dir, 'parchment.png')
potion_icon = (icon_dir, 'potion.png')
ring_icon = (icon_dir, 'ring.png')
shield_icon = (icon_dir, 'shield.png')

    #### ADD RANDOM ITEM ####
def add_random_item_to_inventory():
    random_item_key = random.choice(list(items.keys()))
    random_item = items[random_item_key]
    
    
    global launch #can be call to another func
    launch = random.choice(dice)
    handle = device.play(dice_sound)
    
    if  launch >= 18:
        for i in range(len(inventory)):
            if inventory[i] is None:  # Empty Emplacement
                inventory[i] = random_item
                break

# add random item
class AddRandomItemOperator(bpy.types.Operator):
    bl_idname = "inventory.add_random_item"
    bl_label = "Roll dice"

    def execute(self, context):
        #Go use func add_random_item_to_inventory
        add_random_item_to_inventory() 
        return {'FINISHED'}
        
        
    #### CREATION UI ##### 
class SimplePanel(bpy.types.Panel):
    bl_label = "RPG_CLICKER"
    bl_idname = "VIEW3D_PT_RPG"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'INVENTORY'
    
    
    #Go draw UI
    def draw(self, context):
        layout = self.layout

        # Label
        layout.label(text="INVENTORY")

        # print inventory
        inventory_box = layout.box()
        for slot, item in enumerate(inventory):
            item_name = item["name"] if item else "Empty"
            inventory_box.label(text=f"Slot {slot + 1}: {item_name}")
        
            
        # Button to add random item
        layout.operator("inventory.add_random_item", text="Roll dice")
        layout.label(text = f"result = {launch}")
        
        """
        #Grid
        layout = self.layout
        box = layout.box()  # Optional: Create a bordered box for the grid

        # Create the grid structure
        for row in range(4):  # Number of rows
            row_layout = box.row()
            for col in range(3):  # Number of columns
                row_layout.operator("object.select_all", text=f"({row}, {col})")
        """        
        


    #### ICON #####
class ICONS():
    def load_custom_icon():
        custom_icons = bpy.utils.previews.new()
        file_path = os.path.join(icon_dir, sword_icon)
    
    """
    def draw(self, context):
        #if 'sword' in INVENTORY:
            #load(file_path)
    return
    """  
#Enregistrer Class
def register():
    bpy.utils.register_class(SimplePanel)
    bpy.utils.register_class(AddRandomItemOperator)

def unregister():
    bpy.utils.unregister_class(SimplePanel)
    bpy.utils.unregister_class(AddRandomItemOperator)

if __name__ == "__main__":
    register()

