html5slides-markdown
====================

It's based on Google's html5slides project, we add markdown support for it.

### What is Google's html5slides project?

Please visit \[http://code.google.com/p/html5slides/](http://code.google.com/p/html5slides/) to get more info about this project.

### Installation

You don't need to install this CLI, but to install its dependencies. Run `pip install -r requirements.txt` to install all packages it needs.

That's it!

### Usage

1. Write your slides in a markdown file
2. Remember, '---' is the signal for a new slide
3. Run `python givemeslides.py <your file name> > <your file name>.html` to generate slides file
4. In order to view it, remember to copy `html5slides.js`, `prettify.js` and `default.css` with this html file
