import cv2
from PIL import Image

def increase_resolution(img,out_path):
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = Image.fromarray(rgb_image)
    basewidth = 300
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(out_path)
                
def crop_from_yolo(yolo_coord, img):
    # Extract the YOLO coordinates
    yolo_x, yolo_y, yolo_w, yolo_h = yolo_coord
    
    # Get the height and width of the image
    h, w, _ = img.shape
    
    # Convert YOLO coordinates to pixel coordinates
    x = int(yolo_x * w - yolo_w * w / 2)
    y = int(yolo_y * h - yolo_h * h / 2)
    width = int(yolo_w * w)
    height = int(yolo_h * h)
    
    # Crop the image
    cropped_img = img[y:y+height, x:x+width]
    
    return cropped_img

def show_highest_reading(detections):
    highest_prob_detection = max(detections, key=lambda x: x[2])
    highest_reading = highest_prob_detection[1]
    print(f"Highest probability reading: {highest_reading}")

def find_box_with_least_area(bounding_boxes):
    areas = []
    for bbox in bounding_boxes:
        x, y, w, h = bbox
        area = w * h
        areas.append(area)
    
    # Find the index of the box with the smallest area
    min_area_index = areas.index(min(areas))
    
    # Return the coordinates of the box with the smallest area
    return bounding_boxes[min_area_index]

def string_with_most_numbers(strings):
    max_count = 0
    max_string = None

    for s in strings:
        count = sum(c.isdigit() for c in s)
        if count > max_count:
            max_count = count
            max_string = s

    return max_string

def clean_reading(reading):
    reading = reading.replace('{', '1')
    reading = reading.replace("'", '1')
    reading = reading.replace("k", '')  
    reading = reading.replace(",", '.')    
    reading = reading.replace("m", '')    
    reading = reading.replace('o', '0')
    reading = reading.replace('s', '5')
    reading = reading.replace('y', '4')
    reading = reading.replace('A', '8')
    reading = reading.replace('w', '')
    reading = reading.replace(' ', '')
    return reading

clean_bb_list = lambda x: [[float(k) for k in i.replace('\n',"").split(' ')[1:]] for i in x]
