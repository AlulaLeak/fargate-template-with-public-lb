from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post('/api')
def predict():
    return { 'Message' : "Hello World" }

@app.get("/hello-world/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Hello, World!</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <h2>I'm running an ECS!</h2>
        </body>
    </html>
    """