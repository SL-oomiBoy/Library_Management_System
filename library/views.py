from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from .models import Book, Member, BorrowRecord
from .forms import BookForm, MemberForm, BorrowRecordForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'library/home.html')

# Book views
@login_required
def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            models.Q(title__icontains=query) | models.Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})

@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/book_confirm_delete.html', {'book': book})

# Member views
@login_required
def member_list(request):
    members = Member.objects.all()
    return render(request, 'library/member_list.html', {'members': members})

@login_required
def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'library/member_detail.html', {'member': member})

@login_required
def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'library/member_form.html', {'form': form})

@login_required
def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'library/member_form.html', {'form': form})

@login_required
def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'library/member_confirm_delete.html', {'member': member})

# BorrowRecord views
@login_required
def borrow_record_list(request):
    borrow_records = BorrowRecord.objects.all()
    return render(request, 'library/borrow_record_list.html', {'borrow_records': borrow_records})

@login_required
def borrow_record_detail(request, pk):
    borrow_record = get_object_or_404(BorrowRecord, pk=pk)
    return render(request, 'library/borrow_record_detail.html', {'borrow_record': borrow_record})

@login_required
def borrow_record_create(request):
    if request.method == 'POST':
        form = BorrowRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrow_record_list')
    else:
        form = BorrowRecordForm()
    return render(request, 'library/borrow_form.html', {'form': form})

@login_required
def borrow_record_update(request, pk):
    borrow_record = get_object_or_404(BorrowRecord, pk=pk)
    if request.method == 'POST':
        form = BorrowRecordForm(request.POST, instance=borrow_record)
        if form.is_valid():
            form.save()
            return redirect('borrow_record_list')
    else:
        form = BorrowRecordForm(instance=borrow_record)
    return render(request, 'library/borrow_record_form.html', {'form': form})

@login_required
def borrow_record_delete(request, pk):
    borrow_record = get_object_or_404(BorrowRecord, pk=pk)
    if request.method == 'POST':
        borrow_record.delete()
        return redirect('borrow_record_list')
    return render(request, 'library/borrow_record_confirm_delete.html', {'borrow_record': borrow_record})