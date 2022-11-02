import cv2

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
    img = cv2.imread('./input_data/test.jpg')

    resize_img = resize_image(img, tgt_size=300)

    cv2.imwrite('./output_data/resize.jpg', resize_img)
