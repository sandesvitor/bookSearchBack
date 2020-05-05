from flask_restful import Resource, reqparse
import requests


api_key = 'AIzaSyBxg3xDmKIp1IsX59-R_2TQoqF1IOXCou4'

class Books(Resource):
    def get(self, author_name):
        
        url = f'https://www.googleapis.com/books/v1/volumes?q=inauthor:"{author_name}"&maxResults=40&key={api_key}'
        response = requests.get(url)                 
        bookJson = response.json()                     
                           
        book_titles = []
        object_info = {}
                   
    
        if response.status_code == 200:            
            if (bookJson['totalItems'] > 0):                              
                books = bookJson['items']
               
                for item in books:
                    try: 
                        object_info = {'titulo': item['volumeInfo']['title']}
                    except:
                        object_info.update({'titulo': 'None'})
                    try:
                        object_info.update({'data': item['volumeInfo']['publishedDate']})
                    except:
                        object_info.update({'data': 'None'})
                    try:
                        object_info.update({'pages': item['volumeInfo']['pageCount']})
                    except:
                        object_info.update({'pages': 'None'})
                    try:
                        object_info.update({'preço': item['saleInfo']['listPrice']['amount']})
                    except:
                        object_info.update({'preço': 'None'})
                    try:
                        object_info.update({'link_compra': item['saleInfo']['buyLink']})
                    except:
                        object_info.update({'link_compra': 'None'})          
                                     
                    
                    book_titles.append(object_info)                                                                         

                return book_titles                       
            else:
                return "Erro", 404               
        else:
            return response.text, response.status_code
       