from flask import Flask, request, jsonify

app = Flask(__name__)


courses = [
    {
        "id": 1,
        "name": "Course 1",
        "description": "This is Course 1 description.",
        "keywords": ["math", "algebra", "calculus"],
        "category": "Math",
        "difficulty": "Intermediate",
    },
    {
        "id": 2,
        "name": "Course 2",
        "description": "This is Course 2 description.",
        "keywords": ["history", "world", "civilizations"],
        "category": "History",
        "difficulty": "Beginner",
    },
    {
        "id": 3,
        "name": "Course 3",
        "description": "This is Course 3 description.",
        "keywords": ["computer", "programming", "python"],
        "category": "Computer Science",
        "difficulty": "Advanced",
    },
    
]


def recommend_courses(interests, mental_health, category=None, difficulty=None):
    recommended_courses = []

    for course in courses:
        course_keywords = course["keywords"]
        common_keywords = set(interests).intersection(course_keywords)
        
       
        score = len(common_keywords)

        
        if mental_health == "good":
            score *= 1.2
        elif mental_health == "poor":
            score *= 0.8

       
        if category and course["category"].lower() != category.lower():
            continue

        if difficulty and course["difficulty"].lower() != difficulty.lower():
            continue

        recommended_courses.append({"course": course, "score": score})

    
    recommended_courses.sort(key=lambda x: x["score"], reverse=True)

    return recommended_courses
{
    "interests": ["math", "programming", "history"],
    "mental_health": "good",
    "category": "Computer Science",
    "difficulty": "Intermediate"
}

@app.route('/recommend', methods=['POST','GET'])
def get_recommendations():
    data = request.json
    interests = data['interests']
    mental_health = data['mental_health']
    category = data.get('category')  
    difficulty = data.get('difficulty')   

    recommended_courses = recommend_courses(interests, mental_health, category, difficulty)

    
    recommended_courses = recommended_courses[:5]

    return jsonify({'courses': recommended_courses})




if __name__== '__main__':
    app.run(debug=True,host = 'localhost', port=5000) 