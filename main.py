import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "./us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
turtle.tracer(0)
turtle.speed(0)


# #To get the x, y coordinates when mouse is clicked.
# def get_mouse_click_coor(x, y):
#     print(x, y)
    
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("./us-states-game-start/50_states.csv")
states = data.state.to_list()
value = 0
entered_states = []
while value <= 50:
    answer_state = screen.textinput(title=f"{value}/50 States Correct", prompt="What's the another states name?").title()#Taking input from the user
    if answer_state in states and answer_state not in entered_states:
        entered_states.append(answer_state)
        # State_to_learn.csv
        missing_states = []
        for x in states:
            if x not in entered_states:
                missing_states.append(x)
                # data_dict = { 
                #     "State To learn": missing_states
                # } or
        datas = pandas.DataFrame(missing_states)
        datas.to_csv("./us-states-game-start/state_to_missing_states.csv")   
        get_state = data[data.state ==  f"{answer_state}"]
        x_value = get_state.x.to_list()
        y_vlaue = get_state.y.to_list()
        turtle.setposition(x_value[0], y_vlaue[0])
        turtle.write(f"{answer_state}", align="left")
        turtle.home()
        x_value.pop()
        y_vlaue.pop()
        value += 1
    
    if answer_state is None:
        break
    print(answer_state)
turtle.mainloop()