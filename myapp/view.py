import json
from django.http import HttpResponse
from myapp.model import AlcoholicProduct
from django.views.decorators.csrf import csrf_exempt
import copy


def save_product(name, product_type, manufacturer, degree, price):
    record = AlcoholicProduct.objects.filter(name=name, product_type=product_type, manufacturer=manufacturer)

    try:
        if len(record) == 0:
            new_data = AlcoholicProduct.objects.create(name=name, product_type=product_type,manufacturer=manufacturer,
                                                       degree=degree, price=price)
            new_data.save()
            return 'Data inserted Successfully'
        else:
            record.update(degree=degree, price=price)
            return 'Data updated Successfully'
    except Exception as e:
        return e


def get_high_alcohol_product(product_type):
    record = AlcoholicProduct.objects.filter(product_type=product_type).order_by('-degree').first()
    if record is not None:
        output = json.dumps({'name': record.name, 'product_type': record.product_type,
                             'manufacturer': record.manufacturer, 'degree': str(record.degree),
                             'price': str(record.price)})
        return 'Got product data with the highest alcohol degree Successfully', output
    else:
        raise Exception('Record Not found')


@csrf_exempt
def save_product_api(request):
    if request.method == 'POST':
        inputs = copy.copy(json.load(request))
        name = inputs['name']
        product_type = inputs['product_type']
        manufacturer = inputs['manufacturer']
        degree = inputs['degree']
        price = inputs['price']

        response = None
        try:
            response = save_product(name, product_type, manufacturer, degree, price)
            return HttpResponse(status=200, reason=response)
        except:
            return HttpResponse(status=500, reason=response)


@csrf_exempt
def get_high_alcohol_product_api(request):
    if request.method == 'GET':
        product_type = request.GET.get('product_type')
        try:
            response, outputs = get_high_alcohol_product(product_type)
            print(response)
            return HttpResponse(content=outputs, status=200, reason=response)
        except Exception as e:
            return HttpResponse(status=404, reason=e)
