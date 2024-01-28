class ScraperError(Exception):
    """Base class for exceptions in scraper module."""
    pass

class HTTPResponseError(ScraperError):
    """Raised when there's an HTTP response-related error."""
    pass

class ParserError(Exception):
    """Base class for exceptions in parser module."""
    pass

class ParsingDataError(ParserError):
    """Raised when there's a data parsing error."""
    pass
