from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from custom_admin.routes import ROUTES
from products.forms.brand_form import BrandForm
from products.models import Brand
from products.serializers import Brand_Serializers
from products.custom_pagination import Custom_Pagination


def create_product_brand(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Product brand created successfully')
                # Redirect to the list view
                return redirect(ROUTES["product_brand_list"])
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            messages.error(request, 'Form is invalid. Please check the data.')
    else:
        form = BrandForm()
    return render(request, 'brand/add.html', {'form': form, "routes": ROUTES})


def product_brand_list(request):
    try:
        brands = Brand.objects.all()
        return render(request, "brand/list.html", {"brands": brands, "routes": ROUTES})
    except Exception as error:
        print(error)
        return render(request, "login.html")


def update_product_brand(request, id):
    try:
        # Attempt to retrieve the product category to be updated
        brand = Brand.objects.get(id=id)

        if request.method == 'POST':
            # If the request method is POST, it means the user has submitted the updated data
            form = BrandForm(request.POST, instance=brand)

            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Product brand updated successfully')
                return redirect(ROUTES["product_brand_list"])
            else:
                messages.error(
                    request, 'Form is invalid. Please check the data.')
        else:
            # If the request method is GET, render the update form
            form = BrandForm(instance=brand)

        return render(request, 'brand/update.html', {'form': form, 'brand': brand, "routes": ROUTES})

    except Brand.DoesNotExist:
        messages.error(request, 'Product category does not exist')
        return redirect(ROUTES["product_brand_list"])

    except Exception as error:
        print(error)
        messages.error(
            request, 'An error occurred while updating the product category')
        # Redirect to the list view
        return redirect(ROUTES["product_brand_list"])


def delete_product_brand(request, id):
    try:
        brand = Brand.objects.get(id=id)
        brand.delete()
        messages.success(request, 'Product brand deleted successfully')

        return redirect(ROUTES["product_brand_list"])

    except Brand.DoesNotExist:
        messages.error(request, 'Product brand does not exist')
        return redirect(ROUTES["product_brand_list"])

    except Exception as error:
        print(error)
        messages.error(
            request, 'An error occurred while deleting the product category')
        return redirect(ROUTES["product_brand_list"])


@api_view(['GET'])
def get_brand(request):
    print(request)
    try:
        brands = Brand.objects.all()

        # Initialize the pagination class
        paginator = Custom_Pagination()  # Use your custom pagination class here if needed
        result_page = paginator.paginate_queryset(brands, request)

        serializer = Brand_Serializers(result_page, many=True)

        # Return paginated response
        return paginator.get_paginated_response(serializer.data)

    except Exception as error:
        return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
