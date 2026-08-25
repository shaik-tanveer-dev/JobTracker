JobTrack — Job Application Tracker

JobTrack is a full-stack web application that helps users manage and track their job applications in one place.

Users can create an account, add job applications, update their application status, search and filter applications, and view statistics about their job search progress.

🌐 **Live Demo:** https://jobtracker-1-0jse.onrender.com


## Features

### User Authentication
- User registration
- User login and logout
- Password hashing
- Session-based authentication
- User-specific application data

### Job Application Management
- Add new job applications
- View all applications
- Edit existing applications
- Delete applications
- Track application status

### Search & Filtering
- Search applications by company or job role
- Filter applications by status
- Clear filters

### Dashboard & Statistics
- Total applications
- Interview count
- Selected applications
- Recent applications
- Application progress overview

### Security
- Password hashing using Werkzeug
- Flask session authentication
- User-level authorization
- Server-side form validation
- Environment-based secret key
- Protected application routes

---

## Technologies Used

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- Werkzeug

### Frontend
- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Database
- SQLite

### Deployment
- GitHub
- Render
- Gunicorn

---

## Project Structure

```text
JobTrack/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── applications.html
│   ├── add_application.html
│   └── edit_application.html 
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── venv/
