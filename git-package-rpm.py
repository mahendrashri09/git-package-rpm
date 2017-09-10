#!/usr/bin/env python

import os,argparse,sys,shutil
import tempfile,glob

def argsparsing():
    parser=argparse.ArgumentParser(description = "Pass git repo to package into an RPM")
    parser.add_argument('--repo', action='store', help="your git repo <git@github.home.247-inc.net:devops/name.git")
    parser.add_argument('--spec', action='store', help="Pass your /path/spec file (default - generic)", default='generic' )
    parser.add_argument('--prefix', action='store', help="installation prefix (default - /usr/local/", default='default' )
    return parser.parse_args()  

def main():

    argsparsing
    args = argsparsing()
    if not args.repo:
        print "\n Error - No value passed, type --help"
        exit();
    if args.spec == "generic":
        spec_file = "/opt/generic_template.spec"
    else:
        spec_file = args.spec

    if args.prefix == "default":
        prefix = "/usr/local/"
    else:
        prefix = args.prefix

    if not os.path.isfile(spec_file):
        print "\n The spec file not determined"
        exit();
    repo_url = args.repo
    print "\n Proceeding with spec - %s" %spec_file

    repo = repo_url.split('/')[-1].split('.')[0]
    path="/root/gitrpm/%s" %repo
    dist="./%s/dist" %repo
    repo_spec='/opt/%s_template.spec' %repo
    main_spec='%s/%s.spec' % (dist, repo)

    # Display

    print "\nPackaging git rpm"
    print "===================="
    print "\nGit - %s" % repo_url

    #shutil.copyfile('%s' %spec_file, '%s' %repo_spec )

    replacements = {'Name:':'Name:  %s' %repo, '/usr/local/':'%s' %prefix}

    with open('%s' %spec_file, 'r') as infile:
        with open('%s' %repo_spec, 'w') as outfile:
            for line in infile:
                for src, target in replacements.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)

    if not os.path.isdir(prefix):
        os.makedirs(prefix)

    script_dir="%s-rpm-build" %repo
    if os.path.isdir(script_dir):
        shutil.rmtree(script_dir)
        os.makedirs(script_dir)
    else:
        os.makedirs(script_dir)
    os.chdir("%s" %script_dir)

    print ("-Cloning git..%s" %repo)
    return_code=os.system("git clone %s" %repo_url)

    if return_code == 0:

    # Building Spec

        os.makedirs(dist)

        if not os.path.isdir(path):
            os.makedirs(path)
        shutil.copyfile('%s' %repo_spec, '%s' %main_spec )

        os.chdir("%s" %repo);

	return_code = os.system("git-build-rpm  --spec-file=dist/%s.spec" %repo)
        if return_code == 0:
            for rpm in glob.glob('*.rpm'):
                shutil.move('%s' %rpm, '%s/' %path )
                print "\n %s rpm placed here  - %s/%s" % (repo, path, rpm)
        else:
            print ("\n Error  - RPM Build Failed")
            exit();
    else:
        print ("\n Error - Git clone failed")
        exit();
if __name__ == "__main__":
    main()

