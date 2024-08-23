# zig-keycode-generator
A python script that generates zig-keycode-enums from a given dataset
> [!WARNING]
> This project isn't perfect, and won't be able to map all keys automatically. If you encounter an error, please open the [`resources.py`](./generator/resources.py) file and look up the keywords accepted by the program.

## How to use?
```py
import generator

generator.use_dataset({ ... })

document = generator.generate("my_enum_name")
document.save()
```
> [!TIP]
> This will save the `my_enum_name.zig` file to [`out`](./out/).
> See an example of the config file in [`IOKit_OsX.py`](./IOKit_OsX.py)