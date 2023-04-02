from sqlalchemy import func, desc, select, and_

from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session



def select_1():

    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2():
    discipline_id = input('discipline_id:')
    result = session.query(Discipline.name,
                      Student.fullname,
                      func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Student.id, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .limit(1).all()
    return result


def select_3():
    discipline_id = input('discipline_id:')
    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Discipline).join(Student).join(Group)\
        .filter(Discipline.id == discipline_id).group_by(Group.name).all()
    return result


def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).select_from(Grade).all()
    return result


def select_5():
    teacher_id = input('teacher_id:')
    result = session.query(Discipline.name).select_from(Discipline).join(Teacher).filter(Teacher.id == teacher_id).all()
    return result


def select_6():
    group_id = input('group_id:')
    result = session.query(Student.fullname).select_from(Student).join(Group).filter(Group.id == group_id).all()
    return result


def select_7():
    group_id = input('group_id:')
    discipline_id = input('discipline_id:')
    result = session.query(Student.fullname, Grade.grade)\
        .select_from(Grade).join(Discipline).join(Student).join(Group)\
        .filter(and_(Group.id == group_id, Discipline.id == discipline_id))\
        .group_by(Student.fullname, Grade.grade)\
        .order_by(Student.fullname).all()
    return result


def select_8():
    teacher_id = input('teacher_id:')
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Discipline).join(Teacher)\
        .filter(Teacher.id == teacher_id).all()
    return result


def select_9():
    student_id = input('student_id:')
    result = session.query(Discipline.name)\
        .select_from(Grade).join(Discipline).join(Student)\
        .filter(Student.id == student_id).group_by(Discipline.name).all()
    return result


def select_10():
    student_id = input('student_id:')
    teacher_id = input('teacher_id:')
    result = session.query(Discipline.name)\
        .select_from(Grade).join(Discipline).join(Teacher).join(Student)\
        .filter(and_(Student.id == student_id, Teacher.id == teacher_id))\
        .group_by(Discipline.name).all()
    return result



queries = {
    '1': select_1,
    '2': select_2,
    '3': select_3,
    '4': select_4,
    '5': select_5,
    '6': select_6,
    '7': select_7,
    '8': select_8,
    '9': select_9,
    '10': select_10
}


def options():
    print('''
    1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    2. Знайти студента із найвищим середнім балом з певного предмета.
    3. Знайти середній бал у групах з певного предмета.
    4. Знайти середній бал на потоці (по всій таблиці оцінок).
    5. Знайти які курси читає певний викладач.
    6. Знайти список студентів у певній групі.
    7. Знайти оцінки студентів у окремій групі з певного предмета.
    8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
    9. Знайти список курсів, які відвідує студент.
    10. Список курсів, які певному студенту читає певний викладач.
    ''')


def main():
    while True:
        command = input("enter query's number or one of commands - options / exit\n >>>  ")
        if command in queries or 'exit' or 'options':
            if command == 'exit':
                exit()
            if command == 'options':
                options()
                continue
            print(queries[command]())



if __name__ == '__main__':
    main()