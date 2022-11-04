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
    if src_img.shape[0] == tgt_size and src_img.shape[1] == tgt_size:
        return src_img

    if src_img.shape[0] > src_img.shape[1]:
        resize_ratio = tgt_size / src_img.shape[0]
    else:
        resize_ratio = tgt_size / src_img.shape[1]

    tgt_img = cv2.resize(src_img, dsize=(0, 0), fx=resize_ratio, fy=resize_ratio, interpolation=cv2.INTER_AREA)

    return tgt_img


if __name__ == "__main__":
    im = Image.open('./input_data/test.jpg')
    print(im.size)
