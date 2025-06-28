import re


class RegexValidator:

    @staticmethod
    def prices(price: str) -> bool:
        pattern = re.compile(r"\d+\.?\d{,2}")
        return bool(re.fullmatch(pattern, price))