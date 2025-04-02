
import numpy as np
import pickle
from weather_API import get_weather_data 
import warnings
warnings.filterwarnings("ignore")

# Load ML model and label encoder
with open("rf_model.pkl", "rb") as file:
    rf_model = pickle.load(file)

with open("label_encoder.pkl", "rb") as file:
    label_encoder = pickle.load(file)


# Function to recommend crop
def recommend_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    predicted_label = rf_model.predict(input_data)
    return label_encoder.inverse_transform(predicted_label)[0]

# Main execution
if __name__ == "__main__":
    city = "Kharar"  # Example city
    weather_data = get_weather_data(city)

    if weather_data:
        print(f"Weather Data for {city}: {weather_data}")

        # Example test values for soil nutrients & pH
        test_N, test_P, test_K = 87, 50, 23
        test_ph = 6.5

        # Predict crop using real-time weather data
        test_crop = recommend_crop(
            test_N, test_P, test_K, 
            weather_data["temperature"], 
            weather_data["humidity"], 
            test_ph, 
            weather_data["rainfall"]
        )

        print(f"Recommended Crop for {city}: {test_crop}")
    else:
        print("Error fetching weather data. Check API key or city name.")
