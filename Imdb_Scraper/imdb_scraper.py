from bs4 import BeautifulSoup
import requests

allGenres = ['comedy', 'crime', 'drama', 'short', 'family', 'talk-show', 'romance', 'animation', 'music',                       'fantasy', 'adventure', 'action', 'sci-fi', 'news',
             'game-show', 'mystery', 'musical', 'horror', 'thriller', 'reality-tv', 'documentary', 'sport', 'history', 'biography', 'western', 'war', 'film-noir', 'adult']


def scrapeByGenre(genre, noOfPages):
    for pageNo in range(noOfPages):
        source = requests.get(
            f'https://www.imdb.com/search/title/?genres={genre}&start={(pageNo*50)+1}').text

        soup = BeautifulSoup(source, 'lxml')

        sections = soup.find_all('div', class_='lister-item mode-advanced')

        for section in sections:
            section_content = section.find('div', class_='lister-item-content')

            title = section_content.h3.a.text
            print("Title :", title)

            year = section_content.find(
                'span', class_='lister-item-year text-muted unbold').text.strip('(').strip(')')
            print("Year :", year)

            try:
                rating = section_content.find(
                    'div', class_='inline-block ratings-imdb-rating').strong.text
            except AttributeError:
                rating = ''
            print("Rating :", rating)

            try:
                metascore = section_content.find(
                    'div', class_='inline-block ratings-metascore').span.text
            except AttributeError:
                metascore = ''
            print("Metascore :", metascore)

            paras = section_content.find_all('p')
            castList = []

            try:
                castList = paras[-1].find_all('a')
                castList = list(map(lambda x: x.text, castList))

                divider = paras[-1].find('span', class_='ghost')
                if divider and castList != []:
                    director = castList[0]
                    castList = castList[1:]

                else:
                    castList = paras[-2].find_all('a')
                    castList = list(map(lambda x: x.text, castList))

                    divider = paras[-1].find('span', class_='ghost')
                    if divider:
                        director = castList[0]
                        castList = castList[1:]

            except AttributeError:
                castList = []

            try:
                print("Director :", director)
            except:
                pass

            cast = (', ').join(castList)
            print("Stars :", cast)

            director = ''

            description = paras[1].text.strip()
            print("Description :", description)

            genre_s = section_content.find('span', class_='genre').text.strip()
            print("Genre(s) :", genre_s)

            try:
                runtime = section_content.find('span', class_='runtime').text
            except AttributeError:
                runtime = 'Unknown'
            print("Runtime :", runtime)

            try:
                votes_grossList = section_content.find(
                    'p', class_='sort-num_votes-visible').find_all('span')
                votes_grossList = list(map(lambda x: x.text, votes_grossList))
                votes_gross = ', '.join(votes_grossList)
                if "|" in votes_gross:
                    votes, gross = votes_gross.split('|')
                    _, votes = votes.split(':,')
                    _, gross = gross.split(':,')
                else:
                    votes = votes_gross
                    _, votes = votes.split(':,')
            except AttributeError:
                votes = gross = ''

            print("Votes :", votes)
            try:
                print("Gross :", gross)
            except:
                pass
            votes = gross = ''

            print()


scrapeByGenre('comedy', 1)
