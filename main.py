from flask import Flask

import datetime as dt
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")

    captain = User(surname="Scott", name="Ridley", age=21, position="captain", speciality="research engineer",
                   address="module_1", email="scott_chief@mars.org")
    helper = User(surname="Brown", name="Frank", age=32, position="captain's helper", speciality="navigator",
                  address="module_1", email="frank_helper@mars.org")
    mechanic = User(surname="Lancaster", name="Alex", age=40, position="mechanic", speciality="space welder",
                    address="module_4", email="super_mechanic@mars.org")
    explorer = User(surname="Lambert", name="John", age=26, position="mars explorer", speciality="soil researcher",
                    address="module_7", email="explorer_lambert@mars.org")

    db_sess = db_session.create_session()

    db_sess.add(captain)
    db_sess.add(helper)
    db_sess.add(mechanic)
    db_sess.add(explorer)
    db_sess.commit()

    job = Jobs(team_leader=1, job="deployment of residential modules 1 and 2", work_size=15, collaborators="2, 3",
               start_date=dt.datetime.now(), is_finished=False)

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
