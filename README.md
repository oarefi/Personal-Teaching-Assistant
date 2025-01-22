# Personal Teaching Assistant (PTA)

The Personal Teaching Assistant (PTA) is an intelligent tool designed to facilitate seamless interaction with a student database through natural language queries. By leveraging advanced language models from LangChain and Ollama, PTA translates user queries into actionable insights, making data retrieval intuitive and efficient.

## Features

- **Performance Analysis**: Identify the best and worst performing students based on their scores.
- **Perfect Scores**: Quickly list students who have achieved perfect scores in their assessments.
- **Time Tracking**: Calculate the average time students spend on tests to gain insights into test engagement.
- **Hint Requests**: Discover which students have requested hints, providing a deeper understanding of learning patterns.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies:**

   Ensure Python is installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database:**

   Place a SQLite database named `student_data.db` in the project directory.

## Usage

1. **Run the application:**

   ```bash
   python main.py
   ```

2. **Interact with the assistant:**

   Use preset prompts or type your own questions to explore the database:
   - "Find the best and worst performing students."
   - "List students with perfect scores."
   - "Calculate the average time spent on tests."
   - "List students who requested hints."

3. **Exit the application:**

   Type `quit` or `exit` to close the application.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact [arefianbaraniojan@gmail.com](mailto:arefianbaraniojan.com).
