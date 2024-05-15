
import streamlit as st
import time
import io
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pyresparser import ResumeParser

ds_course = [['Machine Learning Crash Course by Google [Free]', 'https://developers.google.com/machine-learning/crash-course'],
             ['Machine Learning A-Z by Udemy', 'https://www.udemy.com/course/machinelearning/'],
             ['Machine Learning by Andrew NG', 'https://www.coursera.org/learn/machine-learning'],
             ['Data Scientist Master Program of Simplilearn (IBM)',
              'https://www.simplilearn.com/big-data-and-analytics/senior-data-scientist-masters-program-training'],
             ['Data Science Foundations: Fundamentals by LinkedIn',
              'https://www.linkedin.com/learning/data-science-foundations-fundamentals-5'],
             ['Data Scientist with Python', 'https://www.datacamp.com/tracks/data-scientist-with-python'],
             ['Programming for Data Science with Python',
              'https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104'],
             ['Programming for Data Science with R',
              'https://www.udacity.com/course/programming-for-data-science-nanodegree-with-R--nd118'],
             ['Introduction to Data Science', 'https://www.udacity.com/course/introduction-to-data-science--cd0017'],
             ['Intro to Machine Learning with TensorFlow',
              'https://www.udacity.com/course/intro-to-machine-learning-with-tensorflow-nanodegree--nd230']]

web_course = [['Django Crash course [Free]', 'https://youtu.be/e1IyzVyrLSU'],
              ['Python and Django Full Stack Web Developer Bootcamp',
               'https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp'],
              ['React Crash Course [Free]', 'https://youtu.be/Dorf8i6lCuk'],
              ['ReactJS Project Development Training',
               'https://www.dotnettricks.com/training/masters-program/reactjs-certification-training'],
              ['Full Stack Web Developer - MEAN Stack',
               'https://www.simplilearn.com/full-stack-web-developer-mean-stack-certification-training'],
              ['Node.js and Express.js [Free]', 'https://youtu.be/Oe421EPjeBE'],
              ['Flask: Develop Web Applications in Python',
               'https://www.educative.io/courses/flask-develop-web-applications-in-python'],
              ['Full Stack Web Developer by Udacity',
               'https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044'],
              ['Front End Web Developer by Udacity',
               'https://www.udacity.com/course/front-end-web-developer-nanodegree--nd0011'],
              ['Become a React Developer by Udacity', 'https://www.udacity.com/course/react-nanodegree--nd019']]

android_course = [['Android Development for Beginners [Free]', 'https://youtu.be/fis26HvvDII'],
                  ['Android App Development Specialization',
                   'https://www.coursera.org/specializations/android-app-development'],
                  ['Associate Android Developer Certification', 'https://grow.google/androiddev/#?modal_active=none'],
                  ['Become an Android Kotlin Developer by Udacity',
                   'https://www.udacity.com/course/android-kotlin-developer-nanodegree--nd940'],
                  ['Android Basics by Google',
                   'https://www.udacity.com/course/android-basics-nanodegree-by-google--nd803'],
                  ['The Complete Android Developer Course',
                   'https://www.udemy.com/course/complete-android-n-developer-course/'],
                  ['Building an Android App with Architecture Components',
                   'https://www.linkedin.com/learning/building-an-android-app-with-architecture-components'],
                  ['Android App Development Masterclass using Kotlin',
                   'https://www.udemy.com/course/android-oreo-kotlin-app-masterclass/'],
                  ['Flutter & Dart - The Complete Flutter App Development Course',
                   'https://www.udemy.com/course/flutter-dart-the-complete-flutter-app-development-course/'],
                  ['Flutter App Development Course [Free]', 'https://youtu.be/rZLR5olMR64']]

ios_course = [['IOS App Development by LinkedIn', 'https://www.linkedin.com/learning/subscription/topics/ios'],
              ['iOS & Swift - The Complete iOS App Development Bootcamp',
               'https://www.udemy.com/course/ios-13-app-development-bootcamp/'],
              ['Become an iOS Developer', 'https://www.udacity.com/course/ios-developer-nanodegree--nd003'],
              ['iOS App Development with Swift Specialization',
               'https://www.coursera.org/specializations/app-development'],
              ['Mobile App Development with Swift',
               'https://www.edx.org/professional-certificate/curtinx-mobile-app-development-with-swift'],
              ['Swift Course by LinkedIn', 'https://www.linkedin.com/learning/subscription/topics/swift-2'],
              ['Objective-C Crash Course for Swift Developers', 'https://www.udemy.com/course/objectivec/'],
              ['Learn Swift by Codecademy', 'https://www.codecademy.com/learn/learn-swift'],
              ['Swift Tutorial - Full Course for Beginners [Free]', 'https://youtu.be/comQ1-x2a1Q'],
              ['Learn Swift Fast - [Free]', 'https://youtu.be/FcsY1YPBwzQ']]
uiux_course = [['Google UX Design Professional Certificate',
                'https://www.coursera.org/professional-certificates/google-ux-design'],
               ['UI / UX Design Specialization', 'https://www.coursera.org/specializations/ui-ux-design'],
               ['The Complete App Design Course - UX, UI and Design Thinking',
                'https://www.udemy.com/course/the-complete-app-design-course-ux-and-ui-design/'],
               ['UX & Web Design Master Course: Strategy, Design, Development',
                'https://www.udemy.com/course/ux-web-design-master-course-strategy-design-development/'],
               ['The Complete App Design Course - UX, UI and Design Thinking',
                'https://www.udemy.com/course/the-complete-app-design-course-ux-and-ui-design/'],
               ['DESIGN RULES: Principles + Practices for Great UI Design',
                'https://www.udemy.com/course/design-rules/'],
               ['Become a UX Designer by Udacity', 'https://www.udacity.com/course/ux-designer-nanodegree--nd578'],
               ['Adobe XD Tutorial: User Experience Design Course [Free]',
                'https://youtu.be/68w2VwalD5w'],
               ['Adobe XD for Beginners [Free]', 'https://youtu.be/WEljsc2jorI'],
               ['Adobe XD in Simple Way', 'https://learnux.io/course/adobe-xd']]

resume_videos = ['https://youtu.be/y8YH0Qbu5h4', 'https://youtu.be/J-4Fv8nq1iA',
                 'https://youtu.be/yp693O87GmM', 'https://youtu.be/UeMmCex9uTU',
                 'https://youtu.be/dQ7Q8ZdnuN0', 'https://youtu.be/HQqqQx5BCFY',
                 'https://youtu.be/CLUsplI4xMU', 'https://youtu.be/pbczsLkv7Cc']

interview_videos = ['https://youtu.be/Ji46s5BHdr0', 'https://youtu.be/seVxXHi2YMs',
                    'https://youtu.be/9FgfsLa_SmY', 'https://youtu.be/2HQmjLu-6RQ',
                    'https://youtu.be/DQd_AlIvHUw', 'https://youtu.be/oVVdezJ0e7w'
                                                                 'https://youtu.be/JZK1MZwUyUU',
                    'https://youtu.be/CyXLhHQS3KY']


def extract_text_from_pdf(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    converter.close()
    fake_file_handle.close()
    return text


def calculate_efficiency_score(resume_text, keywords):
    resume_text_lower = resume_text.lower()
    matched_keywords = [keyword for keyword in keywords if keyword.lower() in resume_text_lower]
    efficiency_score = (len(matched_keywords) / len(keywords)) * 100
    return efficiency_score, matched_keywords


def classify_efficiency_level(efficiency_score):
    if efficiency_score < 50:
        return "Poor"
    elif efficiency_score < 75:
        return "Intermediate"
    else:
        return "Excellent"


def recommend_skills(job_role):
    # Define sets of skills for different job roles or domains
    skills_dict = {
        "Data Analyst": {"data analysis", "data visualization", "SQL", "Excel", "statistics"},
        "Machine Learning Engineer": {"machine learning", "deep learning", "Python", "TensorFlow", "scikit-learn"},
        # Add more job roles and their associated skills as needed
    }

    if job_role in skills_dict:
        recommended_skills = skills_dict[job_role]
    else:
        recommended_skills = set()  # Default empty set if job role not found

    return recommended_skills


def recommend_courses(skills):
    recommended_courses = []
    courses = [ds_course, web_course, android_course, ios_course, uiux_course]
    for skill in skills:
        for course in courses:
            for course_name, course_link in course:
                if skill.lower() in course_name.lower():
                    recommended_courses.append((course_name, course_link))
    return recommended_courses


def resume_tips(efficiency_level):
    tips_dict = {
        "Poor": [
            "Focus on showcasing relevant skills and experiences prominently.",
            "Consider taking additional courses or certifications to improve your skills."
        ],
        "Intermediate": [
            "Highlight your achievements and projects related to the job role.",
            "Customize your resume for each job application to emphasize relevant skills."
        ],
        "Excellent": [
            "Ensure your resume is concise and well-organized.",
            "Include quantifiable achievements to demonstrate your impact."
        ]
    }
    return tips_dict.get(efficiency_level, [])


def run():
    st.title("Resume Efficiency Analyzer")
    st.sidebar.markdown("# Upload Resume")
    pdf_file = st.sidebar.file_uploader("Choose your Resume (PDF)", type=["pdf"])

    if pdf_file is not None:
        with st.spinner('Analyzing your Resume...'):
            time.sleep(4)
            save_pdf_path = './Uploaded_Resumes/' + pdf_file.name
            with open(save_pdf_path, "wb") as f:
                f.write(pdf_file.getbuffer())

            st.subheader("Resume Content")
            resume_text = extract_text_from_pdf(save_pdf_path)
            st.write(resume_text)

            st.subheader("Efficiency Analysis")
            keywords = ['python', 'machine learning', 'data analysis', 'communication skills', 'problem solving']
            efficiency_score, matched_keywords = calculate_efficiency_score(resume_text, keywords)
            st.write(f"Efficiency Score: {efficiency_score:.2f}%")

            efficiency_level = classify_efficiency_level(efficiency_score)
            st.write(f"Efficiency Level: {efficiency_level}")

            st.write("Matched Keywords:")
            for keyword in matched_keywords:
                st.write(keyword)

            # Extracted job role can be obtained from the user or extracted from the resume (if available)
            job_role = "Data Analyst"  # Example job role, you can replace this with the actual job role
            recommended_skills = recommend_skills(job_role)
            if recommended_skills:
                st.subheader("Recommended Skills:")
                for skill in recommended_skills:
                    st.write(skill)
            else:
                st.write("No recommended skills found for this job role.")

            # Recommend courses based on extracted skills
            recommended_courses = recommend_courses(matched_keywords)

            # Display recommended courses
            if recommended_courses:
                st.subheader("Recommended Courses:")
                for course_name, course_link in recommended_courses:
                    st.write(f"- {course_name}: {course_link}")
            else:
                st.write("No recommended courses found based on the skills in the resume.")

            # Provide tips to improve the resume
            tips = resume_tips(efficiency_level)
            if tips:
                st.subheader("Resume Improvement Tips:")
                for tip in tips:
                    st.write(tip)


if __name__ == "__main__":
    run()
