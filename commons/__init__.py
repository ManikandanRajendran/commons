# This is so that you can import ppack or import average from ppack
# in stead of from ppack.functions import average

from .decorators import singleton
from .functions import listChunker, report, weirdCase
from .api_calls import fetch_all_books


