from dataclasses import dataclass


@dataclass
class Channels:
    suggestion: int = 985554459948122142
    bug_report: int = 985554479405490216
    errors: int = 986531210283069450
    reddit_faq: int = 985908874362093620
    tickets: int = 990679557596135475
    logs: int = 988162723890217040


TICKET_MESSAGE = 990679907795349554
STAFF_ROLE = 985943266115584010
TICKET_EMOJI = 990310706874290216
TICKET_PERMS = {
    "send_messages": True,
    "read_messages": True,
    "add_reactions": True,
    "embed_links": True,
    "attach_files": True,
    "read_message_history": True,
    "external_emojis": True
}
VALID_CODE_LANGUAGES = [
    "abap",
    "aes",
    "apex",
    "awk",
    "azcli",
    "bat",
    "bicep",
    "c",
    "cameligo",
    "cjam",
    "clojure",
    "cobol",
    "coffeescript",
    "cow",
    "cpp",
    "crystal",
    "csharp",
    "csp",
    "css",
    "d",
    "dart",
    "dash",
    "dockerfile",
    "dragon",
    "ecl",
    "elixir",
    "emacs",
    "erlang",
    "fortran",
    "fsharp",
    "go",
    "golfscript",
    "graphql",
    "groovy",
    "handlebars",
    "haskell",
    "hcl",
    "html",
    "ini",
    "java",
    "javascript",
    "jelly",
    "json",
    "julia",
    "kotlin",
    "less",
    "lexon",
    "liquid",
    "lisp",
    "lua",
    "lolcode",
    "m3",
    "markdown",
    "mips",
    "msdax",
    "mysql",
    "sql",
    "objective-c",
    "nasm",
    "nasm64",
    "nim",
    "ocaml",
    "octave",
    "osabie",
    "paradoc",
    "pascal",
    "pascaligo",
    "perl",
    "pgsql",
    "php",
    "plaintext",
    "ponylang",
    "postiats",
    "powerquery",
    "powershell",
    "prolog",
    "pure",
    "pug",
    "py",
    "pyth",
    "python",
    "python2",
    "qsharp",
    "r",
    "raku",
    "razor",
    "redis",
    "redshift",
    "restructuredtext",
    "rockstar",
    "ruby",
    "rust",
    "sb",
    "scala",
    "scheme",
    "scss",
    "shell",
    "sol",
    "sparql",
    "st",
    "swift",
    "systemverilog",
    "tcl",
    "twig",
    "typescript",
    "vb",
    "verilog",
    "vlang",
    "xml",
    "yaml",
    "yeethon",
    "zig",
]