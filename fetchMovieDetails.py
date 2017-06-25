import re
import urllib.request

class fetchMovieDetails:
    def __init__(self, movie):
        self.file = urllib.request.urlopen("http://www.imdb.com/find?ref_=nv_sr_fn&q="+movie+"&s=tt")
        self.file = self.file.read()
        self.file = str(self.file)
        self.file = urllib.request.urlopen(self.fetchURL(movie))
        self.file = self.file.read()
        self.file = str(self.file)

    def fetchURL(self,movie):
        link = "result_text\".*?href=\"(.*?1)\"\s*>.*?</a>"
        check = "result_text\".*?href=\".*?1\"\s*>(.*?)</a>"
        pattern = re.compile(link)
        sync = re.compile(check)
        evaluate = re.findall(sync, self.file)
        if(movie.lower() == evaluate[0].lower()):
            URL = re.findall(pattern, self.file)
            return 'http://www.imdb.com'+URL[0]
        else:
            return 'Not Found..'
        
    def fetchTitle(self):
        getTitle = "<title[^>]*>([^<]+)</title>"
        pattern1 = re.compile(getTitle)
        title = re.findall(pattern1,self.file)
        return title[0]

    
    def fetchRating(self):
        getRating = "itemprop=\"ratingValue\">(\d*?\.?\d)</span>"
        pattern = re.compile(getRating)
        rating = re.findall(pattern, self.file)
        return rating[0]

    
    def fetchDirector(self):
        getName = "(=\"itemprop\" itemprop=\"name\">\w*\s*\w*</span>)"
        name = "itemprop=\"director\".*?itemprop=\"name\">(\w*.?\s*\w*?)</span>"
        pattern1 = re.compile(name)
        director = re.findall(pattern1,self.file)
        return director[0]

    def fetchLanguage(self):
        getLang = "\">Language:.*?>(\w*)</a>"
        pattern = re.compile(getLang)
        lang = re.findall(pattern, self.file)
        return lang[0]

    def fetchCast(self):
        getCast = "itemprop=\"actors\".*?itemprop=\"name\">(\w*\s*?\w*)"
        pattern = re.compile(getCast)
        cast = re.findall(pattern, self.file)
        return cast



movie = input('Enter Movie Name: ')
fetch = fetchMovieDetails(movie)
print('Movie: ', fetch.fetchTitle(), '\t\tRating: ', fetch.fetchRating())
print('Director: ', fetch.fetchDirector())
print('Language: ', fetch.fetchLanguage())
print('Cast: ', fetch.fetchCast())
