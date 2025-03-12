from flask import Flask, render_template

app = Flask(__name__)

# Ma'lumotlar (O'quvchilar, O'qituvchilar va Ishchilar)
students = [
    {'id': 1, 'name': 'Ali', 'surname': 'Karimov', 'age': 14, 'class': '8-A', 'phone': '901234567'},
    {'id': 2, 'name': 'Madina', 'surname': 'Olimova', 'age': 13, 'class': '7-B', 'phone': '902345678'},
    {'id': 3, 'name': 'Hasan', 'surname': 'Rustamov', 'age': 15, 'class': '9-C', 'phone': '903456789'}
]

teachers = [
    {'id': 1, 'name': 'Olim', 'surname': 'Jalilov', 'subject': 'Matematika', 'experience': 10, 'phone': '904567890'},
    {'id': 2, 'name': 'Nodira', 'surname': 'Hamidova', 'subject': 'Ingliz tili', 'experience': 8, 'phone': '905678901'},
    {'id': 3, 'name': 'Rustam', 'surname': 'Soliev', 'subject': 'Fizika', 'experience': 12, 'phone': '906789012'}
]

staff = [
    {'id': 1, 'name': 'Akmal', 'surname': 'Rahimov', 'position': 'Direktor', 'experience': 15, 'phone': '907890123'},
    {'id': 2, 'name': 'Shahlo', 'surname': 'Mahmudova', 'position': 'Laborant', 'experience': 5, 'phone': '908901234'},
    {'id': 3, 'name': 'Javohir', 'surname': 'Norboyev', 'position': 'Xo‘jalik mudiri', 'experience': 7, 'phone': '909012345'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/students')
def students_list():
    return render_template('students.html', students=students)

@app.route('/teachers')
def teachers_list():
    return render_template('teachers.html', teachers=teachers)

@app.route('/staff')
def staff_list():
    return render_template('staff.html', staff=staff)

# Dinamik sahifalar
@app.route('/student/<int:student_id>')
def student_detail(student_id):
    student = next(student for student in students if student['id'] == student_id)
    return render_template('student_detail.html', student=student)

@app.route('/teacher/<int:teacher_id>')
def teacher_detail(teacher_id):
    teacher = next(teacher for teacher in teachers if teacher['id'] == teacher_id)
    return render_template('teacher_detail.html', teacher=teacher)

@app.route('/staff/<int:staff_id>')
def staff_detail(staff_id):
    staff_member = next(staff_member for staff_member in staff if staff_member['id'] == staff_id)
    return render_template('staff_detail.html', staff_member=staff_member)

if __name__ == '__main__':
    app.run(debug=True)
