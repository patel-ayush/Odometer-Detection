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
