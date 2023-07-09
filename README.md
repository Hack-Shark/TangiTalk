# Chat App with Django and Django Channels

This is a real-time chat application project based on Django, Redis, and Django Channels. It allows users to communicate with each other in real time using websockets. In this guide, you'll find instructions on how to set up and run the project.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python (version 3.6 or higher)
- Redis

## Project Setup

1. Install Redis: 

   - Download Redis from the official website or use the link provided in the project. For example, you can download Redis for Windows [here](https://github.com/tporadowski/redis/releases/download/v5.0.14.1/Redis-x64-5.0.14.1.msi).
   - Install Redis by running the downloaded installer.
   - After installation, open the Redis CLI (Command-Line Interface) as shown in the screenshot below:
   
     ![Redis CLI](https://drive.google.com/uc?id=11bEavO5DHfx6Qhd_KH8eIPqicrIVeQa9)
   
2. Clone the project repository:

   ```bash
   git clone https://github.com/Hack-Shark/TangiTalk
   cd TangiTalk-main
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Migrate the database and create a superuser:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

## Run the Application

To run the chat application, follow these steps:

1. Start the Redis server:

   - Open a new terminal or command prompt window.
   - Navigate to the Redis installation directory (where Redis is installed).
   - Run the following command to start the Redis server:
   
     ```bash
     redis-server
     ```

2. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

3. Open a web browser and visit `http://localhost:8000` to access the chat application.

## Usage

Once the chat application is running, you can perform the following actions:

- Register a new user account or log in with an existing account.
- Send and receive real-time messages in the chat rooms.
- View a list of registered users.
- Send private messages to other users.
- Set your profile picture and personalized description.

## Project Structure

Here is a brief overview of the project structure:

- `chat` - The main Django application containing the chat-related functionality.
- `static` - Static files for the project, including JavaScript, CSS, and images.
- `templates` - HTML templates for rendering the web pages.
- `chat/views.py` - Views (controllers) for handling different requests and rendering templates.
- `chat/models.py` - Models representing the database structure.
- `chat/urls.py` - URL patterns for routing requests to appropriate views.
- `chat/consumers.py` - WebSocket consumers for handling real-time chat functionality using Django Channels.

## Additional Improvements

Here are some additional improvements you can consider for the chat application:

- Add functionality to upload and share files in the chat rooms.
- Implement message history and display the chat history when joining a room.
- Enhance the user interface and styling of the chat application.
- Implement notifications for new messages or user activities.
- Add support for emojis or other rich text formatting in the messages.

Feel free to customize and extend the project according to your requirements and preferences.

Enjoy building your real-time chat application with Django and Django Channels!
