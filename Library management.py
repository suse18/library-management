class library:
    def __init__(self,books):
        self.books=books

    def list_books(self):
        print("available books")
        for book in self.books:
            print(book)

    def borrow_book(self,borrow_book):        
        if borrow_book in self.books:
            print("get your book")
            self.books.remove(borrow_book)
        else:
            print("book not available")

    def return_book(self,return_book):
        print("you have returned the book")
        self.books.append(return_book)

books=['c','c++','java','python']
o=library(books)

msg="""
    1.Display book
    2.Barrow book
    3.Return book
    """

while True:
    print(msg)
    ch=int(input("enter your choice:"))
    if ch==1:
           o.list_books()
    elif ch==2:
        book=input("enter book name to borrow:")
        o.borrow_book(book)
    elif ch==3:
        book=input("enter book name to return:")
        o.return_book(book)
    else:
        print("Thank You Come Again")
        quit()
