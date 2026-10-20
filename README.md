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


---

###  Installation & Local Setup

**1. Clone the repository**
```bash
git clone https://github.com/shaik-tanveer-dev/jobtrack.git
cd jobtrack2. Create virtual environmentbashpython -m venv venv
venv\Scripts\activate3. Install dependenciesbashpip install -r requirements.txt4. Run the appbashpython app.pyApp runs at http://127.0.0.1:5000🚀 DeploymentLive on Render FREE tier: https://jobtracker-1-0jse.onrender.comTo deploy your own:Push to GitHubGo to render.com -> New Web Service -> Connect repoBuild: pip install -r requirements.txtStart: gunicorn app:appDeploy📖 How to UseRegister on Live DemoLoginAdd job applicationsUpdate status on interview callsSearch and filter to track progress👨‍💻 AuthorShaik TanveerGitHub: https://github.com/shaik-tanveer-dev/Portfolio: https://github.com/shaik-tanveer-dev/Location: Guntur, Andhra Pradesh, IndiaProject: JobTrack📄 LicenseMIT License⭐Star this repo if you found it useful!javascript
---

Done! Now just:

1. Go to your repo `jobtrack` on GitHub
2. Click `Add file -> Create new file`
3. Name: `README.md`
4. Paste this full content
5. Commit
