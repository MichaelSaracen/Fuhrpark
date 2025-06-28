from pathlib import Path
import subprocess

ui_dir = Path("ui_files")
ui_files = ui_dir.glob("*.ui")
gui_path = Path("app/gui")
init_string = ""
print("🔁 Converting ui files » py files ...")

for ui_file in ui_files:
    output_py = gui_path / f"Ui_{ui_file.stem}.py"
    print(f"[+] {ui_file} » {output_py}")
    subprocess.run(["pyside6-uic", ui_file, "-o", output_py])
    init_string += f"from .{output_py.stem} import {output_py.stem}\n"

init_path = gui_path / "__init__.py"
print(f"\n🔁 Writing to {init_path}")
print(init_string)
init_path.write_text(init_string)

print("🔁 Converting ressources.qrc » ressources_rc.py")
subprocess.run(["pyside6-rcc", "assets/ressources.qrc", "-o", "ressources_rc.py"])

print("🔁 running main.py")
subprocess.run(["python", "main.py"])
