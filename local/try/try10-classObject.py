import tank

start_text= tank.start_text()

# Tank1
first_tank= tank.Tank('TANK MK001', 3)
print(start_text)
print(first_tank.name)
print(first_tank.ammo)

first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.fire_ammo()
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.add_ammo(3)
print(first_tank.ammo)


# Tank2
second_tank= tank.Tank('TANK TT338', 6)
print(start_text)
print(second_tank.name)
print(second_tank.ammo)