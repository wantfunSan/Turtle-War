import with_ai
import turtle
from PIL import Image

def transition(point2win_x, point2win_y, non_reset):
	if non_reset == True:
		with_ai.dvizh(point2win_x, point2win_y)
	with_ai.new_point()

def change_shape():
	with_ai.player.shape('turtle')
def change_bg(file_path, image):
	resized_image = image.resize((with_ai.screen.window_width(), with_ai.screen.window_height()))
	
	resized_image.save(file_path)
	with_ai.screen.bgpic(file_path) 