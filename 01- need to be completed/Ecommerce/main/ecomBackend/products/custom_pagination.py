from rest_framework.pagination import PageNumberPagination

class Custom_Pagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'  # Query parameter for changing page size
    max_page_size = 100  # Maximum page size