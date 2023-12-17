from faker import Faker
import random

fake = Faker()

def generate_random_news():
    sources = ["CNN", "BBC", "Reuters", "NY Times", "Delfi", "WordPress"]
    categories = ["World", "Technology", "Sports", "Entertainment", "Science", "Games", "IT", "USA"]

    source = random.choice(sources)
    category = random.choice(categories)
    headline = fake.catch_phrase()
    content = fake.paragraph()

    news = f"{source} - {category}\n{headline}\n{content}\n"

    return news
