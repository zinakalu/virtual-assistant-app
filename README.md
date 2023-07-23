# Virtual Assistant Application

This project is a Virtual Assistant Application built using Flask, React, SpringBoot and MySQL. Users can interact with the virtual assistant, and all interactions and responses from the virtual assistant are stored in a MySQL database.

## Data Models

The application uses three primary models: `User`, `UserInteractionWithVirtualAssistant`, and `ApiResponse`.

`User`
This model represents an individual user who interacts with the virtual assistant. It has a username field, which must be unique and cannot be null, and an id field, which is its primary key.

`UserInteractionWithVirtualAssistant`
This model represents an instance of interaction between a user and the virtual assistant. Each instance is associated with a user, and has an id field, a user_id field (a foreign key that links to the User model), a parent_id field (another foreign key that links to its own model to represent a self-referential relationship, indicating a chain of interactions), a user_input_speech field, and a date_of_speech field.

`ApiResponse`
This model represents the responses that the virtual assistant generates based on the user interactions. Each instance is associated with a user interaction, and has an id field, an interaction_id field (a foreign key that links to the UserInteractionWithVirtualAssistant model), a response_text field, and a response_date field.

### Relationships between Models

1. **User and UserInteractionWithVirtualAssistant**: A single `User` can have many `UserInteractionWithVirtualAssistant` instances. This represents the various interactions a user has with the virtual assistant.

2. **UserInteractionWithVirtualAssistant and ApiResponse**: A one-to-one relationship, indicating that each interaction has a unique response from the API

3. **UserInteractionWithVirtualAssistant and itself (Self-referential)**: self-referential (relationship refers to the `id` of another interaction in the same table), that tracks a chain of interactions and understands the context of follow-up question. `parent_id` is a foreignkey that references another interaction. When a user asks an original question, `parent_id` will be null. However, when a user asks a follow-up question, `parent_id` will be set to the id of the interaction that the question is following up on (the original question). This structure assumes a follow-up question only relates to the immediate previous interaction and not to earlier interactions

## Getting Started

To get started with this project:

1. Clone the repository: `git clone <repo_url>`
2. Install the requirements: `pip install -r requirements.txt`
3. Set up the database: `flask db upgrade`
4. Run the application: `flask run`
