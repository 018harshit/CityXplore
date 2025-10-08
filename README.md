# CityXplore 🌆

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

**CityXplore** is a Django-based web application that helps users discover cities, tourist spots, and local experiences. Users can explore destinations, plan tours, and view travel guides in an interactive, user-friendly interface.  

---

## 🌐 Live Demo

Check out the live application here: [CityXplore Live](https://cityxplore.onrender.com/)  

### Dashboard
![Dashboard Demo](static/images/demo-dashboard.gif)  
*Explore featured cities and top tourist attractions*

### City Details
![City Details Demo](static/images/demo-city-details.gif)  
*View city information, maps, and top spots*

### Favorite Places
![Favorites Demo](static/images/demo-favorites.gif)  
*Add and manage your favorite places*

### Interactive Map
![Map Demo](static/images/demo-map.gif)  
*Navigate cities using interactive maps*

---

## ⚡ Features

- Browse cities, tourist spots, and local attractions  
- Interactive maps with location details  
- User authentication (Sign up, login, profile)  
- Save favorite places and plan tours  
- Responsive design for desktop and mobile  

---

## 🛠 Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap  
- **Backend**: Python, Django  
- **Database**: SQLite / PostgreSQL  
- **Maps & APIs**: Google Maps API / OpenStreetMap (optional)  
- **Data Handling**: JSON, Pandas  

---

## 🚀 Installation (Optional Local Version)

```bash
# Clone the repository
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
