
# Introduction
The goal is to create a book recommendation algorithm.

### Understanding of the problem
- Recommendation in principle is ordering of all the options from most relevant to least based on past information (book title)
- The relevancy is determined by individual factors that have an impact on rating. 
- Number of factors is dependent on available information 
- For every book, each factor is scored and weighted to get final score
- Ordering books by the final score will produce a list of best recommendations

### Methodology and approach
- Data discovery - snapshot
  - Missing values
  - Distribution and relationships
  - Data extraction and cleaning
- Factor identification
  - Available information
  - Common characteristics
- Scoring function that would assign a correct score to each factor
- Engineering
- Future improvements
  - Recommendation
  - Performance
    
### Assumptions
- Input data is only a book title 
- Recommendation is based on the fact that input book was liked
- Validity of dataset
- 0 is missing rating rather than really bad rating
- At least three ratings per book

# Requirements
- Python 3
- SQLAlchemy~=1.3.19
- flask~=1.1.1
- SQL database

# Run
```bash
python3 start.py
```