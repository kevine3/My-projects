from graphviz import Digraph
from PIL import Image
from fpdf import FPDF

# ERD Diagram
erd = Digraph('ERD', format='png')
erd.attr(rankdir='LR')
erd.node('User', 'User\n(UserID, Name, Email, PasswordHash, Role)')
erd.node('Course', 'Course\n(CourseID, Title, Description, Credits, Schedule, Capacity)')
erd.node('Enrollment', 'Enrollment\n(EnrollmentID, UserID, CourseID, Status)')
erd.node('Prerequisite', 'Prerequisite\n(CourseID, PrerequisiteCourseID)')
erd.edge('User', 'Enrollment', label='1:N')
erd.edge('Course', 'Enrollment', label='1:N')
erd.edge('Course', 'Prerequisite', label='1:N')
erd.edge('Prerequisite', 'Course', label='N:1')
erd_path = erd.render(filename='ERD_Course_Registration', cleanup=False)

# DFD Level 0
dfd0 = Digraph('DFD_Level_0', format='png')
dfd0.attr(rankdir='LR')
dfd0.node('Student', 'Student', shape='rectangle')
dfd0.node('Instructor', 'Instructor', shape='rectangle')
dfd0.node('Admin', 'Admin', shape='rectangle')
dfd0.node('System', 'Course Registration System', shape='circle')
dfd0.edge('Student', 'System', label='View/Enroll Courses')
dfd0.edge('System', 'Student', label='Confirmation')
dfd0.edge('Instructor', 'System', label='View Courses/Students')
dfd0.edge('System', 'Instructor', label='Course Details')
dfd0.edge('Admin', 'System', label='Manage Courses/Users')
dfd0.edge('System', 'Admin', label='Reports/Logs')
dfd0_path = dfd0.render(filename='DFD_Level_0_Course_Registration', cleanup=False)

# DFD Level 1
dfd1 = Digraph('DFD_Level_1', format='png')
dfd1.attr(rankdir='LR')
dfd1.node('Student', 'Student', shape='rectangle')
dfd1.node('Admin', 'Admin', shape='rectangle')
dfd1.node('P1', '1.0 User Management', shape='circle')
dfd1.node('P2', '2.0 Course Management', shape='circle')
dfd1.node('P3', '3.0 Enrollment Process', shape='circle')
dfd1.node('D1', 'D1: User DB', shape='cylinder')
dfd1.node('D2', 'D2: Course DB', shape='cylinder')
dfd1.node('D3', 'D3: Enrollment DB', shape='cylinder')
dfd1.edge('Student', 'P1', label='Register/Login')
dfd1.edge('P1', 'D1', label='Store/Retrieve User Info')
dfd1.edge('Admin', 'P2', label='Create/Edit Course')
dfd1.edge('P2', 'D2', label='Update Course Info')
dfd1.edge('Student', 'P3', label='Enroll/Drop')
dfd1.edge('P3', 'D3', label='Update Enrollment')
dfd1.edge('P3', 'D2', label='Read Course Info')
dfd1.edge('P3', 'D1', label='Verify User')
dfd1_path = dfd1.render(filename='DFD_Level_1_Course_Registration', cleanup=False)

# Create PDF from PNGs
pdf = FPDF()
for img_path in [erd_path, dfd0_path, dfd1_path]:
    image = Image.open(img_path)
    width, height = image.size
    width_mm = width * 0.264583
    height_mm = height * 0.264583
    orientation = 'P' if width_mm < height_mm else 'L'
    pdf.add_page(orientation=orientation)
    pdf.image(img_path, x=10, y=10, w=width_mm * 0.9)

pdf.output("College_Course_Registration_System_Diagrams.pdf")
