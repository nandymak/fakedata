import pandas as pd
from faker.factory import Factory
from stop_watch import stop_watch  # 実行時間測定

# import json  # To create a json file
from random import randint  # For id

Faker = Factory.create
fake = Faker()
fake.seed(20000)  # 設定することで結果が固定される。
fake = Faker("ja_JP")


@stop_watch
def make_data(use_columns, row_count):

    return fake.csv(
        header=None, data_columns=use_columns, num_rows=row_count, include_row_ids=False
    )


def input_data(x):

    test_data = {}
    for i in range(0, x):
        test_data[i] = {}
        test_data[i]["id"] = randint(1, 100)
        test_data[i]["name"] = fake.name()
        test_data[i]["zipcode"] = fake.zipcode()
        test_data[i]["address"] = fake.address()
        test_data[i]["phone_number"] = fake.phone_number()
    return pd.DataFrame(test_data).T  # 転置して返却する


def main():
    # Enter number of records
    number_of_records = 10  # For the above task make this 100
    use_columns = ["{{name}}", "{{zipcode}}", "{{address}}", "{{phone_number}}"]
    # print(make_data(use_columns, number_of_records))
    df = input_data(number_of_records)

    print(df.head(10))
    print(df.dtypes)
    print(df["address"])
    s = pd.Series(df["id"], dtype="uint8")
    print(s.head(10))
    print(s.dtypes)


main()
# The folder or location where this python code
# is save there a students.json will be created
# having 10 students data.
