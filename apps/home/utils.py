def custom_paginate(queryset, page=1, per_page=5):
    """
    A simple pagination function that slices the queryset manually.
    Returns:
        - page_data: the subset of items for this page
        - total_items: total number of items in the queryset
        - total_pages: how many pages are available
        - current_page: the current page as an integer
        - has_previous: bool indicating if there's a previous page
        - has_next: bool indicating if there's a next page
    """
    # Convert page to int safely, default to 1 if invalid
    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1
    
    total_items = queryset.count()
    total_pages = (total_items - 1) // per_page + 1 if total_items else 1
    
    # Correct the page number if out of range
    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages

    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    page_data = queryset[start_index:end_index]

    # Flags for previous/next
    has_previous = page > 1
    has_next = page < total_pages

    return {
        'page_data': page_data,
        'total_items': total_items,
        'total_pages': total_pages,
        'current_page': page,
        'has_previous': has_previous,
        'has_next': has_next,
        'start_index': start_index + 1 if total_items else 0,
        'end_index': min(end_index, total_items),
    }



from apps.home.models import Song
from datetime import datetime, timedelta

