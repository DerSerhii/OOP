import logging

import models as md


def main():
    recr1 = md.Recruiter('Olga Recrutova', 100, 'olrecrut@gmail.com')
    prog1 = md.Programmer('Roman Programenko', 200, 'romprog@gmail.com',
                          'Python, Git&GitHub, Django, Django Rest Framework, API')
    prog2 = md.Programmer('Boris Koder', 170, 'boris_125@gmail.com',
                          'Python, Git&GitHub, PyQT5, PyGame')
    cand1 = md.Candidate('Ivan Skriptov', 'ivan_sk@gmail.com', 'Javascript, React, Angular',
                         'Self-management, Willingness to learn', 'Junior')
    cand2 = md.Candidate('Igor Pytonsky', 'pytonsky_2000@ukr.net', 'Python, Django, Django REST framework',
                         'Leadership, Critical thinking', 'Junior')
    cand3 = md.Candidate('Oleg Bekendin', 'obl12021999@gmail.com',
                         'Java, Spring Framework', 'Teamwork, Communication', 'Junior')
    vac1 = md.Vacancy('Senior Python Developer', 'Django, Flask, Django REST framework, API', 'Junior')
    vac2 = md.Vacancy('Senior Java Developer', 'Spring Framework, SDK, API', 'Junior')

    # cand3.work()
    print(prog2.info)
    print(md.Candidate.input_candidates('candidates.csv'))


if __name__ == '__main__':
    try:
        main()
    except Exception as exp:
        logging.basicConfig(filename='logs.txt',
                            format=f'\n{"-" * 30}%(levelname)s{"-" * 30}\n%(asctime)s - %(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S',
                            level=logging.ERROR)
        logging.exception('{0}: {1}'.format(exp.__class__.__name__, exp))
        raise
