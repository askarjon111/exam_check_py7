from fastapi import FastAPI

app = FastAPI()

news_data = {'1': {"title": "news 1"},
             '2': {"title": "news 2"},
             '3': {"title": "news 3"}, }


@app.get('/news/')
def news():
    return news_data


@app.get('/news/{pk}')
def news(pk):
    return {"result": news_data.get(pk)}
