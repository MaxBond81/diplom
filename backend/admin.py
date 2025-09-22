from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from backend.models import User, Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, \
    Contact, ConfirmEmailToken


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Панель управления пользователями
    """
    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password', 'type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company', 'position')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    """
       Панель управления магазинами
       Attributes:
              list_display: Поля для отображения в списке магазинов
              list_filter: Поля для фильтра
              search_fields: Поля для поиска
    """

    list_display = ('name', 'url', 'user', 'state')
    list_filter = ('state',)
    search_fields = ('name', 'url')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
       Панель управления категориями
       Attributes:
              list_display: Поля для отображения в списке категорий
              filter_horizontal: Поля для горизонтального фильтра
              search_fields: Поля для поиска
    """

    list_display = ('name', )
    filter_horizontal = ('shops',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
      Панель управления продуктами
      Attributes:
             list_display: Поля для отображения в списке продуктов
             list_filter: Поля для фильтра
             search_fields: Поля для поиска
    """

    list_display = ('id', 'name', 'category')
    list_filter = ('category', )
    search_fields = ('name', 'category__name' )


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    """
      Панель управления информацией о продукте
      Attributes:
             list_display: Поля для отображения в списке информации о продукте
             list_filter: Поля для фильтра
             search_fields: Поля для поиска
             readonly_fields: Поля только для чтения
    """

    list_display = ('model', 'product', 'shop', 'quantity', 'price', 'price_rrc')
    list_filter = ('product', 'shop')
    search_fields = ('model', 'product__name', 'shop__name', 'product__category__name')
    readonly_fields = ('external_id',)


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    """
         Панель управления параметрами
         Attributes:
                list_display: Поля для отображения в списке параметров
                search_fields: Поля для поиска
    """

    list_display = ('name', )
    search_fields = ('name', )


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    """
        Панель управления параметрами продукта
        Attributes:
            list_display: Поля для отображения в списке параметров продукта
            list_filter: Поля для фильтра
            search_fields: Поля для поиска
    """

    list_display = ('product_info__product__name', 'parameter', 'value')
    list_filter = ('parameter', 'value')
    search_fields = ('product_info__product__name', 'parameter__name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
        Панель управления заказами
        Attributes:
            list_display: Поля для отображения в списке заказов
            list_filter: Поля для фильтра
            search_fields: Поля для поиска
    """

    list_display = ('id', 'user', 'dt', 'state', 'contact')
    list_filter = ('user', 'dt', 'state')
    search_fields = ('user__last_name', 'user__email')



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
        Панель управления позициями заказов
        Attributes:
            list_display: Поля для отображения позиций заказов
            list_filter: Поля для фильтра
            search_fields: Поля для поиска
    """

    list_display = ('order', 'product_info__product__name', 'quantity')
    list_filter = ('order__user__email', 'product_info__product__category__name')
    search_fields = ('order__user__email', 'product_info__product__name')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
        Панель управления контактами
        Attributes:
            list_display: Поля для отображения контактов
            list_filter: Поля для фильтра
            search_fields: Поля для поиска
    """

    list_display = ('user', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'phone')
    list_filter = ('city', )
    search_fields = ('user__email', 'city')


@admin.register(ConfirmEmailToken)
class ConfirmEmailTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created_at',)
