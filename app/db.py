from langchain_community.utilities import SQLDatabase

def get_database():
    return SQLDatabase.from_uri(
        "mysql+pymysql://root:root@localhost/atliq_tshirts"
    )

