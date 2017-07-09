# mit-course-catalog-cli

Every time I want to check on a course offering, I forget the MIT course catalog link and have to go through google. I am planning on eventually turning this into an API, so that it will be easier to build planner apps for the MIT community in the future.

This is a command line tool to access the [MIT course catalog](http://student.mit.edu/catalog/index.cgi) so that you can quickly find information without using the browser.

# how to install

clone the repository:
```
git clone https://github.com/yczeng/mit-course-catalog-cli
cd mit-course-catalog-cli
```
build the library:

```
sudo pip install --editable .
```
To use, type cc --help to see the list of commands.

For example, to see the main menu, type:
```
cc --menu
```

# license
mit-course-catalog-cli is available under the MIT license (my new favorite license). See `LICENSE` file for more information.
