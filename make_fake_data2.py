from faker.factory import Factory

Faker = Factory.create
fake = Faker()
fake.seed(0)
fake = Faker("ja_JP")

use_columns = ["{{name}}", "{{zipcode}}", "{{address}}", "{{phone_number}}"]
rec_count = 10


def make_data(use_columns, rec_count):
    print(use_columns)
    print(rec_count)

    return fake.csv(
        header=None, data_columns=use_columns, num_rows=rec_count, include_row_ids=False
    )


use_columns = ["{{name}}"]
print(make_data(use_columns, 10))

print(make_data(["{{address}}"], 1))

# result = lambda use_colums, rec_count: fake.csv(
#     header=None, data_columns=use_columns, num_rows=rec_count, include_row_ids=False
# )
# print(result)
