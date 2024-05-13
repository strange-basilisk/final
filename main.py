import turtle
import textwrap
import random
import sys
import game_setup as setup

# # # Colors
background_color = setup.colors("background")
text_color = setup.colors("text")
line_color = setup.colors("line")
wrong_color = setup.colors("red")

# # # Screen Setup
width, height, window = setup.screen_setup(background_color)

# # # Allows user to exit screen with esc key once game is finished
def exitprogram():
    window.bye()

def close():
    close = turtle.Turtle()
    close.speed(0)
    close.penup()
    close.hideturtle()
    close.goto(0,0)
    turtle.clearscreen()
    close.write("Press ESC again to exit", align="center", font = ("Courier", 24, "normal"))
    window.listen()
    window.onkeypress(exitprogram,"Escape")


# # # Damage funcion and it's variables
hull_damage_counter = 0
damage_string = "No Damage"

def roll_attack_dice():
    global hull_damage_counter
    global damage_string
    
    # Roll a dice once for the attack
    hit = random.randint(1, 6)
    tuser_choice.clear()
    tuser_choice.write(textwrap.fill( "As you jump, the hunter(s) open fire. You try to evade their shots!",50),font = ("Courier", 14, "normal" ))
    turtle.ontimer(setup.wait(), t=2000)
    tuser_choice.clear()
    
    if hit == 5 or hit == 6:  # Rolls of 5 or 6 are hits
        
        hull_damage_counter += 1  # Increment hull damage counter
        damage_string = str(hull_damage_counter)
        tdamage.clear()
        tdamage.write(textwrap.fill("Your hull took damage. Total hits: " + damage_string),font = ("Courier", 14, "normal" ))
        if damage_string == "1":
            thull_life.clear()
            thull_life.shape(hull_damage)
            thull_life.stamp()
        elif damage_string == "2":
            thull_life.clear()
            thull_life.shape(hull_empty)
         
            thull_life.stamp()
    else:
        tuser_choice.teleport(-700, -375)
        tuser_choice.pendown()
        tuser_choice.pencolor(text_color)
        tuser_choice.write(textwrap.fill("You escape unscathed."),font = ("Courier", 14, "normal" ))
    if damage_string == "2":
        tdamage.teleport(-700, -375)
        tdamage.clear()
        tdamage.pendown()
        tdamage.write(textwrap.fill("The last of the hunters' shots rip through your hull and split your ship in two. Game Over"),font = ("Courier", 14, "normal" ))
        game_over()


# # # Adds map shapes
def add_shape(image_file_list):
        for image in image_file_list:
            window.addshape(image)


# # # HUD images
text_box_M = 'images/text-box_LG.gif'
text_box_L = 'images/text-box_XLG.gif'
hull_life = 'images/hull-indicator_full.gif'
hull_damage = 'images/hull-indicator_half-full.gif'
hull_empty = "images/hull-indicator_empty.gif"


# # # Write narrative
def narrative(area):
    tnarrative.clear()
    tnarrative.teleport(-750, 325)
    tnarrative.pendown()
    tnarrative.write(textwrap.fill(area_names[area],50),font = ("Courier", 20, "normal" ))
    tnarrative.teleport(-700, 75)
    tnarrative.write(textwrap.fill(area_content[area],50),font = ("Courier", 14, "normal" ))

# # # Game Over prompt
def game_over():
    turtle.ontimer(setup.wait(),t=500)
    tuser_choice.clear()
    tuser_choice.teleport(-700, -350)
    tuser_choice.pencolor(wrong_color)
    tuser_choice.write(textwrap.fill("GAME OVER",50),font = ("Courier", 25, "normal" ))
    tuser_choice.teleport(-700, -400)
    tuser_choice.write(textwrap.fill("Press ESC to closes",50),font = ("Courier", 14, "normal" ))

# # # Win Prompt
def win():
    turtle.ontimer(setup.wait(), t=500)
    tuser_choice.clear()
    tdamage.clear()
    tuser_choice.pencolor(text_color)
    tuser_choice.write(textwrap.fill("YOU WIN!",50),font = ("Courier", 25, "normal" ))
    tuser_choice.teleport(-700, -400)
    tuser_choice.write(textwrap.fill("Press ESC to closes",50),font = ("Courier", 14, "normal" ))

# # # Gives the user their choices on where to jump next and handles invalid input
def user_choices(choice1, choice2):
    valid_choices = [choice1, choice2]
    area_choice = ""
    turtle.ontimer(setup.wait(), t=1000)
    tuser_choice.teleport(-700, -375)
    tdamage.clear()
    tuser_choice.clear()
    tuser_choice.pendown()
    tuser_choice.write(textwrap.fill( "1. " +  area_names[choice1],50),font = ("Courier", 14, "normal" ))
    tuser_choice.teleport(-700, -400)
    tuser_choice.write(textwrap.fill( "2. " +  area_names[choice2],50),font = ("Courier", 14, "normal" ))
    while area_choice not in valid_choices:
        area_choice = turtle.textinput("AWAITING ORDERs", "Enter 'exit' to quit")
        tuser_choice.teleport(-700, -425)
        tuser_choice.pendown()
        tuser_choice.write(textwrap.fill( "You must type 1 or 2",50),font = ("Courier", 14, "normal" ))
        if area_choice == "exit":
            sys.exit()
        elif area_choice == "1":
            tuser_choice.clear()
            return  choice1
        elif area_choice == "2":
            tuser_choice.clear()
            return choice2

# turtle to draw narrative
tnarrative = turtle.Turtle()
tnarrative.pencolor(text_color)
tnarrative.hideturtle()
tnarrative.teleport(-700, 250)

# turtle to draw choices
tuser_choice = turtle.Turtle()
tuser_choice.pencolor(text_color)
tuser_choice.hideturtle()
tuser_choice.teleport(-700, -375)

# turtle to draw damage
tdamage = turtle.Turtle()
tdamage.pencolor(wrong_color)
tdamage.hideturtle()
tdamage.teleport(-700, -375)

# Create turtles to move things around
right_path, wrong_path,tdeep_space, tsilk_road, tasteroid_field, tlawless_lands, tdying_sun, timperial_garrison, tfreedom_graveyard, thive, tguild_outpost, tbig_box, tmedium_box, thull_life = setup.turtle_setup()

# get a list of all the icon locations
area_icon_list = setup.map_icons()

add_shape(area_icon_list)

window.addshape(hull_life)
window.addshape(hull_damage)
window.addshape(hull_empty)
window.addshape(text_box_L)
window.addshape(text_box_M)

thull_life.shape(hull_life)
thull_life.speed(0)
thull_life.teleport(-650, 400)
thull_life.stamp()

tbig_box.shape(text_box_L)
tbig_box.teleport(-450, 200)
tbig_box.stamp()

tmedium_box.shape(text_box_M)
tmedium_box.teleport(-450, -350)
tmedium_box.stamp()

setup.add_map(tdeep_space, area_icon_list[0],20,-400)
setup.add_map(tsilk_road, area_icon_list[1],20, -200)
setup.add_map(tasteroid_field, area_icon_list[2],650, -300)
setup.add_map(tlawless_lands, area_icon_list[3], 300, -100)
setup.add_map(tdying_sun, area_icon_list[4],20,400 )
setup.add_map(timperial_garrison, area_icon_list[5],20,100 )
setup.add_map(tfreedom_graveyard, area_icon_list[6],300,200)
setup.add_map(thive, area_icon_list[7],700, 200 )
setup.add_map(tguild_outpost, area_icon_list[8],600, 400 )

area = ""
area_content = setup.read_area_content("area-content.tab")
area_names = setup. read_area_name("area-names.txt")


# # # Area 1 Deep Space
narrative("Area 1")
area = user_choices("Area 2", "Area 3") #silk roaed, or asteroid field
roll_attack_dice()

while True:
    # # # Area 3 Asteroid Field
    if area == "Area 3":
        setup.paths(right_path, area)
        narrative(area)
        area = user_choices("Area 2", "Area 4") # silk road or Lawless Lands
        roll_attack_dice()
        if damage_string == "2":
            break
    # # # Area 2 Silk Road
    else:
        narrative(area)
        wrong_path.goto(20, -400)#deep space
        wrong_path.pendown()
        wrong_path.goto(20, -250)#silk road
        game_over()
        break
    
    # # # Area 4 Lawless Lands
    if area == "Area 4":
        setup.paths(right_path, area)
        narrative(area)
        area = user_choices("Area 5", "Area 8") # Dying Sun or Hive
        roll_attack_dice()
        if damage_string == "2":
            break        
    # # # hive
    else:
        narrative(area)
        wrong_path.goto(550, -300) #lawless lands
        wrong_path.pendown()
        wrong_path.goto(20, -250)#hive
        game_over()
        break
    
    # # # Area 5 Dying Sun
    if area == "Area 5":
       setup.paths(right_path, area)
       narrative(area)
       area = user_choices("Area 6", "Area 7") #Garrison or Graveyard
       roll_attack_dice()
       if damage_string == "2":
           break    
    # # # Garrison
    else:        
        narrative(area)
        wrong_path.goto(300, -80)#dying sun
        wrong_path.pendown()
        wrong_path.goto(650, 200)#garrison
        game_over()
        break
    
    # # # Graveyard
    if area == "Area 7":
        setup.paths(right_path, area)
        narrative(area)
        area =user_choices("Area 9", "Area 6") # Guild or Garrison
        roll_attack_dice()
        if damage_string == "2":
            break
    
    if area == "Area 9":
        setup.paths(right_path, area)
        narrative("Area 9")
        win()
        break
    
    else:
        wrong_path.penup() ##should be from graveyard to garrison
        wrong_path.goto(230,200)#graveyard
        wrong_path.pendown()
        wrong_path.goto(20, 400)#imperial garrison
        narrative(area)
        game_over()
        break


window.listen()
window.onkeypress(exitprogram, "Escape")
window.update()
window.mainloop()