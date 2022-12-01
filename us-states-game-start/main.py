import turtle

screen = turtle.Screen()
screen.title("Indian State Game")

image="indianmap.gif"
screen.addshape(image)

turtle.shape(image)

# import turtle
#
# def get_mouse_click_coor(x, y):
#     print(f",{x},{y}")
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

import pandas

state_data=pandas.read_csv("50_states.csv")

gussed_options=[]

its_on=True
while its_on:
    user_guess=screen.textinput(title=f"{len(gussed_options)}/28 Guess the state",prompt="What is the name of the state").title()

    if user_guess == "Exit":
        its_on = False


    location=state_data[state_data.state == user_guess]
    if not location.empty and user_guess not in gussed_options:
        x_cor=int(location.x)
        y_cor=int(location.y)

        screen.tracer(0)
        state_name=turtle.Turtle()
        state_name.hideturtle()
        screen.update()
        state_name.penup()
        state_name.goto(x=x_cor,y=y_cor)
        state_name.write(user_guess)

        gussed_options.append(user_guess)

    if len(gussed_options) == 28:
        its_on=False


not_gussed=[]


for state in state_data["state"].to_list():
    if state not in gussed_options:
        not_gussed.append(state)

csv_file={
    "Not Guessed":not_gussed
}

df=pandas.DataFrame(csv_file)
df.to_csv("answers_key.csv")
