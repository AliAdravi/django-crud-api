from faker import Faker
import random
from .models import Author, Publisher, Book, Store

fake = Faker()
def create_bookstore(n) -> None:
    try:
    #     for _ in range(0, 21):
    #         # Auther
    #         aname = fake.name()
    #         aage = random.randint(20, 60)
    #         Author.objects.create(
    #             name = aname,
    #             age = aage
    #         )

    #         # publisher
    #         pname = fake.name()
    #         Publisher.objects.create(
    #             name = pname
    #         )
    
    # except Exception as e:
    #     print(e)

        for _ in range(0, n):
            #Book
            # times = random.randint(1, 5)
            # auther_obj = Author.objects.order_by('?')[0:times]
            # pub_obj = Publisher.objects.order_by('?').first()
            # bname = fake.name()
            # bpages = random.randint(70, 500)
            # bprice = round(random.uniform(10.00, 250.50), 2)
            # brating = random.randint(1, 5)
            # bpubdate = fake.date()
            # book_obj = Book.objects.create(
            #     name = bname,
            #     pages = bpages,
            #     price = bprice,
            #     rating = brating,
            #     publisher = pub_obj,
            #     pubdate = bpubdate
            # )
            # book_obj.authors.set(auther_obj)

            # Store
            sname = fake.name()
            times = random.randint(5, 60)
            books_obj = Book.objects.order_by('?')[0:times]
            store_obj = Store.objects.create(
                name = sname
            )
            store_obj.books.set([books_obj])

    except Exception as e:
        print(e)
