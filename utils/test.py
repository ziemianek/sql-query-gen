from . import generate_sql_query


def main():
    prompts = [
        "create a table for employee",
        "select users older than 30",
        "remove birth_date from students table",
        "add 3 records to customers table",
    ]

    for prompt in prompts:
        query = generate_sql_query(prompt)
        print(query)


if __name__ == "__main__":
    main()
