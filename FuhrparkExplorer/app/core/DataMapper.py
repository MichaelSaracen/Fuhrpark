from typing import List, Tuple, Dict, Any
from decimal import Decimal

class DataMapper:

    @staticmethod
    def extract_first_rows(data: List[List[Tuple[Any]]]) -> List[str]:
        return [ row[0] for row in data ]


    @staticmethod
    def map_customer_data_to_dict(data: List[Any]) -> Dict:
        _id, f_name, name, age, tel, city, zip_, street, h_num, bank, iban = data

        details = {"id": _id, "Vorname": f_name, "Nachname": name, "Telefon": tel }

        return details



    @staticmethod
    def convert_tree_structure_to_view(data: Dict) -> Dict:
        brand = list(data.keys())[0]
        model = list(data[brand].keys())[0]
        details = data[brand][model]
        image = details.pop("Bild")

        d: Dict = {
            "Marke" : brand,
            "Modell" : model,
            "Bild" : image,
            "Details": details
        }
        return d

    @staticmethod
    def map_to_nested_car_status(rows: List[Tuple[Any]]) -> Dict[str, Dict[str, Dict[str, List[Any]]]]:
        results = dict()
        for s_id, status, car_num, brand, model, pic in rows:
            if status not in results:
                results[status] = {}

            if brand not in results[status]:
                results[status][brand] = {}

            results[status][brand][model] = [s_id, car_num, pic]
        return results

    @staticmethod
    def map_to_nested_price_dict(rows: List[Tuple[str, str, Decimal]]) -> Dict[str, Dict[str, float]]:
        """
        Wandelt den Datenbank-Eintrag in ein Dictionary um:\n
        -- Database.call_procedure("p_get_fahrzeug_tagespreis")[0]\n

        von:
        [('Audi', 'A3', Decimal('50.00')), ('Audi', 'Q7', Decimal('50.00'))]

        zu:
        {'Audi': {'A3': 50.0, 'Q7': 50.0}}
        :param rows:
        :return:
        """
        result: Dict[str, Dict[str, float]] = {}
        for brand, model, price in rows:
            if brand not in result:
                result[brand] = {}
            result[brand][model] = float(price)
        return result

    @staticmethod
    def map_to_tree_structure(rows: List[Tuple[Any, ...]]) -> Dict[str, Dict[str, Dict[str, Any]]]:
        tree_data: Dict[str, Dict[str, Dict[str, Any]]] = {}

        for row in rows:

            _id, brand, model, image, fuel, gearbox, power, consumption, doors, seats, color, price = row

            details = DataMapper.map_car_details(_id, image, fuel, gearbox, power, consumption, doors, seats, color, price)

            if brand not in tree_data:
                tree_data[brand] = {}
            tree_data[brand][model] = details

        return tree_data

    @staticmethod
    def map_car_details(_id, image, fuel, gearbox, power, consumption, doors, seats, color, price) -> Dict[str, str]:

        #price_str = f"{int(price):,}".replace(",", ".") + "€"
        details = {
            "Fahrzeugnummer": str(_id).zfill(8),
            "Getriebe": gearbox,
            "Kraftstoff": fuel,
            "Leistung": f"{str(power)}PS",
            "Verbrauch": f"{str(consumption)}L",
            "Türen": str(doors),
            "Sitze": str(seats),
            "Farbe": color,
            "Grundpreis": f"{price:.2f}€",
            "Bild": image
        }
        return details

    @staticmethod
    def sort_dict_by_longest_name(d: Dict[str, Any]):
        """
        Sortiert das Dict nach dem längsten Namen und zusätzlich alphabetisch. Gibt das Sortierte Dict dann wieder.
        :param d:
        :return:
        """
        return dict(
            sorted(
                d.items(), key=lambda item: (len(item[0] + ": " + item[1]), item[0]), reverse=True
            )
        )