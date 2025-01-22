import os
import subprocess
from langchain_ollama import OllamaLLM
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from agent import initialize_sql_agent
from functions import (
    process_user_input,
    find_best_and_worst_students,
    find_students_with_perfect_scores,
    calculate_average_time,
    list_students_requested_hints
)

def run_ollama_model():
    try:
        result = subprocess.run(['ollama', 'run', '<model-name>'], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred while running the model: {e.stderr}"

def retrieve_data_from_db(db, query):
    # Example function to retrieve data from the database
    # This could be a SQL query or a search in a vector store
    return db.run(query)

def main():
    print("Welcome to SQL Assistant! (Type 'quit' to exit)")
    print("Database: student_data.db")
    print("\nPreset Prompts:")
    print("- Find the best and worst performing students.")
    print("- List students with perfect scores.")
    print("- Calculate the average time spent on tests.")
    print("- List students who requested hints.")
    
    agent_executor = initialize_sql_agent()
    
    while True:
        user_input = input("\nYour question: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
            
        if user_input.strip():
            print("\nThinking...\n")
            try:
                processed_input = process_user_input(user_input)
                
                if "best and worst students" in processed_input.lower():
                    best_student, worst_student = find_best_and_worst_students(agent_executor.toolkit.db)
                    print("\nBest Performing Student:", best_student)
                    print("\nWorst Performing Student:", worst_student)
                elif "perfect scores" in processed_input.lower():
                    perfect_students = find_students_with_perfect_scores(agent_executor.toolkit.db)
                    print("\nStudents with Perfect Scores:", perfect_students)
                elif "average time" in processed_input.lower():
                    average_time = calculate_average_time(agent_executor.toolkit.db)
                    print("\nAverage Time Spent on Tests:", average_time)
                elif "requested hints" in processed_input.lower():
                    students_with_hints = list_students_requested_hints(agent_executor.toolkit.db)
                    print("\nStudents Who Requested Hints:", students_with_hints)
                else:
                    response = agent_executor.invoke(processed_input)
                    print("\nResponse:", response["output"])
            except Exception as e:
                print("An error occurred:", str(e))

if __name__ == "__main__":
    print(os.getcwd())
    model_output = run_ollama_model()
    print("Model output:", model_output)
    main()
