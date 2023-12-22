# add your code here
import pandas as pd

wine_reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

wine_reviews_by_country = wine_reviews.groupby(['country']).agg({'title': 'count' , 'points': 'mean' })
def round_avg_points(points):
    points = points.round(1)
    return points 
    
rounded_wine_rev_by_country = wine_reviews_by_country.apply(round_avg_points, axis = 'columns')
wine_reviews_final = rounded_wine_rev_by_country.rename(columns={'title':'count'})

wine_reviews_final.to_csv('data/reviews-per-country.csv')



