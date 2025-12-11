```python
%pip install sqlalchemy psycopg2-binary
```

```python
from sqlalchemy import create_engine
import pandas as pd
```

```python
username = 'username'
password = 'password'
host = 'host'
database = 'world'
```

```python
engine = create_engine(f'postgresql://{username}:{password}@{host}/{database}')
```

```python
table_name = 'country'
df_table = pd.read_sql_table(table_name, con=engine)
df_table
```