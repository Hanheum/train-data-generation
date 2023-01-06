from insert_image import insert_image, random_point, random_size
from os import listdir

back_dir = input('background images directory:')+'\\'
back_titles = listdir(back_dir)

saving_dir_txt = input('coordinate saving file:')
saving_dir_img = input('image saving directory:')+'\\'

original_coordinate = (203, 316)
original_size = (409, 546)

front = 'C:\\Users\\chh36\\Desktop\\target.png'

for back_title in back_titles:
    back = back_dir+back_title

    front_size = random_size((300, 400), (500, 600))
    front_point = random_point(front_size)
    img = insert_image(back, front, front_size, front_point)

    resized_coordinate = ((original_coordinate[0]*front_size[0])/original_size[0], (original_coordinate[1]*front_size[1])/original_size[1])
    inserted_coordinate = (resized_coordinate[0]+front_point[0], resized_coordinate[1]+front_point[1])

    img.save(saving_dir_img+back_title)
    file = open(saving_dir_txt, 'a')
    file.write('{}|{}|{}\n'.format(back_title, round(inserted_coordinate[0]), round(inserted_coordinate[1])))
    file.close()