from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from products.forms.category_form import CategoriesForm
from products.models import Categories
from custom_admin.routes import ROUTES
from products.serializers import Categories_Serializers
from products.custom_pagination import Custom_Pagination



def create_product_category(request):
    if request.method == "POST":
        form = CategoriesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request, 'Product category created successfully')
                # Redirect to the list view
                return redirect(ROUTES["product_category_list"])
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            messages.error(request, 'Form is invalid. Please check the data.')
    else:
        form = CategoriesForm()
        return render(request, 'category/add.html', {'form': form, "routes": ROUTES})


def product_list_category(request):
    try:
        categories = Categories.objects.all()
        for category in categories:
            print(category)
        return render(request, "category/list.html", {"categories": categories, "routes": ROUTES})
    except Exception as error:
        print(error)
        return render(request, "login.html")


def update_product_category(request, id):
    try:
        # Attempt to retrieve the product category to be updated
        category = Categories.objects.get(id=id)

        if request.method == 'POST':
            # If the request method is POST, it means the user has submitted the updated data
            form = CategoriesForm(request.POST, instance=category)

            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Product category updated successfully')
                # Redirect to the list view
                return redirect(ROUTES["product_category_list"])
            else:
                messages.error(
                    request, 'Form is invalid. Please check the data.')
        else:
            # If the request method is GET, render the update form
            form = CategoriesForm(instance=category)

        return render(request, 'category/update.html', {'form': form, 'category': category, "routes": ROUTES})

    except Categories.DoesNotExist:
        messages.error(request, 'Product category does not exist')
        # Redirect to the list view
        return redirect(ROUTES["product_category_list"])

    except Exception as error:
        print(error)
        messages.error(
            request, 'An error occurred while updating the product category')
        # Redirect to the list view
        return redirect(ROUTES["product_category_list"])


def delete_product_category(request, id):
    try:
        category = Categories.objects.get(id=id)
        category.delete()
        messages.success(request, 'Product category deleted successfully')
        return redirect(ROUTES["product_category_list"])

    except Categories.DoesNotExist:
        print("error")
        messages.error(request, 'Product category does not exist')
        return redirect(ROUTES["product_category_list"])

    except Exception as error:
        print(error)
        messages.error(
            request, 'An error occurred while deleting the product category')
        return redirect(ROUTES["product_category_list"])


@api_view(['GET'])
def get_category(request):
    print(request)
    try:
        categories = Categories.objects.all()
        
        # Initialize the pagination class
        paginator = Custom_Pagination()  # Use your custom pagination class here if needed
        result_page = paginator.paginate_queryset(categories, request)
        
        serializer = Categories_Serializers(result_page, many=True)
        
        return paginator.get_paginated_response(serializer.data)  # Return paginated response
        
    except Exception as error:
        return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)