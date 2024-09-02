movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]

#q1 total_number_of_movies
# movies_count=len(movies)
# print("movi count",movies_count)




#------------------------------------------------------------------------------------------------


#movies with genure drama
# genure_filter=[mov.get("title")for mov in movies if "Drama" in mov.get("genres")]
# print(genure_filter)


#-----------------------------------------------------------------------------------------------

#q3 latest movie
# def get_yr(movi):
#     return movi.get("year")
# latest=max(movies,key=get_yr)
# latest_movie=[movi.get("title")for movi in movies if movi.get("year")==latest.get("year")]
# print(latest_movie)







#---------------------------------------------------------------------------------------------------


#q4 top movie
# def get_rating(mov):
#     return mov.get("rating")
# top_movie=max(movies,key=get_rating)
# top_rating=[mov.get("title")for mov in movies if mov.get("rating")==top_movie.get("rating")]
# print(top_rating)



#-----------------------------------------------------------------------------------------------------------

#q5 movies with malayalam language
# malayalam_language=[m.get("title")for m in movies if m.get("language")=="Malayalam"]
# print(malayalam_language)




#---------------------------------------------------------------------------------------------------






#q6 movies released after  year 2016
# year_filter=[m.get("title")for m in movies if m.get("year")>2016]
# print(year_filter)




#----------------------------------------------------------------------------------------------------


#q7movie with lowest rating
# lowest_rating=min(movies,key=get_rating)
# lowest_movie_rating=[for m in movies if m.get("rating")==lowest_rating.get("rating")]
# print(lowest_movie_rating)




#--------------------------------------------------------------------------------------------------------


#q9 movies released in same years
# movie_dictionary={}
# for m in movies:
#     release_year=m.get("year")
#     if release_year in movie_dictionary:
#         movie_dictionary.get(release_year).append(m.get("title"))
#     else:
#         movie_dictionary[release_year]=[m.get("title")]
# print(movie_dictionary)


#-----------------------------------------------------------------------------------------------------

#q10 oldest movie
# oldest_movie=min(movies,key=get_year)
# oldest_movie_name=[m.get("title")for m in movies if m.get("year")==oldest_movie.get("year")]
# print(oldest_movie_name)




#------------------------------------------------------------------------------------------------

#number of movies released in each year
# years=[ m.get("year")for m in movies]
# # print(years)
# year_count={y:years.count(y)for y in years}
# print(year_count)




#-----------------------------------------------------------------------------------------------------



#print genr5us list-["drama","action","comedy"]
# genres_filter=set()
# for m in movies:
#     for g in m.get("genrus"):

    
# genres_filter={g for m in movies for g in m.get("genres")}
# print(genres_filter)



#action:2,drama:4
# genres_filter=[g for m in movies for g in m.get("genres")]
# genre_count={g:genres_filter.count(g) for g in genres_filter}
# print(genre_count)

#---------------------------------------------------------------------------------------



#sorted movies
# sorted_movie=sorted(movies,key=lambda mov)
def get_title(mov):
    return mov.get("title")
sorted_s=sorted(movies,key=get_title)
print(sorted_s)
sorted_movie=[mov.get("title")for mov in movies if mov.get("title")==sorted_s.get("title")]
print(sorted_movie)



