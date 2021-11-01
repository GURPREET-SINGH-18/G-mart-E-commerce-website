from django.shortcuts import render, redirect
import random
from Home.models import Air_Conditioner, Books, Camera, Fashion, Headphones, Laptop, Mobile, Refrigerator, Tablets, Television, Washing_Machine

# Create your views here.


def listmaker(y):
    Z = []
    for i in range(0, len(y), 5):
        Z.append(y[i:i+5])
    return Z


def index(request):
    m = Mobile.objects.all()
    M = listmaker(m)
    h = Headphones.objects.all()
    H = listmaker(h)
    f = Fashion.objects.all()
    F = listmaker(f)
    l = Laptop.objects.all()
    L = listmaker(l)
    t = Television.objects.all()
    T = listmaker(t)
    w = Washing_Machine.objects.all()
    W = listmaker(w)
    r = Refrigerator.objects.all()
    R = listmaker(r)
    a = Air_Conditioner.objects.all()
    A = listmaker(a)
    x = Tablets.objects.all()
    X = listmaker(x)
    c = Camera.objects.all()
    C = listmaker(c)
    b = Books.objects.all()
    B = listmaker(b)
    return render(request, 'index.html', {"m1": M[0], "m2": M[1:], "h1": H[0], "h2": H[1:], "f1": F[0], "f2": F[1:], "l1": L[0], "l2": L[1:], "t1": T[0], "t2": T[1:], "w1": W[0], "w2": W[1:], "r1": R[0], "r2": R[1:], "a1": A[0], "a2": A[1:], "x1": X[0], "x2": X[1:], "c1": C[0], "c2": C[1:], "b1": B[0], "b2": B[1:]})


def forhighlight(m):
    p = m.values()
    o = []
    for i in range(0, len(p)):
        x = dict(p[i])
        y = x['highlights']
        l = y.split('\n')
        o.append(l)
        print(o)
    return o


def rating(m):
    l = []
    for i in range(0, len(m)):
        r1 = random.randint(10000, 90000)
        l.append(r1)
    return l


def review(m):
    l = []
    for i in range(0, len(m)):
        r1 = random.randint(1000, 10000)
        l.append(r1)
    return l


def offer(m):
    l = []
    for i in range(0, len(m)):
        r1 = random.randint(5, 55)
        l.append(r1)
    return l


def extraprices(m, o):
    l = []
    p = m.values()
    for i in range(0, len(p)):
        x = dict(p[i])
        y = x['price']
        # s = y+(y*o[i])//100
        s = (y*100)//(100-o[i])
        l.append(s)
    return l


def mobile(request):
    m = Mobile.objects.all()
    l = forhighlight(m)
    # print(l)
    r1 = rating(m)
    # print(r1)
    r2 = review(m)
    o = offer(m)
    # print(o)
    ep = extraprices(m, o)
    # print(ep)
    return render(request, 'mobileall.html', {'i': m, 'm1': l, 'r1': r1, 'r2': r2, 'o': o, 'ep': ep})


def laptop(request):
    m = Laptop.objects.all()
    l = forhighlight(m)
    # print(l)
    r1 = rating(m)
    # print(r1)
    r2 = review(m)
    o = offer(m)
    # print(o)
    ep = extraprices(m, o)
    # print(ep)
    return render(request, 'laptopall.html', {'i': m, 'm1': l, 'r1': r1, 'r2': r2, 'o': o, 'ep': ep})


def television(request):
    m = Television.objects.all()
    l = forhighlight(m)
    # print(l)
    r1 = rating(m)
    # print(r1)
    r2 = review(m)
    o = offer(m)
    # print(o)
    ep = extraprices(m, o)
    # print(ep)
    return render(request, 'televisionall.html', {'i': m, 'm1': l, 'r1': r1, 'r2': r2, 'o': o, 'ep': ep})


def headphone(request):
    m = Headphones.objects.all()
    l = forhighlight(m)
    # print(l)
    r1 = rating(m)
    # print(r1)
    r2 = review(m)
    o = offer(m)
    # print(o)
    ep = extraprices(m, o)
    # print(ep)
    return render(request, 'headphoneall.html', {'i': m, 'm1': l, 'r1': r1, 'r2': r2, 'o': o, 'ep': ep})


def washingmachine(request):
    m = Washing_Machine.objects.all()
    l = forhighlight(m)
    # print(l)
    r1 = rating(m)
    # print(r1)
    r2 = review(m)
    o = offer(m)
    # print(o)
    ep = extraprices(m, o)
    # print(ep)
    return render(request, 'washingmachineall.html', {'i': m, 'm1': l, 'r1': r1, 'r2': r2, 'o': o, 'ep': ep})


def tablet(request):
    m = Tablets.objects.all()
    l = forhighlight(m)
    # print(l)
    r1 = rating(m)
    # print(r1)
    r2 = review(m)
    o = offer(m)
    # print(o)
    ep = extraprices(m, o)
    # print(ep)
    return render(request, 'tabletsall.html', {'i': m, 'm1': l, 'r1': r1, 'r2': r2, 'o': o, 'ep': ep})


def refrigerator(request):
    m = Refrigerator.objects.all()
    l = forhighlight(m)
    # print(l)
    r1 = rating(m)
    # print(r1)
    r2 = review(m)
    o = offer(m)
    # print(o)
    ep = extraprices(m, o)
    # print(ep)
    return render(request, 'refriall.html', {'i': m, 'm1': l, 'r1': r1, 'r2': r2, 'o': o, 'ep': ep})


def airconditioner(request):
    m = Air_Conditioner.objects.all()
    l = forhighlight(m)
    # print(l)
    r1 = rating(m)
    # print(r1)
    r2 = review(m)
    o = offer(m)
    # print(o)
    ep = extraprices(m, o)
    # print(ep)
    return render(request, 'acall.html', {'i': m, 'm1': l, 'r1': r1, 'r2': r2, 'o': o, 'ep': ep})


def camera(request):
    m = Camera.objects.all()
    l = forhighlight(m)
    r1 = rating(m)
    r2 = review(m)
    o = offer(m)
    ep = extraprices(m, o)
    return render(request, 'camera.html', {'i': m, 'm1': l, 'r1': r1, 'r2': r2, 'o': o, 'ep': ep})


def fashion(request, tp):
    if tp == "all":
        f = Fashion.objects.all()
        # l = forhighlight(f)
        r1 = rating(f)
        r2 = review(f)
        o = offer(f)
        ep = extraprices(f, o)
        return render(request, 'fashion.html', {'i': f,  'r1': r1, 'r2': r2, 'o': o, 'ep': ep})
    elif tp == "Men":
        f = Fashion.objects.filter(gender=tp)
        # l = forhighlight(f)
        r1 = rating(f)
        r2 = review(f)
        o = offer(f)
        ep = extraprices(f, o)
        t = "Men's"
        return render(request, 'fashion.html', {'i': f,  'r1': r1, 'r2': r2, 'o': o, 'ep': ep, 't': t})
    elif tp == "Women":
        f = Fashion.objects.filter(gender=tp)
        # l = forhighlight(f)
        r1 = rating(f)
        r2 = review(f)
        o = offer(f)
        ep = extraprices(f, o)
        t = "Women's"
        return render(request, 'fashion.html', {'i': f,  'r1': r1, 'r2': r2, 'o': o, 'ep': ep, 't': t})
    elif tp == "Kids":
        f = Fashion.objects.filter(gender=tp)
        # l = forhighlight(f)
        r1 = rating(f)
        r2 = review(f)
        o = offer(f)
        ep = extraprices(f, o)
        t = "Kid's"
        return render(request, 'fashion.html', {'i': f,  'r1': r1, 'r2': r2, 'o': o, 'ep': ep, 't': t})


def books(request):
    b = Books.objects.all()
    l = forhighlight(b)
    r1 = rating(b)
    r2 = review(b)
    o = offer(b)
    ep = extraprices(b, o)
    return render(request, 'books.html', {'i': b,  'r1': r1, 'r2': r2, 'o': o, 'ep': ep})


def mobadvt(request):
    m = Mobile.objects.all()
    M = listmaker(m)
    return render(request, 'mobileadver.html', {"m1": M[0], "m2": M[1:]})


def fashadvt(request):
    m = Fashion.objects.filter(gender="Men")
    w = Fashion.objects.filter(gender="Women")
    k = Fashion.objects.filter(gender="Kids")
    M = listmaker(m)
    W = listmaker(w)
    K = listmaker(k)
    return render(request, 'fashionadtv.html', {"m1": M[0], "w1": W[0]})


def electronicadvt(request):
    l = Laptop.objects.all()
    h = Headphones.objects.all()
    c = Camera.objects.all()
    t = Tablets.objects.all()
    L = listmaker(l)
    H = listmaker(h)
    C = listmaker(c)
    T = listmaker(t)
    return render(request, 'electronicadvt.html', {"l1": L[0], "l2": L[1:], "h1": H[0], "h2": H[1:], "c1": C[0], "c2": C[1:], "t1": T[0], "t2": T[1:]})


def appadvt(request):
    t = Television.objects.all()
    a = Air_Conditioner.objects.all()
    r = Refrigerator.objects.all()
    w = Washing_Machine.objects.all()
    T = listmaker(t)
    A = listmaker(a)
    R = listmaker(r)
    W = listmaker(w)
    return render(request, 'appadvt.html', {"t1": T[0], "t2": T[1:], "a1": A[0], "a2": A[1:], "r1": R[0], "r2": R[1:], "w1": W[0], "w2": W[1:]})
