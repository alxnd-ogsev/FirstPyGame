import pygame

pygame.init()

screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("First Game")

# Character atribute
x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100) # Clock (ms)
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If red x is pressed
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel

    if keys[pygame.K_UP] and y > vel:
        y -= vel

    if keys[pygame.K_DOWN] and y < screenHeight - height - vel:
        y += vel


    win.fill((0,0,0))
    

    # Charact representation
    pygame.draw.rect(win, (255,0,0), (x, y, width, height)) # Create a rectangle in the window which is red and has
    pygame.display.update()

pygame.quit()
