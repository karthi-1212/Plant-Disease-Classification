
# Plant Leaf Disease Detection

## Overview

This project provides a deep learning-based solution for detecting and classifying diseases in tomato plants' leaves. Utilizing Convolutional Neural Networks (CNNs) with TensorFlow and Keras, the model is trained on a dataset of labeled leaf images, allowing it to identify various diseases and the healthy condition of tomato plants.

## Features

- **Image Classification**: Classifies tomato plant leaves into specific disease categories, including:
  - Bacterial Spot Disease
  - Early Blight Disease
  - Late Blight Disease
  - Leaf Mold Disease
  - Septoria Leaf Spot Disease
  - Target Spot Disease
  - Yellow Leaf Curl Virus Disease
  - Tomato Mosaic Virus Disease
  - Two-Spotted Spider Mite Disease
  - Healthy and Fresh

- **Web Application**: A Flask-based web interface allows users to upload images of tomato leaves and receive instant predictions regarding the health of their plants.

## Technologies Used

- Python
- TensorFlow
- Keras
- OpenCV
- Flask
- Scikit-learn
- NumPy
- Matplotlib

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tomato-leaf-disease-detection.git
   cd tomato-leaf-disease-detection
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your trained model (`model.h5`) in the appropriate directory.

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:8080`.

3. Upload an image of a tomato leaf to receive a disease prediction.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
- [scikit-learn](https://scikit-learn.org/)
