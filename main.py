import config

from tabulate import tabulate
from src.pandas_parser import PandasParser

args = config.parser.parse_args()
pp = PandasParser(args.file, args.report)
merged = pp._merge_count_and_average("url")
data = [{"handler": key, **value} for key, value in merged.items()]
print(tabulate(data, headers="keys", showindex="always"))
