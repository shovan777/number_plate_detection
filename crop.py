"""Crop image and zoom in"""
import cv2


def display_img(img_array):
    """Display image in window and close on keypress"""
    # image = cv2.imread(img_path)
    cv2.imshow(winname="original", mat=img_array)
    cv2.waitKey(0)

def resize_img(img_array, img_h, img_w, keep_ratio=False, shrink=True):
    """Resize image into given dimension."""
    new_dim = (img_h, img_w)
    if keep_ratio:
        ratio = float(img_h) / img_array.shape[1]
        new_dim = (img_h, int(img_array.shape[0] * ratio))

    if not shrink:
        inter_alg = cv2.INTER_CUBIC
    resized = cv2.resize(image, new_dim, interpolation = cv2.INTER_AREA)
    cv2.resize
    return resized


def crop_img(img_array, x_left, x_right, y_bottom, y_top):
    """
    Crop the image in the bounding box.
    wow cropping is so easy didnt think so
    just slice the img_array like a numpy img_array
    """
    cropped = img_array[y_bottom:y_top, x_left:x_right]
    return cropped



image = cv2.imread("PUL070BEX440.png")
# display_img(image)
print(image.shape)
print(resize_img(image, 220, 210, True).shape)

display_img(crop_img(image, 40, 440, 60, 320))
