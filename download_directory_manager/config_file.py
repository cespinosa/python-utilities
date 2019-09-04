HOME_FOLDER = "/home/sglavoie"
FOLDER_TO_TRACK = f"{HOME_FOLDER}/Downloads"
FORMATS = {
    "archive": (".7z", ".deb", ".pkg", ".rar", ".tar.gz", ".z", ".zip"),
    "audio": (".aac", ".flac", ".m3u", ".m4a", ".mp3", ".ogg", ".wav", ".wma"),
    "book": (".epub",),
    "database": (
        ".csv",
        ".dat",
        ".db",
        ".mdb",
        ".pdb",
        ".sql",
        ".sqlite",
        ".sqlite3",
        ".tar",
        ".xml",
    ),
    "disk": (".dmg", ".iso", ".toast", ".vcd"),
    "document": (
        ".doc",
        ".docx",
        ".odt",
        ".pdf",
        ".rtf",
        ".sla",
        ".txt",
        ".wpd",
    ),
    "executable": (
        ".apk",
        ".bat",
        ".bin",
        ".cgi",
        ".exe",
        ".jar",
        ".pl",
        ".py",
        ".wsf",
    ),
    "font": (".fnt", ".fon", ".otf", ".ttf", ".eot", ".woff", ".woff2"),
    "image": (
        ".ai",
        ".bmp",
        ".eps",
        ".gif",
        ".ico",
        ".jpeg",
        ".jpg",
        ".png",
        ".ps",
        ".psd",
        ".svg",
        ".tif",
        ".tiff",
        ".webp",
        ".xps",
    ),
    "mathematics": (".ggb", ".tex"),
    "presentation": (".odp", ".pps", ".ppt", ".pptx"),
    "programming": (
        ".c",
        ".class",
        ".cpp",
        ".cs",
        ".h",
        ".ipynb",
        ".java",
        ".json",
        ".rb",
        ".sh",
        ".swift",
        ".vb",
    ),
    "security": (".cer", ".gpg", ".kdb", ".key", ".pgp"),
    "spreadsheet": (".ods", ".xlr", ".xls", ".xlsx"),
    "torrent": (".torrent",),
    "video": (
        ".3g2",
        ".3gp",
        ".avi",
        ".flv",
        ".h264",
        ".m4v",
        ".mkv",
        ".mov",
        ".mp4",
        ".mpeg",
        ".mpg",
        ".swf",
        ".vob",
        ".webm",
        ".wmv",
    ),
    "web": (
        ".asp",
        ".css",
        ".htm",
        ".html",
        ".js",
        ".jsp",
        ".php",
        ".rss",
        ".xhtml",
    ),
}