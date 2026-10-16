An attempt to make GIT contribution just a little more comfortable


### Contributing to gerEFI start by forking gerEFI repository
Also important to know that you can only contribute all changes from a branch together.
So, if you plan some changes you do not want to continute you need to operate on multiple branches,
not just the default 'master' branch.



### Once you made a local clone of your fork

Please execute *git_add_upstream.bat* ONCE
which will run the following commands for you:
```
git remote -v
git remote add upstream https://github.com/gerefi/kicad-libraries.git
git remote -v
```
Now your local clone of your personal fork of gerEFI knows where it's originating from.
This would be useful if you want to sync your fork with official gerEFI or if you would want to reset your local changes.

### Reset to current version of gerEFI with loss of your local changes
*git_reset_to_upstream.bat* would get your local copy and remote clone of gerEFI fork to latest gerEFI state by executing following commands for you:
```
git fetch upstream
git checkout master
git reset --hard upstream/master
git push origin master -f
``` 

See also https://git-scm.com/downloads