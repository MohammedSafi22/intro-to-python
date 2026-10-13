age = 20

# أكبر أو تساوي 18 فإنه سيتم تنفيذ الأمر الموجود فيها age هذا الشرط يعني أنه إذا كانت قيمة
if age >= 18:
    print('You are allowed.')
########################################################################
is_logged = True

# فإنه سيتم تنفيذ الأمر الموجود فيها true تساوي isLogged هذا الشرط يعني أنه إذا كانت قيمة
if is_logged:
    print('You can save your progress.')

# إذا لم يتم تنفيذ الجملة الشرطية السابقة فإنه سيتم تنفيذ أمر الطباعة الموجود هنا
else:
    print('You need to log in to save your progress.')

########################################################################

role = 'author'

# فإنه سيتم تنفيذ أمر الطباعة الموجود هنا 'admin' تساوي role إذا كانت قيمة
if role == 'admin':
    print('You logged in as an admin.')
    
# فإنه سيتم تنفيذ أمر الطباعة الموجود هنا 'editor' تساوي role إذا كانت قيمة
elif role == 'editor':
    print('You logged in as an editor.')

# فإنه سيتم تنفيذ أمر الطباعة الموجود هنا 'author' تساوي role إذا كانت قيمة
elif role == 'author':
    print('You logged in as an author.')

# فإنه سيتم تنفيذ أمر الطباعة الموجود هنا 'contributer' تساوي role إذا كانت قيمة
elif role == 'contributer':
    print('You logged in as a contributer.')

# إذا لم يتم تنفيذ الجملة الشرطية السابقة فإنه سيتم تنفيذ أمر الطباعة الموجود هنا
else:
    print('You logged in as a subscriber.')    

################################################################ Class
# Comparator هنا قمنا بتعريف كلاس إسمه
class Comparator:

    # بعدها تطبع القيمة الأكبر بينهما .b و a هنا قمنا بتعريف دالة تأخذ قيمتين عند إستدعائها و تخزنهما في الباراميترين
    def print_max(self, a, b):
        if a > b:
            print(a, 'is bigger')
        elif a < b:
            print(b, 'is bigger')
        else:
            print('They are equal')


# comparator إسمه Comparator هنا قمنا بإنشاء كائن من الكلاس
comparator = Comparator()

# و تمرير قيمتين لها حتى تطبع قيمة العدد الأكبر بينهما print_max() هنا قمنا باستدعاء الدالة
comparator.print_max(2, 6)