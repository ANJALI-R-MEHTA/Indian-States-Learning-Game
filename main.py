import pandas
import turtle
screen=turtle.Screen()
screen.title("Guess All the States Of India")
image="India-state.gif"
screen.addshape(image)
turtle.shape(image)
flag=0
while flag !=29:
    answer_state=screen.textinput(f"{flag}/29 states","Enter a state name")
    data=pandas.read_csv("states_data.csv")
    name=data.state.to_list()
    ans=answer_state.title()        
    for i in range (0,len(name)):
        if ans==name[i]:
            m=data[data.state==ans]
            x=m.x.item()
            y=m.y.item()
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x,y)
            t.write(ans)
            
            flag=flag+1
        
    
#screen.exitonclick()
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
