print('\n' * 4)

masa = float(input('Podaj masę kota w kg  '))

pound = 0.453592
kilogram = 2.3 / 0.453592


zapotrzebowanie_dzienne_na_białko = masa * kilogram

end = round(float(zapotrzebowanie_dzienne_na_białko),2)


print('Zapotrzebowanie dzienne na białko w g:', end)
print ('\n' *2)
print('Co odpowiada:')

kurczak = round(float(end *100 / 31),2)
watrobka = round(float(end *100 / 26), 2)

print(kurczak, 'g piersi kurczaka albo',watrobka, 'g wątróbki drobiowej' )