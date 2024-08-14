# PortoPressRest
PortoPressRest is a content management system designed to streamline the creation and management of blog posts and portfolio projects. Built with Django, it features a powerful RESTful API that seamlessly integrates with modern front end frameworks like React. It uses Django admin panel to quick manage the content.

## Project Scope
The project is divided into two main parts:
1. Blog
2. Portfolio
3. Rest API for serving the content.

I am going to use build-in Django admin for managing the content and I will build a REST API for accessing the content.

The content will be displayed via React app, but with REST API, it could be displayed via any other front-end technology.

## Portfolio
The portfolio will store the information about the projects. Each project will have the following fields:
- Title,
- Short description - to be visible on main page under the image,
- Image,
- Date of creation,
- live website link,
- github link,
- optional detailed description - for projects which doesn't have github link - as other project have details in github, this field is optional. It will be useful for projects like tableau dashboard, where the code is not available.

## Blog
The blog application will be done with guide of the book Django 5 example. The blog will be used for writing articles about programming, projects, machine learning. Each blog post will have the following fields:
- Title,
- Date of creation,
- Image,
- Content,

## REST API
The REST API will be build using Django Rest Framework. It will have the following endpoints:
- /api/portfolio/ - for getting the list of all projects,
- /api/portfolio/<id>/ - for getting the details of the project with the given id,
- /api/blog/ - for getting the list of all blog posts,
- /api/blog/<id>/ - for getting the details of the blog post with the given id.