from address import Address
from mailing import Mailing

to_address = Address("119049", "Moscow", "Donskaya", "8", "5")
from_address = Address("456200", "Zlatoust", "Sverdlova", "41", "3")
cost = int(200)
track = str("456218547896")

my_mailing = Mailing(to_address, from_address, cost, track)

print(my_mailing)
