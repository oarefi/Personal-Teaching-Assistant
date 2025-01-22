from langchain_ollama import OllamaLLM
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit  # Add this import
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import JsonOutputParser

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

def initialize_sql_agent():
    llm = OllamaLLM(model="llama3.1:8b")
    db = SQLDatabase.from_uri("sqlite:///student_data.db", sample_rows_in_table_info=3)
    
    print("\nAvailable tables:", db.get_usable_table_names())
    print("\nDatabase schema:")
    print(db.table_info)
    
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    return create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

def parse_with_retries(content, max_retries=3):
    output_parser = JsonOutputParser()
    for attempt in range(max_retries):
        try:
            message = AIMessage(content=content)
            return output_parser.invoke(message)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            # Optionally modify the content or prompt here
    raise Exception("Failed to parse output after multiple attempts")

def main():
    agent_executor = initialize_sql_agent()
    
    while True:
        user_input = input("\nYour question: ")
        
        if user_input.lower() in ['quit', 'exit']:
            break
            
        if user_input.strip():
            try:
                response = agent_executor.invoke(user_input)
                parsed_output = parse_with_retries(response["output"])
                print("\nResponse:", parsed_output)
            except Exception as e:
                print("An error occurred:", str(e))