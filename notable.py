import urllib.request
import matplotlib.pyplot as plt 
from bs4 import BeautifulSoup
from datetime import date

def mton (month):
    mton_d = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06'
     ,'July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
    return(mton_d[month])

def to_date (d):
    return(str(d[0])+'-'+mton(d[1])+'-'+str(d[2]))

def days_in (month):
    days_d = {'January':'31','February':'29','March':'31','April':'30','May':'31','June':'30'
     ,'July':'31','August':'31','September':'30','October':'31','November':'30','December':'31'}
    return(days_d[month])

class DeathsByMonth:
    def __init__(self, month):
        self.month = month
        self.url = 'https://en.wikipedia.org/wiki/Deaths_in_' + month + '_2020'
        self.page = urllib.request.urlopen(self.url)
        self.soup = BeautifulSoup(self.page, "lxml")
        self.body = self.soup.find('div',{'id': 'mw-content-text'})
        self.xdate = []
        self.ydeaths = []
        self.ycovid = []
        
        date = [2020,self.month,0]
        for row in self.body.findAll(['h3','ul'])[2:]:
            if row.name == 'h3':
                date[2] = row.text[:-6]
                self.xdate += [to_date(date)]
            elif row.name == 'ul':
                tot = 0
                cov = 0
                for person in row.findAll('li'):
                    tot += 1
                    if "COVID" in person.text:
                        cov += 1
                self.ydeaths += [tot]
                self.ycovid += [cov]
                if date == [2020,self.month,days_in(self.month)]:
                    break
                    
        #had to add a patch for the month of August (see wiki page)
        if month == 'August':
            self.ycovid = self.ycovid[:4] + self.ycovid[5:]
            self.ydeaths = self.ydeaths[:4] + self.ydeaths[5:]
                    
    def plot_summary(self, save = False):
        plt.figure(figsize=(15,15))
        plt.subplot(2, 1, 1)
        plt.plot(self.xdate, self.ydeaths, label='Total')
        plt.plot(self.xdate, self.ycovid, label='Covid-19')
        plt.xticks(rotation='vertical')
        plt.ylabel('Number of deaths')
        plt.legend(bbox_to_anchor=(0.1,0.9), loc='upper left', borderaxespad=0.)
        plt.subplot(2, 1, 2)
        plt.plot(self.xdate, [self.ycovid[i]/self.ydeaths[i]*100 for i in range(len(self.xdate))] )
        plt.xticks(rotation='vertical')
        plt.ylabel('% Covid-19 Deaths')
        plt.suptitle('Notable deaths due to COVID-19 in the month of ' + self.month, y=0.90, fontsize = 'xx-large')
        if save:
            plt.savefig('plots_notable/notable'+self.month)



