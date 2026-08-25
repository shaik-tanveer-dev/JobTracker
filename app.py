from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jobtrack.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

app.secret_key = "jobtrack-secret-key"

# User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


# Job Application table
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    salary = db.Column(db.String(50))
    job_url = db.Column(db.String(300))

    status = db.Column(
        db.String(50),
        default="Applied"
    )

    applied_date = db.Column(db.String(50))
    interview_date = db.Column(db.String(50))

    notes = db.Column(db.Text)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered!")
            return redirect(url_for("register"))

        # Hash password
        hashed_password = generate_password_hash(password)

        # Create user
        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please login.")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            session["user_id"] = user.id
            session["user_name"] = user.name

            return redirect(url_for("dashboard"))

        flash("Invalid email or password.")
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        flash("Please login to access the dashboard.")
        return redirect(url_for("login"))

    user_id = session["user_id"]

    # Statistics
    total_applications = Application.query.filter_by(
        user_id=user_id
    ).count()

    interviews = Application.query.filter_by(
        user_id=user_id,
        status="Interview"
    ).count()

    selected = Application.query.filter_by(
        user_id=user_id,
        status="Selected"
    ).count()

    rejected = Application.query.filter_by(
        user_id=user_id,
        status="Rejected"
    ).count()
    assessments = Application.query.filter_by(
    user_id=user_id,
    status="Assessment"
    ).count()
    applied = Application.query.filter_by(
    user_id=user_id,
    status="Applied"
    ).count()

    # Recent 5 applications
    recent_applications = Application.query.filter_by(
        user_id=user_id
    ).order_by(
        Application.id.desc()
    ).limit(5).all()

    return render_template(
        "dashboard.html",
        user_name=session["user_name"],
        total_applications=total_applications,
        applied=applied,
        assessments=assessments,
        interviews=interviews,
        selected=selected,
        rejected=rejected,
        recent_applications=recent_applications
    )

@app.route("/logout")
def logout():

    session.clear()

    flash("You have been logged out.")

    return redirect(url_for("login"))

@app.route("/applications")
def applications():

    if "user_id" not in session:
        flash("Please login first.")
        return redirect(url_for("login"))

    search = request.args.get("search", "").strip()
    status = request.args.get("status", "").strip()

    query = Application.query.filter_by(
        user_id=session["user_id"]
    )

    if search:
        query = query.filter(
            db.or_(
                Application.company.ilike(f"%{search}%"),
                Application.role.ilike(f"%{search}%")
            )
        )

    if status:
        query = query.filter_by(status=status)

    user_applications = query.order_by(
        Application.id.desc()
    ).all()

    return render_template(
        "applications.html",
        applications=user_applications,
        search=search,
        selected_status=status
    )

@app.route("/applications/add", methods=["GET", "POST"])
def add_application():

    if "user_id" not in session:
        flash("Please login first.")
        return redirect(url_for("login"))

    if request.method == "POST":

        company = request.form.get("company", "").strip()
        role = request.form.get("role", "").strip()
        location = request.form.get("location", "").strip()
        status = request.form.get("status", "").strip()

        # Server-side validation
        if not company:
            flash("Company name is required.")
            return redirect(url_for("add_application"))

        if not role:
            flash("Job role is required.")
            return redirect(url_for("add_application"))

        if len(company) < 2:
            flash("Company name must contain at least 2 characters.")
            return redirect(url_for("add_application"))

        if len(role) < 2:
            flash("Job role must contain at least 2 characters.")
            return redirect(url_for("add_application"))

        allowed_statuses = [
            "Applied",
            "Assessment",
            "Interview",
            "Selected",
            "Rejected"
        ]

        if status not in allowed_statuses:
            flash("Invalid application status.")
            return redirect(url_for("add_application"))

        application = Application(
            company=company,
            role=role,
            location=location,
            status=status,
            user_id=session["user_id"]
        )

        db.session.add(application)
        db.session.commit()

        flash("Application added successfully!")

        return redirect(url_for("applications"))

    return render_template("add_application.html")

@app.route(
    "/applications/edit/<int:application_id>",
    methods=["GET", "POST"]
)
def edit_application(application_id):

    if "user_id" not in session:
        flash("Please login first.")
        return redirect(url_for("login"))

    application = Application.query.filter_by(
        id=application_id,
        user_id=session["user_id"]
    ).first_or_404()

    if request.method == "POST":

        company = request.form.get("company", "").strip()
        role = request.form.get("role", "").strip()
        location = request.form.get("location", "").strip()
        status = request.form.get("status", "").strip()

        # Server-side validation

        if not company:
            flash("Company name is required.")
            return redirect(
                url_for(
                    "edit_application",
                    application_id=application.id
                )
            )

        if not role:
            flash("Job role is required.")
            return redirect(
                url_for(
                    "edit_application",
                    application_id=application.id
                )
            )

        if len(company) < 2:
            flash("Company name must contain at least 2 characters.")
            return redirect(
                url_for(
                    "edit_application",
                    application_id=application.id
                )
            )

        if len(role) < 2:
            flash("Job role must contain at least 2 characters.")
            return redirect(
                url_for(
                    "edit_application",
                    application_id=application.id
                )
            )

        allowed_statuses = [
            "Applied",
            "Assessment",
            "Interview",
            "Selected",
            "Rejected"
        ]

        if status not in allowed_statuses:
            flash("Invalid application status.")
            return redirect(
                url_for(
                    "edit_application",
                    application_id=application.id
                )
            )

        # Update application

        application.company = company
        application.role = role
        application.location = location
        application.status = status

        db.session.commit()

        flash("Application updated successfully!")

        return redirect(url_for("applications"))

    return render_template(
        "edit_application.html",
        application=application
    )
@app.route("/applications/delete/<int:application_id>", methods=["POST"])
def delete_application(application_id):

    if "user_id" not in session:
        flash("Please login first.")
        return redirect(url_for("login"))

    application = Application.query.filter_by(
        id=application_id,
        user_id=session["user_id"]
    ).first_or_404()

    db.session.delete(application)
    db.session.commit()

    flash("Application deleted successfully!")

    return redirect(url_for("applications"))
if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run()