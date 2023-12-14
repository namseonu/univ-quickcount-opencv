# 🔢 Quick Count 🔢
- Gachon University
- 2023-2 Open Source Software Course
- Term Project
- Team 68 (Nam Seonwoo)

## 1. Introduction
This is a program that counts the number of people in a image. It is implemented using YOLO, a deep learning algorithm. You can compete with OpenCV to see who is faster and more accurate. It is just game for fun and studying OpenCV.

### 1.1 Objectives
- <u>To learn how to use OpenCV and YOLO</u> with fun.
- To learn how to use other python packages/libraries.

### 1.2 The manual of 'Quick Count' game:
1. Start the game by pressing the 'Start' button.
2. The image is displayed on the screen for about 1 second.
3. The image disappears and the user must enter the number of people in the image.
4. After entering the number, press the 'Confirm' button.
5. Next, the processed image by OpenCV/YOLO is displayed on the screen with bounding boxes detecting people.
6. The result of OpenCV/YOLO is displayed on the bottom of screen with processed image.
7. If press the 'Next' button, the next image is displayed on the screen.
8. Repeat the above steps until the game is over, i.e., all images are displayed.
9. The result of the game is displayed on the screen.
10. Finally, press the 'Close' button to exit the game.

### 1.3 Demo (.gif)


![image](https://github.com/namseonu/univ-quickcount-opencv/assets/77925666/3e7c0f56-0d0b-491f-8d65-015d777873f6)  
![image](https://github.com/namseonu/univ-quickcount-opencv/assets/77925666/6b0c24ad-64b4-458a-8b6d-71f5686e104c)  
![image](https://github.com/namseonu/univ-quickcount-opencv/assets/77925666/c64b82fd-f9c6-4efe-83cc-405860ea7cb7)    
![image](https://github.com/namseonu/univ-quickcount-opencv/assets/77925666/a7d22516-335f-4146-9af5-90bf5bd7f364)  
![image](https://github.com/namseonu/univ-quickcount-opencv/assets/77925666/fe2df917-8737-4bfa-a900-783f2a1fc4fc)  


<br/>

## 2. Used Packages and Versions
| Package | Version | Description                                    |
|:--------|:--------|:-----------------------------------------------|
| Python  | 3.8.5   | Programming language                           |
| OpenCV  | 4.5.3   | A library image processing and computer vision |
| Numpy   | 1.19.5  | Used to handle arrays                          |
| PyQt5   | 5.15.4  | GUI programming                                |

More details are in the requirements.txt file.  
You can install the packages using the following command:
```bash
pip install -r requirements.txt
```

<br/>

## 3. How to Install or Execute
🌟 If you want to execute this program, then follow the guideline below. 🌟
1. Download the YOLOv3 weights file from [here](https://pjreddie.com/media/files/yolov3.weights).
2. Download the YOLOv3 configuration file from [here]()
3. The files should be located in the 'opencv' package. (like below)
4. Install the packages in the requirements.txt file.
5. <u>Execute the 'main.py' file.</u>

```plain text
.
├── README.md
├── image
│ ├── 01_people_by_AdinaVoicu.jpg
│ ├── 02_people_by_Pexels.jpg
│ ├── 03_people_by_StefanSchweihofer.jpg
│ ├── 04_people_by_StockSnap.jpg
│ └── 05_people_by_WernerHieber.jpg
├── main.py
├── model
│ ├── __init__.py
│ ├── __pycache__
│ │ ├── __init__.cpython-38.pyc
│ │ └── answer.cpython-38.pyc
│ └── answer.py
├── opencv
│ ├── __init__.py
│ ├── __pycache__
│ │ ├── __init__.cpython-38.pyc
│ │ └── counting_people.cpython-38.pyc
│ ├── counting_people.py
│ ├── yolov3.cfg
│ └── yolov3.weights
├── requirements.txt
└── ui
    ├── __init__.py
    ├── __pycache__
    │ ├── __init__.cpython-38.pyc
    │ └── main_window.cpython-38.pyc
    └── main_window.py
```
The directory structure as above is my project structure. The 'pycache' file (.pyc) is automatically created when the program is executed. So, you don't have to care about it. At this point, you can execute the program by typing the following command:
```bash
python main.py
```

<br/>

## 4. References
- [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/)
- [[Deep Learning] YOLOv3 Extract Object](https://blog.naver.com/engineerjkk/222266582310)
