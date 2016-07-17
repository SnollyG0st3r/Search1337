#------------------Bombermans Team---------------------------------#
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/Search1337
# LICENSE : https://github.com/b3mb4m/Search1337/blob/master/LICENSE
#------------------------------------------------------------------#


class HelpMan(object):

    def __init__(self):
        # Dynamic loader, require if you are playing with strings
        import importlib
        for lib in ["bs4", "mechanize"]:
            try:    
                importlib.import_module(lib)
            except Exception as err:
                try:
                    self.install(str(err).replace("No module named ", ""))
                except Exception as err2:
                    print("Unexpected error : {0} ".format(err2))

    def install(self, lib):
        from os import system
        system('python -m pip install {0}'.format(lib))

    # http://patorjk.com/software/taag/#p=display&f=Rectangles&t=Search1337
    def usage(self):
        print """

 _____                 _   ___   ___ ___ ___ 
|   __|___ ___ ___ ___| |_|_  | |_  |_  |_  |
|__   | -_| .'|  _|  _|   |_| |_|_  |_  | | |
|_____|___|__,|_| |___|_|_|_____|___|___| |_|
                                             

\tusage: search1337 [-e] [-a] [-d] [-o]
   
\t-e, --exploit  \tExploit name to search or download
\t-a, --all      \tDownload all exploit according to "-e" tag
\t-d, --download \tInitialization download mode, if not will print everything
\t-o, --output   \tOutput path(with "-a" tag) or file(without "-a" tag)

				""";
