# import the software libraries we need (note that these are accessed via APIS as well!)
import requests
import json
import unicodecsv as csv

# Define the query we will use to retrieve data from the Google Books service.
# This query is taken from https://developers.google.com/books/docs/v1/getting_started.

book_idx_range = range(0, {number of items}, {step})
api_url_head = 'https://www.googleapis.com/books/v1/volumes?key={request WSKey}&q={keyword}&maxResults=40&startIndex='
api_url_tail = '&fields=totalItems,items(id,volumeInfo/title,volumeInfo/subtitle,volumeInfo/authors,volumeInfo/publisher,volumeInfo/publishedDate,volumeInfo/description,volumeInfo/pageCount,volumeInfo/printType,searchInfo/textSnippet)'

with open('keywordBooks.csv', 'wb') as keywordBooks:

    for idx in book_idx_range:
        #api_url concatenates the head and tail of the url, with the
        api_url = api_url_head + str(idx) + api_url_tail

        #Use the requests.get function to retrieve the results of our query, which we store in the response variable.
        response = requests.get(api_url)

        #Convert the content of the response variable to a JSON format.print
        jsonData=json.loads(response.content.decode('utf-8'))

        # isolates the list that is produced with each new iteration
        jsonItems = jsonData['items']

        # indicates the total number of results from the query
        print (jsonData['totalItems'])

        # a new json is generated with each iteration of the for loop
        Print (jsonData)


        for volInfo in jsonItems:
            print('\n\n\n')


            if 'volumeInfo' in volInfo:
                info = volInfo['volumeInfo']

                if 'authors' in info:
                    # joins the list of authors into a single string separated by commas
                    authors = ', '.join(info['authors'])
                else:
                    authors = 'unknown author'

                if 'title' in info:
                    title = info['title']
                else:
                    title = 'title unknown'

                if 'subtitle' in info:
                    subtitle = info['subtitle']
                else:
                    subtitle = 'no subtitle'

                if 'publishedDate' in info:
                    date = info['publishedDate']
                else:
                    date = 'pub date unknown'

                if 'description' in info:
                    description = info['description']
                else:
                    description = 'no description'

            if 'id' in volInfo:
                bibID = volInfo['id']


            print('Authors: ', authors)
            print('Authors type: ', authors)
            print('Title: ', title)
            print('Published date: ', date)
            print('gID: ', bibID)
            print('Description: ', description)

            csvwriter = csv.writer(keywordBooks, delimiter = ",", encoding='utf-8')
            csvwriter.writerow([authors, title, subtitle, date, bibID, description])
