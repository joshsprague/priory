import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'priory', False)
libtcod.sys_set_fps(LIMIT_FPS)

playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

def handle_keys():
  global playerx, playery

  #movement keys
  if libtcod.console_is_key_pressed(libtcod.KEY_UP):
    playery -= 1

  elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
    playery += 1

  elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
    playerx -= 1

  elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
    playerx += 1
    
# main loop
while not libtcod.console_is_window_closed():
  libtcod.console_set_default_foreground(0, libtcod.white)
  libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)
  libtcod.console_flush()