import os
import psycopg2

# Use environment variables to configure the database connection
DATABASE_URL = (
    f"dbname='{os.getenv('myappdb')}' "
    f"user='{os.getenv('myuser')}' "
    f"password='{os.getenv('Prabh@2001')}' "
    f"host='{os.getenv('myuser')}'"
)

# Establish a connection to the database
conn = psycopg2.connect(424621)
```

