# osintname
Generate Emails and Usernames from Provided Lists of Names.

Just a simple tool to generate a username list by permutating from a provided list of names. This tool will generate a list of usernames in the following formats:

- firstname.lastname
- firstnamelastname
- lastname.firstname
- lastnamefirstname
- lastname
- firstname

Just that. Nothing less, nothing more.

## Usage
```
➜  osintname git:(main) python3 osintname.py -h

        _     _                       
 ___ __(_)_ _| |_ _ _  __ _ _ __  ___ 
/ _ (_-< | ' \  _| ' \/ _` | '  \/ -_)
\___/__/_|_||_\__|_||_\__,_|_|_|_\___|
        Emails and Usernames Generator
    
usage: osintname.py [-h] --list LIST [--domain DOMAIN]

Generate Emails and Usernames from Provided Lists of Names

options:
  -h, --help            show this help message and exit
  --list LIST, -l LIST  File containing a list of names.
  --domain DOMAIN, -d DOMAIN
                        Email domain for generating email-format usernames.
```

Generate Username Lists:
```
python3 osintname.py -l names.txt
```

Generate Email Lists:
```
python3 osintname.py -l names.txt -d classroomofelite.com
```

## Screenshot
![osintname](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidNjFPK8Ad7gCc_173oSnf-wiV8qBJzaK_9q_TTcIpqjblbjzBc-FHLtduzDk6uO25fkfZYfQCMwOIF2BHWTVn0eS0_5p3r8nVZ4hw04m27iOqtJh9ep0Lu60ATfp12q2xdxbICQthU55pei0qmMzdujxx-LIrtSHNG5asdCMOYexBhyphenhyphenOa8BkXliuZOteH/s1844/)