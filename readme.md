**Important:** When checking for FAQs please be patient and wait for about a min for response as api is deployed on free server it gets paused when inactive and takes about 50 secs when called.

# Fruit.ai FAQ API Backend

This project is a backend API for handling FAQs related to fruits. It is built using Flask and provides basic CRUD functionality (Create, Read, Update, Delete) for FAQs. This backend API can be integrated with any frontend application to handle FAQ data dynamically.

## Features
- **GET all FAQs**: Fetch all FAQ data.
- **GET a single FAQ**: Fetch a specific FAQ by its ID.
- **POST a new FAQ**: Create a new FAQ.
- **PUT to update a FAQ**: Update an existing FAQ by its ID.
- **DELETE a FAQ**: Delete an FAQ by its ID.

## Technologies Used
- **Flask**: Python-based lightweight web framework.
- **Flask-CORS**: To handle Cross-Origin Resource Sharing (CORS) and allow API usage from different domains.
- **Python**: Core language used for the backend.
- **REST API**: CRUD functionality to manage FAQs.

## API Endpoints

### 1. Get All FAQs
- **URL**: `/faqs`
- **Method**: `GET`
- **Description**: Fetch all available FAQs in the system.
- **Response**: Returns a list of FAQs with their id, question, and answer.

```json
[
  {
    "id": 1,
    "question": "What is an apple?",
    "answer": "An apple a day keeps doctor away.😊"
  },
  {
    "id": 2,
    "question": "What is a banana?",
    "answer": "A banana is yellow coloured carbs rich fruit."
  }
]
```

### 2. Get Single FAQ by ID
- **URL**: `/faqs/<faq_id>`
- **Method**: `GET`
- **Description**: Fetch a specific FAQ by its id.
- **Response**: Returns a single FAQ if found.

```json
{
  "id": 1,
  "question": "What is an apple?",
  "answer": "An apple a day keeps doctor away.😊"
}
```

**Error Response:**

```json
{
  "error": "FAQ not found"
}
```

### 3. Create a New FAQ
- **URL**: `/faqs`
- **Method**: `POST`
- **Description**: Create a new FAQ by sending question and answer in the request body.

**Request Body:**

```json
{
  "question": "What is an orange?",
  "answer": "An orange is a citrus fruit rich in Vitamin C."
}
```

**Response:** Returns the newly created FAQ with an assigned id.

```json
{
  "id": 5,
  "question": "What is an orange?",
  "answer": "An orange is a citrus fruit rich in Vitamin C."
}
```

### 4. Update an Existing FAQ
- **URL**: `/faqs/<faq_id>`
- **Method**: `PUT`
- **Description**: Update an existing FAQ's question or answer by sending data in the request body.

**Request Body:**

```json
{
  "question": "What is an updated apple?",
  "answer": "An updated apple a day keeps the doctor even further away!"
}
```

**Response:** Returns the updated FAQ object.

```json
{
  "id": 1,
  "question": "What is an updated apple?",
  "answer": "An updated apple a day keeps the doctor even further away!"
}
```

**Error Response:**

```json
{
  "error": "FAQ not found"
}
```

### 5. Delete a FAQ
- **URL**: `/faqs/<faq_id>`
- **Method**: `DELETE`
- **Description**: Delete a specific FAQ by its id.

**Response:** Returns a success message on successful deletion.

```json
{
  "message": "FAQ deleted successfully"
}
```

**Error Response:**

```json
{
  "error": "FAQ not found"
}
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/fruit-ai-backend.git
cd fruit-ai-backend
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

4. Access the API locally at [http://127.0.0.1:5000/faqs](http://127.0.0.1:5000/faqs).

## Deployment

You can deploy the Flask app on any platform that supports Python web apps. Here’s a simple guide for deploying to Render:

1. Sign up for a Render account.
2. Create a new Web Service on Render.
3. Connect your GitHub repository.
4. Set the build command to:

```bash
pip install -r requirements.txt
```

5. Set the start command to:

```bash
python app.py
```

Render will build and deploy your app. The deployed backend can be accessed at the provided Render URL.

## CORS

The API uses Flask-CORS to allow cross-origin requests from different domains. If integrating this API with a frontend application, ensure that the domain of the frontend is allowed in CORS configuration.

## Folder Structure

```
fruit-ai-backend/
│
├── app.py             # Main application file
├── routes.py          # API route handling file
├── requirements.txt   # Python dependencies
├── venv/              # Virtual environment folder
└── README.md          # Project documentation
```

## Future Enhancements

- Integrate with a database (e.g., SQLite, PostgreSQL) for persistent FAQ storage.
- Implement authentication for managing FAQs.
- Add more FAQs to cover a broader range of fruit-related questions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue for any bug fixes or enhancements.
