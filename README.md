# Project Name

This Django project provides a RESTful API for managing projects, tasks, and tags. It includes user authentication and pagination for tasks.

## Features

- User authentication (Register, Login, Logout)
- CRUD operations for Projects
- CRUD operations for Tasks with pagination (maximum 5 tasks per page)
- CRUD operations for Tags

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL (or your preferred database)
- Python

## Setup

1. Clone the repository:

   ```bash
   git clone https://AhmedFathyMohamed10/Task-management-project-REST-PostgreSQL.git

## API Endpoints
### Projects
```
- List all projects: GET /projects/
- Create a new project: POST /projects/
- Retrieve a project: GET /projects/{id}/
- Update a project: PUT /projects/{id}/
- Delete a project: DELETE /projects/{id}/
```

```
### Tasks
- List all tasks with pagination (5 tasks per page): GET /tasks/
- Create a new task: POST /tasks/
- Retrieve a task: GET /tasks/{id}/
- Update a task: PUT /tasks/{id}/
- Delete a task: DELETE /tasks/{id}/
```

```
### Tags
- List all tags: GET /tags/
- Create a new tag: POST /tags/
- Retrieve a tag: GET /tags/{id}/
- Update a tag: PUT /tags/{id}/
- Delete a tag: DELETE /tags/{id}/
```

Pagination
Tasks are paginated with a maximum of 5 tasks per page. Use the page query parameter to navigate through pages.

Example: GET /tasks/?page=2

Authentication
Authentication is required for certain endpoints using Token-based authentication.

