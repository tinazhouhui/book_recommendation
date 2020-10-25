def main_query():

    who_else_likes = "select user_id from ratings where isbn =:isbn and ratings > 8"
    what_books_they_rated = f"select isbn, count(isbn) as count, avg(ratings) as average from ratings where user_id in ({who_else_likes}) group by isbn"

    what_books_they_like = f"select * from ({what_books_they_rated}) where average > 5 and count > 2"

    relative_popularity = f"select isbn, count*average as relative_popularity from ({what_books_they_like})"

    max_relative_popularity = f"select max(relative_popularity) from ({relative_popularity})"

    query = f"select f.ISBN, f.title, f.author, f.average, f.count, f.popularity, f.avg_sq, similar.relative_popularity from final_index as f left join (select isbn, count*average/({max_relative_popularity}) as relative_popularity from ({what_books_they_like})) as similar on f.isbn = similar.isbn group by lower(f.title) order by similar.relative_popularity desc;"

    return query


def get_book_info_query() -> str:
    return 'select b.ISBN, b.title, b.author, b.average, b.count from book as b where title like :title limit 1;'


