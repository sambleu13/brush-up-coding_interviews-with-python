def sort_course_id(courses):
    # implement this
    return sorted(courses, key=lambda x: x[0], reverse=True)

# test samples
test_courses = [(101, "Astrophysics"), (303, "Galactic Politics"), (202, "Quantum Mechanics"), (404, "Alien Communication")]
print(sort_course_id(test_courses)) # Expected: [(404, 'Alien Communication'), (303, 'Galactic Politics'), (202, 'Quantum Mechanics'), (101, 'Astrophysics')]
