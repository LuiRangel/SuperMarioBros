import sys
import pygame


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    @staticmethod
    def check_events(ai_settings, menu):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                EventLoop.check_keydown_events(event)
            # if event.type == pygame.KEYUP:
            #     EventLoop.check_keyup_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                EventLoop.check_play_button(ai_settings, menu, mouse_x, mouse_y)

    @staticmethod
    def check_keydown_events(event):
        if event.key == pygame.K_RIGHT:
            print('right')
            # pacman.moving_right = True
            # pacman.orientation = "Right"
        elif event.key == pygame.K_LEFT:
            print('left')
            # pacman.moving_left = True
            # pacman.orientation = "Left"
        elif event.key == pygame.K_UP:
            print('up')
            # pacman.moving_up = True
            # pacman.orientation = "Up"
        elif event.key == pygame.K_DOWN:
            print('down')
            # pacman.moving_down = True
            # pacman.orientation = "Down"
        elif event.key == pygame.K_q:
            sys.exit()

    # @staticmethod
    # def check_keyup_events(event):
    #     if event.key == pygame.K_RIGHT:
    #         pacman.moving_right = False
    #     elif event.key == pygame.K_LEFT:
    #         pacman.moving_left = False
    #     elif event.key == pygame.K_UP:
    #         pacman.moving_up = False
    #     elif event.key == pygame.K_DOWN:
    #         pacman.moving_down = False

    @staticmethod
    def check_play_button(ai_settings, menu, mouse_x, mouse_y):
        """Starts a new game when the player clicks play"""
        button_clicked = menu.play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not ai_settings.finished:
            pygame.mixer.music.play(1, 0.0)

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
            ai_settings.finished = True
            print('hi')
