#------------------Bombermans Team---------------------------------#
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/Search1337
# LICENSE : https://github.com/b3mb4m/Search1337/blob/master/LICENSE
#------------------------------------------------------------------#


from useragent import *
import mechanize
import optparse
import sys
import re
import os
from bs4 import BeautifulSoup
from random import randint


class Engine(object):

    def __init__(self, **kwargs):
        self.output = kwargs["output"]
        self.save = kwargs["download"]
        self.folder = None
        self.url = "http://0day.today/search?search_request={0}&search_type=1&category=-1&platform=-1&price_from=0&price_to=10000&author_login=&cve=".format(kwargs["exploit"])

        self.authorization()
        if kwargs["exploit"]:
            if kwargs["all"]:
                self.collectExploits()
            else:
                try:
                    int(kwargs["exploit"])
                except ValueError:
                    sys.exit("\nYou cant use this option without '-a' tag.\n")
                else:
                    self.download(kwargs["exploit"])

    def authorization(self):
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False) 
        self.br.addheaders = [('User-agent', useragent.agents)]
        try:            
            data = self.br.open("http://0day.today/webapps")
        except:
            sys.exit("Site seems like down.")  

        for form in self.br.forms():
            self.br.select_form(nr=0)
            for control in self.br.form.controls:
                if control != None:
                    if control.name == "agree":
                        self.br.submit()     

    def collectExploits(self):
        data = self.br.open(self.url)
        search = re.findall("'/exploit/description/\S+'", data.read())

        if not search:
            sys.exit("\nExploit Not Found ..\n")
        else: 
            if self.save:  
                while True:
                    self.folder = "{0}".format(str(randint(0, 999999999)))
                    if not os.path.isdir(self.folder):
                        break
                os.mkdir(self.folder, 0755)
            print("\n\n")
            for i in search:
                cut = i.replace("'", "").replace("/description", "")
                cut = "http://0day.today" + cut
                data = self.br.open(cut)
                title = self.getTitle(data.read())
                if title:
                    if "private exploit" in title:
                        print("This exploit is private\n\t{0}\n".format(cut))
                    else:   
                        if self.save:
                            if self.output:
                                if os.path.isdir(self.output):
                                    self.download(cut.split("/")["-1"], self.output)
                                sys.exit("Output directory is not exists")
                            else:
                                self.download(cut.split("/")[-1], self.folder)
                                print("{0}\n\t{1}\n".format(title, cut))
                        else:
                            print("{0}\n\t{1}\n".format(title, cut))

    def download(self, exploit, collectExploits=False):
        data = self.br.open("http://0day.today/exploit/" + str(exploit)).read()
        title = self.getTitle(data)
        soup = BeautifulSoup(data, "html.parser")

        for invalid in soup.findAll("pre"):
            if not self.save:
                print invalid.text
            else:
                if not self.output:
                    if collectExploits:
                        defaultpath = os.getcwd() + os.sep + collectExploits + os.sep + exploit + ".txt"
                    else:
                        defaultpath = os.getcwd() + os.sep + exploit + ".txt"

                    if not os.path.isfile(defaultpath):
                        self.savefile(defaultpath, invalid.text)
                    else:
                        while True:
                            name = "{0}.txt".format(str(randint(0, 999999999)))
                            if not os.path.isfile(name):
                                break
                        defaultpath = os.getcwd() + os.sep + name
                        self.savefile(defaultpath, invalid.text)
                else:
                    if os.path.isfile(self.output):
                        sys.exit("Output file already exists.")
                    else:
                        if os.sep not in self.output:
                            self.output = os.getcwd() + os.sep + self.output
                        self.savefile(self.output, invalid.text)

    def getTitle(self, x):
        return re.search('<title>(.*)</title>', x, re.IGNORECASE).group(1)

    def savefile(self, name, text):
        try:
            with open(name, "w") as myexploit:
                myexploit.write((text.replace("\n", "")).encode("utf-8"))
                myexploit.close()
        except Exception as error:
            print("Error while writing : {0}".format(error))       
        else:
            print("\nSaved -> {0}\n".format(name))
