import csv


#with open(r'resources\user_password_recovery_code.csv') as f:
with open(r'D:\Prog\Python\Project\guqa_dz_04_selene\resources\username-password-recovery-code.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#f = csv.DictReader('resourse/user_password_recovery_code.csv', 'r')
#print()

