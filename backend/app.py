from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
roles = {
    "Data Analyst": ["Python", "SQL", "Excel", "Power BI", "Statistics"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
    "Backend Developer": ["Python", "Flask", "SQL", "APIs", "Git"],
    "Mechanical Engineer": ["AutoCAD", "SolidWorks", "Thermodynamics", "Fluid Mechanics", "Manufacturing Processes"],
    "Civil Engineer": ["AutoCAD", "Structural Design", "Surveying", "Reinforced Concrete Design", "Construction Management"],
    "Electrical Engineer": ["Circuit Theory", "Power Systems", "Electronics", "Electrical Machines", "Control Systems"],
    "Electronics Engineer": ["VLSI", "Microcontrollers", "Digital Logic", "Embedded Systems", "PCB Design"],
    "Teacher": ["Communication", "Pedagogy", "Classroom Management", "Lesson Planning", "Educational Psychology"],
    "Business Analyst": ["Excel", "SQL", "Business Knowledge", "Data Visualization", "Requirement Analysis"]
}
skill_suggestions = {
"Python": "Practice Python daily and build small projects.",
"SQL": "Practice SQL queries and learn different types of JOINs.",
"Excel": "Learn advanced formulas, Pivot Tables, and dashboards.",
"Power BI": "Build interactive dashboards using real datasets.",
"Statistics": "Study probability, hypothesis testing, and data analysis.",
"HTML": "Create responsive web pages using semantic HTML.",
"CSS": "Practice Flexbox, Grid, and responsive design.",
"JavaScript": "Build interactive web applications and learn DOM manipulation.",
"React": "Develop projects using components and React Hooks.",
"Git": "Use Git and GitHub for version control in projects.",
"Flask": "Build REST APIs and backend applications using Flask.",
"APIs": "Learn API integration and JSON data handling.",
"AutoCAD": "Practice creating 2D and 3D engineering designs.",
"SolidWorks": "Build mechanical models and assemblies regularly.",
"Thermodynamics": "Study heat transfer and energy conversion concepts.",
"Fluid Mechanics": "Practice fluid flow and pressure-related problems.",
"Manufacturing Processes": "Learn common industrial manufacturing techniques.",
"Structural Design": "Study building and structural analysis methods.",
"Surveying": "Practice land measurement and mapping techniques.",
"Reinforced Concrete Design": "Learn RCC design principles and calculations.",
"Construction Management": "Understand project planning and resource management.",
"Circuit Theory": "Practice solving electrical circuit problems.",
"Power Systems": "Study power generation, transmission, and distribution.",
"Electronics": "Learn analog and digital electronic circuits.",
"Electrical Machines": "Understand motors, generators, and transformers.",
"Control Systems": "Study system stability and feedback mechanisms.",
"VLSI": "Learn chip design and semiconductor fundamentals.",
"Microcontrollers": "Build embedded projects using microcontrollers.",
"Digital Logic": "Practice logic gates and digital circuit design.",
"Embedded Systems": "Develop hardware-software integrated systems.",
"PCB Design": "Learn circuit board design using PCB tools.",
"Communication": "Improve speaking, listening, and presentation skills.",
"Pedagogy": "Learn effective teaching methodologies.",
"Classroom Management": "Develop techniques to manage students efficiently.",
"Lesson Planning": "Create structured and engaging lesson plans.",
"Educational Psychology": "Understand student learning behavior.",
"Business Knowledge": "Study business operations and industry trends.",
"Data Visualization": "Create clear and effective data visualizations.",
"Requirement Analysis": "Learn how to gather and document business requirements."
}

@app.route("/")
def home():
    return "Skill Gap Analyzer API Running "

@app.route("/api/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        role = data.get("role", "")
        skills = data.get("skills", [])

        # lowercase for comparison
        skills_lower = [s.lower() for s in skills]

        required = roles.get(role, [])
        required_lower = [r.lower() for r in required]

        # Missing skills
        missing = [r for r in required if r.lower() not in skills_lower]

        # Score calculation
        if len(required) > 0:
            score = int(((len(required) - len(missing)) / len(required)) * 100)
        else:
            score = 0

        # Status
        if score >= 80:
            msg = "Job Ready"
        elif score >= 50:
            msg = "Needs Improvement"
        else:
            msg = "Beginner Level"

        
        suggestions = []
        for skill in missing:
            tip = skill_suggestions.get(
                skill,
                "Search online courses and build projects"
            )
            suggestions.append({
                "skill": skill,
                "tip": tip
            })

        return jsonify({
            "role": role,
            "score": score,
            "missing_skills": missing,
            "status": msg,
            "suggestions": suggestions  
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
if __name__ == "__main__":
    app.run(debug=True)
