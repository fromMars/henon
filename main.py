#!/usr/bin/python2.7

import pyglet
import sys
from henon import get_all


# group all points into a vertical list
def get_points(a, b, x, y):
	strat_pos = henon(a, b, x, y)


# command line passed params (for example: "python main.py 1.4 0.3 0.6 0.2 100000")
try:
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	x = float(sys.argv[3])
	y = float(sys.argv[4])
	count = int(sys.argv[5])
except Exception as err_input:
	print 'Something wrong with your input:%s' % err_input
	sys.exit(0)

vertics = get_all(a, b, x, y, count)
p_count = len(vertics)/2
print 'p_count: %s' % p_count


# create pyglet window for displaying
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_default_screen()
template = pyglet.gl.Config(alpha_size=8)
config = screen.get_best_config(template)
context = config.create_context(None)
window = pyglet.window.Window(context=context)
window.set_size(1600, 1050)

# get window location & size
lx, ly = window.get_location()
sx, sy = window.get_size()


# enlarge the graph
larger_list = []
for i in range(0, p_count, 2):
	larger_list.append(vertics[i]*sx/6*1.2 + x+sx/2)
	larger_list.append(vertics[i+1]*sy*1.2 + y+sy/2)


@window.event()
def on_draw():
	for i in range(0, p_count, 2):
		tmp_point = [larger_list[i], larger_list[i+1]]
		pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2f', tmp_point))
		
	
	#pyglet.graphics.draw(p_count, pyglet.gl.GL_POINTS, ('v2f', larger_list))
	


pyglet.app.run()
