from flask import Flask
import fredapi as fa
from datetime import datetime
import requests 
import time

app = Flask(__name__)


@app.route("/qli")
def qli():
    # Fetch the data from the remote data source
    fred = fa.Fred(api_key='17896fd7f8b88504ee1595d3b8199492')   #im@quanta
    t10y2y = fred.get_series('T10y2y')

    #df = pd.read_csv('http://example.com/data.csv')

    # Select the last row
    number = t10y2y.iloc[-1]

    ## 1000 lines to be here to make the final qli, but now we only use t10y2y
    qli = 0.2+number/10

    json_qli= {}
    json_qli.update({"date": datetime.today(), "qli": qli})
    return json_qli

@app.route('/')
def home():
    # print(number[0])
    # Extract the number from the last row
    #number = last_row[1]
    url = "http://127.0.0.1:5000/qli"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
    qli = data["qli"]
    round_qli= round(qli*100,2)
    # Return the number in an HTML page
    return f'<h1 style="text-align:center">{round_qli}%</h1>'

if __name__ == '__main__':
    app.run()
