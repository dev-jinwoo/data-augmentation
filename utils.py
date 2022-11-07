from PIL import Image
import random
import numpy as np


def crop_image(img, bbox):
    """
    :param img: PIL image
    :param bbox: [lx, ly, rx, ry]
    :return: cropped image
    """
    cropped_image = img.crop(bbox)

    return cropped_image


def rotate_image(img, angle):
    """
    :param img: PIL image
    :param angle: 0~360
    :return: rotated image
    """
    rotated_image = img.rotate(angle)

    return rotated_image


def resize_image(src_img, tgt_size=512):
    """
    :param src_img: PIL image
    :param tgt_size: Image size to change
    :return: resized image
    """
    width, height = src_img.size

    if width == tgt_size and height == tgt_size:
        return src_img

    if width > height:
        resize_ratio = tgt_size / width
    else:
        resize_ratio = tgt_size / height

    resize_width = int(width * resize_ratio)
    resize_height = int(height * resize_ratio)

    tgt_img = src_img.resize((resize_width, resize_height))

    return tgt_img


def occlude_image(src_img, prob=2):
    """
    :param src_img: PIL image
    :param prob: augmentation probability
          (prob = 1 : 100%, prob = 2 : 50%, prob = 3 :  33%, ...)
    :return: occluded image
    """
    aug_prob = random.uniform(0, prob)

    np_img = np.array(src_img)

    # RGB Color Codes Chart : https://www.rapidtables.com/web/color/RGB_Color.html
    color = (200 + random.randint(-30, 30), 150 + random.randint(-30, 30), 50 + random.randint(-30, 30))

    width, height = np_img.shape[0], np_img.shape[1]

    if 0 < aug_prob < 0.25:
        np_img[:, :height // 2, :] = color
    elif 0.25 < aug_prob < 0.5:
        np_img[:, height // 2:, :] = color
    elif 0.5 < aug_prob < 0.75:
        np_img[width // 2:, :, :] = color
    elif 0.75 < aug_prob < 1:
        np_img[:width // 2, :, :] = color

    tgt_img = Image.fromarray(np_img)

    return tgt_img


if __name__ == "__main__":
    im = Image.open('./input_data/test.jpg')

    print(im.size)
