import pandas as pd
import sqlite3

with sqlite3.connect('C:/Users/student1/Desktop/PythonAdvanced/Ex1/Exercise1/db.sqlite3') as conn:
    df = pd.read_sql('Select * from usersmodel', conn)
    new_column = df['first_name'] + ' ' + df['last_name']
    df['full_name'] = new_column
    print(df)

    df.to_excel("Users_details.xlsx", index = False)

    print("\nMedia pentru coloana number_of_login este:", df['number_of_login'].mean())
    print("\nStandard deviation pentru coloana number_of_login:", df['number_of_login'].std())