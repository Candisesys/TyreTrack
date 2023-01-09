from pyray import *
import math
import random
import classes
import tkinter.messagebox

# Window and processes init
init_window(800, 600, "Tyre Tracks")
set_target_fps(120)
# Object init
car = classes.Car(Vector2(get_screen_width()/2 - 30, 500))
track = classes.Road(Vector2(get_screen_width()/2 - 150, 450))
# Timers
speed = 0.5
track_miles = 630
track_timer = 0
ontrack = True
while not window_should_close():
    # Update
    track_timer += 1
    # Lower the amount of miles until finish
    track_miles -= speed
    # Update Objects
    car.update()
    track.update()
    if (track_timer%15==0):
        track.speed = vector2_multiply(Vector2(2, 0), Vector2(random.choice([1, -1]), 0))
    ontrack = check_collision_recs(car.collrec, track.collrec)
    if (ontrack):
        speed = 0.5
        car.move_speed = Vector2(2, 0)
    else:
        speed = 0.1
        car.move_speed = Vector2(1, 0)
    if (track_miles < 0):
        tkinter.messagebox.showinfo("You win!", f"You win with a time of {math.floor(track_timer/120)} seconds.")
        close_window()
    print(track_miles)
    # Draw
    begin_drawing()
    clear_background(SKYBLUE)
    draw_text(f"Miles Until Finish: {math.floor(track_miles)}", 0, 0, 24, RAYWHITE)
    draw_rectangle_v(Vector2(0, 450), Vector2(880, 500), GREEN)
    track.draw()
    car.draw()
    end_drawing()
close_window()