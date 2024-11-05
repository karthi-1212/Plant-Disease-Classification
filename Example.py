import cv2
from matplotlib import pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

# Load the model
filepath = r'D:\VIT\Sem 3\DL\Projects\Festival\Plant-Leaf-Disease-Prediction-main2\Plant-Leaf-Disease-Prediction-main\model.h5'
model = load_model(filepath)
print("Model Loaded Successfully")

# Load and preprocess the image
image_path = r'D:\VIT\Sem 3\DL\Projects\Festival\Plant-Leaf-Disease-Prediction-main2\Plant-Leaf-Disease-Prediction-main\Dataset\test\Tomato___Bacterial_spot (1).JPG'
tomato_plant = cv2.imread(image_path)

if tomato_plant is None:
    print("Error: Image not loaded. Check the file path or format.")
else:
    # Resize and preprocess the image
    test_image = cv2.resize(tomato_plant, (128, 128))
    test_image = img_to_array(test_image) / 255.0  # Normalize the image
    test_image = np.expand_dims(test_image, axis=0)  # Convert to 4D for model input

    # Model prediction
    result = model.predict(test_image)
    pred = np.argmax(result, axis=1)[0]  # Get the predicted class index

    # Mapping the prediction to disease names
    disease_dict = {
        0: "Tomato - Bacterial Spot Disease",
        1: "Tomato - Early Blight Disease",
        2: "Tomato - Healthy and Fresh",
        3: "Tomato - Late Blight Disease",
        4: "Tomato - Leaf Mold Disease",
        5: "Tomato - Septoria Leaf Spot Disease",
        6: "Tomato - Target Spot Disease",
        7: "Tomato - Yellow Leaf Curl Virus Disease",
        8: "Tomato - Tomato Mosaic Virus Disease",
        9: "Tomato - Two-Spotted Spider Mite Disease"
    }

    # Print the prediction
    print(disease_dict.get(pred, "Unknown Disease"))
