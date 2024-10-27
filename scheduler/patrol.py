

import database.patrol
import random
from database import Database
from database.user import User

def create_patrol():
    session = Database().get_marker()
    for user in session.query(User).order_by(User.id).all():
        patrol = database.patrol.Patrol()
        patrol.headers = 'Задача патруля: Ростов-на-Дону'

        latitude = random.uniform(47.266681, 47.243828)
        longitude = random.uniform(39.580366, 39.849199)

        patrol.x_pos = latitude
        patrol.y_pos = longitude
        patrol.radius = 5

        patrol.user_id = user.id

        session.add(patrol)
    session.commit()

