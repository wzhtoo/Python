import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 "
                                           f"States Correct",
                                    prompt="What's another state's name?"
                                    ).title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("State_to_learn.csv")
        break
    # If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # If the got it right:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        # Create a turtle to write the name os the state at the state's x and y coordinate
        # t.write(state_data.state.item())
        t.write(answer_state)
