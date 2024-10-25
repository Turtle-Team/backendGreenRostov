

import database.patrol
import random
from database import Database
from database.user import User

def create_patrol():
    patrol = database.patrol.Patrol()
    patrol.headers = 'Задача патруля: Ростов-на-Дону'

    latitude = random.uniform(47.266681, 47.243828)
    longitude = random.uniform(39.580366, 39.849199)

    patrol.x_pos = latitude
    patrol.y_pos = longitude
    patrol.radius = 5

    session = Database().get_marker()
    db_user = session.query(User).order_by(User.id).first()
    patrol.user_id = db_user.id

    session = Database().get_marker()
    session.add(patrol)
    session.commit()

