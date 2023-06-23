Approach for Odometer Recognition from Dashboard Images:

The task at hand involved identifying and reading the odometer value from a given image of a car's dashboard. The performance of the model was evaluated based on the odometer recognition accuracy. To accomplish this task, I chose to split the task into two parts: object detection to locate the odometer and Optical Character Recognition (OCR) to read the value.

The following detailed steps outline the approach:

1. Dataset Preparation:
The provided dataset contained dashboard images organized in different folders along with corresponding JSON files, which included filenames, coordinates, and odometer readings. First, I merged all the images into a single folder and created a dataframe containing filenames, coordinates, and odometer readings.

2. Object Detection Model:
I trained an object detection model to identify the odometer within the dashboard images. In this case, YOLOv7 was selected for its high accuracy and real-time object detection capabilities.

3. Coordinate Conversion:
I converted the coordinates of the odometer to YOLO format, which was necessary for training the YOLOv7 model.

4. Dataset Split:
I split the dataset into training, testing, and validation sets in an 80:10:10 ratio.

5. Model Configuration and Training:
I configured the YOLOv7 model to train on a single class (odometer) for 50 epochs, using a batch size of 16, an image size of 640, and an initial learning rate of 0.01. I used YOLOv7's hyp.scratch.p5.yaml file to set hyperparameters. I trained the YOLOv7 model on the prepared dataset and saved the best weights.

6. Odometer Localization:
I used the trained YOLOv7 model with the best weights to predict the bounding box of the odometer within the dashboard images.

7. Image Extraction:
I extracted the region of interest (ROI) corresponding to the bounding box of the odometer from the dashboard images.

8. Optical Character Recognition (OCR):
I performed OCR on the extracted ROI to read the odometer value. I compared the performance of EasyOCR, Keras OCR, and Tesseract OCR. In this case, EasyOCR significantly outperformed the other methods.

9. Inference Pipeline:
I created an inference/prediction pipeline in a Python script named test_predict.py. This script read images from a test folder, applied the trained model to locate the odometer, extracted the ROI, and performed OCR using EasyOCR. I stored the image name and its predicted odometer reading in a pandas dataframe for evaluation.

By following this approach, an efficient and accurate solution for odometer recognition from dashboard images was developed.