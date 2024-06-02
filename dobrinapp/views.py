from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Gallery, Media, News, Orders
from itertools import zip_longest
from django_user_agents.utils import get_user_agent
from .email_sender import send_mail


# Create your views here.
def index(request):
    context = create_context(request)
    return render(request, 'index.html', context)


def shopping_cart(request):
    pictures_obj = list()
    pictures_id = None #request.session.get('pictures_id')
    if request.method == 'POST' and 'submit_order' in request.POST and pictures_id is not None:
        # отправка письма на почту
        # Order info
        pictures_info = "Название требуемых картин: "
        for i in pictures_id:
            picture_info = Gallery.objects.get(id=i).name
            pictures_info += f'{picture_info}, '
            print("pictures_info: ", pictures_info)
        # Contacts
        print(request.POST['FIO'])
        print(request.POST['phone'])
        print(request.POST['email'])
        contacts = f"ФИО: {request.POST['FIO']}\nТелефон: {request.POST['phone']}\nEmail: {request.POST['email']}"
        # Comment
        comment = "Комментарий: " + request.POST['order_comment']
        order = Orders()
        order.FIO = request.POST['FIO']
        order.phone = request.POST['phone']
        order.email = request.POST['email']
        order.comment = comment
        order.save()
        last_order_id = Orders.objects.last().id
        print("last_order_id: ", last_order_id)
        send_mail(last_order_id, pictures_info, contacts, comment)

        print("shopping_cart=", pictures_id)
    if request.method == 'POST' and 'del_picture' in request.POST and pictures_id is not None:
        pictures_id = request.session.get('pictures_id')
        print(pictures_id)
        if request.POST['picture_id'] in pictures_id:
            pictures_id.remove(request.POST['picture_id'])
            print(pictures_id)
        request.session['pictures_id'] = pictures_id
        print("del picture ", request.POST['picture_id'])

    context = create_context(request)
    if pictures_id is not None:
        for id in pictures_id:
            pictures_obj.append(Gallery.objects.filter(id=id))
        context['shopping_cart'] = pictures_obj
    print(context)
    return render(request, 'shopping_cart.html', context)


def gal(request):
    gallery = Gallery.objects.filter(instock=1)
    genre = '0'
    instock = '1'
    if request.method == 'POST' and 'filter-apply' in request.POST:
        genre = request.POST['genre']
        instock = request.POST['instock']
        print("success POST!")
        print('genre:', genre)
        print('instock:', instock)
        if genre == '0':
            gallery = Gallery.objects.filter(instock=instock)
        else:
            gallery = Gallery.objects.filter(genres=genre, instock=instock)

    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        num_columns = 1
        pass
    elif user_agent.is_tablet:
        num_columns = 2
        pass
    elif user_agent.is_pc:
        num_columns = 4
        pass
    num_images = len(gallery)
    print('count of pict ', num_images)
    num_images_per_column = (num_images + num_columns - 1) // num_columns
    columns = list(zip_longest(*[iter(gallery)] * num_images_per_column, fillvalue=None))
    context = create_context(request)
    context['instock'] = instock
    context['genre'] = genre
    context['gallery'] = gallery
    context['columns'] = columns
    print('render...')
    return render(request, 'gal.html', context)


def picture(request):
    session_data = list()
    picture_id = request.GET.get('id')
    if request.method == 'POST' and 'in_cart' in request.POST:
        session_data = request.session.get('pictures_id')
        if session_data is not None and not (picture_id in session_data):
            session_data.append(picture_id)
        print("pictres_id= ", session_data)
        request.session['pictures_id'] = session_data
        print("picture")
    context = create_context(request)
    context['picture'] = Gallery.objects.get(id=picture_id)
    return render(request, 'picture.html', context)


def nov(request):
    news = News.objects.all()
    context = create_context(request)
    return render(request, 'nov.html', context)


def bio(request):
    context = create_context(request)
    return render(request, 'bio.html', context)


def vid(request):
    media = Media.objects.all()
    context = create_context(request)
    return render(request, 'vid.html', context)


def nov_page(request):
    nov_id = request.GET.get('id')
    context = create_context(request)
    return render(request, 'nov_page.html', context)


# установка куки
def set_cookie(request, picture_id: int):
    # получаем из строки запроса имя пользователя
    pictures = list()
    pictures = get_cookie(request)
    response = HttpResponse(f"Hello {pictures}")
    pictures.append(picture_id)
    # передаем его в куки
    response.set_cookie("picture_id", picture_id)
    print("set_cookie " + picture_id)
    return response


# получение куки
def get_cookie(request):
    # получаем куки с ключом picture
    picture_id = list()
    try:
        picture_id = request.COOKIES["picture_id"]
        print("get_cookie" + type(picture_id))
    except:
        print("Error: cookie is empty")
    return picture_id


# удаление куки
def delete_cookie(request):
    picture = HttpResponse()
    picture.delete_cookie()
    return picture


def create_context(request):
    shopping_cart = request.session.get('pictures_id')
    shopping_cart_length = len(shopping_cart) if shopping_cart else 0
    context = {
        'nav_pict1': Gallery.objects.order_by('?').first(),
        'nav_pict2': Gallery.objects.order_by('?').first(),
        'nav_pict3': Gallery.objects.order_by('?').first(),
        'nav_pict4': Gallery.objects.order_by('?').first(),
        'shopping_cart': shopping_cart,
        'shopping_cart_length': shopping_cart_length
    }
    return context
