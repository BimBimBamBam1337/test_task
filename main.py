# main.py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True, help="Путь к файлу для обработки")
parser.add_argument("--report", choices="average", help="Тип отчета (только average)")
args = parser.parse_args()

print(f"Файл: {args.file}")
print(f"Отчет: {args.report}")
