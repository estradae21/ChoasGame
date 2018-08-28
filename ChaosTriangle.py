import turtle

vertices = [[-200, -100], [0, 200], [200, -100]]
yes = {'yes', 'ye', 'y'}
no = {'no', 'n'}


# function to have the turtle draw a triangle, the basic unit of our fractal
def draw_triangle(vertices, ChaosTriangle):
    ChaosTriangle.up()
    ChaosTriangle.goto(vertices[0][0], vertices[0][1])
    ChaosTriangle.down()
    ChaosTriangle.goto(vertices[1][0], vertices[1][1])
    ChaosTriangle.goto(vertices[2][0], vertices[2][1])
    ChaosTriangle.goto(vertices[0][0], vertices[0][1])


# the same midpoint function we wrote for the chaos game
def midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]


# recursive function that draws the different "levels" of the fractal
def draw_fractal(vertices, level, my_turtle):
    draw_triangle(vertices, my_turtle)
    # call function recursively to draw all levels of fractal
    if level > 0:
        # draw first segment of fractal
        # the vertices being passed in are the bottom corner of the first
        # section, the bottom corner of the second section, and the bottom
        # corner of the third secion.
        draw_fractal([vertices[0],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                     level - 1, my_turtle)
        draw_fractal([vertices[1],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[1], vertices[2])],
                     level - 1, my_turtle)
        draw_fractal([vertices[2],
                      midpoint(vertices[2], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                     level - 1, my_turtle)


level = int(input("ow many recursions deep do we want to draw the fractal? "))
Chaos_triangle = turtle.Turtle()
Chaos_triangle.shape('turtle')
screen = turtle.Screen()
screen.colormode(255) # to use the RGB codes for the colors
vertices = [[-200, -100], [0, 200], [200, -100]]
draw_fractal(vertices, level, Chaos_triangle)
screen.exitonclick()





