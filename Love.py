class Love:
    a = "Язва"
    b = "потебяша"
    c = "жопкалюблюпопка"
    d = "<3"

    def foo(self):
        return "{} {} {} {}".format(self.a[0], self.b[2:6], self.c[5:10], self.d)


g = Love()

print(g.foo())
