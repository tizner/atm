#-*-coding: utf-8 -*-

def cupurnosty(i):
    cup = array[i].strip()
    cup_nom = cup.split(" ")[0]
    cup_val = cup.split(" ")[1].replace('\n', '')
    return(cup_nom,cup_val)


def if_schet_deb_zad(valuta,schet_obs, schet_deb_zad, schet_kor_podkrep, schet_inkas, schet_izlish):
    my_file.write("[enter]" + '\n')
    my_file.write("[pf6]" + '\n')
    my_file.write("[wait inp inh]" + '\n')
    my_file.write("wait 10 sec until FieldAttribute 0008 at (3,28)" + '\n')
    my_file.write("[wait app]" + '\n')
    my_file.write("[wait inp inh]" + '\n')
    my_file.write("[enter]" + '\n')
    my_file.write("[wait inp inh]" + '\n')
    my_file.write("wait 10 sec until FieldAttribute 0008 at (7,28)" + '\n')
    my_file.write("wait 10 sec until cursor at (7,29)" + '\n')
    my_file.write("[wait app]" + '\n')
    my_file.write("[wait inp inh]" + '\n')
    my_file.write('"'+valuta + '\n')
    my_file.write("[enter]" + '\n')
    my_file.write("[wait inp inh]" + '\n')
    my_file.write("wait 10 sec until FieldAttribute 0008 at (9,28)" + '\n')
    my_file.write("wait 10 sec until cursor at (9,29)" + '\n')
    my_file.write("[wait app]" + '\n')
    my_file.write("[wait inp inh]" + '\n')

    if schet_obs != '':
        my_file.write('"' + schet_obs + '\n')
    else:
        my_file.write("[down]" + '\n')

    if schet_deb_zad != '':
        my_file.write('"' + schet_deb_zad + '\n')
    else:
        my_file.write("[down]" + '\n')

    if schet_kor_podkrep != '':
        my_file.write('"' + schet_kor_podkrep + '\n')
    else:
        my_file.write("[down]" + '\n')

    if schet_inkas != '':
        my_file.write('"' + schet_inkas + '\n')
    else:
        my_file.write("[down]" + '\n')

    if schet_izlish != '':
        my_file.write('"' + schet_izlish + '\n')
    else:
        my_file.write("[down]" + '\n')


array = list(open('банкомат.txt', 'r'))

kniga = open('Книга.csv', 'r')


branch =''
schet_obsl = ''
schet_inkas = ''
schet_izlish = ''
schet_kor_podkr = ''

schet_deb_zad_usd = ''
schet_deb_zad_eur = ''


schet_obs_rur_cn = ''
schet_obs_usd_cn = ''
schet_obs_eur_cn = ''

schet_inkas_rur_cn =''
schet_inkas_usd_cn =''
schet_inkas_eur_cn =''

schet_izlish_rur_cn=''
schet_izlish_usd_cn=''
schet_izlish_eur_cn=''




for i, st in enumerate(array):
    # берем номер банкомата
    if '1. Присвоенный номер банкомата (терминал)' in st:
        b = st.split(":")
        b = b[1].replace('.\n', '')

    # берем  адрес
    if 'Населенный пункт:' in st:
        g = st.split(":")
        g = g[1].replace('\n', '').strip()

    if 'Улица:' in st:
        s = st.split(":")
        s = s[1].replace('\n', '').strip()

    if 'Дом:' in st:
        d = st.split(":")
        d = d[1].replace('\n', '').strip()

    # купюрность todo проверка количества диспенсеров

    if 'Купюрность' in st:
        cup1_nom, cup1_val = cupurnosty(i+1)
        # print(cup1_nom + ' и ' + cup1_val)

        cup2_nom, cup2_val = cupurnosty(i + 2)
        # print(cup2_nom + ' и ' + cup2_val)

        cup3_nom, cup3_val = cupurnosty(i + 3)
        # print(cup3_nom + ' и ' + cup3_val)

        cup4_nom, cup4_val = cupurnosty(i + 4)
        # print(cup4_nom + ' и ' + cup4_val)

    if 'Отделение Банка, на бранче которого необходимо открыть' in st:
        bran = st.split(":")
        bran = bran[1].replace('\n', '').strip()
        print(bran)

    if 'Счет обслуживания ПТС' in st:
        schet_obsl = array[i+1].replace('\n', '').strip()
        print(schet_obsl)

    if 'Счета дебиторской задолженности ПТС' in st:
        schet_deb_zadolsh = array[i+1].replace('\n', '').strip()
        print(schet_deb_zadolsh)

    if 'Корр.счет подкрепления ПТС' in st:
        schet_kor_podkr = array[i+1].replace('\n', '').strip()
        print(schet_kor_podkr)

    if 'Корр.счет инкассации ПТС' in st:
        schet_inkas = array[i+1].replace('\n', '').strip()

    if 'Счет излишков ПТС' in st:
        schet_izlish = array[i+1].replace('\n', '').strip()

    if 'Счет подкрепления ПТС' in st:
        schet_deb_zad_usd = array[i+1].replace('\n', '').strip()



    if 'Счета обслуживания Cash In' in st:
        for item in range(1, 4):
            sch = array[i + item].replace('\n', '').strip()
            if sch[6] == "1":
                schet_obs_rur_cn = sch
                print('schet_obsl_cashin_rus:' + schet_obs_rur_cn +'\n')

            if sch[6] == "4":
                schet_obs_usd_cn = sch
                print('schet_obsl_cashin_usd:' + schet_obs_usd_cn +'\n')

            if sch[6] == "7":
                schet_obs_eur_cn = sch
                print('schet_obsl_cashin_rus:' + schet_obs_eur_cn +'\n')

adr_old = ('г. ' + g + ', ул. ' + s + ', д.' + d + '.')
print(adr_old)
adr = input('исправить: ')
if not adr:
    adr = adr_old
print(adr)

# поиск отделения todo  а если отеделний много?
for line in kniga:
    if bran.lower() in line.lower():
        branch = line.split(';')
        branch = branch[1].replace('\n', '').strip()
        print(branch)


my_file = open(b + ".mac", 'w')

my_file.write("Description = Регистрация банкомата " + b + '\n')
my_file.write("[wait app]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write('"yjp' + '\n')
my_file.write("[enter]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("wait 10 sec until FieldAttribute 0008 at (3,28)" + '\n')
my_file.write("wait 10 sec until cursor at (3,29)" + '\n')
my_file.write("[wait app]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write('"' + b + '\n')
my_file.write("[enter]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("wait 10 sec until FieldAttribute 0008 at (5,28)"+ '\n')
my_file.write("wait 10 sec until cursor at (5,29)"+ '\n')
my_file.write("[wait app]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write('"Банкомат ' + b + '\n')
my_file.write("[home]" + '\n')
my_file.write("[down]" + '\n')
my_file.write('"' + branch + "0" + '\n')
my_file.write('"' + adr + '\n')
my_file.write("[enter]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("wait 10 sec until FieldAttribute 0008 at (5,28)" + '\n')
my_file.write("wait 10 sec until cursor at (5,29)" + '\n')
my_file.write("[wait app]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("[down]" + '\n')
my_file.write("[down]" + '\n')
my_file.write("[down]" + '\n')
my_file.write("[down]" + '\n')
my_file.write("[down]" + '\n')


for i in range(0, 6-len(str(cup1_nom)), 1):
    my_file.write("[Right]" + '\n')
my_file.write('"' + cup1_nom + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write('"' + cup1_val+ '\n')


for i in range(0, 6-len(str(cup2_nom)), 1):
    my_file.write("[Right]" + '\n')
my_file.write('"' + cup2_nom + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write('"' + cup2_val+ '\n')


for i in range(0, 6-len(str(cup3_nom)), 1):
    my_file.write("[Right]" + '\n')
my_file.write('"' + cup3_nom + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write('"' + cup3_val+ '\n')


for i in range(0, 6-len(str(cup4_nom)), 1):
    my_file.write("[Right]" + '\n')
my_file.write('"' + cup4_nom + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write('"' + cup4_val+ '\n')




my_file.write("[pf5]" + '\n')
'''
my_file.write("[wait inp inh]" + '\n')
my_file.write("wait 10 sec until FieldAttribute 0000 at (16,28)" + '\n')
my_file.write("wait 10 sec until cursor at (16,29)" + '\n')
my_file.write("[wait app]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("[end field]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')
my_file.write("[Right]" + '\n')

'''
my_file.write('"USD' + '\n')
my_file.write("[enter]" + '\n')
my_file.write("[pf3]" + '\n')
my_file.write("[wait app]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write('"Y8Z' + '\n')
my_file.write("[enter]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("wait 4 sec until FieldAttribute 0008 at (3,28)" + '\n')
my_file.write("wait 4 sec until cursor at (3,29)" + '\n')
my_file.write("[wait app]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write('"' + b + '\n')
my_file.write("[enter]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("wait 4 sec until FieldAttribute 0020 at (7,70)" + '\n')
my_file.write("[wait app]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("[pf6]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("wait 4 sec until FieldAttribute 0008 at (3,28)" + '\n')
my_file.write("[wait app]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("[enter]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("wait 4 sec until FieldAttribute 0008 at (7,28)" + '\n')
my_file.write("wait 4 sec until cursor at (7,29)" + '\n')
my_file.write("[wait app]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write('"RUR' + '\n')
my_file.write("[enter]" + '\n')
my_file.write("[wait inp inh]" + '\n')
my_file.write("wait 5 sec until FieldAttribute 0008 at (9,28)" + '\n')
my_file.write("wait 5 sec until cursor at (9,29)" + '\n')
my_file.write("[wait app]" + '\n')
my_file.write("[wait inp inh]" + '\n')


if schet_obsl != '':
    my_file.write('"' + schet_obsl + '\n')
else:
    my_file.write("[down]" + '\n')

if schet_deb_zadolsh != '':
    my_file.write('"' + schet_deb_zadolsh + '\n')
else:
    my_file.write("[down]" + '\n')

if schet_kor_podkr != '':
    my_file.write('"' + schet_kor_podkr + '\n')
else:
    my_file.write("[down]" + '\n')


if schet_inkas != '':
    my_file.write('"' + schet_inkas + '\n')
else:
    my_file.write("[down]" + '\n')

if schet_izlish != '':
    my_file.write('"' + schet_izlish + '\n')
else:
    my_file.write("[down]" + '\n')





if schet_deb_zad_usd != '':
    if_schet_deb_zad('USD', schet_obs_usd, schet_deb_zad_usd, schet_kor_podkrep_usd, schet_inkas_usd, schet_izlish_usd)


if schet_deb_zad_eur != '':
    if_schet_deb_zad('EUR', schet_obs_eur, schet_deb_zad_eur, schet_kor_podkrep_eur, schet_inkas_eur, schet_izlish_eur)



my_file.write("[enter]" + '\n')



if schet_obs_rur_cn != '':
    my_file2 = open(b + "CN.mac", 'w')
    my_file2.write("Description = Добавление счетов " + b + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write('"yjp' + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (3,28)" + '\n')
    my_file2.write("wait 10 sec until cursor at (3,29)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write('"' + b + "CN" + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (5,28)" + '\n')
    my_file2.write("wait 10 sec until cursor at (5,29)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write('"Cash-in' + b + '\n')
    my_file2.write("[home]" + '\n')
    my_file2.write("[down]" + '\n')
    my_file2.write('"' + branch + "1" + '\n')
    my_file2.write('"' + adr + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (5,28)" + '\n')
    my_file2.write("wait 10 sec until cursor at (5,29)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("[pf5]" + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[pf3]" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write('"Y8Z' + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (3,28)" + '\n')
    my_file2.write("wait 10 sec until cursor at (3,29)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write('"' + branch + b + "CN" + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait  10 sec until FieldAttribute 0020 at (7,70)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[pf6]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (3,28)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (7,28)" + '\n')
    my_file2.write("wait 10 sec until cursor at (7,29)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write('"RUR' + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (9,28)" + '\n')
    my_file2.write("wait 10 sec until cursor at (9,29)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write('"' + schet_obs_rur_cn + '\n')
    if schet_inkas_rur_cn != "" or schet_izlish_rur_cn != "":
        my_file2.write("[down]" + '\n')
        my_file2.write("[down]" + '\n')
        if schet_inkas_rur_cn != "":
            my_file2.write('"' + schet_inkas_rur_cn + '\n')
        else:
            my_file2.write("[down]" + '\n')

        if schet_izlish_rur_cn != "":
            my_file2.write('"' + schet_izlish_rur_cn + '\n')
        my_file2.write( "[enter]" + '\n')
    my_file2.write("[pf6]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (3,28)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (7,28)" + '\n')
    my_file2.write("wait 10 sec until cursor at (7,29)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write('"USD' + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (9,28)" + '\n')
    my_file2.write("wait 10 sec until cursor at (9,29)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write('"' + schet_obs_usd_cn + '\n')
    if schet_inkas_usd_cn != "" or schet_izlish_usd_cn !="":
        my_file2.write("[down]" + '\n')
        my_file2.write("[down]" + '\n')
        if schet_inkas_usd_cn != "":
            my_file2.write('"' + schet_inkas_usd_cn + '\n')
        else:
            my_file2.write( "[down]" + '\n')
        if schet_izlish_usd_cn != "":
            my_file2.write('"' + schet_izlish_usd_cn + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[pf6]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (3,28)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (7,28)" + '\n')
    my_file2.write("wait 10 sec until cursor at (7,29)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write('"EUR' + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write("wait 10 sec until FieldAttribute 0008 at (9,28)" + '\n')
    my_file2.write("wait 10 sec until cursor at (9,29)" + '\n')
    my_file2.write("[wait app]" + '\n')
    my_file2.write("[wait inp inh]" + '\n')
    my_file2.write('"' + schet_obs_eur_cn + '\n')
    if schet_inkas_eur_cn != "" or schet_izlish_eur_cn != "":
        my_file2.write("[down]" + '\n')
        my_file2.write("[down]" + '\n')
        if schet_inkas_rur_cn != "":
            my_file2.write('"' + schet_inkas_eur_cn + '\n')
        else:
            my_file2.write("[down]" + '\n')

        if schet_izlish_eur_cn != "":
            my_file2.write('"' + schet_izlish_eur_cn + '\n')
    my_file2.write("[enter]" + '\n')
    my_file2.close()

my_file.close()

print("ok")
