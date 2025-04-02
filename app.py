import streamlit as st
from realtime_recommender import recommend_crop
from weather_API import get_weather_data 

# Apply CSS for dark theme and styling
st.markdown(
    """
    <style>
        /* Dark Theme */
        body, .stApp {
            background-color: #121212;
            color: #e0e0e0;
        }
        /* Headers */
        h1, h2 {
            color: #106305;
            text-align: center;
        }
        /* input labels*/
        label {
            color: #ffffff !important;
            font-size: 16px !important;
            font-weight: bold !important;
        }
        /* Input Fields */
        .stNumberInput, .stTextInput {
            background-color: #1e1e1e;
            color: #ffffff;
            border-radius: 10px;
            padding: 10px;
            border: 1px solid #bb86fc;
        }
        /* Buttons */
        div.stButton > button {
            background-color: #106305;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
        }
        div.stButton > button:hover {
            background-color: #227305;
        }
        .recommended_crop {
            color:green;
            text-align:center;
            font-size: 24px;
            font-weight: bold;
            padding: 10px
            background-color:#ffffff;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌿 Smart Crop Recommender")

# Create two columns
col1, col2 = st.columns(2)

# Column 1: Soil Details
with col1:
    st.header(" Soil Composition")
    N = st.number_input("Nitrogen (N)", min_value=0, max_value=300, value=80)
    P = st.number_input("Phosphorus (P)", min_value=0, max_value=300, value=50)
    K = st.number_input("Potassium (K)", min_value=0, max_value=300, value=21)
    ph = st.number_input("Soil pH Level", min_value=3.5, max_value=10.0, value=6.5, step=0.1)

# Column 2: Location & Weather
with col2:
    st.header(" Location & Weather")
    city = st.text_input("Enter your city:", "Kharar")

with col2:
    if st.button("Get Recommendation"):
        weather_data = get_weather_data(city)

        if weather_data:
            st.success(f" Weather Data for {city}")
            st.write(f"🌡 **Temperature:** {weather_data['temperature']}°C")
            st.write(f"💧 **Humidity:** {weather_data['humidity']}%")
            st.write(f"🌧 **Total Yearly Rainfall:** {weather_data['rainfall']} mm")

            # Predict crop
            recommended_crop = recommend_crop(
                N, P, K,
                weather_data["temperature"],
                weather_data["humidity"],
                ph,
                weather_data["rainfall"]
            )
            #display recommended crop
            st.markdown(
                f"<div class='recommended-crop'> Recommended crop: <b>{recommended_crop}</b></div>",
                unsafe_allow_html=True
            )
           # st.subheader(f"🌱 Recommended Crop: **{recommended_crop}**")
        else:
            st.error(" Error fetching weather data. Check city name.")
