import requests
import pandas as pd
import io

url = 'https://raw.githubusercontent.com/ElijahWandimi/open-data-repo/master/GHED_data.XLSX'

def load_to_csv():
    res = requests.get(url)

    if res.status_code == 200:
        df = pd.read_excel(io.BytesIO(res.content))
        csv_path = 'data/GHED.csv'
        df.to_csv(csv_path, index = False)
        print(f"csv file successfully saved at {csv_path}")
    else:
        print(f"file download failed: {res.status_code}")

if __name__ == "__main__":
    load_to_csv()
