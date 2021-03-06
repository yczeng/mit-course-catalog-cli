# mit-course-catalog-cli

This is a command line tool to access the [MIT course catalog](http://student.mit.edu/catalog/index.cgi) so that you can quickly find information without using the browser.

I was inspired to make this because every time I want to check on a course offering, I forget the MIT course catalog link and have to go through google. I am planning on eventually turning this into a python API, so that it will be easier to build planner apps for the MIT community in the future.


# Installation

Clone the repository:
```
git clone https://github.com/yczeng/mit-course-catalog-cli
cd mit-course-catalog-cli
```
Build the library. Note that there's a period after install.

```
sudo pip2 install --editable .
```
To see the list of commands, type:
```
mit-cc --help
```
Really though, there are just two commands. To search courses by either name or subject number, use the following command. Make sure you include quotations when searching up multiple words.
```
mit-cc --search "TEXT"
```
To see the main menu, type:
```
mit-cc --menu
```

# License
mit-course-catalog-cli is available under the MIT license. See `LICENSE` file for more information.
