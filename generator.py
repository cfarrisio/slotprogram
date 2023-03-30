from faker import Faker
import random

fake = Faker()

# Define the headers
headers = ['Reservation ID', 'Customer Name', 'Check-In Date',
           'Check-Out Date', 'Reservation_Source', 'Number of Guests', 'Room Type']

# Generate 100 random reservations
reservations = []
for i in range(100):
    reservation_id = fake.random_number(digits=10)
    customer_name = fake.name()
    checkin_date = fake.date_between(start_date='-1y', end_date='today')
    checkout_date = fake.date_between(start_date=checkin_date, end_date='+1y')
    reservation_sources = random.choice(
        ['Direct', 'Phone', 'Email', 'Walk-In', 'OTA'])
    num_guests = random.randint(1, 3)
    room_type = random.choice(
        ['Corner Suite', 'Riverfront Suite w/ Kitchen K', 'Riverfront Suite w/ Kitchen QQ'])

    reservations.append([reservation_id, customer_name,
                        checkin_date.strftime('%Y-%m-%d'), checkout_date.strftime('%Y-%m-%d'), num_guests, room_type])

# Write the reservations to an HTML table
with open('reservations.html', 'w') as f:
    f.write('<table>\n')

    # Write the headers
    f.write('\t<tr>\n')
    for header in headers:
        f.write(f'\t\t<th>{header}</th>\n')
    f.write('\t</tr>\n')

    # Write the data
    for reservation in reservations:
        f.write('\t<tr>\n')
        for field in reservation:
            f.write(f'\t\t<td>{field}</td>\n')
        f.write('\t</tr>\n')

    f.write('</table>')

print('Done!')
