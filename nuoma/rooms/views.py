from django.shortcuts import render, get_object_or_404
from rooms.models import Room, Category, RoomImage


def room_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    rooms = Room.objects.filter(visible=True)
    imag = RoomImage.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        rooms = Room.objects.filter(category=category,  visible=True)

        imag = RoomImage.objects.filter(room_id=3)
    return render(request,
                  'hotel/rooms/list.html',
                  {'category': category,
                   'categories': categories,
                   'rooms': rooms,
                   'imag': imag})


def room_detail(request, id, slug):

    room = get_object_or_404(Room,
                             id=id,
                             slug=slug,
                             visible=True)
    r_id = room.id
    images = RoomImage.objects.filter(room_id=r_id)
    prop = room.properties1.all()

    return render(request,
                  'hotel/rooms/detail.html',
                  {'room': room,
                   'images': images,
                   'prop': prop})





