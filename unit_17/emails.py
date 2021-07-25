def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + "." + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + "." + i[0][0:letter] + '@company.io')
    return emails


def fill_emails():
    list_of_names_gen = []
    list2 = []
    file = open("file_sample.txt", 'r+')
    for line in file:
        list1 = line.split(',')
        list2.append(list1[1][1:])
        list2.append(list1[2][1:])
        list_of_names_gen.append(list2)
        list2 = []
    emails_raw = email_gen(list_of_names_gen)
    file.seek(0)
    j = 0
    list_of_lines = file.readlines()
    for line in list_of_lines:
        if list_of_lines[j].split(',')[0] == '':
            list_of_lines[j] = emails_raw[j] + list_of_lines[j]
        j += 1
    file.close()
    file = open("file_sample.txt", 'w+')
    file.writelines(list_of_lines)
    file.close()
