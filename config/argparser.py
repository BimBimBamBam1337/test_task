import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--file", required=True, help="Путь к файлу для обработки", nargs="+"
)
parser.add_argument("--report", choices="average", help="Тип отчета (только average)")
