# zig-keycode-generator
A python script that generates zig-keycode-enums from a given dataset

## How to use?
```py
import generator

generator.use_dataset({ ... })

document = generator.generate("my_enum_name")
document.save()
```
> [!TIP]
> This will save the `my_enum_name.zig` file to [`out`](./out/).