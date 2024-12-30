from flask import Flask, render_template
import pandas as pd

# Flask app
app = Flask(__name__)

import os
predictions_df = pd.read_csv(os.path.join("data", "apple_stock_data.csv"))

@app.route('/')
def home():
    # Convert predictions_df to HTML table
    table = predictions_df.to_html(classes='table table-striped', index=False)
    return render_template('index.html', table=table)

if __name__ == '__main__':
    app.run(debug=True)
