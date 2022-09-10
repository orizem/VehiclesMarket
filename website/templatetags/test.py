from django import template
import pandas as pd

register = template.Library()

@register.filter(name='search_filter')
def search_filter(df=None):
    return 'search filter is working'
    # return df.sort_values(by=[df.columns[0]])

    
register.filter('search_filter', search_filter)