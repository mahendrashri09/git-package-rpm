***Git Packaging Into an Rpm***



usage: git-package-rpm.py [-h] [-r REPO]

Pass git repo to package into an RPM

optional arguments:
  -h, --help            show this help message and exit
  -r REPO, --repo REPO  your git repo
                        <git@github.home.247-inc.net:devops/name.git

***How it works***

- Clones your project
- Navigates to the root of your project
- Creates directory name 'dist' and copy spec template under ./dist/
- Calls git-build-rpm 
- Move the rpm under the defined path
