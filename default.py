import generator

generator.use_dataset({})

document = generator.generate("default", generator.MENUM)
document.save()
