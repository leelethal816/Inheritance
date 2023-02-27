import PersonClass as pc

name = "Lee Zhang"
address = "1624 S 5th St APT 109 Waco, TX 76706"
phone = "254-640-0515"
cn = "234"
mailing = False
customer1 = pc.Customer(name, address, phone, cn, mailing)

customer1.print_person()
