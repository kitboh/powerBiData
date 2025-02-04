import csv
import random
from datetime import datetime, timedelta

rooms = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 301, 302, 303, 304, 305]

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def generate_dates(room_bookings, room):
    while True:
        if random.random() < 0.40:
            preferred_months = [11, 12, 5, 6, 7]
            start_date = random_date(datetime.now() - timedelta(days=365*10), datetime.now())
            while start_date.month not in preferred_months:
                start_date = random_date(datetime.now() - timedelta(days=365*10), datetime.now())
        else:
            start_date = random_date(datetime.now() - timedelta(days=365*10), datetime.now())
        end_date = start_date + timedelta(days=random.randint(1, 14))
        if all(not (start_date <= booking['end_date'] and end_date >= booking['start_date']) for booking in room_bookings[room]):
            return start_date, end_date

room_bookings = {room: [] for room in rooms}
data = []

for _ in range(12156):
    room = random.choice(rooms)
    start_date, end_date = generate_dates(room_bookings, room)
    number_of_nights = (end_date - start_date).days
    if str(room).startswith('1'):
        cost = random.randint(90, 110) * number_of_nights
    elif str(room).startswith('2'):
        cost = random.randint(140, 150) * number_of_nights
    else:
        cost = random.randint(300, 350) * number_of_nights
    is_cancelled = random.random() > 0.942
    if number_of_nights < 4:
        breakfast = random.random() < 0.25
    elif number_of_nights > 7:
        breakfast = random.random() < 0.80
    else:
        breakfast = random.random() < 0.50
    dinner = breakfast if random.random() < 0.80 else not breakfast

    room_bookings[room].append({'start_date': start_date, 'end_date': end_date})
    data.append([room, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), cost, is_cancelled, number_of_nights, breakfast, dinner])

with open('hotel_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Room', 'Start_date', 'End_date', 'Cost', 'Is_cancelled', 'Number_of_nights', 'Breakfast', 'Dinner'])
    writer.writerows(data)
