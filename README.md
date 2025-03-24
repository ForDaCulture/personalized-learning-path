Personalized Learning Path Generator
Python Flask License
Project Overview
The Personalized Learning Path Generator is a web application designed to help teachers create customized learning paths for students, focusing on math education. It uses a rule-based AI system to recommend learning modules based on student grades and learning styles (e.g., visual, auditory). Built with Flask, SQLAlchemy, and Bootstrap, this project showcases skills in web development, database management, and process optimization inspired by Business Process Management (BPM) principles.
Features
Add and manage student profiles (name, grade level, learning style).

Generate personalized learning paths by inputting student grades.

View recommended modules in a clean, tabular format.

Persistent storage using SQLite.

Responsive UI with Bootstrap for an intuitive user experience.

Tech Stack
Backend: Python 3.8+, Flask, Flask-SQLAlchemy

Frontend: HTML, Bootstrap 4.5.2

Database: SQLite

Dependencies: flask, flask-sqlalchemy

Prerequisites
Before running the project, ensure you have the following installed:
Python 3.8 or higher: Download Python

pip: Comes with Python; verify with pip --version

Git: To clone the repository (optional); Download Git

VS Code: Recommended IDE; Download VS Code

Setup Instructions
Follow these steps to get the project running locally:
1. Clone the Repository
Clone this repository to your local machine:
bash

git clone https://github.com/your-username/personalized-learning-path.git
cd personalized-learning-path

Replace your-username with your GitHub username after creating the repository.
2. Create a Virtual Environment (Optional but Recommended)
Set up a virtual environment to keep dependencies isolated:
bash

python -m venv venv

Activate it:
On Windows:
bash

venv\Scripts\activate

On macOS/Linux:
bash

source venv/bin/activate

3. Install Dependencies
Install the required Python packages:
bash

pip install flask flask-sqlalchemy

4. Verify Project Structure
Ensure your directory matches this structure:

personalized-learning-path/
├── app.py
├── models.py
├── recommendation.py
├── templates/
│   ├── index.html
│   ├── add_student.html
│   └── student_detail.html
├── static/ (optional)
└── README.md

The learning.db SQLite database will be created automatically when you run the app.
Running the Project
1. Launch the Application
Run the Flask app from the terminal:
bash

python app.py

You’ll see output indicating the server is running in debug mode on http://127.0.0.1:5000.

2. Access the Web App
Open your web browser and navigate to:

http://127.0.0.1:5000/

The home page displays a list of students (initially empty).

3. Test the Workflow
Add a Student:
Click "Add Student".

Fill in the form (e.g., Name: "John Doe", Grade Level: 5, Learning Style: "Visual").

Submit to return to the student list.

Generate a Learning Path:
Click "View Details" next to a student.

Enter a grade (e.g., 85) and submit.

Check the table for the recommended module (e.g., "Advanced Video Lessons").

4. Stop the Server
Press Ctrl+C in the terminal to stop the Flask server.
Testing the Project
Manual Testing
Add Student: Test with different names, grade levels (1-12), and learning styles.

Generate Path: Input grades like 90 (Advanced), 70 (Intermediate), 50 (Basic) and verify the output matches the learning style.

Edge Cases: Try invalid inputs (e.g., grade > 100 or < 0) to ensure the app handles errors gracefully (future enhancement needed).

Debugging
If the app doesn’t start:
Check app.py is in the root directory.

Ensure dependencies are installed (pip list to verify).

If the database doesn’t work:
Delete learning.db and restart the app to recreate it.

Pushing to GitHub
1. Initialize a Git Repository
If not already cloned:
bash

git init
git add .
git commit -m "Initial commit: Personalized Learning Path Generator"

2. Create a GitHub Repository
Go to GitHub, sign in, and click "New Repository".

Name it (e.g., personalized-learning-path), keep it public, and don’t initialize with a README (we’re using this one).

3. Link and Push
Link your local repo to GitHub and push:
bash

git remote add origin https://github.com/your-username/personalized-learning-path.git
git branch -M main
git push -u origin main

Replace your-username with your GitHub username.
Future Enhancements
Authentication: Add teacher login with Flask-Login.

Progress Tracking: Allow updating module status (e.g., "completed").

Machine Learning: Upgrade to a predictive model with scikit-learn.

UI Improvements: Add custom CSS or progress charts with Chart.js.

Deployment: Host on Heroku or Render for a live demo.

License
This project is licensed under the MIT License - see the LICENSE file for details (create one if you wish to include it).
Contact
For questions or feedback:

