from faker.factory import Factory

Faker = Factory.create
fake = Faker()
fake.seed(0)
fake = Faker("ja_JP")

print(
    fake.csv(
        header=None,
        data_columns=(
            "{{name}}",
            "{{first_kana_name}}",
            "{{last_kana_name}}",
            "{{zipcode}}",
            "{{city_suffix}}",
            "{{address}}",
            "{{phone_number}}",
        ),
        num_rows=10,
        include_row_ids=False,
    )
)

