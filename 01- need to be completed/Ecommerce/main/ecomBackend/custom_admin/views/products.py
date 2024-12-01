from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from custom_admin.routes import ROUTES
from custom_admin.forms.products_form import ProductsForm
from products.models import Products


def create_product(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Product created successfully')
                # Redirect to the list view
                brands = Brand.objects.all()
                return render(request, "brand/list.html", {"brands": brands, "routes": ROUTES})
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            messages.error(request, 'Form is invalid. Please check the data.')
    else:
        form = ProductsForm()
    return render(request, 'product/add.html', {'form': form, "routes": ROUTES})


def product_list(request):
    try:
        products = Products.objects.values("id", "name", "image", "price", "stock")
        return render(request, "product/list.html", {"products": products, "routes": ROUTES})
    except Exception as error:
        print(error)
        return render(request, "login.html")


def view_product(request, id):
    try:
        # Attempt to retrieve the product category to be updated
        product = Products.objects.get(id=id)

        if request.method == 'POST':
            # If the request method is POST, it means the user has submitted the updated data
            form = ProductsForm(request.POST, instance=product)

            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Product brand updated successfully')
                # Redirect to the list view
                products = Products.objects.all()
                return render(request, "product/list.html", {"products": products, "routes": ROUTES})
            else:
                messages.error(
                    request, 'Form is invalid. Please check the data.')
        else:
            # If the request method is GET, render the update form
            form = ProductsForm(instance=product)

        return render(request, 'product/update.html', {'form': form, 'product': product, "routes": ROUTES})

    except Products.DoesNotExist:
        messages.error(request, 'Product category does not exist')
        # Redirect to the list view
        products = Products.objects.all()
        return render(request, "product/list.html", {"products": products, "routes": ROUTES})

    except Exception as error:
        print(error)
        messages.error(
            request, 'An error occurred while updating the product category')
        # Redirect to the list view
        products = Products.objects.all()
        return render(request, "product/list.html", {"products": products, "routes": ROUTES})


def update_product(request, id):
    try:
        # Attempt to retrieve the product category to be updated
        product = Products.objects.get(id=id)

        if request.method == 'POST':
            # If the request method is POST, it means the user has submitted the updated data
            form = ProductsForm(request.POST, instance=product)

            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Product brand updated successfully')
                # Redirect to the list view
                products = Products.objects.all()
                return render(request, "product/list.html", {"products": products, "routes": ROUTES})
            else:
                messages.error(
                    request, 'Form is invalid. Please check the data.')
        else:
            # If the request method is GET, render the update form
            form = ProductsForm(instance=product)

        return render(request, 'product/update.html', {'form': form, 'product': product, "routes": ROUTES})

    except Products.DoesNotExist:
        messages.error(request, 'Product category does not exist')
        # Redirect to the list view
        products = Products.objects.all()
        return render(request, "product/list.html", {"products": products, "routes": ROUTES})

    except Exception as error:
        print(error)
        messages.error(
            request, 'An error occurred while updating the product category')
        # Redirect to the list view
        products = Products.objects.all()
        return render(request, "product/list.html", {"products": products, "routes": ROUTES})


def delete_product(request, id):
    try:
        product = Products.objects.get(id=id)
        product.delete()
        messages.success(request, 'Product brand deleted successfully')

        products = Products.objects.all()
        return render(request, "product/list.html", {"products": products, "routes": ROUTES})

    except Products.DoesNotExist:
        messages.error(request, 'Product category does not exist')
        products = Products.objects.all()
        return render(request, "product/list.html", {"products": products, "routes": ROUTES})

    except Exception as error:
        print(error)
        messages.error(
            request, 'An error occurred while deleting the product category')
        return render(request, "login.html")
