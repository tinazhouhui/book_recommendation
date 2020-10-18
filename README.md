
# Introduction
The goal is to create a book recommendation algorithm. This task is part of a interview process.

### Understanding of the problem
- Book recommendation in principle is a decision making process of choosing the best option
- the best option is determined by ordering of all the options from best to worst
- the order is determined by scoring of common characteristics - factors
- the scoring is based on the input data
- the importance of the factors can be dependent on personal preference (weighted average)

### Methodology and approach
- Data discovery - snapshot
  - Missing values
  - Statistical information
  - Distribution and relationships
  - ISBN - language info extraction
- Scoring function that would assign a correct score to each factor
  - available info from input data
  - determine common characteristics with dataset
  - assign score - ??
    - determined by historical data? what about ambiguous factors? Is year publishing good if it is similar or bad?  
- implementation and testing
  - benchmark?
- trends and clusters analysis?
- future improvements
    
### Assumptions
- Input data from reader is just the book (ISBN)

# Data Discovery
## Users
- total of 278 856 userIDs
- 110 760 missing age - INCOMPLETE DATA, probably not use age as one of deciding factors

## Ratings
- 1 149 780 ratings of 340 558 books
- by 105 283 users
  - max number of ratings 13600, min 0 (only 5)
  - average ratings per person - 11
  
## Books
- total 271 379
- 270 170 books rated (1 031 175 ratings)

# What could be improved
