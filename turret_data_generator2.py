from insert_image import insert_image, random_point, random_size
from os import listdir
from random import randint

inserting_images_dir = 'C:\\Users\\chh36\\Desktop\\turret_training_images\\'
original_images_dir = 'C:\\Users\\chh36\\Desktop\\turret\\primary\\original_data\\'

inserting_images = []
original_images = listdir(original_images_dir)
coordinates = []

raw_cor = open('C:\\Users\\chh36\\Desktop\\turret_cor.txt', 'r').readlines()
for cor in raw_cor:
    txt = cor.split('\n')[0]
    txts = txt.split('|')
    inserting_images.append(txts[0])
    x = int(txts[1])
    y = int(txts[2])
    coordinates.append((x, y))

for i, original_image in enumerate(original_images):
    size = random_size((500, 600), (600, 699))
    point = random_point(size)
    img_index = randint(0, 3)
    front_img = inserting_images[img_index]
    x, y = coordinates[img_index]

    new_x = (size[0]*x)/700
    new_y = (size[1]*y)/700
    new_x, new_y = new_x+point[0], new_y+point[1]
    saving_txt = '{}|{}|{}\n'.format(i, new_x, new_y)
    file = open('C:\\Users\\chh36\\Desktop\\train_cor.txt', 'a')
    file.write(saving_txt)
    file.close()

    img = insert_image(original_images_dir + original_image, inserting_images_dir + front_img, size, point)
    img.save('C:\\Users\\chh36\\Desktop\\turret\\primary\\dataset\\{}.png'.format(i))

