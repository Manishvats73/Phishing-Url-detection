# feature.py
import re
import socket
import requests
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urlparse
from requests.exceptions import RequestException

class FeatureExtraction:
    def __init__(self, url):
        self.url = url
        self.domain = urlparse(url).netloc
        self.response = self.get_response()

    def get_response(self):
        try:
            return requests.get(self.url, timeout=5)
        except RequestException:
            return None

    def HavingIP(self):
        try:
            socket.inet_aton(self.domain)
            return 1
        except:
            return -1

    def URLLength(self):
        return -1 if len(self.url) >= 75 else 1

    def ShortiningService(self):
        shorteners = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.ly|tinyurl\.com"
        return -1 if re.search(shorteners, self.url) else 1

    def HavingAtSymbol(self):
        return -1 if "@" in self.url else 1

    def DoubleSlashRedirecting(self):
        return -1 if self.url.rfind('//') > 6 else 1

    def PrefixSuffix(self):
        return -1 if "-" in self.domain else 1

    def SubDomains(self):
        dots = self.domain.split('.')
        return -1 if len(dots) > 3 else 1

    def SSLfinal_State(self):
        try:
            return 1 if self.url.startswith("https") else -1
        except:
            return -1

    def Domain_registeration_length(self):
        return -1  # Placeholder

    def Favicon(self):
        try:
            if self.response is None:
                return -1
            soup = BeautifulSoup(self.response.text, 'html.parser')
            for head in soup.find_all('head'):
                for link in head.find_all('link', href=True):
                    dots = link['href'].split('.')
                    if self.url in link['href'] or len(dots) == 1 or self.domain in link['href']:
                        return 1
            return -1
        except:
            return -1

    def Port(self):
        return 1  # Simplified

    def HTTPS_token(self):
        return -1 if 'https' in self.domain else 1

    def RequestURL(self):
        try:
            if self.response is None:
                return -1
            soup = BeautifulSoup(self.response.text, 'html.parser')
            i, success = 0, 0
            for img in soup.find_all('img', src=True):
                dots = urllib.parse.urlparse(img['src']).netloc
                if self.url in img['src'] or self.domain in img['src'] or dots == "":
                    success += 1
                i += 1
            for audio in soup.find_all('audio', src=True):
                dots = urllib.parse.urlparse(audio['src']).netloc
                if self.url in audio['src'] or self.domain in audio['src'] or dots == "":
                    success += 1
                i += 1
            if i == 0:
                return 1
            percent = success / float(i)
            return 1 if percent > 0.5 else -1
        except:
            return -1

    def AnchorURL(self):
        try:
            if self.response is None:
                return -1
            soup = BeautifulSoup(self.response.text, 'html.parser')
            i, unsafe = 0, 0
            for a in soup.find_all('a', href=True):
                if "#" in a['href'] or "javascript" in a['href'].lower() or "mailto" in a['href'].lower() or not (self.url in a['href'] or self.domain in a['href']):
                    unsafe += 1
                i += 1
            if i == 0:
                return 1
            percent = unsafe / float(i)
            return -1 if percent > 0.67 else 1
        except:
            return -1

    def LinksInScriptTags(self):
        try:
            if self.response is None:
                return -1
            soup = BeautifulSoup(self.response.text, 'html.parser')
            i, success = 0, 0
            for script in soup.find_all('script', src=True):
                if self.url in script['src'] or self.domain in script['src']:
                    success += 1
                i += 1
            if i == 0:
                return 1
            percent = success / float(i)
            return 1 if percent > 0.5 else -1
        except:
            return -1

    def SFH(self):
        return 1  # Simplified

    def SubmittingToEmail(self):
        try:
            if self.response is None:
                return -1
            return -1 if re.findall(r"[mail\(\)|mailto:?]", self.response.text) else 1
        except:
            return -1

    def AbnormalURL(self):
        return 1  # Simplified

    def IFrame(self):
        try:
            if self.response is None:
                return -1
            return -1 if re.findall(r"<iframe>|<frameBorder>", self.response.text) else 1
        except:
            return -1

    def AgeofDomain(self):
        return 1  # Placeholder

    def DNSRecord(self):
        return 1  # Placeholder

    def WebTraffic(self):
        return 1  # Placeholder

    def PageRank(self):
        return 1  # Placeholder

    def GoogleIndex(self):
        return 1  # Placeholder

    def LinksPointingToPage(self):
        return 1  # Placeholder

    def StatsReport(self):
        return 1  # Placeholder

    def extract_features(self):
        features = [
            self.HavingIP(),
            self.URLLength(),
            self.ShortiningService(),
            self.HavingAtSymbol(),
            self.DoubleSlashRedirecting(),
            self.PrefixSuffix(),
            self.SubDomains(),
            self.SSLfinal_State(),
            self.Domain_registeration_length(),
            self.Favicon(),
            self.Port(),
            self.HTTPS_token(),
            self.RequestURL(),
            self.AnchorURL(),
            self.LinksInScriptTags(),
            self.SFH(),
            self.SubmittingToEmail(),
            self.AbnormalURL(),
            self.IFrame(),
            self.AgeofDomain(),
            self.DNSRecord(),
            self.WebTraffic(),
            self.PageRank(),
            self.GoogleIndex(),
            self.LinksPointingToPage(),
            self.StatsReport()
        ]
        return features
