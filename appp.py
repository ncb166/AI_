import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input

# Load model
model = load_model('model.keras')

# Tên class - bạn đổi nếu model của bạn khác
class_names = [
    "Tiger", "Zebra", "Lion", "Panda", "Horse",
    "Kangaroo", "Giraffe", "Dolphin", "Elephant", "Deer",
    "Dog", "Cat", "Cow", "Bear", "Bird"
]

# CSS giao diện + logo bo viền đẹp
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
    }
    .title {
        font-size: 48px;
        color: #FF6F61;
        text-align: center;
        font-weight: bold;
        padding: 10px;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.5);
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .result {
        font-size: 28px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
        background: rgba(255, 255, 255, 0.5);
        padding: 10px;
        border-radius: 10px;
    }
    .confidence {
        font-size: 20px;
        color: #2196F3;
        text-align: center;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 10px;
    }
    .logo-img {
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        max-width: 90%;
        height: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar logo
st.sidebar.markdown(
    """
    <div class="logo-container">
        <img class="logo-img" src="https://media.istockphoto.com/id/1217252882/vi/vec-to/ch%C3%BA-ch%C3%B3-corgi-x%E1%BB%A9-wales-d%E1%BB%85-th%C6%B0%C6%A1ng-v%E1%BA%ABy-ch%C3%A2n-ho%E1%BA%A1t-h%C3%ACnh-minh-h%E1%BB%8Da-vector.jpg?s=612x612&w=0&k=20&c=yZN-DSWFNX0USgx46R4ck61K08_zuW8wfuGo_75PK7Y=">
    </div>
    """,
    unsafe_allow_html=True
)
st.sidebar.title("🐾 Animal AI APP")

# Tiêu đề
st.markdown('<div class="title"> Ứng dụng Nhận diện Động vật</div>', unsafe_allow_html=True)
st.write("📸 Tải lên một bức ảnh để AI dự đoán loài động vật đó!")

# Upload ảnh
uploaded_file = st.file_uploader("Chọn ảnh động vật...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Ảnh đã tải lên", use_column_width=True)

    # Tiền xử lý
    img_resized = image.resize((224, 224))
    img_array = np.array(img_resized)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    # Dự đoán
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)

    # Hiển thị kết quả
    st.markdown(f"<div class='result'>🔍 {predicted_class}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='confidence'>Độ tin cậy: {confidence*100:.2f}%</div>", unsafe_allow_html=True)

else:
    st.info("💡 Hãy tải lên một ảnh để bắt đầu dự đoán.")
