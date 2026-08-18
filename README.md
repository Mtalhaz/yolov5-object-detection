# YOLOv5 Object Detection

A lightweight computer vision project built with **PyTorch and YOLOv5** for detecting people and vehicles in images.

The project uses the pretrained **YOLOv5s** model and filters detections to focus on five object classes:

- Person
- Car
- Truck
- Bus
- Motorbike

It also generates a class-frequency visualization from the detected objects.

## Overview

The application follows a simple object-detection pipeline:

```text
Input Image
    ↓
Pretrained YOLOv5s
    ↓
Object Detection
    ↓
Filter Relevant Classes
    ↓
Detection Results
    ↓
Class Distribution Visualization
```

## Features

- Pretrained YOLOv5 object detection
- Detection of people and common road vehicles
- Filtering of irrelevant object classes
- Tabular detection results with bounding-box information
- Visualized detection results
- Class-distribution chart using Pandas and Matplotlib

## Technologies

| Technology | Purpose |
|---|---|
| Python | Application development |
| PyTorch | Deep learning framework |
| YOLOv5 | Object detection |
| Pandas | Detection result analysis |
| Matplotlib | Visualization |

## Project Structure

```text
YOLOv5-Object-Detection/
├── nesnetanıma.py    # Main detection script
├── sokak.jpg         # Example input image
├── .gitignore
├── .gitattributes
└── README.md
```

## Installation

Create a Python environment and install the required packages:

```bash
pip install torch torchvision pandas matplotlib
```

The YOLOv5 model is loaded through PyTorch Hub, so the required YOLOv5 components are downloaded when the script is executed.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Mtalhaz/yolov5-object-detection.git
cd yolov5-object-detection
```

2. Make sure the input image is available as `sokak.jpg`, or change the image path in `nesnetanıma.py`.

3. Run the script:

```bash
python nesnetanıma.py
```

The script will:

1. Load the pretrained YOLOv5s model.
2. Run object detection on the input image.
3. Extract detection results into a Pandas DataFrame.
4. Keep only `person`, `car`, `truck`, `bus`, and `motorbike` detections.
5. Display the detected objects.
6. Generate a class-distribution chart.

## Example

The repository includes `sokak.jpg` as an example input image. YOLOv5 draws bounding boxes around detected objects, while the script also produces a table and a distribution chart for the selected classes.

## Notes

This project uses a pretrained YOLOv5 model rather than training a detector from scratch. It is intended as a practical demonstration of object detection, result filtering, and basic computer-vision data analysis.

## Future Improvements

Potential extensions include:

- Real-time webcam detection
- Video-based object detection
- Confidence-threshold configuration
- Saving detection results automatically
- Custom YOLOv5 training on a domain-specific dataset
- Performance evaluation with precision, recall and mAP

## License

This repository is provided for educational and portfolio purposes. See the repository for the applicable usage terms.

## Author

**Talha**

Computer Engineering

GitHub: [@Mtalhaz](https://github.com/Mtalhaz)
