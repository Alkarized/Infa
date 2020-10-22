file = open('src.yaml', "r", encoding='utf-8')
string = file.read()
file.flush()

#Замена : на \ для последующих преобразований + разбиение String на массив строк
string = string.replace(": ", "\\")
array = string.split("\n")
#Содержит тэги, которые в последствии надо будет закрыть по очереди.
lastbig = []
#Кол-во " " - пробелов в данной строке
countx = 0
#Кол-во " " - пробелов в предыдущей строке
county = 0
#Выходно xml код
addstring = ""

for i in range(0, len(array)):
    #делит строку на 2 элемента
    arrs_of_strings = array[i].split("\\")
    county = countx
    countx = arrs_of_strings[0].count(" ")
    #Убирает ненужные символы.
    if len(arrs_of_strings) > 1:
        arrs_of_strings[1] = arrs_of_strings[1].replace("' '", "\\")
        arrs_of_strings[1] = arrs_of_strings[1].replace("'", "")
        #Если значение идущее после : было пустым, то удаляет элемент
        if arrs_of_strings[1] == "":
            del arrs_of_strings[1]
    else:
        arrs_of_strings[0] = arrs_of_strings[0].replace(":", "")
    #Это нужно, чтобы выводить закрывающие элементы, которые имеют дочерних элементов.
    if county > countx:
        addstring += " " * lastbig[len(lastbig)-1].count(" ") + \
                     "</" + lastbig[len(lastbig)-1].replace(" ", "") + ">" + "\n"
        lastbig.pop()
    #Выводит элементы, которые не имеют дочерних элементов
    if len(arrs_of_strings) > 1:

        addstring += " " * countx + "<" + arrs_of_strings[0].replace(" ", "") + ">" \
                     + arrs_of_strings[1].replace("\\", "") + "</" + arrs_of_strings[0].replace(" ", "") + ">" + "\n"
    #Программа видит, что появился элемент, которые будет иметь дочерние элементы, запоминает его,
    #чтобы потом вывести его.
    else:
        lastbig.append(arrs_of_strings[0])
        addstring += " " * lastbig[len(lastbig)-1].count(" ") + \
                     "<" + lastbig[len(lastbig)-1].replace(" ", "") + ">" + "\n"

#Дописывает закрывающие элементы
while len(lastbig) > 1:
    addstring += " " * lastbig[len(lastbig)-1].count(" ") + \
                 "</" + lastbig[len(lastbig)-1].replace(" ", "") + ">" + "\n"
    lastbig.pop()
addstring += " " * lastbig[len(lastbig)-1].count(" ") + \
                 "</" + lastbig[len(lastbig)-1].replace(" ", "") + ">"
lastbig.pop()
file_write = open("bin.xml", "w")
file_write.write(addstring)