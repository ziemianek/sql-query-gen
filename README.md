# todo:
* add users and sign in option
* add history for every user
* create ci/cd pipeline
* deploy project on aws

# SQL Query Generator

### SQL Query Generator using OpenAI API
This is a Django project that leverages OpenAI's API to generate custom SQL queries based on prompts provided by users. The application allows users to input a prompt describing their desired query, and it generates the corresponding SQL query using OpenAI's powerful language model.

### What is Django?
Django is a high-level Python web framework that enables rapid development and clean design of web applications. It follows the model-view-controller (MVC) architectural pattern, emphasizing reusability, modularity, and simplicity.


### Application Overview
The SQL Query Generator is a web application built with Django that integrates OpenAI's API to generate SQL queries. Users can provide prompts such as "Get all customers from the 'Orders' table," and the application will generate the appropriate SQL query based on the prompt.
 
### Prerequisites
To run this project locally, make sure you have the following requirements installed:

    Python (3.10 or higher)
    Django (4.2.1 or higher)
    OpenAI (0.27.8 or higher)

### How to Use
To use this application, follow these steps:

1. Clone the repository to your local machine:

    on windows:
    ```bash
    git clone https://github.com/ziemianek/sql-query-gen.git
    ```

    on linux/mac:
    ```bash
    git clone git@github.com:ziemianek/sql-query-gen.git
    ```

2. Change into the project directory:

    ```bash
    cd sql-query-generator
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

5. Open your web browser and navigate to http://localhost:8000 to access the application.

6. Input your desired query prompt and click the "Generate Query" button.

7. **The generated SQL query will be displayed on the page.**

### Conclusion
With this SQL Query Generator application, you can quickly generate complex SQL queries by providing simple prompts. The integration with OpenAI's API allows for efficient and accurate query generation based on user input. Feel free to explore the codebase, customize the application, and enhance its capabilities further!