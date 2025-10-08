# CityXplore 🌆

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

**CityXplore** is a Django-based web application that helps users discover cities, tourist spots, and local experiences. Users can explore destinations, plan tours, and view travel guides in an interactive, user-friendly interface.  

---

## 🌐 Demo

![CityXplore Demo](https://your-demo-gif-link.com/demo.gif)  
*Example of the CityXplore dashboard and city discovery features*

---

## ⚡ Features

- Explore cities, tourist spots, and local attractions  
- Interactive maps and travel guides  
- User authentication (Sign up, login, profile)  
- Add favorite places and plan tours  
- Responsive design for web and mobile  

---

## 🛠 Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap  
- **Backend**: Python, Django  
- **Database**: SQLite / PostgreSQL  
- **Maps & APIs**: Google Maps API / OpenStreetMap (optional)  
- **Data Handling**: Pandas, JSON for API responses  

---

## 🚀 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/CityXplore.git
cd CityXplore

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run server
python manage.py runserver
