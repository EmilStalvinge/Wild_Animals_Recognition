import json
import cv2
import os


def export_cropped_images(json_file, image_folder, output_folder):
    with open(json_file) as f:
        data = json.load(f)
    for images in data['images']:
        s1 = images['file']
        s2 = "\\"
        filename = s1[s1.index(s2) + len(s2):]
        img = cv2.imread(image_folder + filename)
        for detections in images['detections']:
            if img is not None:
                h, w = img.shape[:2]
                # bbox = [x_min, y_min, width_of_box, height_of_box];
                x_min = int(w * detections['bbox'][0])
                y_min = int(h * detections['bbox'][1])
                x_max = int(w * (detections['bbox'][0] + detections['bbox'][2]))
                y_max = int(h * (detections['bbox'][1] + detections['bbox'][3]))
                cropped_image = img[y_min:y_max, x_min:x_max]
                if cropped_image is not None:
                    img_name = 'cropped_'+filename
                    #print(img_name)
                    cv2.imwrite(os.path.join(output_folder, img_name), cropped_image)
    print('cropped images exported')
    return


def main():
    image_folder = 'C:/Users/emils/Pictures/kagglecatsanddogs_3367a/PetImages/ny/'
    output_folder = 'C:/Users/emils/Pictures/kagglecatsanddogs_3367a/PetImages/output/'
    json_file = 'hittadedjur.json'
    export_cropped_images(json_file, image_folder, output_folder)


if __name__ == '__main__':
    main()

