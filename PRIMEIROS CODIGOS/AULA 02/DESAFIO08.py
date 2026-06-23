print("===== METROS EM CENTIMETROS E MILIMETROS =====")

metro = float(input("Digite quantos metros deseja transformar: "))

km = metro / 1000
hm = metro / 100
dam = metro / 10

dm = metro * 10
cm = metro * 100
milimetros = metro * 1000

print("Metros: {} \nDIMINUINDO == Centimetros {:.0f} == Milimetros {:.0f} \nAUMENTANDO == Decimetros {} == Hectometros {} == Quilometros {}".format(metro,cm,milimetros,dm,dam,km))