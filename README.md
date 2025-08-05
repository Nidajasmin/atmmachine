Net Bank – ATM Dashboard Web Project Documentation
1. Project Overview
Net Bank is a web-based dashboard application simulating a banking environment. It features a user-friendly interface for registration, user listing, profile editing, and an interactive ATM interface that allows users to check balance, deposit, withdraw, and exit.
2. Technology Stack
- Backend: Django (Python)
- Frontend: HTML5, CSS3, Bootstrap 5
- Database: SQLite (default with Django)
3. Features
- User Registration with form validation and profile image upload
- User List display with images
- Edit user functionality with pre-filled form
- ATM Interface: Check Balance, Deposit, Withdraw, Exit
- Modern, mobile-responsive UI with styled modals and feedback messages
4. Project Structure
atmmachine/
├── api/
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── register_user.html
│   │   ├── user_list.html
│   │   └── atm_interface.html
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── urls.py
├── atmmachine/urls.py
└── manage.py
5. URL Patterns
path('', views.dashboard, name='dashboard')
path('register/', views.register_user, name='register_user')
path('users/', views.user_list, name='user_list')
path('edit-user/<int:user_id>/', views.edit_user, name='edit_user')
path('atm/', views.atm_interface, name='atm_interface')
6. ATM Interface
The ATM page mimics a real ATM experience with styled modals using Bootstrap 5.
Operations:
- Check Balance: Shows current balance
- Deposit: Opens a modal to input deposit amount
- Withdraw: Opens a modal to input withdrawal amount
- Exit: Displays thank you message and redirects to dashboard
7. How to Run Locally
1. Clone the repo:
   git clone <your-repo-url>
2. Navigate to the project folder
3. Create a virtual environment and activate it
4. Install requirements: pip install -r requirements.txt
5. Run migrations: python manage.py migrate
6. Start server: python manage.py runserver
7. Visit http://127.0.0.1:8000/ to access the dashboard


  









 
 
 
 

 
 
 
 

 

 
 
 
 
 
 
 
