from pandas import read_sql


def init(con, inline):
    queries = [
        f'SELECT name AS "Name of the event", event_manager AS "Event Manager", budget AS "Budget in Rs" FROM events ORDER BY budget DESC;',
        f'SELECT name AS "Name of the event", event_manager AS "Event Manager", DATEDIFF(end_date, start_date) AS "Duration in days" FROM events ORDER BY DATEDIFF(end_date, start_date) DESC;',
    ]
    headings = [
        "Events ordered by highest budget",
        "Events ordered by longest duration",
    ]
    dfs = []
    for i, query in enumerate(queries):
        df = read_sql(query, con)
        if not inline:
            print(f"\n --- {headings[i]} ---\n\n {df}")
        dfs.append(df)
    return headings, dfs
