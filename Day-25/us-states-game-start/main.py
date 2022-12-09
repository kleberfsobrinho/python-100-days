import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_name = data["state"]
states_list = states_name.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)

        state_data = data[states_name == answer_state]

        x = state_data["x"].values[0]
        y = state_data["y"].values[0]
        cord = (x, y)

        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.speed("fastest")
        state_turtle.goto(cord)
        state_turtle.write(answer_state)
        state_turtle.hideturtle()
