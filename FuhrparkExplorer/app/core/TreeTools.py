from typing import Callable, Any, Optional

from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem


class TreeTools:

    @staticmethod
    def check_removed_car(
        tree_widget: QTreeWidget,
        car: str,
        sender: Optional[Callable[..., None]] = None,
        *args: Any
    ) -> None:
        for i in range(tree_widget.topLevelItemCount()):
            brand_item: QTreeWidgetItem = tree_widget.topLevelItem(i)

            for j in range(brand_item.childCount()):
                model_item: QTreeWidgetItem = brand_item.child(j)

                if model_item.text(0).lower() == car.lower():
                    # 🔁 Auswahl vorbereiten: Nachbar oder Parent
                    next_item: Optional[QTreeWidgetItem] = None
                    if brand_item.childCount() > 1:
                        if j < brand_item.childCount() - 1:
                            next_item = brand_item.child(j + 1)
                        elif j > 0:
                            next_item = brand_item.child(j - 1)

                    # Entferne das Modell
                    brand_item.removeChild(model_item)

                    # Marke entfernen, wenn leer
                    if brand_item.childCount() == 0:
                        index = tree_widget.indexOfTopLevelItem(brand_item)
                        tree_widget.takeTopLevelItem(index)
                        # 🔁 als Fallback z. B. nächstes Brand-Item selektieren
                        if tree_widget.topLevelItemCount() > 0:
                            fallback_item = tree_widget.topLevelItem(0)
                            fallback_child = fallback_item.child(0)
                            if fallback_child:
                                tree_widget.setCurrentItem(fallback_child)

                    # 🔁 Modell selektieren, falls vorhanden
                    elif next_item:
                        tree_widget.setCurrentItem(next_item)

                    # 🔁 Eventuell Signal feuern
                    if sender:
                        sender(*args)
                    return
