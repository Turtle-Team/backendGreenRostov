from sqlalchemy.orm import Session

import database.events
import faker
import random
import base64

with open('fake/Terminator-obzor_1572430502 — копия.jpg', 'rb') as f:
    data = base64.b64encode(f.read()).decode()

for _ in range(10):
    fake = faker.Faker()

    latitude = random.uniform(47.266681, 47.243828)
    longitude = random.uniform(39.580366, 39.849199)

    new_event = database.events.Event()
    new_event.name = fake.sentence()
    new_event.description = fake.sentence()
    new_event.latitude = latitude
    new_event.longitude = longitude
    new_event.picture = data

    db: Session = database.Database().get_marker()
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
