def main_query(isbn):

    who_else_likes = f"select user_id from ratings_cleaned where isbn = '{isbn}' and ratings > 8"
    what_books_they_like = f"select isbn, count(isbn) as count, avg(ratings) as average from ratings_cleaned where user_id in ({who_else_likes}) group by isbn"

    relative_popularity = f"select isbn, count*average as relative_popularity from ({what_books_they_like})"

    max_relative_popularity = f"select max(relative_popularity) from ({relative_popularity})"

    query = f"select final_index.ISBN, final_index.title, final_index.author, final_index.language, final_index.average, final_index.count, final_index.popularity, final_index.avg_sq, similar.relative_popularity from final_index left join (select isbn, count*average/({max_relative_popularity}) as relative_popularity from ({what_books_they_like})) as similar on final_index.isbn = similar.isbn order by similar.relative_popularity desc;"

    return query


def get_book_info_query(title: str) -> str:
    return f'select f.ISBN, f.title, f.author, f.language, f.average, f.count, f.popularity, f.avg_sq from final_index as f where title like "%{title}%" order by popularity desc limit 1;'


