from PIL import Image


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


if __name__ == "__main__":
    im = Image.open('./input_data/test.jpg')
    print(im.size)
