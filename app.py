from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "my store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            },
            {
                "name": "Table",
                "price": 24.99
            },
        ]
    }
]

@app.get('/store')
def get_stores():
    return {"stores": stores}