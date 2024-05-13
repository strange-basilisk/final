import turtle


wrong_color = ('#E02612')
background_color = ('#040c06' )
text_color = ('#BEDC7F')
line_color = ('#EEFFCC')
red = ('#E02612')



def turtle_setup():
    tline1 = turtle.Turtle() # main turtle used to clone wrong_path and right_path
    tline1.color(line_color)
    tline1.speed(0)
    tline1.width(5)
    tline1.penup()
    tline1.hideturtle()
    right_path = tline1.clone()
    wrong_path = tline1.clone()
    wrong_path.pencolor(red)
    tdeep_space = turtle.Turtle()
    tdeep_space.speed(0)

    tsilk_road = turtle.Turtle()
    tsilk_road.speed(0)

    tasteroid_field = turtle.Turtle()
    tasteroid_field.speed(0)

    tlawless_lands = turtle.Turtle()
    tlawless_lands.speed(0)

    tdying_sun = turtle.Turtle()
    tdying_sun.speed(0)

    timperial_garrison = turtle.Turtle()
    timperial_garrison.speed(0)

    tfreedom_graveyard = turtle.Turtle()
    tfreedom_graveyard.speed(0)

    thive = turtle.Turtle()
    thive.speed(0)

    tguild_outpost = turtle.Turtle()
    tguild_outpost.speed(0)

    tbig_box = turtle.Turtle()
    tbig_box.speed(0)

    tmedium_box = turtle.Turtle()
    tmedium_box.speed(0)


    thull_life = turtle.Turtle()
    thull_life.speed(0)
    return right_path, wrong_path, tdeep_space, tsilk_road, tasteroid_field, tlawless_lands, tdying_sun, timperial_garrison, tfreedom_graveyard, thive, tguild_outpost, tbig_box, tmedium_box, thull_life



def colors(purpose):
    if purpose == "background":
        return background_color
    elif purpose == "text":
        return text_color
    elif purpose == "line":
        return line_color
    elif purpose == "red":
        return wrong_color
    

def screen_setup(screen_color):
    width=1600
    height=1024
    window = turtle.Screen()
    window.setup(width, height)
    window.bgcolor(screen_color)
    return width, height, window

def paths(line_type, area):
    if area == "Area 3":
        line_type.goto(15,-400)#deep space
        line_type.pendown()
        line_type.goto(550, -300)#astroid fields
    elif area == "Area 4":
        line_type.goto(300, -120)#lawless lands
    elif area == "Area 5":
        line_type.penup()
        line_type.goto(200, -100)#dying sun
        line_type.pendown()
        line_type.goto(20, 50)#graveyard
    elif area == "Area 7":
        line_type.penup()
        line_type.goto(20, 100)#dying sun
        line_type.pendown()
        line_type.goto(220,200)#graveyard
    elif area == "Area 9":
        line_type.penup()
        line_type.goto(300,200)#graveyard
        line_type.pendown()
        line_type.goto(600,380)#trading guild

def map_icons():
  area_1_icon = ('images/transparent/icon-label_01_deep-space.gif')
  area_2_icon = ('images/transparent/icon-label_02_silk-road-trading-route.gif')
  area_3_icon = ('images/transparent/icon-label_03_astroid-mining-fields.gif')
  area_4_icon = ('images/transparent/icon-label_04_lawless_lands.gif')
  area_5_icon = ('images/transparent/icon-label_05_dying-sun-p1075.gif')
  area_6_icon = ('images/transparent/icon-label_06_imperial-garrison.gif')
  area_7_icon = ('images/transparent/icon-label_07_battle-for-freedom-graveyard.gif')
  area_8_icon = ('images/transparent/icon-label_08_the-hive.gif')
  area_9_icon = ('images/transparent/icon-label_09_trade-guild-outpost.gif')
  area_list = [area_1_icon, area_2_icon, area_3_icon,area_4_icon, area_6_icon, area_5_icon, area_7_icon, area_8_icon, area_9_icon]
  return area_list

def add_map(tclone, file, x, y):
    tclone.shape(file)  # Set the shape to the registered image
    tclone.teleport(x, y)
    tclone.stamp()
# # # Reads in narrative
def read_area_content(filename):
    area_content = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            parts = line.split("\t")
            area_content[parts[1]] = parts[0]
    return area_content

# # # Reads in Area Name
def read_area_name(filename):
    area_names = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            parts = line.split(",")
            area_names[parts[1]] = parts[0]
    return area_names

# # # Used for ontimer method
def wait():
    count_down = 5