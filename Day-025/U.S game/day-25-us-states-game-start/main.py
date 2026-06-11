import turtle
import os
import pandas as pd
base_dir = os.path.dirname(os.path.abspath(__file__))

screen = turtle.Screen()
screen.title("U.S. States Game")
image = os.path.join(base_dir, "blank_states_img.gif")
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_clikck_coor)

# turtle.mainloop()

base_dir = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(base_dir, "50_states.csv"))

states = data.state
state_list = states.to_list()


writer = turtle.Turtle()
writer.hideturtle()
writer.penup()



def write_answer(x, y, answer_state):
    writer.goto(x, y)
    writer.write(answer_state)

guessed_states = []
while len(guessed_states) < 50:
    
    answer_state = screen.textinput(
        title=f"score{len(guessed_states)}/50 States correct:",
        prompt="What's another states name?"
    )

    user_guess = answer_state.title()

    
    if user_guess == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        # for state in state_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # print(missing_states)
        df = pd.DataFrame(missing_states)
        df.to_csv("Missing States")
        break

    if user_guess in state_list:

        guessed_states.append(user_guess)
        
        state_data = data[data.state == user_guess]

       
        x = state_data.x.item()
        y = state_data.y.item()

        write_answer(x, y, answer_state)
        
