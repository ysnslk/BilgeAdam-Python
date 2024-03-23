# File I/O
# Dosya açma ve kapama ve üzerimde crud işlemleri yapabileceğimiz bize fonksiyonlar tanımlayan file modülü ile çalışır.

# # Dosya açma
# file = open(file='new_file.txt', mode='w', encoding='utf-8')
# file.write('Full Name: Yasin Solak\nOccupation: Developer\n')
# file.close()
#
# # Yukarıda yaratılan dosya üzerine yeni kayıt ekleyelim.
# file = open(file='new_file.txt', mode='a', encoding='utf-8')
# file.write('Programming Language: Python\n')
# file.close()
#
# # Dosyadan veri okuyalım.
# file = open(file='new_file.txt', mode='r', encoding='utf-8')
# for line in file.readlines():
#     print(line)

# region Task 1
# exam_grades.txt dosyasını yaratın
def create_exam_grades() -> None:
    file = open(file='exam_grades.txt', mode='w', encoding='utf-8')
    file.close()
# endregion
# region Task 2
# Kullanıcıdan first_name, last_name, midterm, final, homework bilgilerini alarak exam_grades dosyasına yazalım. Aşağıdaki formatta yazalım
# Burak Yılmaz:30,30,30
# İlgili dosyayı with open() kullanarak açalım.
def create_exams() -> None:
    first_name = input('First Name: ').strip()
    last_name = input('Last Name: ').strip()
    midterm = float(input('Midterm: '))
    final = float(input('Final: '))
    homework = float(input('Homework: '))
    with open("exam_grades.txt", "w",encoding="utf-8") as file:
        file.write('{} {}:{}, {}, {}'.format(first_name, last_name,midterm,final,homework))
# endregion

# region Task 3
# harf notunu hesapla ve return et
def calculate_grade(row: str) -> str:
    values = row.split(':')
    full_name = values[0]
    grade_list = values[1].split(',')
    ort = float(grade_list[0]) * 0.3 + float(grade_list[1]) * 0.6 + float(grade_list[2]) * 0.1
    if 90<=ort <= 100:
        return f'{full_name}:AA'
    elif 85<=ort <= 89:
        return f'{full_name}:BA'
    elif 80<=ort <= 84:
        return f'{full_name}:BB'
    elif 75<=ort <= 79:
        return f'{full_name}:CB'
    elif 70<=ort <= 74:
        return f'{full_name}:CC'
    elif 65<=ort <= 69:
        return f'{full_name}:CD'
    elif 60<=ort <= 64:
        return f'{full_name}:DD'
    elif 55<=ort <= 59:
        return f'{full_name}:DC'
    elif 50<=ort <= 54:
        return f'{full_name}:FD'
    else:
        return f'{full_name}:FF'
    return 'harf notu'
# endregion

# region Task 4
# exam_grades.txt verileri satır satır okuyalım
# harf notlarını hesaplatalım. ve bir listeye ekleyelimö
# ilgili listeyi return
def read_exam_grades() -> list:
    grades_list = []
    with open('exam_grades.txt', 'r', encoding='utf-8') as file:
        for line in file:
            grade = calculate_grade(line)
            grades_list.append(grade)
    return grades_list

#endregion

# region Task 5
# result.txt isimli dosyaya öğrencilerin isim soyisin: harf notunu yazdıralım.
def register_grades(grades_list: list) -> None:
    with open('result.txt', 'w', encoding='utf-8') as file:
        for grade in grades_list:
            file.write(grade + "\n")
# endregion

# region Task 5
# result.txt dosyasının verilerini ekrana yaz
def read_result():
    with open('result.txt', 'r', encoding='utf-8') as file:
        for row in file:
            print(row)
# endregion

def menu():
    print(f"""
    Menu
    ===============
    Read Grades      ==> 1
    Enter Grades     ==> 2
    Calculate Grades ==> 3
    Read Result      ==> 4
    """)

def main():
    menu()
    while True:
        process = input('Please choose a transaction: ')
        if process == '1':
            read_exam_grades()
            print('Grades have been read')
        elif process == '2':
            create_exams()
            print('Grades have been created')
        elif process == '3':
            grades_list = read_exam_grades()
            for grade in grades_list:
                print(grade)
            print('Grades have been calculated and displayed..!')
        elif process == '4':
            read_result()
        elif process == 'e':
            print("Application has been closing")
            break
        else:
            print("Please choose a valid transaction number...!")

main()


main()