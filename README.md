# Heavenscent E-Store

## To run locally:
-   ```bash
    pip install requirements.txt
    ```  
    Or if using Anaconda  
    ```bash
    conda install --file requirements.txt
    ```
- Generate a secret key [from this site](https://djecrety.ir/).
- Create a `.env` file inside the `ecommerce` folder and add the following
    ```text
    export SECRET_KEY='value_from_step_above'
    export ALLOWED_HOSTS='*'
    export DEBUG=True
    export ENGINE='django.db.backends.sqlite3'
    export SQL_ENGINE='django.db.backends.mysql'
    export DB_HOST=''
    export DB_NAME=''
    export DB_PORT=
    export DB_USER=''
    export DB_PWD=''
    ```
- [Contact me](boywilder99@gmail.com) for the missing values
- If using another database other than SQLite, change the value of `ENGINE` accordingly.
- **Ensure `.env` is included in the `.gitignore` file**
- Create a superuser
- Run 
    ```bash
    make migrations
    ``` 
    and 
    ```bash
    make migrate
    ``` 
    if using a database other than SQLite
- Run the app
    ```bash
    make serve
    ```