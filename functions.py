def process_user_input(user_input):
    return user_input

def find_best_and_worst_students(db):
    best_student_query = """
    SELECT User_ID, AVG(Response_Score / Possible_Score) AS average_score
    FROM your_table_name
    GROUP BY User_ID
    ORDER BY average_score DESC
    LIMIT 1
    """
    
    worst_student_query = """
    SELECT User_ID, AVG(Response_Score / Possible_Score) AS average_score
    FROM your_table_name
    GROUP BY User_ID
    ORDER BY average_score ASC
    LIMIT 1
    """
    
    best_student = db.run(best_student_query)
    worst_student = db.run(worst_student_query)
    
    return best_student, worst_student

def find_students_with_perfect_scores(db):
    query = """
    SELECT User_ID
    FROM your_table_name
    WHERE Response_Score = Possible_Score
    """
    return db.run(query)

def calculate_average_time(db):
    query = """
    SELECT AVG(Duration_In_Seconds) AS average_time
    FROM your_table_name
    """
    return db.run(query)

def list_students_requested_hints(db):
    query = """
    SELECT DISTINCT User_ID
    FROM your_table_name
    WHERE Hint_Requested = 1
    """
    return db.run(query)
