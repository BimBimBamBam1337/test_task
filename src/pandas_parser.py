import pandas as pd

from collections import Counter

from .constants import DATA_DIR


class PandasParser:
    def __init__(self, files: list, mode: str):
        self.files = files
        self.mode = mode

    def _get_df(self):
        merged_df = []
        for file in self.files:
            df = pd.read_json(DATA_DIR / file, lines=True)
            merged_df.append(df)
        return pd.concat(merged_df, ignore_index=True)

    def get_count(self, *params: str):
        df = self._get_df()
        result = {}
        for param in params:
            if param in df.columns:
                result[param] = dict(Counter(df[param]))
        return result

    def get_average(self):
        df = self._get_df()
        return df.groupby("url")["response_time"].mean().to_dict()

    def _merge_count_and_average(self, param: str, sort_by="count", reverse=True):
        average_data = self.get_average()
        count_all_data = self.get_count(param).get(param, {})

        merged_dict = {
            key: {"average": average_data.get(key), "count": count_all_data.get(key)}
            for key in average_data.keys()
        }

        merged_dict = dict(
            sorted(
                merged_dict.items(),
                key=lambda item: (item[1][sort_by]),
                reverse=reverse,
            )
        )

        return merged_dict
