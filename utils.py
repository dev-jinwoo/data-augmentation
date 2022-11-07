from PIL import Image
import cv2


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
    :return: rotate image
    """
    rotated_image = img.rotate(angle)

    return rotated_image


def resize_image(src_img, tgt_size=512):
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


if __name__ == "__main__":
    im = Image.open('./input_data/test.jpg')

    print(im.size)
