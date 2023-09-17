# Datature-Ultralytics YOLOv8 Model Guide

This guide is for carrying out predictions using exported Ultralytics YOLOv8 models trained with Datature.


## Requirements

To use GPU, the CUDA requirement is >= 11.2. 

Install the required packages using:

`pip3 install -r requirements.txt`


## Making Predictions

The `predict.py` file can be run as follows:

```shell
python predict.py -i "Val" -m "datature-yolov8n.pt" -t 0.5
```

**input_folder_path** refers to the path to the folder where the images for prediction are stored.

**model_path** refers to the path to saved_model (not the saved_model directory)

**threshold** refers to the threshold value in range (0.0, 1.0) for the prediction score. Only predictions with scores above the threshold value will be shown on the output image. 
