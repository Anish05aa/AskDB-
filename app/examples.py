
QUERY_EXAMPLES = [
    {
        "input": "How many white Nike t-shirts are in stock for XS size?",
        "query": "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand='Nike' AND color='White' AND size='XS';"
    },
    {
        "input": "What is total inventory value for small size t-shirts?",
        "query": "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE size='S';"
    },
]
