# 🥭🥭🥭 MangoDiseaseOrg

MangoDiseaseOrg is a web-based orchard management platform designed to assist mango growers in identifying, recording, and planning for diseases and pests affecting their orchards. The application supports data entry, automated orchard inspection planning, and risk-based recommendations.

## 🌱 Features

- **Admin Dashboard**
  Log in as an admin to access advanced features for managing diseases, locations, and mango varieties.
- **Planner**
  Automatically generate orchard inspection schedules based on disease/pest risk levels.
- **Record Findings**
  Log disease and pest findings for each orchard to track orchard health over time.
- **Orchard Management**
  Add and manage multiple orchards with specific locations and mango varieties.
- **Disease & Pest Database**
  Maintain a centralized knowledge base of mango diseases, their symptoms, and regional impact.

## 🚀 Live Demo

Visit the live application:
🔗 [MangoDiseaseOrg on PythonAnywhere](https://franksnelling.eu.pythonanywhere.com)

## 🔐 Roles & Access

- **Admin**: Full access to disease entry, location and variety management.
- **Registered Users**: Can create and manage orchards, open cases, record findings, and generate inspection schedules.

## ⚙️ Tech Stack

- **Framework**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default, easily swappable)
- **Forms**: Django's built-in forms and `ModelForm`s
- **Authentication**: Django Auth system
- **Image Handling**: Pillow
- **Scientific Computation**: SciPy (for risk modeling and scheduling)

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/mango-disease-app.git
cd mango-disease-app
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (for admin tools)
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` in your browser.

## 🔍 Example Use Cases

Farmers can view recommended inspection intervals and plan field visits.
Agricultural researchers can analyze disease spread by location and mango variety.
Admins can update the disease database with new findings and recommendations.

## 🧠 Risk Planning Logic
The app uses a weighted risk score algorithm to determine which orchards require more frequent inspections. Key components:

| Factor                  | Description                                            | Weight |
| ----------------------- | ------------------------------------------------------ | ------ |
| Severity                | Max disease severity among active cases                | 0.15   |
| Spreadability           | Max disease spreadability                              | 0.15   |
| Variety Susceptibility  | Variety's susceptibility to observed diseases          | 0.025  |
| Location Susceptibility | Region-specific disease risk                           | 0.025  |
| Stocking Rate           | Tree density (trees per area)                          | 0.20   |
| Last Inspection         | Time since last inspection                             | 0.05   |
| Seasonal Risk           | Seasonal disease/pest likelihood (based on hemisphere) | 0.25   |
| Sensitivity             | % of orchard sampled in last check                     | 0.15   |

All inputs are normalized to a 0–1 scale. The final risk score helps prioritize inspections.

## 🛠 Admin Tools
Once logged in as a superuser (admin), you can:
- Add/edit/delete diseases, varieties, and orchard locations.
- Promote other people to be admins and add them to the authors page.

## 🧪 Sample Test Users
### Normal User Test
- Username: `testuser`
- Password: `testpass`
> You can use this account to explore the app without affecting real data

### Admin User Test
- Username: `testadmin`
- Password: `testadmin`

## 📂 Project Structure
```bash
mango_disease_app/
├── models.py           # Core database models
├── views/              # View logic
├── forms.py            # Form classes
├── templates/          # HTML templates and templatetags
├── services/planner.py # Risk calculation logic
├── static/             # CSS, images
```

## 📝  Disclaimer

*This website is for learning purposes only, for a university project. It is not constructed to be used in industry.*

## 👥 Authors

This project was developed by students at Charles Darwin Univeristy as a learning project. See About page for more credits. 

## 🙏 Acknowledgments

Special thanks to the open-source community for providing invaluable libraries and tools that made this project possible. Thanks to resources online for providing the information about mango diseases and pests.

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](/LICENSE) file for details.
