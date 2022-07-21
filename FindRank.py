import requests
from bs4 import BeautifulSoup


def url(rank_name):
    # this webpage has all the icons for all the ranks
    page = requests.get("https://paladins.fandom.com/wiki/Category:Ranked_icons")

    # read html
    soup = BeautifulSoup(page.content, "html.parser")

    # for every a tag (href) with the cla
    for a in soup.findAll('a', class_="image", href=True):
        # if the players rank is in the tag and make sure it's not a rank border but an icon
        if rank_name in str(a) and "RankIcon" in str(a):
            # then isolate the url by quotations
            urlFind = str(a).split('"')
            # now the isolated url is in a list of chunks from the tag
            for string in urlFind:
                # if the chunk of the tag contains the rank name
                if rank_name in string:
                    # then that is the icon url for the players rank
                    return string
