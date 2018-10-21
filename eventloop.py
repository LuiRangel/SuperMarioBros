import sys
import pygame


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    @staticmethod
    def check_events(ai_settings):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                EventLoop.check_keydown_events(event)
            if event.type == pygame.KEYUP:
                print("placeholder")

    @staticmethod
    def check_keydown_events(event):
        if event.key == pygame.K_q:
            sys.exit()
