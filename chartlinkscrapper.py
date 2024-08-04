import os.path
import datetime
from utilities.scan_url import scan_main


if __name__ == '__main__':
    today = dict()
    today["Time"] = datetime.datetime.now().strftime('%H:%M')
    today["Date"] = datetime.datetime.now().strftime('%d-%m-%Y')
    today["Duration"] = 'Daily'
    today["Pattern"] = 'Pink'
    response = scan_main()
    if not os.path.exists('Response.csv'):
        print("File does not exists")
        print("File created exists")
    with open('Response.csv', 'w+') as csv_file:
        temp_text = 'Date' + ',' + 'Time' + ',' + 'Duration' + ',' + 'Pattern' + ',' + 'Stock' + ',' + 'Price'
        csv_file.writelines(temp_text)
        csv_file.writelines('\n')
        for element in response:
            temp_text = str(today['Date']) + ',' + str(today['Time']) + ',' \
                        + str(today['Duration']) + ',' + str(today['Pattern']) \
                        + ',' + str(element["short_name"]) + ',' + str(element["price"])
            csv_file.writelines(temp_text)
            csv_file.writelines('\n')
    print("Response file is created")
