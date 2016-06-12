#!/usr/bin/env python3

class animal:
    def __init__(self, e, n, va):
        self.eyes = e
        self.name = n
        self.vat  = va

    def idme(self):
        print("Mein name ist "+ self.name + ". Ich habe " + str(self.eyes) + " Augen.")

    def ppar(self):
        if self.vat != None:
            print(self.name + "'s Parent ist: " + self.vat)
        else:
            print("Ich habe kein Parent")

    def rpar(self):
        return self.va

    def test(self):
        print("nur ein test zum branching!!")
