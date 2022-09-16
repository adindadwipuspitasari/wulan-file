# program untuk menghitung suhu
 
# konversi celcius fahrenheit
def conv_farenheit(celcius):
    convert_farenheit = 9 * celcius / 5 + 32
    return convert_farenheit

# konversi celcius ke kelvin
def conv_kelvin(celcius):
    convert_kelvin = celcius + 273
    return convert_kelvin

# konversi celcius ke reamur
def conv_reamur(celcius):
    convert_reamur = 4 * celcius / 5
    return convert_reamur
 
 
# create main menu
def main():
    print('Program Konversi Suhu')
    print('=======================')
 
    # create input
    temperatur = int(input('Masukan Skala Celcius: '))
 
    # cetak hasil
    print('++++++++++++++++++++++++++++++++++++++++++++')
    print(f'Hasil Konversi Suhu {temperatur} C adalah {conv_farenheit(temperatur)} Farenheit')
    print(f'Hasil Konversi Suhu {temperatur} C adalah {conv_reamur(temperatur)} Reamur')
    print(f'Hasil Konversi Suhu {temperatur} C adalah {conv_kelvin(temperatur)} Kelvin')
    print('++++++++++++++++++++++++++++++++++++++++++++++')
 
if __name__=='__main__':
    main()