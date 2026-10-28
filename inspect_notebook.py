

# import json

# with open("fraud-detection-project.ipynb", encoding="utf-8") as f:
#     notebook = json.load(f)

# for i in [2, 3, 4]:
#     cell = notebook["cells"][i]
#     source = "".join(cell.get("source", []))

#     print(f"\n{'=' * 25} CELL {i} {'=' * 25}")
#     print(source)


import json

with open("fraud-detection-project.ipynb", encoding="utf-8") as f:
    notebook = json.load(f)

i = 5
print("CELL 5: BASELINE MODELS")
print("".join(notebook["cells"][i].get("source", [])))


