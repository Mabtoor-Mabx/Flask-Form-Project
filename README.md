# **Flask Form Project**

## **📌 Introduction**

The **Flask Form Project** is a simple web application built with **Flask** that demonstrates two different methods for handling user input through forms:

* **Manual Form Handling** (with custom validation logic)
* **Flask-WTF Form Handling** (with built-in validation and CSRF protection)

This project showcases the integration of templates, form validation, and flash messaging in Flask, making it an excellent starting point for beginners learning Flask web development.

---

## **✅ Features**

* Home page with navigation menu
* Manual form submission with custom validation
* Flask-WTF form submission with validators
* Flash messages for user feedback (success, error, info)
* Template inheritance using **Jinja2**
* CSRF protection enabled through Flask-WTF
* Responsive navigation and simple styling

---

## **🛠 Technologies & Libraries Used**

* **Flask** – Python web framework
* **Flask-WTF** – Extension for form handling and CSRF protection
* **WTForms** – Provides form fields and validation
* **Jinja2** – Template engine for HTML rendering

---

## **📂 Project Structure**

```
Flask-Form-Project/
│
├── app.py                 # Main Flask application file
├── templates/
│   ├── base.html          # Base template with navigation and flash messages
│   ├── home.html          # Home page template
│   ├── manual_form.html   # Manual form template
│   └── wtf_form.html      # Flask-WTF form template

```

---

## **⚙️ Workflow**

1. **Home Page:**
   Displays navigation links to access both forms.

2. **Manual Form:**

   * Accepts user input for **name** and **email**.
   * Performs manual validation:

     * Checks if fields are filled.
     * Ensures the email contains "@" symbol.
   * On success, flashes a success message and redirects to the home page.

3. **Flask-WTF Form:**

   * Utilizes Flask-WTF and WTForms to create a registration form.
   * Includes built-in validators for username, email, and password.
   * CSRF protection is automatically handled.
   * Displays flash message upon successful submission.

---

## **🚀 How It Works**

* **Manual Form** → HTML form → POST request → Flask route → Custom validation → Flash message → Redirect.
* **Flask-WTF Form** → FlaskForm class → Automatic validation → Flash message → Redirect.

---

## **📌 Key Highlights**

* Demonstrates **two methods** of form handling in Flask.
* Implements **flash messaging system** for real-time user feedback.
* Uses **template inheritance** for clean, maintainable HTML.
* Provides an example of **secure form handling** using CSRF tokens.

---
