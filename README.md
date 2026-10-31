# OpenUAV-Drone-Ben

Author: BEN, Software Engineer

A small UAV / drone object-detection workflow built around YOLOv5: annotation conversion, training and detection scripts, a tutorial notebook, and a simple frame-by-frame demo script.

## What is in this repository
| Path | What it is |
|---|---|
| `scripts/convert_xml_to_yolo.py` | Converts XML (Pascal VOC style) annotations to YOLO label files |
| `scripts/DroneUAV.py` | Demo that overlays a **simulated** value on a video, computed from the frame number (not a real measurement) |
| `yolov5_custom/train.py`, `detect.py` | YOLOv5 training and detection scripts from Ultralytics (AGPL-3.0), with small edits |
| `yolov5_custom/requirements.txt` | YOLOv5 dependencies |
| `notebooks/tutorial.ipynb` | Tutorial notebook |
| `results/UAV_output_values.csv` | Output of the demo script: simulated per-frame values, **not detection accuracy** |
| `requirements.txt` | Project dependencies |
| `sample_images/` | Sample image |

## Usage
1. Install dependencies: `pip install -r requirements.txt` (and `yolov5_custom/requirements.txt` for YOLOv5).
2. Edit the folder paths at the top of `scripts/convert_xml_to_yolo.py` and the video path in `scripts/DroneUAV.py`; they point to folders on the author's computer.
3. Convert annotations, then train and detect with the YOLOv5 scripts in `yolov5_custom/`.

## Status and limits
- No trained-model accuracy (mAP, precision, recall) is reported in this repository yet.
- `results/UAV_output_values.csv` comes from a simulation rule, so it says nothing about detection quality.
- The dataset and trained weights are not included.

## License and credits
The YOLOv5 files in `yolov5_custom/` are from Ultralytics YOLOv5 (https://github.com/ultralytics/yolov5), licensed under **AGPL-3.0**.
This repository is therefore released under **AGPL-3.0**; see `LICENSE`.
