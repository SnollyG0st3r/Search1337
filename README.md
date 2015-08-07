# Search1337

Well as you know 1337day closed.So new domain 0day.today, I made some edit for it  .. 


# Installation guide
    root@root:~/Desktop# cd 1337
    root@root:~/Desktop/1337# python setup.py install
    running install
    running bdist_egg
    running egg_info
    writing cmdline_search1337.egg-info/PKG-INFO
    writing top-level names to cmdline_search1337.egg-info/top_level.txt
    writing dependency_links to cmdline_search1337.egg-info/dependency_links.txt
    writing entry points to cmdline_search1337.egg-info/entry_points.txt
    reading manifest file 'cmdline_search1337.egg-info/SOURCES.txt'
    writing manifest file 'cmdline_search1337.egg-info/SOURCES.txt'
    installing library code to build/bdist.linux-i686/egg
    running install_lib
    running build_py
    copying 1337/helper.py -> build/lib.linux-i686-2.7/1337
    copying 1337/call.py -> build/lib.linux-i686-2.7/1337
    creating build/bdist.linux-i686/egg
    creating build/bdist.linux-i686/egg/1337
    copying build/lib.linux-i686-2.7/1337/day1337.py -> build/bdist.linux-i686/egg/1337
    copying build/lib.linux-i686-2.7/1337/__init__.py -> build/bdist.linux-i686/egg/1337
    copying build/lib.linux-i686-2.7/1337/helper.py -> build/bdist.linux-i686/egg/1337
    copying build/lib.linux-i686-2.7/1337/useragent.py -> build/bdist.linux-i686/egg/1337
    copying build/lib.linux-i686-2.7/1337/call.py -> build/bdist.linux-i686/egg/1337
    byte-compiling build/bdist.linux-i686/egg/1337/day1337.py to day1337.pyc
    byte-compiling build/bdist.linux-i686/egg/1337/__init__.py to __init__.pyc
    byte-compiling build/bdist.linux-i686/egg/1337/helper.py to helper.pyc
    byte-compiling build/bdist.linux-i686/egg/1337/useragent.py to useragent.pyc
    byte-compiling build/bdist.linux-i686/egg/1337/call.py to call.pyc
    creating build/bdist.linux-i686/egg/EGG-INFO
    copying cmdline_search1337.egg-info/PKG-INFO -> build/bdist.linux-i686/egg/EGG-INFO
    copying cmdline_search1337.egg-info/SOURCES.txt -> build/bdist.linux-i686/egg/EGG-INFO
    copying cmdline_search1337.egg-info/dependency_links.txt -> build/bdist.linux-i686/egg/EGG-INFO
    copying cmdline_search1337.egg-info/entry_points.txt -> build/bdist.linux-i686/egg/EGG-INFO
    copying cmdline_search1337.egg-info/top_level.txt -> build/bdist.linux-i686/egg/EGG-INFO
    zip_safe flag not set; analyzing archive contents...
    creating 'dist/cmdline_search1337-0.1-py2.7.egg' and adding 'build/bdist.linux-i686/egg' to it
    removing 'build/bdist.linux-i686/egg' (and everything under it)
    Processing cmdline_search1337-0.1-py2.7.egg
    Removing /usr/local/lib/python2.7/dist-packages/cmdline_search1337-0.1-py2.7.egg
    Copying cmdline_search1337-0.1-py2.7.egg to /usr/local/lib/python2.7/dist-packages
    cmdline-search1337 0.1 is already the active version in easy-install.pth
    Installing search1337 script to /usr/local/bin
    
    Installed /usr/local/lib/python2.7/dist-packages/cmdline_search1337-0.1-py2.7.egg
    Processing dependencies for cmdline-search1337==0.1
    Finished processing dependencies for cmdline-search1337==0.1
    
# Help
    root@root:~/Desktop# search1337
     _____     _           _      _ 
    |_   _|  _| |_ ___ _ _(_)__ _| |
      | || || |  _/ _ \ '_| / _` | |
      |_| \_,_|\__\___/_| |_\__,_|_|
                                    
                         
    	search1337 --e [SEARCH TAG]
    				
    Also you can append CVE number.
    	search1337 --e [SEARCH TAG] --cve [CVE]
    
    You must read it, if you dont have any idea about CVE.	
    	http://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures
    

# Usage Type
    root@root:~/Desktop# search1337 --e Python
    Endian Firewall &lt; 3.0.0 - OS Command Injection (Python PoC) Exploit
    http://0day.today/exploit/23824
        
    Python socket.recvfrom_into() remote buffer overflow exploit
    http://0day.today/exploit/21938
        
    This exploit is private, cant get name..
    http://0day.today/exploit/20996
        
    Debian OpenSSL Predictable PRNG Bruteforce SSH Exploit (Python)
    http://0day.today/exploit/9201
        
    Python Untrusted Search Path/Code Execution Vulnerability
    http://0day.today/exploit/18938

    ...
    
    
    
    Python - Interpreter Heap Memory Corruption (PoC)
    http://0day.today/exploit/22241
    
    PyPAM Python bindings for PAM Double Free Corruption
    http://0day.today/exploit/17653
    
    Python < 2.5.2 Imageop Module 'imageop.crop()' BOF Vulnerability
    http://0day.today/exploit/9791
    
    linux/x86 Run /usr/bin/python | setreuid(),execve() - 54 Bytes
    http://0day.today/exploit/22502

