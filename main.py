from pygame import *
from pygame import display as display
from pygame import event as event
from pygame import time as time
from pygame import font as font
from pygame import draw as draw
from pygame import mouse as mouse
from pygame import image as image

init()
font.init()

screen = display.set_mode((1600, 900))
running = True

Font = font.SysFont("Arial", 30)

start_ticks = time.get_ticks() #starter tick
timer_total, timer = 3600, 3600
time_stopped = False
frame = 1

items = []
user_input = ""
active = False

x_button = image.load("/~/Documents/Masseyhacks_VII/images/x-button.png")

while running:
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed(3)

    for evt in event.get():
        if evt.type == QUIT:
            running = False
        
        if active:
            if evt.type == KEYDOWN:
                if evt.key == K_BACKSPACE:
                    user_input = user_input[:-1]
                    items[-1] = user_input
                elif evt.key == K_RETURN:
                    active = False
                else:
                    if len(user_input) < 20:
                        user_input += evt.unicode
                    items[-1] = user_input
                print(user_input)

        if evt.type == MOUSEBUTTONDOWN:
            if Rect(35, 90, 100, 50).collidepoint(mx, my): # Stop/Play
                time_stopped = not time_stopped
            elif Rect(145, 90, 100, 50).collidepoint(mx, my): # Reset
                timer = timer_total
            elif Rect(145, 40, 45, 40).collidepoint(mx, my): # +
                timer += 300
            elif Rect(200, 40, 45, 40).collidepoint(mx, my): # -
                timer -= 300
                if timer < 0:
                    timer = 0

            if Rect(35, 185, 45, 40).collidepoint(mx, my):
                items.append("")
                user_input = ""
                active = True

    
    screen.fill((255, 255, 255))
    # Timer
    if not time_stopped:
        if frame % 60 == 0:
            timer -= 1

    if timer <= 0:
        timer = 0
    min, sec = divmod(timer, 60)
    timer_display = "%02d:%02d" % (int(min), int(sec))

    draw.rect(screen, (255, 255, 255), (25, 25, 230, 125)) # Timer Box (White)
    draw.rect(screen, (0, 0, 0), (25, 25, 230, 125), 2)    # Timer Box (Outline)

    if Rect(35, 90, 100, 50).collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), (35, 90, 100, 50))
    elif Rect(145, 90, 100, 50).collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), (145, 90, 100, 50))
    elif Rect(145, 40, 45, 40).collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), (145, 40, 45, 40))
    elif Rect(200, 40, 45, 40).collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), (200, 40, 45, 40))
    
    draw.rect(screen, (0, 0, 0), (35, 90, 100, 50), 1)     # Stop
    draw.rect(screen, (0, 0, 0), (145, 90, 100, 50), 1)    # Reset
    draw.rect(screen, (0, 0, 0), (145, 40, 45, 40), 1)     # +
    draw.rect(screen, (0, 0, 0), (200, 40, 45, 40), 1)     # -

    screen.blit (Font.render(timer_display, False, (0, 0, 0)), (50, 50))
    if not time_stopped:
        screen.blit (Font.render("Stop", False, (0, 0, 0)), (55, 100))
    else:
        screen.blit(Font.render("Play", False, (0, 0, 0)), (55, 100))
    screen.blit (Font.render("Reset", False, (0, 0, 0)), (155, 100))
    screen.blit (Font.render("+", False, (0, 0, 0)), (158, 45))
    screen.blit (Font.render("-", False, (0, 0, 0)), (217, 45))

    # To Do
    draw.rect(screen, (255, 255, 255), (25, 175, 400, 700))
    draw.rect(screen, (0, 0, 0), (25, 175, 400, 700), 2)
    screen.blit(Font.render("To-Do List", False, (0, 0, 0)), (150, 200))

    if Rect(35, 185, 45, 40).collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), (35, 185, 45, 40))
    draw.rect(screen, (0, 0, 0), (35, 185, 45, 40), 1)
    screen.blit(Font.render("+", False, (0, 0, 0)), (50, 190))

    for i in range(len(items)-1, -1, -1):
        if i < 24:
            if Rect(350, 230 + 25 * i, 25, 25).collidepoint(mx, my):
                draw.rect(screen, (255, 0, 0), (350, 230 + 25 * i, 25, 25))
                if mb[0] == 1 and frame % 4 == 0:
                    del items[i]
                    continue
            screen.blit(Font.render("- " + items[i], False, (0, 0, 0)), (75, 230 + 25 * i))
            draw.rect(screen, (0, 0, 0), (350, 230 + 25 * i, 25, 25), 1)
            screen.blit(x_button, (350, 230 + 25 * i))

        else:
            continue
    
    # Flashcards
    draw.rect(screen, (0, 0, 0), (445, 25, 1100, 400), 2)

    display.flip()
    time.Clock().tick(60)
    frame += 1