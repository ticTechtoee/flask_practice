# Task Master

Task Master is a simple task management web application built with Flask. It allows users to create, update, and delete tasks. This application demonstrates basic CRUD (Create, Read, Update, Delete) operations and serves as a foundation for learning Flask web development.

## Features

- **Create Tasks**: Add new tasks with a description.
- **Read Tasks**: View a list of all tasks.
- **Update Tasks**: Edit the description of existing tasks.
- **Delete Tasks**: Remove tasks from the list.

## Requirements

- Python 3.6+
- Flask
- SQLite (default database)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/task-master.git
    cd task-master
    ```

2. **Create a virtual environment**:

    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the environment variables**:

    Create a `.env` file in the root directory and add the following environment variables:

    ```plaintext
    FLASK_APP=app.py
    FLASK_ENV=development
    ```

6. **Initialize the database**:

    ```bash
    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

## Usage

1. **Run the Flask development server**:

    ```bash
    flask run
    ```

2. **Open your web browser** and go to `http://127.0.0.1:5000` to access the application.

## Project Structure

```plaintext
task-master/
├── app.py              # Main application file
├── models.py           # Database models
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # Main page template
│   ├── update.html     # Update page template
├── static/             # Static files (CSS, JS)
│   ├── CSS/
│   │   └── main.css    # Main stylesheet
├── instance/           # Flask instance folder
│   └── app.db          # SQLite database file
├── .env                # Environment variables
├── .gitignore          # Git ignore file
├── README.md           # README file
└── requirements.txt    # Python dependencies


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

    Flask
    SQLite