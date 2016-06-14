import urllib
import BeautifulSoup

from common.abstracts import Module


class print_url(Module):

    def run(self, url):

        self.getUrlTitle(url)

    def getUrlTitle(self, url):

        soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(url))

        print soup.title.string
