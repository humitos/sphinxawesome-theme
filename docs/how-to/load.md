(sec:load)=

# Load the theme

```{rst-class} lead
Learn how to add the theme to your Sphinx project.
```

```{contents} On this page
---
local: true
backlinks: none
---
```

## Load the theme from a Python package

Add the `html_theme` configuration option to your Sphinx configuration file `conf.py`:

```{code-block} python
---
caption: "File: conf.py"
---
html_theme = "sphinxawesome_theme"
```

## Load the theme from a local directory

You can load the theme from a directory on your computer. This can be useful if you
want to build your own theme, and you don't want to separate your documentation from the
theme.

:::{note}
When loading the theme from a local directory, you need to manage the dependencies
yourself. This theme needs the `beautifulsoup` package to run. You can install it with
`pip`:

```shell-session
pip install bs4
```

:::

The following example assumes you have a Sphinx project with the following structure,
and you want to load the theme from the `_themes/` folder.

```shell-session
./
├── conf.py
├── index.rst
├── _themes/
└── ...
```

To load the theme from a local directory:

1. {ref}`sec:fork-and-clone`.

1. Copy the directory `sphinxawesome-theme/src/sphinxawesome_theme/` into your
   `_themes/` directory in the Sphinx project:

   ```shell-session
   cp -r sphinxawesome-theme/src/sphinxawesome_theme _themes/
   ```

1. Add the `_themes/` directory to the system path in the Sphinx configuration:

   ```{code-block} python
   ---
   caption: "File: conf.py"
   ---
   import os
   import sys

   sys.path.append(os.path.abspath("_themes"))
   ```

   Adding this directory makes it discoverable for Python.

1. Add the `themes` directory to the `exclude_patterns` list to prevent Sphinx from
   searching this path for documentation files:

   ```{code-block} python
   ---
   caption: "File: conf.py"
   ---
   exclude_patterns = ["_themes"]
   ```

1. Add the theme as an extension and as a theme:

   ```{code-block} python
   ---
   caption: "File: conf.py"
   ---
   extensions = ["sphinxawesome_theme"]
   html_theme = "sphinxawesome_theme"
   ```