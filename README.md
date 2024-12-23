# Blog Website Using Django

## Overview
This is a fully functional blog website built using the Django framework. It includes several features such as:

- A **Contact Form** to enable users to send inquiries or feedback.
- A **Blog Post Page** to display and manage blog posts, with content stored in a database.
- A **Search Bar** that allows users to search for relevant posts based on keywords.

## Features

1. **Contact Form**
   - Users can submit inquiries or messages.
   - Submitted data is saved in the database for future reference.

2. **Blog Post Page**
   - Displays all blog posts dynamically.
   - Posts are stored and managed in the database.

3. **Search Functionality**
   - Users can search for posts using keywords.
   - The search engine retrieves and displays relevant posts.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, and JavaScript
- **Database**: SQLite (default Django database)

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:
   ```
   http://127.0.0.1:8000
   ```

## Usage

- Navigate to the blog post page to view all posts.
- Use the search bar to find posts by entering relevant keywords.
- Fill out the contact form to submit a message.

## Screenshots
*(Add relevant screenshots of the blog interface, contact form, and search functionality.)*

## Contributions
Contributions are welcome! Feel free to fork the repository and create a pull request with your enhancements or fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
If you have any questions or feedback, please feel free to reach out to me via LinkedIn or email.

---
Thank you for checking out this project! 😊
