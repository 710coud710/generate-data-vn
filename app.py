from flask import Flask, render_template, jsonify
from flask_cors import CORS
from faker import Faker
import random
import json
import unidecode
import os
app = Flask(__name__)
CORS(app)

fake = Faker("vi_VN")  


def load_file(filename):  # Đảm bảo tham số filename được truyền vào
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Lấy đường dẫn thư mục hiện tại
    file_path = os.path.join(base_dir, "data", filename)  # Ghép với thư mục data
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def get_random_name(gender):
    return random.choice(male_names if gender == "Nam" else female_names)

def load_locations():
    with open("locations.json", "r", encoding="utf-8") as f:
        return json.load(f)
def get_random_address():
    province = random.choice(list(locations.keys()))  # Chọn tỉnh/thành phố
    district = random.choice(list(locations[province].keys()))  # Chọn quận/huyện
    ward = random.choice(locations[province][district])  # Chọn xã/phường

    street_number = random.randint(1, 999)  # Số nhà ngẫu nhiên

    full_address = f"{street_number}, {ward}, {district}, {province}"
    return full_address, province, district, ward
def generate_vietnam_phone():
    prefixes = ["09", "03"]  # Đầu số hợp lệ
    prefix = random.choice(prefixes)  # Chọn 09 hoặc 03
    number = "".join([str(random.randint(0, 9)) for _ in range(8)])  # Random 8 số còn lại
    return f"{prefix}{number}"  # Ghép thành số hoàn chỉnh


male_names = load_file("nam.json")
female_names = load_file("nu.json")
locations = load_file("locations.json")

def generate_fake_data():
    gender = random.choice(["Nam", "Nữ"])
    full_name = get_random_name(gender)
    email = f"{unidecode.unidecode(full_name).lower()}@gmail.com".replace(" ", "")
    username = unidecode.unidecode(full_name).lower().replace(" ", "")
    cccd = "".join([str(random.randint(0, 9)) for _ in range(12)])  # Sinh CCCD 12 số hợp lệ
    address, province, district, ward = get_random_address() 
    data = {
        "full_name": full_name,
        "gender": gender,
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=30).strftime("%d/%m/%Y"),
        "phone_number": generate_vietnam_phone(),
        "email": email,
        "address": address,
        "cccd": cccd,
        "job": fake.job(),
        "nationality": "Việt Nam",
        "company": fake.company(),
        "salary": f"{random.randint(8, 50)} triệu VND",
        "province": province,
        "district": district,
        "ward": ward,
        # "facebook_link": f"https://facebook.com/{unidecode.unidecode(full_name).replace(' ', '').lower()}",
        "facebook": f"https://www.facebook.com/{username}",
        "username": f"{username}{random.randint(1, 99)}",
    }
    return data

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/random-user", methods=["GET"])
def get_random_user():
    return jsonify(generate_fake_data())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port, debug=False) 
    # app.run(host="0.0.0.0", port=5000, debug=True)