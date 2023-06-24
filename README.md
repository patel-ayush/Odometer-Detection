# Odometer Recognition from Dashboard Images

This project involves identifying and reading the odometer value from given images of a car's dashboard. The model's performance is evaluated based on the odometer recognition accuracy. The task was divided into two parts: object detection to locate the odometer and Optical Character Recognition (OCR) to read the value.

## Approach

<details>
<summary>1. Dataset Preparation</summary>
The provided dataset contained dashboard images organized in different folders along with corresponding JSON files, which included filenames, coordinates, and odometer readings. The images were merged into a single folder and a dataframe was created containing filenames, coordinates, and odometer readings.
</details>

<details>
<summary>2. Object Detection Model</summary>
An object detection model was trained to identify the odometer within the dashboard images. YOLOv7 was chosen due to its high accuracy and real-time object detection capabilities.
</details>

<details>
<summary>3. Coordinate Conversion</summary>
The coordinates of the odometer were converted to YOLO format, which was necessary for training the YOLOv7 model.
</details>

<details>
<summary>4. Dataset Split</summary>
The dataset was split into training, testing, and validation sets in an 80:10:10 ratio.
</details>

<details>
<summary>5. Model Configuration and Training</summary>
The YOLOv7 model was configured to train on a single class (odometer) for 50 epochs, using a batch size of 16, an image size of 640, and an initial learning rate of 0.01. YOLOv7's hyp.scratch.p5.yaml file was used to set hyperparameters. The model was trained on the prepared dataset and the best weights were saved.
</details>

<details>
<summary>6. Odometer Localization</summary>
The trained YOLOv7 model with the best weights was used to predict the bounding box of the odometer within the dashboard images.
</details>

<details>
<summary>7. Image Extraction</summary>
The region of interest (ROI) corresponding to the bounding box of the odometer was extracted from the dashboard images.
</details>

<details>
<summary>8. Optical Character Recognition (OCR)</summary>
OCR was performed on the extracted ROI to read the odometer value. The performance of EasyOCR, Keras OCR, and Tesseract OCR was compared. In this case, EasyOCR significantly outperformed the other methods.
</details>

<details>
<summary>9. Inference Pipeline</summary>
An inference/prediction pipeline was created in a Python script named `test_predict.py`. This script read images from a test folder, applied the trained model to locate the odometer, extracted the ROI, and performed OCR using EasyOCR. The image name and its predicted odometer reading were stored in a pandas dataframe for evaluation.
</details>

## Results

<table>
 <tr>
  <th>Dashboard(Input image)</th>
  <th>Odometer(YOLO output)</th>
  <th>Reading(OCR output)</th>
 </tr>
<tr>
 <td><img src="https://drive.google.com/uc?id=1tin2e-x2QeyARfXM-YIfccJe0wri0G_a" width="320px"/>
 <td><img src="https://drive.google.com/uc?id=1OGZc-iQqQGyHVhMImU8D14XwedCORpJi" width="320px"/>
 <td>52563</td>
</td>
 <tr>
 <td><img src="https://drive.google.com/uc?id=1NVdGq-_U6C5rrgiqW-1MzZdMO59A_jOw" width="320px"/>
 <td><img src="https://drive.google.com/uc?id=1rUfKVJi1BYg-GOkrYJ9kCz6ztF46g4VV" width="320px"/>
 <td>0864i2</td>
</td>
<tr>
 <td><img src="https://drive.google.com/uc?id=17pMO7cvW1pB2bosnHJjcycBMUAGy_Qog" width="320px"/>
 <td><img src="https://drive.google.com/uc?id=1uZyg_w8kW9Ucm0TjEdX_M4Lsw0oxW1sU" width="320px"/>
 <td>24348</td>
</td>
<tr>
 <td><img src="https://drive.google.com/uc?id=15QppMAp11psj9XiHikXOjlVf5gIIsVnQ" width="320px"/>
 <td><img src="https://drive.google.com/uc?id=1EzPyKzATxlEA2dyvx_FTfMhrhiKsduJ8" width="320px"/>
 <td>38613</td>
</td>
<tr>
 <td><img src="https://drive.google.com/uc?id=1uFobIg-uQBdL7scHYfkduZlxw2qI7RlI" width="320px"/>
 <td><img src="https://drive.google.com/uc?id=1iDyJh_y54tu2UgFoBaJjliihaG4zfJpS" width="320px"/>
 <td>13557</td>
</td>
<tr>
 <td><img src="https://drive.google.com/uc?id=19ooKeAc4NS78BZh0XIh5aUbueaaHbeoF" width="320px"/>
 <td><img src="https://drive.google.com/uc?id=1ttdTkTir89oP95h19tgg4QZKPBtcWpI0" width="320px"/>
 <td>34959</td>
</tr>
<tr>
 <td><img src="https://drive.google.com/uc?id=1Fn6SRIAMmY5ifamNKXqQGMcCJ0UuY3Ie" width="320px"/>
 <td><img src="https://drive.google.com/uc?id=1Q3ryq9kjgUG_D8-dkZ7l1865emHNKyJA" width="320px"/>
 <td>34959</td>
</tr>
