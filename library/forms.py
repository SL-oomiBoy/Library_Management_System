
from django import forms
from .models import Book, Member, BorrowRecord

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'available']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone']

class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['book', 'member', 'borrow_date', 'return_date']
