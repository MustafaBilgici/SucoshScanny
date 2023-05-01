import sqlparse

def is_vulnerable(sql_query):
    parsed = sqlparse.parse(sql_query)[0]
    if not parsed.is_statement:
        return False
    if not parsed.get_type() == 'SELECT':
        return False
    for token in parsed.tokens:
        if token.match(sqlparse.tokens.Keyword, 'WHERE'):
            return True
    return False