import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

write = turtle.Turtle()
write.penup()
write.hideturtle()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct",
                                    "What's another state's name?").title()
    if answer_state in states_list:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            state = data[data.state == answer_state]
            write.goto(state.x.item(), state.y.item())
            write.write(arg=answer_state)

    elif answer_state == "Exit":
        break

states_to_learn = [state for state in states_list if state not in guessed_states]
df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")