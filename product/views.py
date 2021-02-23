from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from product.models import Category, Product


def homepage(request):
    categories = Category.objects.all()
    return render(request, 'product/index.html', {'categories': categories})

#class ProductImage(models.Model):
   # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    #image = models.ImageField(upload_to='products', null=True, blank=True)

    d#ef get_image_url(self):
      #  if self.image:
       # return self.image.url
        #return ''

    #def products_list(request, category_slug):
    #products = Product.objects.all()
    #if not Category.objects.filter(slug=category_slug).exists():
        #raise Http404
    #products = Product.objects.filter(category_id=category_slug)
    #category = get_object_or_404(Category, slug=category_slug) 3 вариант
    #products = Product.objects.filter(category=category)
    #products = get_list_or_404(Product, category_id=category_slug)  #2 вариант
    #return render(request,'product/products_list.html', {'products': products})

#def products_list(request, category_slug):
 #   if not Category.objects.filter(slug = category_slug).exists():
  #      raise Http404('Нет такой категории')
   # products = Product.objects.filter(category_id=category_slug)
    #return render(request, 'product/products_list.html', {'products': products})

class ProductListView(View):
    def get(self,request, category_slug):
        if not Category.objects.filter(slug=category_slug).exists():
            raise Http404('Нет такой категории')
        products = Product.objects.filter(category_id=category_slug)
        return render(request, 'product/products_list.html', {'products': products})

class ProductsListView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    context_object_name = 'products'
    #def get(self, request, category_slug):
     #   if not Category.objects.filter(slug=category_slug).exists():
      #      raise Http404('Нет такой категории')
       # products = self.get_queryset().filter(category_id=category_slug)
        #return render(request, 'product/products_list.html', {'products': products})

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if not Category.objects.filter(slug=category_slug).exists():
            raise Http404('Нет такой категории')
        queryset = queryset.filter(category_id=self.kwargs['category_slug'])
        return queryset

#def product_details(request, product_id):
 #   product = get_object_or_404(Product, id=product_id)
  #  return render(request, 'product/product_details.html', {'product': product})

class ProductsDetailsView(DetailView):
    model = Product
    template_name = 'product/product_details.html'



#class HomePageView(View):
 #   def get(self, request):
  #      categories = Category.objects.all()
   #     return render(request, 'product/index.html', {'categories': categories})


class HomePageView(ListView):
    model = Category
    template_name = 'product/index.html'
    context_object_name = 'categories'





#TODO: переписать вьюшку product_lists+++
#TODO: добавить детали продукта+++
#TODO: сделать переход из категории в листинг продуктов+++
#TODO: подключить картинки для товаров+++
#TODO: переписать вьющки на CBV(Class Base View)

#def products_list2(request):   # 1  вариант
    #category_slug = request.GET.get('category')
    #products = Product.objects.all()
    #if category_slug is not None:
        #products = products.filter(category_id=category_slug)



#all() - выводит все обьекты
#SELECT * FROM table;

#Category.objects.filter(...).all()

#filter() - фильтрует результаты запроса

#SELECT * FROM table WHERE'

#exclude(условие) - исключает из результатов обьекты отвечающие условию

#SELECT FROM table WHERE category != 1;

#exclude(title__startswith='Apple')


#SELECT FROM table WHERE title NOT LIKE 'Apple%'


#order_by() - сортировка результатов запроса

#Product.objects.order_by('price');

#SELECT * FROM product ORDER BY price ASC

#Product.objects.order_by('-price');

#SELECT * FROM product ORDER BY price DESC

#Product.objects.order_by('proce', 'popularity')

#SELECT * FROM product ORDER BY price ASC, popularity ASC;

#Product.objects.order_by('?') - рандомная сортировка


#Product.objects.reverse() - возвращает в обратном порядке


#distinct() - исключает повторения



#Product.objects.values_list('category').distinct()

#values()

#Product.objects.values()

#Возвращает словарь в списке где ключи это их значения



#values_list() - возвращает котрежи

#представляет обьекты в виде кортежей

#none() - пустой request

#Product.objects.none() - возвращает постой список




#select_related()
#prod = Product.objects.get(id=1)
#prod.category
#prod. Product.objects.select_related('category').get(id=1) - делает запрос на раз в БД

#prod = SELECT * FROM product WHERE id=5;
#SELECT * FROM category WHERE id =prod.

#prefatch_related()

#SELECT * FROM product WHERE category_id in(4, 6 ,9 ....)


#get() возвращает обьект
# product = Product.objects.get(id=1) -> Молоко
#product.id = 1

#Если нет обьекта по условию:
#Product.DoesNotExist
#Если get находит несколько обьектов:
#Product.MultipleObjectsReturned


#create() -  позволяет создавать новые обьекты модели

#get_or_create(условие) - выбирает обьект, отвечающий условию, если нет такого условия , то он создает обьект

#update_or_create()  - обновляет обект или создает новый


#bulk_create() позволяет создать несколько обьектов

#bulk_update() обновляет несколько обьектов


#count() возвращает количество результатов queryset

#exists()  проверяет есть ли в queryset хоть один результат


#Fields lookups:

#gt ->   '>'
#lt ->   '<'
#gte ->  '>='
#lte -> '<='
#= ->    '='


#startswith 'A'like
#istartswith 'A'  ilike

#contains='day'  like
#icontains='day  ilike

#exact='Milk' -> WHERE title = 'MILK'
#iexact='Milk' => WHERE title ilike = 'Milk'

#category__isnul= True  Where category IS NULL
#category__isnul= False Where category is NOT NULL

#id__id=[1, 2, 3, 4]


#Order.objects.filter(data__range=(start_date, stop_date)) - > WHERE date BETWEEN start_date AND end_date
