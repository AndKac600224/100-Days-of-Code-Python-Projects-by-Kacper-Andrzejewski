# Flask Blog (Jinja2)

A simple dynamic blog application built using Flask and Jinja2 templating.  
Blog posts are fetched from a public API and rendered using templates.  
This project demonstrates backend routing, template rendering, classes, and integration with an external API.

## Project Structure

Jinja_blog  
├── main.py # Flask app, routing, API integration  
├── post.py # Post class representing blog post objects  
├── templates  
│ ├── index.html # Home page template  
│ └── post.html # Individual post page  
├── static  
│ └── css  
│ └── styles.css # Styling for the application  
└── README.md # This file  

## How It Works?

1. The app fetches blog posts from a public JSON API:  
   `https://api.npoint.io/c790b4d5cab58020d391`

2. Each post is converted into a `Post` object and stored in a list.

3. Routes:
   - `/` → Home page displaying all posts  
   - `/<int:index>` → Displays an individual blog post based on its ID  

4. HTML templates use **Jinja2** for rendering dynamic content.

5. ## How to Run?

1. Install dependencies:
   `pip install flask requests`

2. Run the application:
   `main.py`

3. Open the app in your browser:  
**http://127.0.0.1:5000/**

## Features

- Dynamic routing based on post ID  
- Rendering templates with Jinja2  
- Clean separation of logic using a `Post` class  
- Integration with external API  
- Minimalistic front-end with custom CSS  
- Scalable structure suitable for future expansion

## Technologies 

- Python 3.12  
- Flask (routing, templates, server)  
- Jinja2 template engine  
- HTTP requests (`requests` module)  
- API consumption  
- OOP basics for structuring data  
- HTML/CSS

## Future Improvements

- Add a real database (SQLite or PostgreSQL)  
- Admin panel for adding/editing/deleting posts  
- Pagination for large blog datasets  
- User authentication and comments  
- Switch from external API to local data storage  
- Improve front-end design using Bootstrap
- Add more content on pages

# Screenshots

<img width="2514" height="1281" alt="image" src="https://github.com/user-attachments/assets/bec8c389-e2ba-4cc6-b5fd-fc8af760ecb6" />
