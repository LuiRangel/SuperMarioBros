import pygame
import sys
from time import sleep

class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    def __str__(self): return 'eventloop, finished=' + str(self.finished) + ')'

    @staticmethod
    def check_events(ai_settings, menu, pacman):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                EventLoop.check_keydown_events(event, pacman)
            if event.type == pygame.KEYUP:
                EventLoop.check_keyup_events(event, pacman)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                EventLoop.check_play_button(ai_settings, menu, mouse_x, mouse_y)


    @staticmethod
    def check_keydown_events(event, pacman):
        if event.key == pygame.K_RIGHT:
            pacman.moving_right = True
            pacman.orientation = "Right"
        elif event.key == pygame.K_LEFT:
            pacman.moving_left = True
            pacman.orientation = "Left"
        elif event.key == pygame.K_UP:
            pacman.moving_up = True
            pacman.orientation = "Up"
        elif event.key == pygame.K_DOWN:
            pacman.moving_down = True
            pacman.orientation = "Down"
        elif event.key == pygame.K_q:
            sys.exit()

    @staticmethod
    def check_keyup_events(event, pacman):
        if event.key == pygame.K_RIGHT:
            pacman.moving_right = False
        elif event.key == pygame.K_LEFT:
            pacman.moving_left = False
        elif event.key == pygame.K_UP:
            pacman.moving_up = False
        elif event.key == pygame.K_DOWN:
            pacman.moving_down = False

    @staticmethod
    def check_play_button(ai_settings, menu, mouse_x, mouse_y):
        """Starts a new game when the player clicks play"""
        button_clicked = menu.play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not ai_settings.finished:
            #pygame.mixer.music.play(0)

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
            ai_settings.finished = True

    @staticmethod
    def update_collisions(ai_settings, pacman, ghosts):
        if pygame.sprite.spritecollideany(pacman, ghosts):
            EventLoop.pacman_ghost_collide(ai_settings, pacman, ghosts)

    @staticmethod
    def pacman_ghost_collide(ai_settings, pacman, ghosts):
        ghost_collision = pygame.sprite.groupcollide(ghosts, pacman, True, True)
        if ghost_collision:
            if ai_settings.lives > 0:
                ai_settings.live -= 1

                pacman.center_pacman()
                sleep(1)
            else:
                EventLoop.finished = True
