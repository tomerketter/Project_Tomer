from ext_depth.common import Human

sample = Human()
print(type(sample))

sample2 = Human()

sample2.name = "Giuseppe"

sample.print_name()
sample2.print_name()
