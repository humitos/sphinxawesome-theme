"""Add more line highlighting options to Pygments.

The theme uses a custom pygments HTML formatter,
that adds the ability to highlight added/removed
lines in code.

To make use of this new function, this theme also
extends the default Sphinx ``code-block`` directive.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE for details.
"""
from typing import Any, Dict, Generator, List, Tuple

from docutils import nodes
from docutils.nodes import Node
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from pygments.formatters import HtmlFormatter
from pygments.util import get_list_opt
from sphinx.application import Sphinx
from sphinx.directives.code import CodeBlock, dedent_lines
from sphinx.highlighting import PygmentsBridge
from sphinx.locale import __
from sphinx.util import logging, parselinenos
from sphinx.util.docutils import SphinxDirective

from . import __version__

logger = logging.getLogger(__name__)


def container_wrapper(
    directive: SphinxDirective, literal_node: Node, caption: str
) -> nodes.container:
    """We need the container to have class highlight."""
    container_node = nodes.container(
        "", literal_block=True, language=literal_node["language"], classes=["highlight"]
    )
    parsed = nodes.Element()
    directive.state.nested_parse(
        StringList([caption], source=""), directive.content_offset, parsed
    )
    if isinstance(parsed[0], nodes.system_message):
        msg = __("Invalid caption: %s" % parsed[0].astext())
        raise ValueError(msg)
    elif isinstance(parsed[0], nodes.Element):
        caption_node = nodes.caption(parsed[0].rawsource, "", *parsed[0].children)
        caption_node.source = literal_node.source
        caption_node.line = literal_node.line
        container_node += caption_node
        container_node += literal_node
        return container_node
    else:
        raise RuntimeError  # never reachedo


class AwesomeHtmlFormatter(HtmlFormatter):
    """Implement additional line-highlighting options."""

    def __init__(self, **options: Any) -> None:
        """Implement `hl_added` and `hl_removed` options."""
        self.added_lines = set()
        self.removed_lines = set()

        for lineno in get_list_opt(options, "hl_added", []):
            try:
                self.added_lines.add(int(lineno))
            except ValueError:
                pass

        for lineno in get_list_opt(options, "hl_removed", []):
            try:
                self.removed_lines.add(int(lineno))
            except ValueError:
                pass

        super().__init__(**options)

    def _highlight_lines(self, tokensource: Tuple[Any, Any]) -> Generator:
        """Add classes to `hl_added` and `hl_removed` lines.

        This implementation only deals with class based styling and removes
        the parent's implementation for inline styling simply because I don't
        need them in Sphinx.
        """
        for i, (t, value) in enumerate(tokensource):
            if t != 1:
                yield t, value
            if i + 1 in self.hl_lines:  # i + 1 because Python indexes start at 0
                yield 1, "<mark>%s</mark>" % value
            elif i + 1 in self.added_lines:  # I could use semantic <ins> here
                yield 1, "<ins>%s</ins>" % value
            elif i + 1 in self.removed_lines:  # I could use semantic <del> here
                yield 1, "<del>%s</del>" % value
            else:
                yield 1, value

    def wrap(self, source: Generator, outfile: Any) -> Generator:
        """Return a <pre><code> wrapped element.

        Pygments returns the highlighted block wrapped inside a ``div.highlight``.
        We want to get the <pre> only, and we'll wrap it in a div later, so that
        we can add the code button, and an optional caption.

        Returning a <pre><code> block follows the HTML5 specification for marking
        up code blocks.
        """
        return self._wrap_pre(self._wrap_code(source))

    def _wrap_pre(self, inner: Generator) -> Generator:
        """Overwrite because no unecessary empty spans.

        This is a simplification as the theme doesn't use inline styles.
        """
        if self.filename:
            yield 0, ('<span class="filename">' + self.filename + "</span>")

        yield 0, ("<pre>")
        yield from inner
        yield 0, ("</pre>")

    def format_unencoded(self, tokensource: Tuple[Any, Any], outfile: Any) -> None:
        """Add added/removed lines highlighting to the formatting pipeline."""
        source = self._format_lines(tokensource)
        if self.hl_lines or self.added_lines or self.removed_lines:
            source = self._highlight_lines(source)
        if not self.nowrap:
            if self.linenos == 2:
                source = self._wrap_inlinelinenos(source)
            if self.lineanchors:
                source = self._wrap_lineanchors(source)
            if self.linespans:
                source = self._wrap_linespans(source)
            source = self.wrap(source, outfile)
            if self.linenos == 1:
                source = self._wrap_tablelinenos(source)
            if self.full:
                source = self._wrap_full(source, outfile)

        for _, piece in source:
            outfile.write(piece)


class AwesomeCodeBlock(CodeBlock):
    """Add options to highlight added and removed lines to `code-block` directives."""

    new_options = {
        "emphasize-added": directives.unchanged_required,
        "emphasize-removed": directives.unchanged_required,
    }

    option_sec = CodeBlock.option_spec.update(new_options)

    def run(self) -> List[Node]:  # noqa: C901
        """Implement option method."""
        document = self.state.document
        code = "\n".join(self.content)
        location = self.state_machine.get_source_and_line(self.lineno)

        linespec = self.options.get("emphasize-lines")
        if linespec:
            try:
                nlines = len(self.content)
                hl_lines = parselinenos(linespec, nlines)
                if any(i >= nlines for i in hl_lines):
                    logger.warning(
                        __("line number spec is out of range(1-%d): %r")
                        % (nlines, self.options["emphasize-lines"]),
                        location=location,
                    )

                hl_lines = [x + 1 for x in hl_lines if x < nlines]
            except ValueError as err:
                return [document.reporter.warning(err, line=self.lineno)]
        else:
            hl_lines = None

        # add parsing for hl_added and hl_removed
        linespec = self.options.get("emphasize-added")
        if linespec:
            try:
                nlines = len(self.content)
                hl_added = parselinenos(linespec, nlines)
                if any(i >= nlines for i in hl_added):
                    logger.warning(
                        __("line number spec is out of range(1-%d): %r")
                        % (nlines, self.options["emphasize-added"]),
                        location=location,
                    )
                hl_added = [x + 1 for x in hl_added if x < nlines]
            except ValueError as err:
                return [document.reporter.warning(err, line=self.lineno)]
        else:
            hl_added = None

        # add parsing for hl_added and hl_removed
        linespec = self.options.get("emphasize-removed")
        if linespec:
            try:
                nlines = len(self.content)
                hl_removed = parselinenos(linespec, nlines)
                if any(i >= nlines for i in hl_removed):
                    logger.warning(
                        __("line number spec is out of range(1-%d): %r")
                        % (nlines, self.options["emphasize-removed"]),
                        location=location,
                    )
                hl_removed = [x + 1 for x in hl_removed if x < nlines]
            except ValueError as err:
                return [document.reporter.warning(err, line=self.lineno)]
        else:
            hl_removed = None

        if "dedent" in self.options:
            location = self.state_machine.get_source_and_line(self.lineno)
            lines = code.split("\n")
            lines = dedent_lines(lines, self.options["dedent"], location=location)
            code = "\n".join(lines)

        literal = nodes.literal_block(code, code)
        if "linenos" in self.options or "lineno-start" in self.options:
            literal["linenos"] = True
        literal["classes"] += self.options.get("class", [])
        literal["force"] = "force" in self.options
        if self.arguments:
            # highlight language specified
            literal["language"] = self.arguments[0]
        else:
            # no highlight language specified.  Then this directive refers the current
            # highlight setting via ``highlight`` directive or ``highlight_language``
            # configuration.
            literal["language"] = self.env.temp_data.get(
                "highlight_language", self.config.highlight_language
            )
        extra_args = literal["highlight_args"] = {}
        if hl_lines is not None:
            extra_args["hl_lines"] = hl_lines
        if hl_added is not None:
            extra_args["hl_added"] = hl_added
        if hl_removed is not None:
            extra_args["hl_removed"] = hl_removed
        if "lineno-start" in self.options:
            extra_args["linenostart"] = self.options["lineno-start"]
        self.set_source_info(literal)

        # if there is a caption, we need to wrap this node in a container
        caption = self.options.get("caption")
        if caption:
            try:
                literal = container_wrapper(self, literal, caption)
            except ValueError as exc:
                return [document.reporter.warning(exc, line=self.lineno)]

        self.add_name(literal)

        return [literal]


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Set up this internal extension."""
    PygmentsBridge.html_formatter = AwesomeHtmlFormatter
    directives.register_directive("code-block", AwesomeCodeBlock)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
