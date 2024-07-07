# Computer Vision RPS

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description
Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock.

The player who shows the first option that beats the other player's option wins.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Michaelaicore/computer-vision-rock-paper-scissors30.git
    ```
2. Navigate to the project directory:
    ```bash
    cd computer-vision-rock-paper-scissors30
    ```

## Usage
1. Go to [Teachable-Machine](https://teachablemachine.withgoogle.com/) to creat a model with four classes, Nothing, Rock, Paper and Scissors. Each class is trained with images of yourself showing each option to the camera. The more images you train with, the more accurate the model will be.
Download the model from the "Tensorflow" tab in Teachable-Machine. The model should be named keras_model.h5 and the text file containing the labels should be named labels.txt to replace those two files in converted_keras folder.

2. Run the Python script:
    ```bash
    python main/camera_rps.py
    ```
3. Follow the instructions on the screen to play the word guessing game.

## File Structure
```
├── converted_keras
│   ├── keras_model.h5
│   └── labels.txt
├── __init__.py
├── main
│   ├── camera_rps.py
│   ├── __init__.py
│   ├── manual_rps.py
│   └── __pycache__
│       ├── camera_rps.cpython-38.pyc
│       └── __init__.cpython-38.pyc
├── README.md
├── requirements.txt
└── test
    ├── __init__.py
    ├── __pycache__
    ├── test_camera_rps.py
    └── test_manual_rps.py
```


## License
This project is licensed under the [MIT License](LICENSE).