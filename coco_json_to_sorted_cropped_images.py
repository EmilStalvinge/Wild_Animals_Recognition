import json
import cv2
import os

'''
categories: "images": [
                     {
                     "id": "1",
                     "file_name": "1.jpg",
                     "width": 1920,
                     "height": 1080
                     },
            "annotations": [
                           {
                          "id": "d8e94bd2-1df9-11ea-8572-5cf370671a19",
                             "image_id": "1",
                             "category_id": 0,
                          "bbox": [
                            5.47008,
                            974.4170399999999,
                            162.279168,
                            72.97300800000001
                            ]
                            },
'''


# make a folder
def export_cropped_images(json_file, image_folder, output_folder):
    with open(json_file) as f:
        data = json.load(f)

    for annotations in data['annotations']:
        category = annotations['category_id']
        filepath = image_folder + annotations['image_id'] + ".jpg"
        img = cv2.imread(filepath)
        output_foldername = output_folder + str(category) + '/'
        os.makedirs(os.path.dirname(output_foldername), exist_ok=True)

        if img is not None:
            # bbox = [x_min, y_min, width_of_box, height_of_box];
            x_min = int(annotations['bbox'][0])
            y_min = int(annotations['bbox'][1])
            x_max = int(annotations['bbox'][0] + annotations['bbox'][2])
            y_max = int(annotations['bbox'][1] + annotations['bbox'][3])
            cropped_image = img[y_min:y_max, x_min:x_max]
            if cropped_image is not None:
                img_name = 'cropped_' + annotations['image_id'] + ".jpg"
                print(img_name)
                cv2.imwrite(os.path.join(output_foldername, img_name), cropped_image)
    print('cropped images exported')

def main():
    image_folder = 'C:/Users/emils/Pictures/en24/'
    output_folder = 'C:/Users/emils/Pictures/en_24_categories/'
    json_file = 'C:/Users/emils/Pictures/ena24.json'
    export_cropped_images(json_file, image_folder, output_folder)


if __name__ == '__main__':
    main()

