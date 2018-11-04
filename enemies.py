import pygame as pg
import os


SCREEN_HEIGHT = 600
GROUND_HEIGHT = SCREEN_HEIGHT - 62


def load_all_gfx(directory, colorkey=(255, 0, 255), accept=('.png', 'jpg', 'bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name]=img
    return graphics

GFX = load_all_gfx(os.path.join("resources","graphics"))


class Enemy(pg.sprite.Sprite):
    """Base class for all enemies (Goombas, Koopas, etc.)"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

    def setup_enemy(self, x, y, direction, name, setup_frames):
        """Sets up various values for enemy"""
        self.sprite_sheet = GFX['smb_enemies_sheet']
        self.frames = []
        self.frame_index = 0
        self.animate_timer = 0
        self.death_timer = 0
        self.gravity = 1.5
        self.state = 'walk'

        self.name = name
        self.direction = direction
        setup_frames()

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.set_velocity()

    def set_velocity(self):
        """Setting velocity vector """
        if self.direction == 'left':
            self.x_vel = -2
        else:
            self.x_vel = 2

        self.y_vel = 0

    def get_image(self, x, y, width, height):
        """Getting the image frame from the sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((  0,   0,   0))


        image = pg.transform.scale(image,
                                   (int(rect.width*2.5),
                                    int(rect.height*2.5)))
        return image

    def handle_state(self):
        """Enemy behavior based on state"""
        if self.state == 'walk':
            self.walking()
        elif self.state == 'fall':
            self.falling()
        elif self.state == 'jumped on':
            self.jumped_on()
        elif self.state == 'shell slide':
            self.shell_sliding()
        elif self.state == 'death jump':
            self.death_jumping()

    def walking(self):
        """Default state of moving sideways"""
        if (self.current_time - self.animate_timer) > 125:
            if self.frame_index == 0:
                self.frame_index += 1
            elif self.frame_index == 1:
                self.frame_index = 0

            self.animate_timer = self.current_time

    def falling(self):
        """For when it falls off a ledge"""
        if self.y_vel < 10:
            self.y_vel += self.gravity

    def jumped_on(self):
        """Placeholder for when the enemy is stomped on"""
        pass

    def death_jumping(self):
        """Death animation"""
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        self.y_vel += self.gravity

        if self.rect.y > 600:
            self.kill()

    def start_death_jump(self, direction):
        """Transitions enemy to death state"""
        self.y_vel = -8
        if direction == 'right':
            self.x_vel = 2
        else:
            self.x_vel = -2
        self.gravity = .5
        self.frame_index = 3
        self.image = self.frames[self.frame_index]
        self.state = 'death jump'

    def animation(self):
        """switching between two frames"""
        self.image = self.frames[self.frame_index]

    def update(self, game_info, *args):
        """Updating enemy behavior"""
        self.current_time = game_info['current time']
        self.handle_state()
        self.animation()


class Goomba(Enemy):

    def __init__(self, y=GROUND_HEIGHT, x=0, direction='left', name='goomba'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)

    def setup_frames(self):
        """Putting the image frame for animation"""

        self.frames.append(
            self.get_image(0, 4, 16, 16))
        self.frames.append(
            self.get_image(30, 4, 16, 16))
        self.frames.append(
            self.get_image(61, 0, 16, 16))
        self.frames.append(pg.transform.flip(self.frames[1], False, True))

    def jumped_on(self):
        """mario squishies him"""
        self.frame_index = 2

        if (self.current_time - self.death_timer) > 500:
            self.kill()


class Koopa(Enemy):

    def __init__(self, y=GROUND_HEIGHT, x=0, direction='left', name='koopa'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)

    def setup_frames(self):
        """Setting the frame list"""
        self.frames.append(
            self.get_image(150, 0, 16, 24))
        self.frames.append(
            self.get_image(180, 0, 16, 24))
        self.frames.append(
            self.get_image(360, 5, 16, 15))
        self.frames.append(pg.transform.flip(self.frames[2], False, True))

    def jumped_on(self):
        """MARIO jumps on koopa and puts him in his shell"""
        self.x_vel = 0
        self.frame_index = 2
        shell_y = self.rect.bottom
        shell_x = self.rect.x
        self.rect = self.frames[self.frame_index].get_rect()
        self.rect.x = shell_x
        self.rect.bottom = shell_y

    def shell_sliding(self):
        """koopa is sliding along the ground in his shell"""
        if self.direction == 'right':
            self.x_vel = 10
        elif self.direction == 'left':
            self.x_vel = -10
