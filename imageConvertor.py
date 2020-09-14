import sys
import os
from PIL import Image

image_floder=sys.argv[1]
output_floder=sys.argv[2]

if not os.path.exists(output_floder):
	os.makedirs(output_floder)

for filename in os.listdir(image_floder):
	img=Image.open(f'{image_floder}{filename}')
	clean=os.path.splitext(filename)[0]
	img.save(f'{output_floder}{clean}.png','png')
	print('all done!')
