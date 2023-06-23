import subprocess
import cv2
import os
import shutil
import easyocr
import matplotlib.pyplot as plt
import subprocess
import pandas as pd
import numpy as np
from helper import *
import argparse
import subprocess
from PIL import Image

reader = easyocr.Reader(['en'])

exp_path = os.path.join(os.path.join("runs","detect"),"exp")
if os.path.exists(exp_path):
    shutil.rmtree(exp_path)

parser = argparse.ArgumentParser()
parser.add_argument("test_images_path", help="Path to test images folder")
args = parser.parse_args()

test_folder = args.test_images_path

if os.path.exists("runs"):
    print("Removed")
    shutil.rmtree("runs")
    
print('[INFO] : Detecting odometer from dashboards...')
command = f"python yolov7/detect.py --weights best.pt --source {test_folder} --save-txt"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

if not os.path.exists("runs"):
    command = f"python3 yolov7/detect.py --weights best.pt --source {test_folder} --save-txt"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

if result:
    df_results = pd.DataFrame(columns=["filename", "reading"])

    print('[INFO] : Extracting readings from odometer ...')
    for img_path in os.listdir(test_folder)[:2]:
        print("Image name : ",img_path)

        if not os.path.exists("crp_img_for_predictions"):
          os.mkdir("crp_img_for_predictions")
          
        out_path = os.path.join("crp_img_for_predictions", img_path)
        fn =img_path.split('.')[0]
        lab_path =os.path.join(os.path.join(exp_path,"labels"),f"{fn}.txt")
        
        img = cv2.imread(os.path.join(test_folder,img_path))
        if os.path.exists(lab_path):
            with open(lab_path,'r') as f:
                bboxes = f.readlines()
                
            bboxes =clean_bb_list(bboxes)
            bbox = find_box_with_least_area(bboxes)

            crp =crop_from_yolo(bbox,img)
            
            img =increase_resolution(crp,out_path)
          
            results = reader.readtext(out_path)

            readings = [clean_reading(i[-2]) for i in results]
            reading = string_with_most_numbers(readings)    
            print("results :",reading)
            print(10*'###')
            
            #df_results = df_results.append({"filename": img_path, "reading": reading}, ignore_index=True)
            new_row = pd.DataFrame({"filename": [img_path], "reading": [reading]})
            df_results = pd.concat([df_results, new_row], ignore_index=True)

        else:
            print("No predictions")
            print(10*'###')
            #df_results = df_results.append({"filename": img_path, "reading": "No predictions"}, ignore_index=True)
            new_row = pd.DataFrame({"filename": [img_path], "reading": ["No predictions"]})
            df_results = pd.concat([df_results, new_row], ignore_index=True)
            
    df_results.to_csv("prediction_readings.csv", index=False)