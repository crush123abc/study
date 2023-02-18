import faker
fk=faker.Faker(locale='zh-CN')
name=fk.name()
address=fk.address
print(name)
print(address)