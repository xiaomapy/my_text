import time
from django.shortcuts import render,redirect,HttpResponse
from BookManageSystem import models
# Create your views here.


#展示书单
def book_list(request):
    books = models.Book.objects.all().order_by('id')
    return render(request, 'book_list.html', {'book_list': books})

#添加新书
def add_book(request):
    error_msg=''
    if request.method == 'POST':
        now_book = request.POST.get('new_book', None)
        if now_book:
            models.Book.objects.create(name=now_book)
            return redirect('/book_list/')
        else:
            error_msg = '书名不能为空'
    return render(request, 'add_book.html', {'error': error_msg})

#删除书籍
def del_book(request):
    #获取当前request参数的id
    del_id = request.GET.get('id', None)
    if del_id:
        del_obj = models.Book.objects.get(id=del_id)
        del_obj.delete()
        return redirect('/book_list/')
    else:
        return HttpResponse('删除的数据不存在')

#编辑书籍
def eid_book(request):
    if request.method == 'POST':
        eid_id = request.POST.get('id')
        new_name = request.POST.get('book_name')
        eid_obj = models.Book.objects.get(id=eid_id)
        eid_obj.name = new_name
        eid_obj.save()
        return redirect('/book_list/')
    eid_id = request.GET.get('id')
    if eid_id:
        book_obj = models.Book.objects.get(id=eid_id)
        return render(request, 'eid_book.html', {'new_id': book_obj})
    else:
        return HttpResponse('编辑的书籍不存在')


#当前时间
def timer(request):
    ctime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    # return HttpResponse(ctime)
    return render(request, 'timer.html', {'now_time': ctime})


def publisher_list(request):
    def __str__():
        return request
    return render(request, 'publisher_list.html')
