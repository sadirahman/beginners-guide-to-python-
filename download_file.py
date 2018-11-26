from urllib import request

goog_url ='https://drive.google.com/file/d/0B99eYMb_95RkeGNwY2dfN0pPeU1Walp6eFVTX1dEanJGNmtV/view?usp=sharing'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'

    fw = open(dest_url, 'w')
    for line in lines:
        fw.write(line + '\n')
    fw.close()

download_stock_data(goog_url)