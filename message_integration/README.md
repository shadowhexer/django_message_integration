Messaging Integration using Django and Twilio

Source code: https://www.twilio.com/en-us/blog/bulk-sms-service-django-twilio

## It is recommended to run Django in a virtual environment

1. Create virtual environment inside message_integration folder (not in the folder of the same name located within message_integration)
    ```
    py -m venv venv
    ```
 
2. Activate the virtual environment

    ```
    C:\path\to\your\message_integration>venv\Scripts\activate
    ```

3. Install Django, Twilio, Django-environ

    ```
    (venv)C:\path\to\your\message_integration>pip install django twilio django-environ
    ```

    or install all dependecies from requirments.txt

    ```
    pip install -r requirements.txt
    ```

4. Run the server
    ```
    (venv)C:\path\to\your\message_integration>py manage.py runserver
    ```

5. Rename the `.env.sample` to `.env` and fill in all the values required.
