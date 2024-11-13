
berat= int(input('MAsukan Berat Badan (Kg): '))
tinggi= float(input('Masukan Tinggi Badan (M): '))



bmi= berat/(tinggi**2)
print(f'Berat Badan : {berat}')
print(f'Tinggi Badan : {tinggi}')
print(f'Nilai BMI Anda : {bmi}')

if bmi<18.5:
    print("Berat bedan kurang")
elif  (bmi>= 18.5 and bmi<24.9):
    print('Berat badan normal')
elif (bmi>= 25 and bmi <29.9):
    print("Kelabihan berat badan")
elif bmi>=30:
    print('Obesitas')

