from flask import Flask, render_template, request, redirect, url_for
from models import db, Student, Module, LearningPath
from recommendation import recommend_path

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create database tables and add sample modules
with app.app_context():
    db.create_all()

# Add sample modules if the database is empty
def add_sample_modules():
    if Module.query.count() == 0:
        modules = [
            Module(name="Basic Math - Text", level="Basic", type="Text Lessons"),
            Module(name="Basic Math - Video", level="Basic", type="Video Lessons"),
            Module(name="Intermediate Math - Text", level="Intermediate", type="Text Lessons"),
            Module(name="Intermediate Math - Video", level="Intermediate", type="Video Lessons"),
            Module(name="Advanced Math - Text", level="Advanced", type="Text Lessons"),
            Module(name="Advanced Math - Video", level="Advanced", type="Video Lessons"),
        ]
        db.session.add_all(modules)
        db.session.commit()

with app.app_context():
    add_sample_modules()

# Home page: List all students
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

# Add a new student
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        grade_level = int(request.form['grade_level'])
        learning_style = request.form['learning_style']
        student = Student(name=name, grade_level=grade_level, learning_style=learning_style)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_student.html')

# View student details and learning path
@app.route('/student/<int:student_id>')
def student_detail(student_id):
    student = Student.query.get_or_404(student_id)
    paths = LearningPath.query.filter_by(student_id=student_id).all()
    return render_template('student_detail.html', student=student, paths=paths)

# Generate a learning path based on grade input
@app.route('/generate_path/<int:student_id>', methods=['POST'])
def generate_path(student_id):
    student = Student.query.get_or_404(student_id)
    grade = float(request.form['grade'])
    recommendation = recommend_path(grade, student.learning_style)
    module = Module.query.filter_by(level=recommendation['level'], type=recommendation['type']).first()
    if module:
        path = LearningPath(student_id=student_id, module_id=module.id)
        db.session.add(path)
        db.session.commit()
    return redirect(url_for('student_detail', student_id=student_id))

if __name__ == '__main__':
    app.run(debug=True)