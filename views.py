from datetime import date
from django.shortcuts import render
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions


# Use a ContactDetail instance to encapsulate the detail of the contact.
DEMO_CONTACT = ContactDetail(
        first_name='سلطان',
        last_name='10321',
        first_name_reading='المعاملة',
        last_name_reading='تاريخها',
        tel='+41769998877',
        email='رقم القيد',
        URL='تاريخه',
        birthday=date(month=5, day=16, year=1986),
        Nickname='1986-05-08',
        address='مكة',
        memo='نوع الإحداثي',
        org='محكمة مكذا',
    )


# Use a WifiConfig instance to encapsulate the configuration of the connexion.
DEMO_WIFI = WifiConfig(
        ssid='my-wifi',
        authentication=WifiConfig.AUTHENTICATION.WPA,
        password='wifi-password'
    )

DEMO_COORDINATES = Coordinates(latitude=586000.32, longitude=250954.19, altitude=500)

DEMO_OPTIONS = QRCodeOptions(size='t', border=6, error_correction='L')

IMG_LIST = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


def index(request):
    """
    Build the home page of this demo app.

    :param request:
    :return: HTTP response providing the home page of this demo app.
    """

    # Build context for rendering QR codes.
    context = dict(
        contact_detail=DEMO_CONTACT,
        wifi_config=DEMO_WIFI,
        video_id='J9go2nj6b3M',
        google_maps_coordinates=DEMO_COORDINATES,
        geolocation_coordinates=DEMO_COORDINATES,
        options_example=DEMO_OPTIONS,
        img_list=IMG_LIST
    )

    # Render the index page.
    return render(request, 'index.html', context=context)


def start(request):

    return render(request, 'start.html')


def new(request):
    uname = request.POST.get('uname')
    uid = request.POST.get('uid')
    mobile = request.POST.get('mobile')
    file_from = request.POST.get('file_from')
    file_num = request.POST.get('file_num')
    file_date = request.POST.get('file_date')

    n1 = request.POST.get('n1')
    n2 = request.POST.get('n2')
    n3 = request.POST.get('n3')
    n4 = request.POST.get('n4')

    e1 = request.POST.get('e1')
    e2 = request.POST.get('e2')
    e3 = request.POST.get('e3')
    e4 = request.POST.get('e4')

    zone = request.POST.get('zone')

    QR_LIST = {
        "رقم المعاملة": file_num,
        "تاريخ المعاملة": file_date,
        "جهة المعاملة": file_from,

        "اسم مقدم الطلب": uname,
        "السجل المدني": uid,
        "رقم الجوال": mobile,

        "شماليات 1": n1,
        "شماليات 2": n2,
        "شماليات 3": n3,
        "شماليات 4": n4,

        "شرقيات 1": e1,
        "شرقيات 2": e2,
        "شرقيات 3": e3,
        "شرقيات 4": e4,
    }

    context = dict(
        qr_list=QR_LIST,

        file_num=file_num,
        file_date=file_date,
        file_from=file_from,

        uname=uname,
        uid=uid,
        mobile=mobile,


        n1=n1,
        n2=n2,
        n3=n3,
        n4=n4,
        e1=e1,
        e2=e2,
        e3=e3,
        e4=e4,
        zone=zone,
    )

    return render(request, 'new.html', context=context)



