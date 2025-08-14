from model.model import Model

model = Model()
conn = model.getConnections()
for r in conn:
    print(r)
