class Persona:
    lita=[]
    def personador(self,nombre,edad):
        self.lita.append((nombre,edad))
        return self.lita
    
    def entregador(self):
        return self.lita

for i in range(5):
    per=input("Ingresa una persona: ")
    ed=int(input("Ingresa su edad: "))
    Persona.personador(Persona,per,ed)
print(Persona.entregador(Persona))