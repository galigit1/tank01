import numpy as np
from PIL import Image
import math

resolution = 10  # the resolution of the tiff map, in meters

# HISTMIN = -291.677448852539
# HISTMAX = 3066.575153930664
HISTMIN = 0
HISTMAX = 3200
RANGE_COLORS = 256

def matrix_from_tiff(filename: str) -> np.ndarray:
    """
    Get a tiff file and return a 2d matrix such that for each
    location (x, y) on the map contains the actual height of
    this point (in meters).

    :param filename: .tiff filename
    :return: 2d matrix (np.ndarray) as described above.
    """
    heigth_array = []
    photo = Image.open(filename)
    data = np.array(photo)
    img_arr = np.array(data)
    for i in range(img_h_pxl):
        for j in range(len(img_w_pxl):
            heigth_in_x_y = colored_to_heigth(i, j, img_arr)
            heigth_array.append(heigth_in_x_y)

    img_w_pxl = img_arr.shape[1]
    img_h_pxl = img_arr.shape[0]
    return img_arr, img_w_pxl, img_h_pxl


def aerial_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Calculate the aerial distance between 2 points.

    :param x1: x-position of point 1.
    :param y1: y-position of point 1.
    :param x2: x-position of point 2.
    :param y2: y-position of point 2.
    :return: the aerial distance between the given points.
    """
    p = [x1, y1]
    q = [x2, y2]
    return(math.dist(p, q))

def real_3d_distance(x1: int, y1: int, x2: int, y2: int, img_arr,  img_w_pxl, img_h_pxl, air_distance) -> float:
    """
    Calculate the 3D distance between 2 points.

    :param x1: x-position of point 1.
    :param y1: y-position of point 1.
    :param x2: x-position of point 2.
    :param y2: y-position of point 2.
    :return: the aerial distance between the given points.
    """
    # calculate for each x and y index in the array
    # get color (0 - 255) for each index
    # calculate color difference
    # calculate distance by air distance and color difference = 3D distance

    if x1 >= 0 and x1 <= img_w_pxl and y1 >= 0 and y1 <= img_h_pxl:
        color_by_cord_A = img_arr[y1-1][x1-1]

    # from array to 1 number
    if x2 >= 0 and x2 <= img_w_pxl and y2 >= 0 and y2 <= img_h_pxl:
        color_by_cord_B = img_arr[y2-1][x2-1]

    max_color = img_arr.max()
    min_color = img_arr.min()
    height_range = HISTMAX - HISTMIN
    meters_per_color = height_range/RANGE_COLORS
    height_by_cord_A = get_real_heigth(color_by_cord_A[0], meters_per_color)
    height_by_cord_B = get_real_heigth(color_by_cord_B[0], meters_per_color)

    print(height_by_cord_A, height_by_cord_B)

    if height_by_cord_A > height_by_cord_B:
        difference_height = height_by_cord_A - height_by_cord_B

    if height_by_cord_B > height_by_cord_A:
        difference_height = height_by_cord_B - height_by_cord_A

    real_3d_dist = math.sqrt(air_distance**2 + difference_height**2)
    print(real_3d_dist)


def colored_to_heigth(color_by_cord, meters_per_color):
     return color_by_cord * meters_per_color


def get_by_index(y, x, img_arr):
    color_by_cord = img_arr[y][x]



def is_in_sightline(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    Check if there's a s sightline between 2 points.
    For instance, there might be a mountain between them.
    This is useful if we want to know whether we can send a laser
    ray between 2 points.

    :param x1: x-position of point 1.
    :param y1: y-position of point 1.
    :param x2: x-position of point 2.
    :param y2: y-position of point 2.
    :return: True if there's a linesight, otherwise return False.
    """

    pass

def trim(x1, y1, x2, y2):
    width = abs(x1 - x2)
    heigh = abs(y1-y2)
    box - (x1, y1, x2, y2)
    cropped_image = image.crop(box)

def trim_rac(x1, y1, x2, y2, meters_per_color):
    width = abs(x1 - x2)
    height = abs(y1-y2)
    Medium_width_point = width/2
    Middle_height_point = height/2
    color_by_cord_Midpoint = img_arr[Middle_height_point-1][Medium_width_point-1]

    # get_real_heigth(color_by_cord_Midpoint, meters_per_color)


def main():
    img_arr, img_w_pxl, img_h_pxl = matrix_from_tiff("map.tiff")
    i_cord_x1 = 1
    i_cord_y1 = 23
    i_cord_x2 = 9
    i_cord_y2 = 18
    if i_cord_x1 < img_w_pxl and i_cord_x2 < img_w_pxl and i_cord_y1 < img_h_pxl and i_cord_y2 < img_h_pxl:
        air_distance = aerial_distance(i_cord_x1, i_cord_y1, i_cord_x2, i_cord_y2)
        real_3d_distance(i_cord_x1, i_cord_y1, i_cord_x2, i_cord_y2, img_arr,  img_w_pxl, img_h_pxl, air_distance)


if __name__ == "__main__":
    main()
