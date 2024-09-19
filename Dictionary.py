def manage_courses():
    # Step 1: Create the dictionary with the initial courses
    courses = {
        "CSE101": {
            "Course name": "Introduction to Programming",
            "Credits": 3,
            "Instructor": "Dr. Alice"
        },
        "CSE102": {
            "Course name": "Data Structures",
            "Credits": 4,
            "Instructor": "Dr. Bob"
        },
        "CSE103": {
            "Course name": "Database Systems",
            "Credits": 3,
            "Instructor": "Dr. Carol"
        }
    }
    
    # Step 2: Update the instructor's name for CSE102 to "Dr. Bob Jr."
    courses["CSE102"]["Instructor"] = "Dr. Bob Jr."
    
    # Step 3: Add a new course CSE104 with the details
    courses["CSE104"] = {
        "Course name": "Algorithms",
        "Credits": 4,
        "Instructor": "Dr. Dave"
    }
    
    # Step 4: Remove the course CSE101 from the dictionary
    del courses["CSE101"]
    
    # Step 5: Loop through the dictionary and print course code and details
    for course_code, details in courses.items():
        print(f"Course Code: {course_code}")
        print(f"  Course Name: {details['Course name']}")
        print(f"  Credits: {details['Credits']}")
        print(f"  Instructor: {details['Instructor']}")
        print()  # Empty line for better readability

# Call the function to see the output
manage_courses()
