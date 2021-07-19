# How to install the theme

Depending on how you want to use the theme and its extensions, use one of the following
methods to install the Sphinx awesome theme.

```{contents} On this page
:local:
:backlinks: none
```

## Install the theme as a Python package (recommended)

In most use cases, you should install the theme as a Python package. You can make small
modifications by adding custom CSS or JavaScript files. See {ref}`Add or override styles` for more information.

You can install a released version from the Python Package Index,
[PyPI](https://pypi.org/project/sphinxawesome-theme/):

```console
pip install sphinxawesome-theme
```

You can also install the latest development version of the theme directly from GitHub:

```console
pip install git+https://github.com/kai687/sphinxawesome-theme.git
```

<!-- vale 18F.UnexpandedAcronyms = NO -->
Check the "HEAD" section at the top of the
<!-- vale 18F.UnexpandedAcronyms = YES -->
[CHANGELOG](https://github.com/kai687/sphinxawesome-theme/blob/master/CHANGELOG.rst)
file. These features and bugfixes are available in the version on GitHub but not yet in
the released version on PyPI\*.

## Install the theme as a local package

If you want to use a modified version of the theme, you can load the theme from a local
Python package. This doesn't require any special configuration, but can be slower
initially, since you need to rebuild and reinstall the local package after each
modification.

1. {ref}`Create a local copy of the theme`
1. Build the theme as a Python package:

   ```console
   poetry build
   ```

   This command creates a new directory `dist/` containing the source distribution in
   `.tar.bz2` format and as wheel in a `.whl` file.

1. In your project, install the theme from the locally built package:

   ```console
   pip install /path/to/sphinxawesome_theme/dist/sphinxawesome_theme-*-py3-none-any.whl
   ```

   This command installs the pre-built package in the current environment.

   :::{tip}
   You can also skip the separate build step and install the top level directory:

   ```console
   pip install /path/to/sphinxawesome_theme
   ```

   This command builds and installs the package in one step. It's a bit slower than the
   procedure outlined before.
   :::

## Set up a development environment

The project has two different sets of dependencies, for Python and JavaScript. If you
want to write documentation, write tests, or modify the Python extensions, install the
Python dependencies. See {ref}`Install Python dependencies` for more information.

If you want to modify the Jinja2 templates[^1], the CSS, or the JavaScript files, you
also need to install the JavaScript dependencies. See {ref}`Install JavaScript
dependencies` for more information.

<!-- vale Google.Colons = NO -->
<!-- vale 18F.SentenceLength = NO -->
<!-- vale 18F.Reading = NO -->
[^1]: Technically, you only need to add the JavaScript dependencies, if you want to _change_ the CSS classes inside the templates. For example, if you add a utility class that wasn't previously used, you need to run the JavaScript/CSS pipeline again to include it in the final style sheet.
<!-- vale Google.Colons = YES -->
<!-- vale 18F.SentenceLength = YES -->
<!-- vale 18F.Reading = YES -->

In both cases, create a local copy first.

## Create a local copy of the theme

In order to modify the theme, create a local copy first:

1. **Optional:** fork the repository

   If you don't want to merge your changes with the original repository, you can skip
   this step. See
   <!-- vale Awesome.SpellCheck = NO -->
   [Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
   <!-- vale Awesome.SpellCheck = YES -->
   in the GitHub documentation for more information.

1. Clone the (forked) repository:

   If you forked the repository, enter:

   ```{samp}
   git clone https://github.com/{YOUR_GITHUB_USERNAME}/sphinxawesome-theme.git
   ```

   Replace {samp}`{YOUR_GITHUB_USERNAME}` with your GitHub username. If you didn't fork
   the repository, clone the original repository:

   ```console
   git clone https://github.com/kai687/sphinxawesome-theme.git
   ```

   See [Cloning a
   repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)
   in the GitHub documentation for more information.

## Install Python dependencies

The Sphinx awesome theme uses [Poetry](https://python-poetry.org/) to manage the Python
dependencies. Testing, linting, and building the documentation is handled by
[Nox](https://nox.thea.codes/en/stable/).

Follow these steps to install the Python dependencies:

1. Follow the recommended steps for [how to install Poetry](https://python-poetry.org/docs/#installation).

   On macOS and Linux, enter:

   ```console
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
   ```

   On Windows PowerShell:

   ```PowerShell
   (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
   ```

1. Install Nox via pip:

   ```console
   pip install --user --upgrade nox
   ```

   If you want to use the same version of Poetry and Nox as the original repository, see
   the versions in the file
   [`constraints.txt`](https://github.com/kai687/sphinxawesome-theme/blob/master/.github/workflows/constraints.txt)

1. Install the Python dependencies:

   ```console
   poetry install
   ```

Check Poetry's [documentation](https://python-poetry.org/docs/basic-usage/) for more information.

<!-- vale 18F.Clarity = NO -->
1. **Optional:** install pre-commit hooks:

   ```console
   poetry run pre-commit install
   ```

   If you don't plan on committing any changes to the forked repository, you can skip
   this step. Check the file
   [`.pre-commit-config.yaml`](https://github.com/kai687/sphinxawesome-theme/blob/master/.pre-commit-config.yaml)
   to see which pre-commit hooks are active.

   To test pre-commit in combination with poetry, run:

   ```console
   poetry run pre-commit run --all
   ```
<!-- vale 18F.Clarity = YES -->

1. Run a Nox session.

   You can run any Nox session to confirm that the environment is working.
   To list the available sessions, enter:

   ```console
   nox -ls
   ```

   Enter `nox` without any option to run the default sessions,
   such as building the docs, testing, and linting.

   For example, to build the documentation with Python 3.9, enter:

   ```console
   nox -s docs -p 3.9
   ```

## Install JavaScript dependencies

Follow these steps to install the JavaScript dependencies:

1. Check, if [Node.js](https://nodejs.org/en/) is installed:

   ```console
   node --version
   ```

   If Node.js is installed, this command returns the version number,
   for example:

   ```console
   v14.15.0
   ```

   If the command fails, you may need to install Node.js first,
   or activate it in your current terminal session.
   Have a look at the [Node Version Manager](https://github.com/nvm-sh/nvm)
   project for a way to install and manage multiple versions of Node.js.

1. **Optional:** install [`yarn`](https://classic.yarnpkg.com/lang/en/):

   ```console
   npm install --global yarn
   ```

   The awesome theme uses yarn (classic). The dependencies are pinned to the specific
   versions in the `yarn.lock` file. If you don't want to use the same versions of the
   JavaScript packages, you can use `npm` as well.

1. Change to the `theme-src/` directory:

   ```{code-block} console
   ---
   emphasize-lines: 4
   ---
   ./sphinxawesome-theme/
      ├src/
      │ ├sphinxawesome_theme/
      │ └theme-src/
      ├docs/
      └...
   ```

1. Install the JavaScript dependencies:

   ```console
   yarn install
   ```

1. Build the theme:

   ```console
   yarn build
   ```