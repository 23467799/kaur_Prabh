```python
import os
import psycopg2

# Use environment variables to configure the database connection
DATABASE_URL = (
    f"dbname='{os.getenv('DB_NAME')}' "
    f"user='{os.getenv('DB_USER')}' "
    f"password='{os.getenv('DB_PASSWORD')}' "
    f"host='{os.getenv('DB_HOST')}'"
)

# Establish a connection to the database
conn = psycopg2.connect(DATABASE_URL)
```

