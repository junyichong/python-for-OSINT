import wayback
from datetime import datetime

client = wayback.WaybackClient()

# num = 1

for record in client.search('http://nasa.gov', to_date=datetime(1999, 1, 1)):

    memento = client.get_memento(record)

    fileName=memento.memento_url.replace("/","-").replace(":","-")+".html"

    # fileName= str(num) +".html"
    # num = num + 1

    memento_file = open(fileName, "a")

    memento_file.write(memento.text)

    memento_file.close()

    print (fileName)
